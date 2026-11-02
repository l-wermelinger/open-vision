#!/usr/bin/env python3
"""Check published documentation without requiring raw archives, a Mac or a headset."""

import json
import re
import subprocess
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^\]\n]*\]\(([^\s)]+)\)")
SOURCE = re.compile(r"\bS\d{2,}\b")
PRIVATE = re.compile(
    r"/(?:Users|home)/[^/\s]+|"
    r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b|"
    r"-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----"
)


def link_error(document: Path, target: str) -> str | None:
    url = urlsplit(target.strip("<>"))
    if url.scheme in {"http", "https", "mailto"}:
        return None
    if url.scheme or url.netloc:
        return f"unsupported link: {target}"
    if not url.path:
        return None  # Heading fragments do not require a filesystem target.
    relative = Path(unquote(url.path))
    resolved = (document.parent / relative).resolve()
    if relative.is_absolute() or not resolved.is_relative_to(ROOT):
        return f"link escapes repository: {target}"
    if not resolved.exists():
        return f"missing link target: {target}"
    return None


def check() -> None:
    # Small regression checks for the link validator's distinct branches.
    readme = ROOT / "README.md"
    assert link_error(readme, "docs/architecture.md") is None
    assert link_error(readme, "https://example.org/missing") is None
    assert link_error(readme, "#goal") is None
    assert link_error(readme, "../outside.md") is not None
    assert link_error(readme, "%2e%2e/outside.md") is not None
    assert link_error(readme, "does-not-exist.md") is not None
    assert link_error(readme, "file:///etc/passwd") is not None

    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT, check=True, capture_output=True, text=True,
    )
    files = sorted(set(filter(None, result.stdout.split("\0"))))
    sources = json.loads((ROOT / "docs/research/sources.json").read_text())
    assert isinstance(sources, list) and sources, "source ledger must be a non-empty list"
    identifiers = set()
    for source in sources:
        for field in ("id", "title", "url", "checked_at", "source_family", "note", "use", "limitation"):
            assert isinstance(source.get(field), str) and source[field].strip(), (source, field)
        assert re.fullmatch(r"S\d{2,}", source["id"]), source["id"]
        assert source["id"] not in identifiers, f"duplicate source: {source['id']}"
        identifiers.add(source["id"])
        date.fromisoformat(source["checked_at"])
        url = urlsplit(source["url"])
        assert url.scheme in {"http", "https"} and url.netloc, source["url"]

    markdown_count = 0
    for name in files:
        assert name != "docs/research/state.json", "local harness state must stay untracked"
        assert not name.startswith(("docs/research/tmp/", ".local/")), name
        path = ROOT / name
        assert path.resolve().is_relative_to(ROOT), f"file escapes repository: {name}"
        if path.suffix not in {".md", ".json", ".py", ".yml", ".yaml"}:
            continue
        text = path.read_text()
        assert not PRIVATE.search(text), f"potential private data in {name}"
        if path.suffix != ".md":
            continue
        markdown_count += 1
        assert SOURCE.findall(text) == [] or set(SOURCE.findall(text)) <= identifiers, name
        for target in LINK.findall(text):
            error = link_error(path, target)
            assert error is None, f"{name}: {error}"

    print(f"PASS: {markdown_count} Markdown files, {len(sources)} sources, local links and publication hygiene.")
    print("Native Simulator/headset tests: not performed by this check.")


if __name__ == "__main__":
    check()
