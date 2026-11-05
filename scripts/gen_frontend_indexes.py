#!/usr/bin/env python3
"""Generate and maintain frontend index pages (ADR 0012). Works on docs/en only (ADR 0011).

Replaces gen_skin_indexes.py. Idempotent: run after every change under frontends/.

Per category  programs/<level>/<category>/
    frontends/index.md        fully generated: table of programs, file set, links
    requirements.md           created once as a skeleton if missing (ADR 0006), then by hand
    index.md                  block between <!-- gen:frontends --> markers (replaces the
                              old "## Frontend documentation … Reference schema:" section)
Per program   frontends/<program>/index.md   (hand-written text is kept)
    - title "X Documentation" -> "X"; "## Overview" -> "## What it is"
    - "## Notable ideas" inserted as a to-do if missing (ADR 0013)
    - "## File structure…" replaced by the generated block "## Documented versions"
      (<!-- gen:versions --> markers): per version folder the file table, short
      descriptions taken over from the old file list, missing required files listed
Per version   --extract-themes: colour/typography/theme sections are moved out of
              layout.md into themes/default.md + themes/index.md

Options
    --check             exit 1 if anything would change (CI)
    --dry-run           report, write nothing
    --extract-themes    also do the layout.md -> themes/ move
    --suggest-versions FILE   write "program<TAB>version" candidates found in the texts
                              ("Currently documented version: **x**") for temp/frontend-versions.tsv
"""
import argparse
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROGRAMS = ROOT / "docs" / "en" / "programs"
LEVELS = ["apps", "suites", "platform"]

# ADR 0012 file set: (path inside the version folder, default description, required)
FILESET = [
    ("description.md", "Detailed description, differentiation, who it suits", True),
    ("features.md", "What the program can do — and what not", True),
    ("layout.md", "Window structure, regions, panels", True),
    ("menus.md", "Menu structure, context menus, menus by role", True),
    ("shortcuts.md", "Keyboard shortcuts", True),
    ("api.md", "APIs and protocols, authentication, rate limits", True),
    ("themes/index.md", "Themes: colours, typography, spacing — what can be rebuilt", True),
    ("interaction.md", "Hover, focus, drag, gestures (finger, mouse, pen)", False),
    ("states.md", "UI states and transitions", False),
    ("events.md", "Events to the outside (webhooks, push, streams)", False),
    ("limits.md", "Known limitations", False),
    ("i18n.md", "Localisation, writing direction", False),
    ("dependencies.md", "Which of our components a frontend in this style needs", False),
]
OLD_NAMES = {"menu.md": "menus.md", "structure.md": "layout.md"}

GEN_V = ("<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->",
         "<!-- /gen:versions -->")
GEN_C = ("<!-- gen:frontends (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->",
         "<!-- /gen:frontends -->")
NOTABLE_TODO = ("_To do: what does this program do that others don't? Why is it documented "
                "here (ADR 0013)?_")
THEME_HEAD = re.compile(r"^(#{2,4})\s+.*\b(colou?r|typograph|theme|dark mode)", re.I)
VERSION_RE = re.compile(r"Currently documented version:\**\s*(?:[A-Za-z][\w .-]*?\s)?\**v?(\d[\w.\-]*)\**")


# ------------------------------------------------------------------ helpers --
def sections(text):
    """Split markdown into [(heading_line or None, body)] at level-2 headings."""
    parts, cur_h, cur = [], None, []
    fence = False
    for line in text.splitlines(keepends=True):
        if re.match(r"^\s*(```|~~~)", line):
            fence = not fence
        if not fence and line.startswith("## "):
            parts.append((cur_h, "".join(cur)))
            cur_h, cur = line, []
        else:
            cur.append(line)
    parts.append((cur_h, "".join(cur)))
    return parts


def join(parts):
    return "".join((h or "") + b for h, b in parts)


def title_of(index_md, fallback):
    if index_md.is_file():
        for line in index_md.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^#\s+(.+?)\s*$", line)
            if m:
                return re.sub(r"\s*[–-]?\s*Documentation\s*$", "", m.group(1)).strip(" –-")
    return fallback


def blurb_of(index_md):
    """First sentence of the 'What it is'/'Overview' section or the intro."""
    if not index_md.is_file():
        return ""
    for h, body in sections(index_md.read_text(encoding="utf-8")):
        if h is None or re.match(r"## (What it is|Overview|Short profile)", h):
            for para in body.split("\n\n"):
                p = " ".join(l.strip() for l in para.splitlines()
                             if l.strip() and not l.lstrip().startswith(("#", ">", "-", "|", "<!--")))
                if p:
                    m = re.match(r"(.+?[.!?])(\s|$)", p)
                    s = (m.group(1) if m else p)
                    return s if len(s) <= 200 else s[:197] + "…"
    return ""


def version_dirs(prog_dir):
    return sorted(d.name for d in prog_dir.iterdir() if d.is_dir() and not d.name.startswith("."))


def write(path, text, args, changed):
    old = path.read_text(encoding="utf-8") if path.exists() else None
    if old == text:
        return
    changed.append(path.relative_to(ROOT).as_posix())
    if not (args.dry_run or args.check):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")


def replace_block(text, markers, block):
    pat = re.compile(re.escape(markers[0]) + r".*?" + re.escape(markers[1]), re.S)
    new = f"{markers[0]}\n{block.rstrip()}\n{markers[1]}"
    return pat.sub(lambda _: new, text, count=1) if pat.search(text) else None


# ---------------------------------------------------------------- program ---
def old_descriptions(body):
    """{filename: description} from an old hand list/table of files."""
    out = {}
    for line in body.splitlines():
        m = re.search(r"\[[^\]]*\]\((?:[\w.\-]+/)?([\w\-]+\.md)\)\s*(?:[-–|]\s*)?(.*?)\s*\|?\s*$", line)
        if m and m.group(2):
            name = OLD_NAMES.get(m.group(1), m.group(1))
            out[name] = m.group(2).strip(" |")
    return out


def versions_block(prog_dir, descs):
    vers = version_dirs(prog_dir)
    lines = []
    if not vers:
        lines += ["No version documented in English yet.", ""]
        return "\n".join(lines)
    lines += ["| Version | Required files present |", "|---------|------------------------|"]
    for v in vers:
        have = sum((prog_dir / v / f).is_file() for f, _, req in FILESET if req)
        total = sum(1 for _, _, req in FILESET if req)
        lines.append(f"| [{v}]({v}/description.md) | {have}/{total} |")
    for v in vers:
        lines += ["", f"### {v}", "", "| File | Contents |", "|------|----------|"]
        missing = []
        for f, default, req in FILESET:
            if (prog_dir / v / f).is_file():
                lines.append(f"| [{f}]({v}/{f}) | {descs.get(f, default)} |")
            elif req:
                missing.append(f)
        extra = sorted(p.relative_to(prog_dir / v).as_posix() for p in (prog_dir / v).rglob("*.md")
                       if p.relative_to(prog_dir / v).as_posix() not in {f for f, _, _ in FILESET}
                       and not p.relative_to(prog_dir / v).as_posix().startswith("themes/"))
        for f in extra:
            lines.append(f"| [{f}]({v}/{f}) | {descs.get(f, '')} |")
        if missing:
            lines += ["", "⚠️ Missing required files: " + ", ".join(f"`{m}`" for m in missing)]
    return "\n".join(lines)


def update_program(prog_dir, category_link, args, changed, report):
    idx = prog_dir / "index.md"
    if not idx.is_file():
        report.append(f"no index.md: {prog_dir.relative_to(PROGRAMS)}")
        return
    text = idx.read_text(encoding="utf-8")
    text = re.sub(r"^(#\s+.+?)[ \t]*[–-]?[ \t]*Documentation[ \t]*$", r"\1", text, count=1, flags=re.M)
    # repair: blank line after the category line (older runs ate it)
    text = re.sub(r"^(> Category: .*)\n(?!\n)", r"\1\n\n", text, count=1, flags=re.M)
    parts = sections(text)
    descs = {}
    out, placed = [], False
    for h, body in parts:
        if h and re.match(r"## Overview\s*$", h):
            h = "## What it is\n"
        if h and re.match(r"## File structure", h):
            descs.update(old_descriptions(body))
            out.append(("## Documented versions\n\n", "@@VERSIONS@@\n\n"))
            placed = True
            continue
        out.append((h, body))
    text = join(out)
    block = versions_block(prog_dir, descs)
    if "@@VERSIONS@@" in text:
        text = text.replace("@@VERSIONS@@", f"{GEN_V[0]}\n{block}\n{GEN_V[1]}")
    else:
        new = replace_block(text, GEN_V, block)
        if new is not None:
            text = new
        else:
            # insert before Sources, else at the end
            sec = f"## Documented versions\n\n{GEN_V[0]}\n{block}\n{GEN_V[1]}\n\n"
            m = re.search(r"^## Sources", text, re.M)
            text = text[:m.start()] + sec + text[m.start():] if m else text.rstrip() + "\n\n" + sec
    if not re.search(r"^## Notable ideas", text, re.M):
        notable = f"## Notable ideas\n\n{NOTABLE_TODO}\n\n"
        m = re.search(r"^## (?!What it is)", text, re.M)
        text = text[:m.start()] + notable + text[m.start():] if m else text.rstrip() + "\n\n" + notable
    if not re.search(r"^> Category:", text, re.M):
        text = re.sub(r"^(#\s+.+\n)", rf"\1\n> Category: [{category_link[0]}]({category_link[1]})\n",
                      text, count=1, flags=re.M)
    write(idx, text.rstrip() + "\n", args, changed)


def extract_themes(prog_dir, title, args, changed, report):
    for v in version_dirs(prog_dir):
        layout = prog_dir / v / "layout.md"
        if not layout.is_file():
            continue
        lines = layout.read_text(encoding="utf-8").splitlines(keepends=True)
        keep, taken, cut_level = [], [], None
        for line in lines:
            m = re.match(r"^(#{1,6})\s", line)
            if m and cut_level is not None and len(m.group(1)) <= cut_level:
                cut_level = None
            if cut_level is None and THEME_HEAD.match(line):
                cut_level = len(THEME_HEAD.match(line).group(1))
            (taken if cut_level is not None else keep).append(line)
        if not taken:
            continue
        tdir = prog_dir / v / "themes"
        default = tdir / "default.md"
        if default.exists():
            report.append(f"themes/default.md exists, not touched: {default.relative_to(PROGRAMS)}")
            continue
        body = "".join(taken)
        body = re.sub(r"^#{2,4}\s", "## ", body, flags=re.M)
        write(default, f"# {title} {v} — Theme \"default\"\n\n"
                       "Moved from `layout.md` (ADR 0012). Values are described, not copied (ADR 0013).\n\n"
              + body.rstrip() + "\n", args, changed)
        write(tdir / "index.md", f"# {title} {v} — Themes\n\n"
              "What can be rebuilt with FreeSynergy theming and what not.\n\n"
              "| Theme | File | Rebuildable |\n|-------|------|-------------|\n"
              "| default | [default](default.md) | ⚠️ not assessed yet |\n", args, changed)
        keep.append("\n## Themes\n\nColours, typography and theme details: see [themes](themes/index.md).\n")
        write(layout, "".join(keep).rstrip() + "\n", args, changed)


# --------------------------------------------------------------- category ---
def category_page(level, cat, progs):
    lines = [f"# {cat.capitalize()} — Frontends", "",
             "Frontends of well-known programs in this category, analysed for their **functions** — "
             "nothing is copied (ADR 0013). A program is documented here because it is widely learned "
             "or because it has a notable idea. Our own program for this category is "
             f"`FreeSynergy.{cat.capitalize()}` (ADR 0017); its capabilities and status live in "
             "[requirements](../requirements.md).", "",
             "## Programs", "",
             "| Program | Versions | What it is |", "|---------|----------|------------|"]
    for p, title, blurb, vers in progs:
        v = ", ".join(f"[{x}]({p}/{x}/description.md)" for x in vers) or "—"
        lines.append(f"| [{title}]({p}/index.md) | {v} | {blurb} |")
    lines += ["", "## File set per program (ADR 0012)", "", "```",
              f"programs/{level}/{cat}/frontends/<program>/",
              "├── index.md        what it is, notable ideas, documented versions, sources",
              "├── changelog.md    changes between documented versions (≥ 2 versions)",
              "└── <version>/"]
    for i, (f, d, req) in enumerate(FILESET):
        branch = "└──" if i == len(FILESET) - 1 else "├──"
        lines.append(f"    {branch} {f:<17} {'required' if req else 'if needed'} · {d}")
    lines += ["```", "", "Protocols (Matrix, IMAP, CalDAV, …) are not frontends; they are described "
              "under [data](../../../../data/standards.md).", ""]
    return "\n".join(lines)


def requirements_stub(cat):
    """Created once if missing (ADR 0006 §4); afterwards maintained by hand."""
    name = cat.capitalize()
    return f"""# {name} — Requirements

What `FreeSynergy.{name}` must and can do, derived from the [frontends](frontends/index.md)
(ADR 0006, 0013). Each capability names its data standard (ADR 0014) and our status.

Status: `implemented` · `planned` · `proposed`

## Required (common to the analysed programs)

| Capability | Seen in | Data / standard | Status |
|------------|---------|-----------------|--------|

## Optional (notable ideas)

| Capability | Seen in | Data / standard | Status |
|------------|---------|-----------------|--------|

## Not planned (deliberately)
"""


def category_block(level, cat, progs):
    links = "\n".join(f"- [{t}](frontends/{p}/index.md)" + (f" — {b}" if b else "")
                      for p, t, b, _ in progs)
    return (f"Analysed programs ({len(progs)}), by function, nothing copied (ADR 0012/0013):\n\n"
            f"{links}\n\nOverview: [frontends](frontends/index.md)")


def update_category(level, cat, args, changed, report, suggestions):
    cat_dir = PROGRAMS / level / cat
    fdir = cat_dir / "frontends"
    if not fdir.is_dir():
        return
    progs = []
    for p in sorted(d.name for d in fdir.iterdir() if d.is_dir()):
        pdir = fdir / p
        idx = pdir / "index.md"
        title = title_of(idx, p)
        if args.extract_themes:
            extract_themes(pdir, title, args, changed, report)
        update_program(pdir, (cat, "../../index.md"), args, changed, report)
        if idx.is_file():
            m = VERSION_RE.search(idx.read_text(encoding="utf-8"))
            if m:
                suggestions[p] = m.group(1).rstrip(".")
        progs.append((p, title, blurb_of(idx), version_dirs(pdir)))
    write(fdir / "index.md", category_page(level, cat, progs), args, changed)
    req = cat_dir / "requirements.md"
    if not req.exists():
        write(req, requirements_stub(cat), args, changed)
    ci = cat_dir / "index.md"
    if ci.is_file():
        text = ci.read_text(encoding="utf-8")
        block = category_block(level, cat, progs)
        new = replace_block(text, GEN_C, block)
        if new is None:
            sec = f"## Frontends\n\n{GEN_C[0]}\n{block}\n{GEN_C[1]}\n"
            old = re.compile(r"^## (Frontend|Mask|Skin) documentation.*?Reference schema:.*?$\n?",
                             re.S | re.M | re.I)
            new = old.sub(lambda _: sec, text, count=1) if old.search(text) else text.rstrip() + "\n\n" + sec
        write(ci, new, args, changed)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--extract-themes", action="store_true")
    ap.add_argument("--suggest-versions")
    args = ap.parse_args()

    changed, report, suggestions = [], [], {}
    for level in LEVELS:
        base = PROGRAMS / level
        if base.is_dir():
            for cat in sorted(d.name for d in base.iterdir() if d.is_dir()):
                update_category(level, cat, args, changed, report, suggestions)

    print(f"files {'to change' if (args.dry_run or args.check) else 'changed'}: {len(changed)}")
    for c in changed[:15]:
        print("  " + c)
    if len(changed) > 15:
        print(f"  … {len(changed) - 15} more")
    for r in report:
        print("note: " + r)
    if args.suggest_versions:
        Path(args.suggest_versions).write_text(
            "".join(f"{p}\t{v}\n" for p, v in sorted(suggestions.items())), encoding="utf-8")
        print(f"version suggestions: {len(suggestions)} -> {args.suggest_versions}")
    return 1 if (args.check and changed) else 0


if __name__ == "__main__":
    sys.exit(main())
