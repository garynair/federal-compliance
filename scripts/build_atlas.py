#!/usr/bin/env python3
"""Regenerate the reading-view HTML from README.md.

Usage: python3 scripts/build_atlas.py [README.md] [output.html]

Requires pandoc on PATH. Produces a single self-contained HTML file ready
to publish as a Claude Artifact (or open directly in a browser).
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "README.md"
OUTPUT = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "dist" / "atlas.html"
TEMPLATE = Path(__file__).resolve().parent / "atlas-template.html"


def pandoc_to_html(md_path: Path) -> str:
    result = subprocess.run(
        ["pandoc", "-f", "gfm", "-t", "html", str(md_path)],
        capture_output=True, text=True, check=True,
    )
    return result.stdout


def extract_intro(html: str) -> tuple[str, str]:
    scope_m = re.search(r"<p><strong>Scope:</strong>(.*?)</p>", html, re.S)
    whynow_m = re.search(r"<p><strong>Why now:</strong>(.*?)</p>", html, re.S)
    scope = re.sub(r"\s+", " ", scope_m.group(1)).strip() if scope_m else ""
    whynow = re.sub(r"\s+", " ", whynow_m.group(1)).strip() if whynow_m else ""
    return scope, whynow


def find_main_content_start(html: str) -> int:
    """Find where the real content starts: right after the Contents section's list."""
    contents_m = re.search(r'<h2 id="contents">', html)
    if not contents_m:
        raise SystemExit("Could not find '## Contents' section — is README.md structure unchanged?")
    ul_end_m = re.search(r"</ul>", html[contents_m.end():])
    if not ul_end_m:
        raise SystemExit("Could not find end of the Contents list.")
    return contents_m.end() + ul_end_m.end()


def _tag_entry_lists(html: str) -> str:
    """Add entry-list/entry classes only to <ul><li> blocks, never to <ol><li> (e.g. numbered steps)."""
    def transform(m: re.Match) -> str:
        inner = m.group(1).replace("<li>", '<li class="entry">')
        return f'<ul class="entry-list">{inner}</ul>'
    return re.sub(r"<ul>(.*?)</ul>", transform, html, flags=re.S)


def wrap_sections(html: str) -> tuple[str, list[tuple[str, str, int]]]:
    start_idx = find_main_content_start(html)
    main_html = html[start_idx:]

    parts = re.split(r'(<h2 id="[^"]+">.*?</h2>)', main_html, flags=re.S)
    sections = []
    i = 1
    while i < len(parts):
        h2 = parts[i]
        content = parts[i + 1] if i + 1 < len(parts) else ""
        m = re.match(r'<h2 id="([^"]+)">(.*?)</h2>', h2, re.S)
        sec_id = m.group(1)
        sec_title = re.sub(r"\s+", " ", re.sub("<[^<]+?>", "", m.group(2))).strip()

        content_clean = re.sub(r"\s*<hr\s*/?>\s*", "\n", content).strip()
        content_clean = _tag_entry_lists(content_clean)
        entry_count = len(re.findall(r'<li class="entry">', content_clean))
        sections.append((sec_id, sec_title, entry_count, content_clean))
        i += 2

    out = []
    for sec_id, title, count, content in sections:
        out.append(f'<section class="gov-section" id="{sec_id}" data-count="{count}">')
        out.append(f"<h2>{title}</h2>")
        out.append(content)
        out.append("</section>")

    return "\n".join(out), [(s[0], s[1], s[2]) for s in sections]


def build_toc_js(sections: list[tuple[str, str, int]]) -> str:
    entries = ",\n".join(
        f'  {{id:"{sid}", title:{title!r}, count:{count}}}' for sid, title, count in sections
    )
    return "[\n" + entries + "\n]"


def main() -> None:
    if not README.exists():
        raise SystemExit(f"README not found: {README}")
    if not TEMPLATE.exists():
        raise SystemExit(f"Template not found: {TEMPLATE}")

    raw_html = pandoc_to_html(README)
    scope, whynow = extract_intro(raw_html)
    sections_html, section_meta = wrap_sections(raw_html)
    toc_js = build_toc_js(section_meta)

    total_entries = sum(c for _, _, c in section_meta)
    total_sections = len(section_meta)

    page = TEMPLATE.read_text()
    page = page.replace("__TOTAL_ENTRIES__", str(total_entries))
    page = page.replace("__TOTAL_SECTIONS__", str(total_sections))
    page = page.replace("__SCOPE_TEXT__", scope)
    page = page.replace("__WHYNOW_TEXT__", whynow)
    page = page.replace("__SECTIONS_HTML__", sections_html)
    page = page.replace("__TOC_JS__", toc_js)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(page)
    print(f"Wrote {OUTPUT} ({len(page):,} bytes, {total_entries} resources across {total_sections} sections)")


if __name__ == "__main__":
    main()
