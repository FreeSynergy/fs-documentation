#!/usr/bin/env python3
"""Publish the decision records (conventions/decisions/*.md) on the site.

The ADRs are written in German and stay the single source in conventions/decisions/.
This script copies them to docs/<lang>/decisions/ (content unchanged, German) and writes
an overview page per language (English / German). Idempotent; --check exits 1 on drift (CI).
Links that point outside the decision folder are turned into plain GitHub links.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "conventions" / "decisions"
GH = "https://github.com/FreeSynergy/fs-documentation/blob/main/conventions/decisions/"
TEXT = {
    "en": ("Decisions", "Decision records (ADR)",
           "The decisions behind FreeSynergy, numbered in the order they were made. The records are written in German; "
           "this page is the English overview. Status and title are taken from each record.",
           ["No.", "Title", "Status"]),
    "de": ("Entscheidungen", "Entscheidungen (ADR)",
           "Die Entscheidungen hinter FreeSynergy, in der Reihenfolge, in der sie fielen. Status und Titel stammen aus dem jeweiligen Eintrag.",
           ["Nr.", "Titel", "Status"]),
}
SORT = {"en": "7 Decisions", "de": "7 Decisions"}


def fix_links(text):
    def sub(m):
        label, target = m.group(1), m.group(2)
        if re.match(r"^(https?:|#|mailto:)", target) or re.match(r"^\d{4}-[^/]+\.md(#.*)?$", target):
            return m.group(0)
        return f"[{label}]({GH}{target})" if not target.startswith("/") else m.group(0)
    return re.sub(r"\[([^\]]*)\]\(([^)\s]+)\)", sub, text)


def build():
    out = {}
    rows = []
    for p in sorted(SRC.glob("[0-9][0-9][0-9][0-9]-*.md")):
        text = p.read_text(encoding="utf-8")
        title = text.split("\n", 1)[0].lstrip("# ").strip()
        m = re.search(r"^Status:\s*(.+)$", text, re.M)
        status = (m.group(1).split("·")[0].strip() if m else "").replace("|", "/")
        rows.append((p.name, title, status))
        out[p.name] = fix_links(text)
    pages = {}
    for lang, (_, h1, intro, head) in TEXT.items():
        lines = [f"# {h1}", "", intro, "", f"| {head[0]} | {head[1]} | {head[2]} |", "|---|---|---|"]
        for name, title, status in rows:
            lines.append(f"| {name[:4]} | [{title.split(' – ', 1)[-1]}]({name}) | {status} |")
        pages[lang] = {"index.md": "\n".join(lines) + "\n", ".pages": f"title: {SORT[lang]}\n", **out}
    return pages


def main():
    check = "--check" in sys.argv
    drift = []
    for lang, files in build().items():
        d = ROOT / "docs" / lang / "decisions"
        for name, content in files.items():
            f = d / name
            if not f.is_file() or f.read_text(encoding="utf-8") != content:
                drift.append(str(f.relative_to(ROOT)))
                if not check:
                    d.mkdir(parents=True, exist_ok=True)
                    f.write_text(content, encoding="utf-8")
    if check and drift:
        print("stale (run scripts/gen_decisions.py):", *drift[:10], sep="\n  ")
        return 1
    print(f"decisions: {len(drift)} files {'stale' if check else 'written'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
