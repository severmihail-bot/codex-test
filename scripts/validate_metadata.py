#!/usr/bin/env python3
"""Validate metadata/documents.yml without external YAML dependencies."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
METADATA_FILE = ROOT / "metadata" / "documents.yml"
REQUIRED_ENTRY_FIELDS = (
    "id",
    "title",
    "source_type",
    "jurisdiction",
    "language",
    "raw_file",
    "normalized_file",
    "knowledge_dir",
    "status",
    "review_required",
)


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def strip_value(value: str) -> str:
    return value.strip().strip('"').strip("'")


def parse_documents(text: str) -> list[dict[str, str]]:
    lines = text.splitlines()
    if not any(line.strip().startswith("documents:") for line in lines):
        fail("metadata/documents.yml must contain a top-level `documents:` key")

    documents_line = next(line.strip() for line in lines if line.strip().startswith("documents:"))
    if documents_line == "documents: []":
        return []

    entries: list[dict[str, str]] = []
    current: dict[str, str] | None = None

    for line_no, raw_line in enumerate(lines, start=1):
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("documents:"):
            continue

        if stripped.startswith("- "):
            if current is not None:
                entries.append(current)
            current = {}
            remainder = stripped[2:]
            if remainder:
                if ":" not in remainder:
                    fail(f"metadata/documents.yml:{line_no}: invalid list entry")
                key, value = remainder.split(":", 1)
                current[key.strip()] = strip_value(value)
            continue

        if current is None:
            fail(f"metadata/documents.yml:{line_no}: field outside a document entry")
        if ":" not in stripped:
            fail(f"metadata/documents.yml:{line_no}: invalid field")
        key, value = stripped.split(":", 1)
        current[key.strip()] = strip_value(value)

    if current is not None:
        entries.append(current)

    return entries


def validate_entry(entry: dict[str, str], index: int) -> None:
    label = f"documents[{index}]"
    for field in REQUIRED_ENTRY_FIELDS:
        if field not in entry:
            fail(f"{label}: missing `{field}`")

    if entry.get("jurisdiction") != "RO":
        fail(f"{label}: `jurisdiction` must be `RO`")
    if entry.get("language") != "ro":
        fail(f"{label}: `language` must be `ro`")
    if entry.get("review_required") not in {"true", "false"}:
        fail(f"{label}: `review_required` must be true or false")

    for path_field in ("raw_file", "normalized_file", "knowledge_dir"):
        value = entry.get(path_field, "")
        if value and value.startswith("/"):
            fail(f"{label}: `{path_field}` must be a repository-relative path")


def main() -> int:
    if not METADATA_FILE.exists():
        fail("metadata/documents.yml is missing")

    entries = parse_documents(METADATA_FILE.read_text(encoding="utf-8"))
    seen_ids: set[str] = set()
    for index, entry in enumerate(entries):
        validate_entry(entry, index)
        document_id = entry.get("id", "")
        if document_id in seen_ids:
            fail(f"documents[{index}]: duplicate id `{document_id}`")
        if document_id:
            seen_ids.add(document_id)

    print(f"Validated metadata for {len(entries)} document(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
