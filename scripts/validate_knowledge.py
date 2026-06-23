#!/usr/bin/env python3
"""Validate generated Markdown files in the knowledge library."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_DIR = ROOT / "knowledge"
REQUIRED_FRONTMATTER_FIELDS = (
    "title",
    "document_id",
    "source_document",
    "source_file",
    "source_type",
    "jurisdiction",
    "language",
    "status",
    "generated_by",
    "last_reviewed",
    "review_required",
)
LEGAL_KEYWORDS = (
    "obliga",
    "sancți",
    "sancti",
    "termen",
    "procedur",
    "interdic",
    "dreptul",
    "trebuie",
    "poate fi",
)
SOURCE_MARKER = "**Sursă:**"
WARNING_MARKER = "> [!WARNING]"
UNCLEAR_MARKER = "**NECLAR:**"


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def parse_frontmatter(text: str, path: Path) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        fail(f"{path}: missing YAML frontmatter")

    end = text.find("\n---\n", 4)
    if end == -1:
        fail(f"{path}: frontmatter is not closed with ---")

    raw = text[4:end]
    body = text[end + len("\n---\n") :]
    fields: dict[str, str] = {}
    for line_no, line in enumerate(raw.splitlines(), start=2):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in stripped:
            fail(f"{path}:{line_no}: invalid frontmatter line")
        key, value = stripped.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')

    return fields, body


def validate_frontmatter(path: Path, fields: dict[str, str]) -> None:
    for key in REQUIRED_FRONTMATTER_FIELDS:
        if key not in fields:
            fail(f"{path}: missing frontmatter field `{key}`")

    if fields.get("jurisdiction") != "RO":
        fail(f"{path}: `jurisdiction` must be `RO`")
    if fields.get("language") != "ro":
        fail(f"{path}: `language` must be `ro`")
    if fields.get("review_required") not in {"true", "false"}:
        fail(f"{path}: `review_required` must be true or false")


def validate_unclear_blocks(path: Path, text: str) -> None:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if UNCLEAR_MARKER in line:
            previous = lines[index - 1].strip() if index > 0 else ""
            if previous != WARNING_MARKER:
                fail(f"{path}:{index + 1}: `NECLAR` must use the standard warning block")


def validate_citation_heuristic(path: Path, body: str) -> None:
    """Catch obvious legal-content files without any citation marker.

    This is intentionally conservative. It avoids trying to prove every legal
    sentence has a citation until we have richer validators.
    """

    lower_body = body.lower()
    has_legal_content = any(keyword in lower_body for keyword in LEGAL_KEYWORDS)
    if has_legal_content and SOURCE_MARKER not in body:
        fail(f"{path}: appears to contain legal content but has no `{SOURCE_MARKER}` citation")


def validate_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    fields, body = parse_frontmatter(text, path)
    validate_frontmatter(path, fields)
    validate_unclear_blocks(path, text)
    validate_citation_heuristic(path, body)


def main() -> int:
    if not KNOWLEDGE_DIR.exists():
        fail("knowledge/ directory is missing")

    markdown_files = sorted(KNOWLEDGE_DIR.rglob("*.md"))
    if not markdown_files:
        print("No knowledge Markdown files found; nothing to validate yet.")
        return 0

    for path in markdown_files:
        validate_file(path)

    print(f"Validated {len(markdown_files)} knowledge Markdown file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
