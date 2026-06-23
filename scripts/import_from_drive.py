#!/usr/bin/env python3
"""Import .md and .txt files from Google Drive into sources/raw/."""

from __future__ import annotations

import io
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "sources" / "raw"
MANIFEST_FILE = RAW_DIR / "import-manifest.json"
ALLOWED_EXTENSIONS = {".md", ".txt"}
DRIVE_READONLY_SCOPE = "https://www.googleapis.com/auth/drive.readonly"


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def get_required_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        fail(f"Missing required environment variable `{name}`")
    return value


def load_service_account_info() -> dict[str, Any]:
    raw_json = get_required_env("GOOGLE_SERVICE_ACCOUNT_JSON")
    try:
        return json.loads(raw_json)
    except json.JSONDecodeError as exc:
        fail(f"`GOOGLE_SERVICE_ACCOUNT_JSON` is not valid JSON: {exc}")


def build_credentials():
    """Build Google credentials from WIF/ADC, with JSON key fallback for local use."""
    try:
        import google.auth
        from google.oauth2 import service_account
    except ImportError as exc:
        fail(
            "Google API dependencies are not installed. "
            "Run `pip install -r requirements-drive.txt`. "
            f"Original error: {exc}"
        )

    if os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON", "").strip():
        return service_account.Credentials.from_service_account_info(
            load_service_account_info(),
            scopes=[DRIVE_READONLY_SCOPE],
        )

    try:
        credentials, _ = google.auth.default(scopes=[DRIVE_READONLY_SCOPE])
    except Exception as exc:  # noqa: BLE001 - surface a friendly configuration error.
        fail(
            "Could not find Google Application Default Credentials. "
            "In GitHub Actions, configure Workload Identity Federation via "
            "google-github-actions/auth. For local runs, set "
            "GOOGLE_SERVICE_ACCOUNT_JSON only if your organization permits JSON keys. "
            f"Original error: {exc}"
        )
    return credentials


def build_drive_service():
    try:
        from googleapiclient.discovery import build
    except ImportError as exc:
        fail(
            "Google API dependencies are not installed. "
            "Run `pip install -r requirements-drive.txt`. "
            f"Original error: {exc}"
        )

    return build("drive", "v3", credentials=build_credentials(), cache_discovery=False)


def safe_filename(name: str) -> str:
    cleaned = re.sub(r"[\\/:*?\"<>|]+", "-", name).strip()
    cleaned = re.sub(r"\s+", " ", cleaned)
    if not cleaned or cleaned in {".", ".."}:
        fail(f"Unsafe Drive filename `{name}`")
    return cleaned


def is_supported_file(name: str, mime_type: str) -> bool:
    extension = Path(name).suffix.lower()
    if extension in ALLOWED_EXTENSIONS:
        return True
    if mime_type == "text/plain" and extension == "":
        return True
    return False


def list_source_files(service, folder_id: str) -> list[dict[str, str]]:
    query = f"'{folder_id}' in parents and trashed = false"
    fields = "nextPageToken, files(id, name, mimeType, modifiedTime, size)"
    files: list[dict[str, str]] = []
    page_token: str | None = None

    while True:
        response = (
            service.files()
            .list(
                q=query,
                spaces="drive",
                fields=fields,
                pageToken=page_token,
                orderBy="name",
            )
            .execute()
        )
        for item in response.get("files", []):
            if item.get("mimeType") == "application/vnd.google-apps.folder":
                continue
            if is_supported_file(item.get("name", ""), item.get("mimeType", "")):
                files.append(item)
            else:
                print(f"Skipping unsupported Drive file: {item.get('name', '<unnamed>')}")

        page_token = response.get("nextPageToken")
        if not page_token:
            break

    return files


def download_file(service, file_id: str) -> bytes:
    try:
        from googleapiclient.http import MediaIoBaseDownload
    except ImportError as exc:
        fail(
            "Google API dependencies are not installed. "
            "Run `pip install -r requirements-drive.txt`. "
            f"Original error: {exc}"
        )

    request = service.files().get_media(fileId=file_id)
    buffer = io.BytesIO()
    downloader = MediaIoBaseDownload(buffer, request)
    done = False
    while not done:
        _, done = downloader.next_chunk()
    return buffer.getvalue()


def write_manifest(records: list[dict[str, str]]) -> None:
    manifest = {
        "imported_at": datetime.now(timezone.utc).isoformat(),
        "source": "google_drive",
        "accepted_extensions": sorted(ALLOWED_EXTENSIONS),
        "files": records,
    }
    MANIFEST_FILE.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    folder_id = get_required_env("GOOGLE_DRIVE_SOURCES_FOLDER_ID")
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    service = build_drive_service()
    files = list_source_files(service, folder_id)
    imported: list[dict[str, str]] = []

    for item in files:
        name = safe_filename(item["name"])
        target = RAW_DIR / name
        content = download_file(service, item["id"])
        target.write_bytes(content)
        imported.append(
            {
                "drive_file_id": item["id"],
                "name": item["name"],
                "path": str(target.relative_to(ROOT)),
                "mime_type": item.get("mimeType", ""),
                "modified_time": item.get("modifiedTime", ""),
                "size": item.get("size", ""),
            }
        )
        print(f"Imported {item['name']} -> {target.relative_to(ROOT)}")

    write_manifest(imported)
    print(f"Imported {len(imported)} file(s) from Google Drive.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
