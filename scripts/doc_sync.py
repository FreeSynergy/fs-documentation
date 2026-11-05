#!/usr/bin/env python3
"""
doc_sync.py – EN/DE Documentation Tree Sync Checker + translation queue
State-machine based. The state file is the single source of truth; the markdown
queue (--list) is a render of it and can be regenerated at any time.

States per file:
  PENDING  – needs review (new, or changed since last verification)
  VERIFIED – reviewed and OK; stays quiet until a hash changes

Transitions (automatic, no manual verify/unverify):
  File not in state          → PENDING
  Hash changed (either side) → PENDING
  AI confirms OK             → VERIFIED  (via --confirm)
  Hash unchanged + VERIFIED  → stays VERIFIED (untouched)

Work kinds (why a file is PENDING) – these drive the queue sections:
  needs_en    – path exists in de/ only  → translate de → en
  needs_de    – path exists in en/ only  → draw de alongside en
  en_german   – both sides exist, en/ still carries German prose → finish en
  de_english  – both sides exist, de/ still carries English prose → finish de
  copy        – en/ byte-identical to de/ → untranslated copy
  parity      – structural mismatch between the two sides (headings/tables/links)
  review      – nothing detected, both sides exist → confirm after reading

This is the only translation checker for the tree (ADR 0010). Former helpers
(find_german_prose, find_untranslated*, check-translation.sh, check-box-width,
boxgen, update-progress, mark-progress, translate-index-templates) are archived
in scripts/_archive/; extend this script instead of adding another one.

Usage:
    # scan + regenerate the list
    python3 scripts/doc_sync.py --en docs/en --de docs/de \
        --state temp/sync_state.json --list temp/translation-queue.md

    # after reviewing/translating a file – this is what clears it from the list
    python3 scripts/doc_sync.py ... --confirm data/contacts.md --note "translated de->en"
    python3 scripts/doc_sync.py ... --unconfirm data/contacts.md

    # machine-readable
    python3 scripts/doc_sync.py ... --json

    # box frames: shape EN lines like the DE frame, or repair existing ones
    python3 scripts/doc_sync.py ... --gen-box path.md --cell "Save|Close"
    python3 scripts/doc_sync.py ... --fix-boxes path.md

Exit: 1 while files are PENDING, 0 when everything is VERIFIED, 2 on bad paths.
Not wired into CI on purpose – it reports open translations, so a hard exit
would be noise; check_components.py stays the CI checker for form.
"""

import re
import json
import hashlib
import argparse
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict


# ─── Language Detection ──────────────────────────────────────────────────────
#
# Words that are identical (or near-identical) in EN and DE are NOT evidence of
# anything: "in", "an", "auf", "bei", "mit", "was", "war", "will", "man", "nur"
# all appear in correct English *and* correct German prose. The original word
# lists counted them, which made every clean file look suspicious. They live in
# CROSS_LANGUAGE and are dropped from both sides.

CROSS_LANGUAGE = {
    "in", "an", "auf", "bei", "mit", "nur", "man", "was", "war", "will", "would",
    "may", "so", "also", "aus", "vor", "nach", "gegen", "ohne", "bis",
    "element", "elemente", "struktur", "auto", "daten", "bereich", "bereiche",
    "wert", "werte", "werten", "feld", "felder", "punkt", "punkte", "datum",
    "events", "links", "aktiv", "optionen", "typ", "typen", "plan", "filter",
    "status", "text", "texts", "design", "objekt", "objekte", "detail",
    "details", "info", "infos", "version", "client", "server", "host", "cache",
    "index", "monitor", "protokoll", "medium", "medien", "symbol", "symbole",
    "speicher", "kanal", "kanale", "form", "formen", "gruppe", "gruppen",
}

GERMAN_WORDS = {
    "und", "der", "die", "das", "dem", "den", "des", "ein", "eine", "einen",
    "einem", "einer", "eines", "ist", "sind", "waren", "wird", "werden",
    "wurde", "wurden", "kann", "können", "muss", "müssen", "soll", "sollen",
    "dürfen", "nicht", "auch", "oder", "aber", "wenn", "dann", "für", "von",
    "zur", "zum", "vom", "im", "am", "über", "unter", "zwischen", "während",
    "dass", "ob", "weil", "diese", "dieser", "dieses", "jeder", "jede",
    "jedes", "siehe", "beschreibung", "verwendung", "verwendungszweck",
    "beispiel", "beispiele", "eigenschaften", "zustände", "hinweis",
    "hinweise", "komponente", "komponenten", "anwendung", "einsatz", "aufbau",
    "unterscheidung", "verwechslung", "übersicht", "weiterführende",
    "kategorie", "kategorien", "erbt", "verwandt", "dokumentiert", "kein",
    "keine", "sowie", "etwa", "jeweils", "dabei", "dadurch", "daher",
    "danach", "bevor", "durch", "gegenüber", "oben", "unten", "links",
    "rechts", "immer", "bzw", "usw", "deswegen", "ebenso", "bereits",
    "welche", "etwas", "sehr", "beste", "aussehen", "größe", "größen",
    "höhe", "farbe", "farben", "verhalten", "effekte", "barrierefreiheit",
    "geerbt", "hauptattribute", "darstellung", "variante", "varianten",
    "grundlayout", "menüleiste", "menüpunkt", "menüpunkte", "einklappbar",
    "ausgegraut", "aktionen", "auswahl", "einstellungen", "werkzeugleiste",
    "seitenleiste", "bereit", "fehler", "geladen", "leer", "klein", "groß",
    "schnell", "einfach", "speichern", "löschen", "öffnen", "schließen",
    "bearbeiten", "abbruch", "bestätigen", "vorschau", "vorschlag",
    "beschriftung", "einordnung", "szenarien", "merkmale", "abgrenzung",
    "einträge", "eintrag", "fläche", "flächen", "klick", "klickt",
    "auflösung", "benutzer", "eigene", "eigener", "eigenes", "eigenen",
    "sondern", "wobei", "damit", "mehrere", "einzelne", "deutlich",
    "dauerhaft", "bleibt", "bleiben", "gewählt", "getroffen", "gestellt",
    "gesetzt", "gelöscht", "verlassen", "verwenden", "verwendet",
    "vorhanden", "verschiedene", "verbessern", "vollständig", "wichtig",
    "wichtige", "zusammen", "zurück", "zurückkehrt", "zeigen", "zeigt",
    "ziehen", "setzen", "setzt", "suchen", "starten", "stellen", "stellt",
    "laufen", "legen", "legt", "lesen", "laden", "halten", "hält",
    "gehen", "geht", "folgen", "folgt", "fahren", "denken", "brauchen",
    "braucht", "bedienen", "bedient", "achten", "öffnet", "schließt",
    "läuft", "bekommt", "bekommen", "erreicht", "ermöglicht", "erlaubt",
    "erzeugt", "enthält", "entscheidet", "ergänzt", "erhöht", "verhindert",
    "verhindern", "verursacht", "vergleichen", "verschieben", "verstärkt",
    "verteilt", "versteckt", "wählen", "wählt", "zusätzlich", "zurzeit",
    "bitte", "vielen", "danke", "leider", "natürlich", "genau", "gerne",
    "allerdings", "insbesondere", "sollte", "sollten", "wäre", "könnte",
    "möchte", "gibt", "gegeben", "folgende", "folgenden",
    "nötig", "außerhalb", "darüber", "darunter", "häufige", "übergeben",
    "ausgewählt", "ausgewählter", "gewählten", "gefüllt", "geöffnet",
    "geschlossen", "gehalten", "übersteht", "überall", "ausschließender",
    "schlüsselbasierte", "häkchen", "hinzufügen",
}

ENGLISH_WORDS = {
    "the", "is", "are", "was", "were", "been", "being", "this", "that",
    "these", "those", "with", "from", "into", "onto", "upon", "could",
    "shall", "should", "might", "must", "has", "have", "had", "does", "did",
    "done", "each", "every", "any", "such", "another", "less", "least",
    "very", "than", "then", "when", "where", "which", "who", "whom",
    "whose", "how", "what", "because", "since", "although", "however",
    "therefore", "please", "thank", "thanks", "sorry", "really", "just",
    "still", "already", "yet", "even", "only", "quite", "rather", "about",
    "would", "their", "there", "they", "them", "your", "ours", "here",
    "while", "within", "without",
}

GERMAN_WORDS -= CROSS_LANGUAGE
ENGLISH_WORDS -= CROSS_LANGUAGE

# English has no umlauts or sz at all, so a umlaut anywhere in a word is German
# evidence – including at the word start ("ändern", "Änderung").
UMLAUT_INSIDE = re.compile(r"[äöüßÄÖÜ]")
FENCE = re.compile(r"^\s*(```|~~~)")
BOX_ART = re.compile(r"^\s*[┌└├─│╔═╒╞╛╭╰╮┐]")
COMMENTISH = re.compile(r"^\s*(//|;|<!--|%)")
WORD_RE = re.compile(r"[A-Za-zÄÖÜäöüß]+")
# single-line inline code; must not match a fence opening, see declared_names()
INLINE_CODE = re.compile(r"(?<!`)`([^`\n]+)`(?!`)")
BOLD_SPAN = re.compile(r"\*\*[^*]+\*\*")

# Closed-class German: articles, pronouns, prepositions, conjunctions, adverbs.
# Proper names are almost never one of these, so they are safe evidence even
# inside sample data – unlike nouns such as "Klein" or "Müller".
GERMAN_FUNC = {
    "der", "die", "das", "dem", "den", "des", "ein", "eine", "einen", "einem",
    "einer", "und", "oder", "aber", "nicht", "ist", "sind", "war", "waren",
    "wird", "werden", "wurde", "wurden", "für", "mit", "von", "zur", "zum",
    "vom", "im", "am", "auf", "aus", "bei", "nach", "vor", "über", "unter",
    "als", "diese", "dieser", "dieses", "kein", "keine", "sowie", "dann",
    "wenn", "weil", "dass", "ob", "sondern", "wobei", "damit", "dadurch",
    "daher", "jeweils", "bereits", "etwa", "sehr", "auch", "immer", "hier",
    "danach", "hierzu", "hierfür", "ihre", "sein", "seine", "ihr", "unsere",
    "können", "muss", "müssen", "soll", "sollen", "sollte", "dürfen", "wäre",
    "könnte", "hat", "haben", "hatte", "hätte", "bitte", "danke", "leider",
}


def prose_lines(text: str):
    """Yield (lineno, prose_only_text) outside code fences and diagram art,
    with inline identifiers stripped (backticks, bold variant/state names)."""
    in_fence = False
    for i, line in enumerate(text.splitlines(), 1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence or BOX_ART.match(line) or COMMENTISH.match(line):
            continue
        line = INLINE_CODE.sub("", line)   # identifiers stay German (ADR 0002)
        line = BOLD_SPAN.sub("", line)     # variant / state names
        if not line.strip():
            continue
        yield i, line


def identifier_tokens(text: str) -> set:
    """Tokens used as identifiers/values (code fences + inline code). A word that
    also occurs there is a name or a value, not untranslated prose – this keeps
    proper nouns such as `Tübingen` from being reported as German."""
    toks = set()
    in_fence = False
    for line in text.splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            for w in WORD_RE.findall(line):
                toks.add(w.lower())
        for span in INLINE_CODE.findall(line):
            for w in WORD_RE.findall(span):
                toks.add(w.lower())
    return toks


def declared_names(text: str) -> set:
    """Identifiers declared *outside* code blocks: inline `code` spans and **bold**
    table cells. Those stay German on purpose (ADR 0002), so inside a code example
    they are exempt – but the surrounding example text is not.

    The inline pattern must not match a fence opening (``` ```jsx ```): a naive
    `` `[^`]+` `` pairs with the next fence and swallows the whole block, which
    silently exempts every German word in it."""
    toks = set()
    in_fence = False
    for line in text.splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for span in INLINE_CODE.findall(line) + BOLD_SPAN.findall(line):
            for w in WORD_RE.findall(span):
                toks.add(w.lower())
    return toks


# Quoted material is evidence, not prose to translate: German product UI labels in
# en/ docs and English spec/RFC sentences in de/ docs are intentional (ADR 0002/0006).
# Typical quotes, straight quotes, guillemets. Nested glosses are covered because the
# pattern is non-greedy and applied repeatedly.
QUOTED = re.compile(
    r"(\u201e[^\u201c\"]*[\u201c\"]"   # „…“ (mixed closing quote is used in this repo)
    r"|\u201c[^\u201d]*\u201d"        # “…“
    r"|\u00ab[^\u00bb]*\u00bb"        # «…»
    r"|\"[^\"]*\""                    # "…"
    r"|'[^']*')"                      # '…'
)


def unquote(line: str) -> str:
    """Blank out quoted spans so quotes do not count as wrong-language prose."""
    prev = None
    while prev != line:
        prev = line
        line = QUOTED.sub(lambda m: " " * len(m.group(0)), line)
    return line


def detect_code_language(text: str, names: frozenset = frozenset()) -> list[dict]:
    """German inside code examples and box art of an EN file. ADR 0002 keeps code
    English, so labels, strings and comments in a code example are translation
    debt. Words declared as identifiers outside the block (inline code, bold
    table cells) stay exempt; a word that is only known from the block itself is
    sample data and counts as weak unless it is closed-class German."""
    findings = []
    in_fence = False
    for i, line in enumerate(text.splitlines(), 1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if not (in_fence or BOX_ART.match(line)):
            continue
        for w in WORD_RE.findall(line):
            wl = w.lower()
            if wl in names or wl in CROSS_LANGUAGE:
                continue
            if wl in GERMAN_FUNC:
                findings.append({"line": i, "word": w, "strength": "strong",
                                 "reason": f"German in code/example → \"{w}\""})
                break
            if wl in GERMAN_WORDS and w[0].islower():
                findings.append({"line": i, "word": w, "strength": "strong",
                                 "reason": f"German word in code → \"{w}\""})
                break
            if UMLAUT_INSIDE.search(w) and w[0].islower():
                findings.append({"line": i, "word": w, "strength": "strong",
                                 "reason": f"German word in code → \"{w}\""})
                break
            if wl in GERMAN_WORDS or UMLAUT_INSIDE.search(w):
                findings.append({"line": i, "word": w, "strength": "weak",
                                 "reason": f"possibly German in code → \"{w}\""})
                break
    return findings


def detect_suspicion(text: str, expected_lang: str, names: frozenset = frozenset()) -> list[dict]:
    """Find prose that is in the wrong language for this side of the tree."""
    findings = []
    for i, raw in prose_lines(text):
        if s_skip(raw):
            continue
        line = unquote(raw)
        if not line.strip():
            continue
        words = [w.lower() for w in WORD_RE.findall(line)]
        if expected_lang == "en":
            hits = [w for w in words if w in GERMAN_WORDS]
            umlauts = [w for w in WORD_RE.findall(line) if UMLAUT_INSIDE.search(w)]
            if len(hits) >= 2:
                findings.append({"line": i, "words": hits, "strength": "strong",
                                 "reason": f"DE prose in EN: {hits[:6]}"})
            elif len(hits) == 1:
                findings.append({"line": i, "words": hits, "strength": "weak",
                                 "reason": f"DE word in EN: {hits[0]}"})
            if umlauts:
                for w in umlauts[:4]:
                    if w.lower() in names:
                        continue          # name/value also used in code – not prose
                    findings.append({"line": i, "word": w, "strength": "strong",
                                     "reason": f"German umlaut in EN word → \"{w}\""})
        elif expected_lang == "de":
            hits = [w for w in words if w in ENGLISH_WORDS]
            if len(hits) >= 3:
                findings.append({"line": i, "words": hits, "strength": "strong",
                                 "reason": f"EN prose in DE: {hits[:6]}"})
    return findings


def s_skip(line: str) -> bool:
    s = line.strip()
    return s.startswith(("http://", "https://", "./", "../", "/", "www."))


def suspicion_score(findings: list[dict]) -> int:
    """Weighted line-level severity: strong evidence dominates weak hits."""
    strong = {f["line"] for f in findings if f["strength"] == "strong"}
    weak = {f["line"] for f in findings if f["strength"] == "weak"}
    return len(strong) * 2 + len(weak - strong)


# ─── Structural Parity ───────────────────────────────────────────────────────

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)")
HEADING_RE = re.compile(r"^(#{1,6})\s+\S", re.M)


def norm_link(target: str) -> str:
    """Link target without anchor/query, language tree stripped (CONVENTIONS §9)."""
    t = target.split("#")[0].split("?")[0]
    t = re.sub(r"^\.\./+", "", t).lstrip("/")
    t = re.sub(r"^(en|de)/", "", t)
    return t.rstrip("/")


def parity(en_text: str, de_text: str) -> list[str]:
    """Structural comparison: same shape on both sides? Text length is not
    compared – DE prose is routinely 10–20 % longer than EN."""
    diffs = []
    h_en, h_de = len(HEADING_RE.findall(en_text)), len(HEADING_RE.findall(de_text))
    if h_en != h_de:
        diffs.append(f"headings {h_en} vs {h_de}")
    t_en = sum(1 for l in en_text.splitlines() if l.strip().startswith("|"))
    t_de = sum(1 for l in de_text.splitlines() if l.strip().startswith("|"))
    if t_en != t_de:
        diffs.append(f"table rows {t_en} vs {t_de}")
    l_en = {norm_link(m) for m in LINK_RE.findall(en_text)}
    l_de = {norm_link(m) for m in LINK_RE.findall(de_text)}
    only_en, only_de = sorted(l_en - l_de), sorted(l_de - l_en)
    if only_en or only_de:
        diffs.append(f"links en-only={only_en[:3]} de-only={only_de[:3]}")
    n_en = len([1 for l in en_text.splitlines() if l.strip()])
    n_de = len([1 for l in de_text.splitlines() if l.strip()])
    if max(n_en, n_de) and abs(n_en - n_de) / max(n_en, n_de) > 0.45:
        diffs.append(f"line count {n_en} vs {n_de}")
    # ASCII boxes: a frame renders broken when its lines differ in width. Only
    # report it when en/ is worse than de/ – most width drift predates the
    # translation and exists on both sides, so it is not a sync finding.
    b_en, b_de = broken_boxes(en_text), broken_boxes(de_text)
    if b_en > b_de:
        diffs.append(f"box frames broken en={b_en} de={b_de}")
    return diffs


def box_runs(text: str) -> list[list[int]]:
    """Widths per box: one entry per run of consecutive box-drawing lines.
    Per-run matters – a file usually holds several frames of different widths,
    and one file-wide width would blow the small frames up."""
    runs, run = [], []
    for line in text.splitlines():
        if BOX_ART.match(line.rstrip("\n")):
            run.append(len(line))
        else:
            if run:
                runs.append(run)
            run = []
    if run:
        runs.append(run)
    return runs


BOX_CLOSE = ("│", "┤", "┘", "├", "┐", "┬", "┴", "╢", "╛", "╝", "╣", "╕")
# opening char -> the closing char the line is missing when it has none
BOX_OPENER_CLOSE = {"│": "│", "└": "┘", "┌": "┐", "├": "┤",
                    "╰": "╯", "╭": "╮", "╞": "╡"}


def box_run_spans(text: str) -> list[tuple[int, int]]:
    """(start, end) line indices of each box run, end exclusive."""
    spans, start = [], None
    for i, line in enumerate(text.splitlines()):
        if BOX_ART.match(line.rstrip("\n")):
            if start is None:
                start = i
        elif start is not None:
            spans.append((start, i))
            start = None
    if start is not None:
        spans.append((start, len(text.splitlines())))
    return spans


def fix_box_width(path: Path, targets: list[int]) -> int:
    """Normalise each box of `path` to the width of the same-positioned box in
    `targets` (the DE file's per-run widths, document order). Extra EN runs keep
    their own dominant width.

    Padding goes just before the closing box character; a line missing one gets it
    appended – padding before the opening character would push the frame inward."""
    lines = path.read_text(encoding="utf-8").split("\n")
    changed = 0
    for n, (start, end) in enumerate(box_run_spans("\n".join(lines))):
        widths = [len(lines[i]) for i in range(start, end)]
        width = targets[n] if n < len(targets) else max(set(widths), key=widths.count)
        for i in range(start, end):
            if len(lines[i]) == width:
                continue
            body = lines[i].rstrip()
            if body and body[-1] in BOX_CLOSE:
                prefix = body[:body.rindex(body[-1])]
                prefix = prefix[: max(0, width - 1)]   # trim: drop padding, not text
                lines[i] = prefix + " " * max(0, width - len(prefix) - 1) + body[-1]
            else:
                close = BOX_OPENER_CLOSE.get(body.lstrip()[:1], "│")
                lines[i] = body + " " * max(0, width - len(body) - 1) + close
            changed += 1
    path.write_text("\n".join(lines), encoding="utf-8")
    return changed


def gen_box_lines(de_text: str, cells: list) -> list[str]:
    """Build box body lines for the EN side, mirroring the DE frame widths and
    column segments (replaces temp/boxgen.py). A cell is either a whole inner
    string or a tuple of column texts; text longer than its column is cut, so the
    EN frame cannot drift out of shape."""
    de_lines = de_text.split("\n")
    widths = [len(l) for l in de_lines if BOX_ART.match(l)]
    if not widths:
        return []
    # first box line carrying a T-junction defines the column widths; that is
    # usually the top border (┌──┬──┐) rather than a middle rule (├──┼──┤)
    rule = next((l for l in de_lines if BOX_ART.match(l) and ("┬" in l or "┼" in l)), None)
    segs = None
    if rule:
        segs, cur = [], 0
        for ch in rule[1:-1]:
            if ch in ("┬", "┴"):
                segs.append(cur)
                cur = 0
            else:
                cur += 1
        segs.append(cur)
    out = []
    for k, c in enumerate(cells):
        w = widths[k] if k < len(widths) else widths[0]
        if isinstance(c, tuple):
            if not segs or len(c) != len(segs):
                raise SystemExit(f"cell {k}: {len(c)} columns but {len(segs) if segs else 0} segments in DE")
            line = "│"
            for i, t in enumerate(c):
                t = t[: segs[i]]
                line += t + " " * (segs[i] - len(t)) + "│"
            line = line.rstrip()
            out.append(line + " " * max(0, w - len(line)))
        else:
            c = c[: w - 2]
            out.append("│" + c + " " * (w - 2 - len(c)) + "│")
    return out


def broken_boxes(text: str) -> int:
    """Count box runs whose lines are not all the same width."""
    return sum(1 for run in box_runs(text) if len(set(run)) > 1)


# ─── File Scanning ───────────────────────────────────────────────────────────

def scan_tree(root: Path) -> dict[str, dict]:
    """Return {rel_path: {hash, bytes}} for all .md files.

    No mtime on purpose: it changes on every checkout without changing content,
    which would churn the committed state file on each run."""
    result = {}
    for f in root.rglob("*.md"):
        rel = f.relative_to(root).as_posix()
        data = f.read_bytes()
        result[rel] = {
            "hash": hashlib.sha256(data).hexdigest()[:16],
            "bytes": len(data),
        }
    return result


# ─── State Machine ───────────────────────────────────────────────────────────

def load_state(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {"entries": {}}


# derived every run by classify(); storing them would rewrite ~35 % of the state
# file on every detector-rule change and bloat git history for no benefit
DERIVED_FIELDS = ("suspicion", "code_suspicion", "parity",
                  "en_german_score", "de_english_score")
HISTORY_KEEP = 15


def save_state(path: Path, state: dict):
    """Persist the state machine only. Findings/parity/scores are recomputed on
    every run and still reach --list, --json and the console report in full."""
    state["last_run"] = datetime.now(timezone.utc).isoformat()
    slim = {k: v for k, v in state.items() if k != "entries"}
    slim["entries"] = {}
    for p, e in state["entries"].items():
        keep = {k: v for k, v in e.items() if k not in DERIVED_FIELDS}
        if len(keep.get("history", [])) > HISTORY_KEEP:
            keep["history"] = keep["history"][-HISTORY_KEEP:]
        slim["entries"][p] = keep
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(slim, indent=2, ensure_ascii=False), encoding="utf-8")


def update_state(en_scan: dict, de_scan: dict, state: dict) -> dict:
    """
    Core state machine. For each file:
      - Not in state → PENDING
      - In state, VERIFIED, but hash changed (either side) → PENDING
      - In state, VERIFIED, hashes unchanged → stays VERIFIED
      - In state, PENDING → stays PENDING (unless confirmed externally)
    """
    all_paths = sorted(set(en_scan) | set(de_scan))
    entries = state.setdefault("entries", {})
    now = datetime.now(timezone.utc).isoformat()

    for p in all_paths:
        en_info, de_info = en_scan.get(p), de_scan.get(p)
        en_hash = en_info["hash"] if en_info else None
        de_hash = de_info["hash"] if de_info else None

        if p not in entries:
            # NEW file → PENDING
            entries[p] = {
                "status": "PENDING",
                "en_hash": en_hash,
                "de_hash": de_hash,
                "first_seen": now,
                "last_verified": None,
                "suspicion": [],
                "kind": [],
                "note": None,
                "history": [],
            }
        else:
            e = entries[p]
            hash_changed = (
                (en_hash and e.get("en_hash") != en_hash) or
                (de_hash and e.get("de_hash") != de_hash) or
                (en_hash is None and e.get("en_hash") is not None) or
                (de_hash is None and e.get("de_hash") is not None)
            )
            if e["status"] == "VERIFIED" and hash_changed:
                # Was verified, but content changed → back to PENDING
                e["status"] = "PENDING"
                e["last_verified"] = None
                e["change_reason"] = "hash changed since verification"
                e["history"].append({"at": now, "event": "hash changed → PENDING"})
            e["en_hash"] = en_hash
            e["de_hash"] = de_hash

    # Keep tombstones for files that no longer exist on either side
    for p in entries.copy():
        if p not in all_paths and entries[p]["status"] != "DELETED":
            entries[p]["status"] = "DELETED"
            entries[p]["history"].append({"at": now, "event": "file gone → DELETED"})

    return state


def classify(entries: dict, en_scan: dict, de_scan: dict,
             en_root: Path, de_root: Path) -> None:
    """Fill kind/suspicion/parity for every PENDING entry."""
    for p, e in entries.items():
        if e["status"] != "PENDING":
            e["kind"] = []
            continue
        kinds = []
        findings: list[dict] = []
        code: list[dict] = []
        en_text = de_text = None
        if p not in en_scan:
            kinds.append("needs_en")
        if p not in de_scan:
            kinds.append("needs_de")
        if p in en_scan:
            en_text = (en_root / p).read_text(encoding="utf-8", errors="replace")
            findings += detect_suspicion(en_text, "en", frozenset(identifier_tokens(en_text)))
            # Code examples are checked on the en side only: German sample strings in
            # de/ are the established convention, German ones in en/ are leftovers.
            code += detect_code_language(en_text, frozenset(declared_names(en_text)))
        if p in de_scan:
            de_text = (de_root / p).read_text(encoding="utf-8", errors="replace")
            findings += detect_suspicion(de_text, "de", frozenset(identifier_tokens(de_text)))

        en_score = suspicion_score([f for f in findings
                                    if f["reason"].startswith(("DE prose", "German umlaut", "DE word"))])
        de_score = suspicion_score([f for f in findings if f["reason"].startswith("EN prose")])
        e["en_german_score"] = en_score
        e["de_english_score"] = de_score
        if en_score >= 2:
            kinds.append("en_german")
        if de_score >= 2:
            kinds.append("de_english")
        if any(f["strength"] == "strong" for f in code):
            kinds.append("code_german")
        if en_text is not None and de_text is not None:
            if e["en_hash"] == e["de_hash"]:
                kinds.append("copy")
            pdiffs = parity(en_text, de_text)
            e["parity"] = pdiffs
            if pdiffs and "needs_en" not in kinds and "needs_de" not in kinds:
                kinds.append("parity")
            if not kinds:
                kinds.append("review")
        else:
            e["parity"] = []

        if is_german_name(p):
            kinds.append("rename")
        e["kind"] = kinds
        e["suspicion"] = findings
        e["code_suspicion"] = code


# ─── Report (console) ────────────────────────────────────────────────────────

def print_report(state: dict, en_scan: dict, de_scan: dict, verbose: bool = False):
    entries = state["entries"]
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    pending = {p: e for p, e in entries.items() if e["status"] == "PENDING"}
    verified = {p: e for p, e in entries.items() if e["status"] == "VERIFIED"}
    deleted = {p: e for p, e in entries.items() if e["status"] == "DELETED"}

    kinds = defaultdict(int)
    for e in pending.values():
        for k in e.get("kind", []):
            kinds[k] += 1

    print("=" * 80)
    print(f"  DOC SYNC  |  {now}")
    print(f"  📊 {len(entries)} tracked | ⏳ {len(pending)} pending | "
          f"✅ {len(verified)} verified | 🗑️ {len(deleted)} deleted")
    order = ["needs_en", "needs_de", "en_german", "code_german", "de_english",
             "copy", "parity", "rename", "review"]
    print("  work kinds: " + " · ".join(f"{k}={kinds[k]}" for k in order if kinds[k]))
    print("=" * 80)

    if pending:
        print(f"\n  ⏳ PENDING ({len(pending)}) – needs review\n")
        print(f"  {'File':<58} {'EN':<4} {'DE':<4} {'Kinds'}")
        print(f"  {'─'*58} {'─'*4} {'─'*4} {'─'*30}")
        for p, e in sorted(pending.items(), key=lambda kv: (kind_rank(kv[1]), kv[0])):
            en_mark = "✓" if p in en_scan else "✗"
            de_mark = "✓" if p in de_scan else "✗"
            print(f"  {p:<58} {en_mark:<4} {de_mark:<4} {','.join(e.get('kind', []))}")
        print()

    if verified and verbose:
        print(f"  ✅ VERIFIED ({len(verified)}) – quiet, no action needed\n")
        for p, e in sorted(verified.items()):
            lv = (e.get("last_verified") or "?")[:10]
            print(f"  {p:<58} verified {lv}")
        print()

    if deleted and verbose:
        print(f"  🗑️  DELETED ({len(deleted)})\n")
        for p in sorted(deleted):
            print(f"  {p}")
        print()

    print("=" * 80)


# Dateinamen muessen englisch sein (ADR 0002) – deutsches Wort oder Umlaut im Namen ist ein Befund
GERMAN_NAME_STEMS = GERMAN_WORDS | {
    "beschreibung", "speicherung", "grundlagen", "rückgabe", "ruckgabe", "einordnung",
    "zuordnung", "übersicht", "uebersicht", "hinweise", "beispiele", "felder", "formate",
    "modelle", "mappings", "standards", "anforderungen", "konventionen", "verwendung",
}
_NAME_WORDS = re.compile(r"[a-zäöüß]+")


def is_german_name(rel_path: str) -> bool:
    stem = rel_path.rsplit("/", 1)[-1][:-3] if rel_path.endswith(".md") else rel_path.rsplit("/", 1)[-1]
    words = _NAME_WORDS.findall(stem.lower())
    return any(w in GERMAN_NAME_STEMS for w in words) or any(c in stem for c in "äöüßÄÖÜ")

KIND_RANK = {"needs_en": 0, "needs_de": 0, "copy": 1, "en_german": 1,
             "code_german": 1, "de_english": 1, "parity": 2, "review": 3, "rename": 1}


def kind_rank(e: dict) -> int:
    return min((KIND_RANK.get(k, 9) for k in e.get("kind", [])), default=9)


# ─── Markdown queue (--list) ─────────────────────────────────────────────────
#
# The queue is the translation checker for the whole tree: one line per file
# that is not VERIFIED, grouped by kind. Regenerating keeps hand/AI notes and
# the changelog, so the file can be rewritten after every run.

# which side's size is worth showing per kind (the side to be translated)
SOURCE_SIZE = {"needs_en": "de_bytes", "needs_de": "en_bytes", "copy": "de_bytes",
               "en_german": "en_bytes", "code_german": "en_bytes", "de_english": "de_bytes",
               "parity": "en_bytes", "review": "en_bytes", "rename": "de_bytes"}

SECTION_ORDER = [
    ("needs_en", "A. `en/` fehlt – aus `de/` übersetzen"),
    ("needs_de", "B. `de/` fehlt – englische Quelle nachziehen"),
    ("copy", "C. `en/` ist eine Kopie von `de/` – unübersetzt"),
    ("en_german", "D. `en/` enthält noch deutschen Text – Rest übersetzen"),
    ("code_german", "D2. Deutscher Text in Codebeispielen/Boxen (ADR 0002: Code ist englisch)"),
    ("de_english", "E. `de/` enthält noch englischen Text – Rest rückübersetzen"),
    ("parity", "F. Form nicht gleich – Struktur abgleichen"),
    ("rename", "G. Deutscher Dateiname – Pfad englisch machen (ADR 0002)"),
    ("review", "H. Beide Seiten da, kein Befund – lesen und bestätigen"),
]
ROW_RE = re.compile(r"^- \[( |x|!)\] `([^`]+)`").match
NOTE_MARK = " · Notiz: "
CHANGELOG_KEEP = 40   # runs kept; older entries fall off the tail


PLAN_ROW = re.compile(r"^-\s+\[([ x~!])\]\s+`?([^`\s]+)`?\s*$")


def read_plan(path: Path) -> dict:
    """Optional prioritisation aid: marks from the work plan (`temp/apps-plan.md`).
    `[x]` = verified against primary sources, `[~]` = present but unverified."""
    marks = {}
    if not path or not path.exists():
        return marks
    for line in path.read_text(encoding="utf-8").splitlines():
        m = PLAN_ROW.match(line.strip())
        if m:
            marks[m.group(2)] = m.group(1)
    return marks


def read_existing(path: Path) -> tuple[dict, list[str]]:
    """Recover notes and the changelog from a previously generated queue."""
    notes = {}
    changelog = []
    if not path.exists():
        return notes, changelog
    in_changelog = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## Changelog"):
            in_changelog = True
            continue
        if in_changelog:
            if line.startswith("## "):
                in_changelog = False
            else:
                changelog.append(line)
            continue
        m = ROW_RE(line.rstrip())
        if m and NOTE_MARK in line:
            notes[m.group(2)] = line.split(NOTE_MARK, 1)[1].strip()
    return notes, [c for c in changelog if c.strip()]


def human_size(n):
    if n is None:
        return "—"
    return f"{n/1024:.1f}k" if n >= 1024 else f"{n}b"


def write_queue(path: Path, state: dict, en_scan: dict, de_scan: dict,
                en_root: Path, de_root: Path, list_verified: bool, plan: dict | None = None):
    notes, changelog = read_existing(path)
    entries = state["entries"]
    pending = {p: e for p, e in entries.items() if e["status"] == "PENDING"}
    verified = {p: e for p, e in entries.items() if e["status"] == "VERIFIED"}
    deleted = {p: e for p, e in entries.items() if e["status"] == "DELETED"}
    now = datetime.now(timezone.utc).isoformat()

    out = []
    out.append("# Übersetzungsliste – der Übersetzungs-Checker für den ganzen Baum")
    out.append("")
    out.append(f"Stand: {now[:16].replace('T', ' ')} UTC · "
               f"{len(entries)} Dateien verfolgt · {len(pending)} offen · {len(verified)} bestätigt")
    out.append("")
    out.append("Erzeugt von `python3 scripts/doc_sync.py --en docs/en --de docs/de \\`")
    out.append("    `--state temp/sync_state.json --list temp/translation-queue.md`")
    out.append("")
    out.append("Wahrheit ist `temp/sync_state.json`. Diese Liste ist seine Ansicht; sie darf")
    out.append("per Hand oder vom Agenten annotiert werden (`· Notiz: …`) – Anmerkungen und das")
    out.append("Changelog bleiben beim Neu-Erzeugen erhalten. Abhaken heißt: Datei ist übersetzt")
    out.append("und geprüft. Das Abhaken allein ist nichts wert – erst `--confirm <pfad>` setzt den")
    out.append("Eintrag im Zustand auf `VERIFIED`; beim nächsten Lauf verschwindet die Zeile.")
    out.append("")
    out.append("| Befund | Heißt | Zu tun |")
    out.append("|--------|-------|--------|")
    out.append("| `needs_en` | Datei fehlt in `en/` | aus `de/` übersetzen, dann `--confirm` |")
    out.append("| `needs_de` | Datei fehlt in `de/` | aus `en/` rückübersetzen, dann `--confirm` |")
    out.append("| `copy` | `en/` == `de/` (Byte für Byte) | übersetzen, dann `--confirm` |")
    out.append("| `en_german` | `en/` hat deutschen Rest | Rest übersetzen, dann `--confirm` |")
    out.append("| `code_german` | deutscher Text im Codebeispiel | Beschriftungen im Beispiel englisch machen |")
    out.append("| `de_english` | `de/` hat englischen Rest | Rest rückübersetzen, dann `--confirm` |")
    out.append("| `parity` | Überschriften/Tabellen/Links ungleich | Form angleichen, dann `--confirm` |")
    out.append("| `rename` | Dateiname ist deutsch (ADR 0002) | umbenennen + Links nachziehen |")
    out.append("| `review` | kein Befund | lesen, dann `--confirm` |")
    out.append("")
    out.append("Nie über Sprachbäume hinweg verlinken (CONVENTIONS §9): Links aus `en/` zeigen")
    out.append("nach `en/`, Links aus `de/` nach `de/`. Dateinamen bleiben englisch (ADR 0002).")
    out.append("")
    out.append("**Reihenfolge:** A–G (inkl. D2) sind die eigentliche Arbeit, H ist nur Bestätigungs-Backlog.")
    out.append("`Plan[x]`/`Plan[~]` kommt aus `temp/apps-plan.md`: `[x]` = an Primärquellen verifiziert")
    out.append("(Übersetzung also sicher), `[~]` = vorhanden ohne Beleg. Eine Datei kann in mehreren")
    out.append("Abschnitten stehen (z. B. `needs_en` + `rename`); die Abschnittszahlen zählen deshalb")
    out.append("öfter als die Gesamtzahl offener Dateien.")
    out.append("")

    # section counts
    counts = defaultdict(int)
    for e in pending.values():
        for k in e.get("kind", []):
            counts[k] += 1
    out.append("## Offene Posten")
    out.append("")
    out.append("| Abschnitt | Dateien |")
    out.append("|-----------|---------|")
    for key, title in SECTION_ORDER:
        out.append(f"| {title} | {counts.get(key, 0)} |")
    out.append(f"| 🗑️ gelöscht (tombstone) | {len(deleted)} |")
    out.append("")

    for key, title in SECTION_ORDER:
        rows = [(p, e) for p, e in pending.items() if key in e.get("kind", [])]
        if not rows:
            continue
        out.append(f"## {title} – {len(rows)} Dateien")
        out.append("")
        by_dir = defaultdict(list)
        for p, e in rows:
            by_dir[p.rsplit("/", 1)[0] if "/" in p else "(wurzel)"].append((p, e))
        for d in sorted(by_dir):
            group = by_dir[d]
            out.append(f"### `{d}/` · {len(group)}")
            out.append("")
            for p, e in sorted(group, key=lambda t: t[0].rsplit("/", 1)[-1]):
                size = SOURCE_SIZE.get(key, "de_bytes")
                shown = human_size(e.get(size)) if e.get(size) else "—"
                detail = []
                if key == "rename":
                    detail.append("Zielpfad englisch, dann Links + `mkdocs.yml` nachziehen")
                if e.get("parity"):
                    detail.append("Parität: " + "; ".join(e["parity"][:2]))
                src = "code_suspicion" if key == "code_german" else "suspicion"
                strong = [f for f in e.get(src, []) if f["strength"] == "strong"]
                if key in ("en_german", "de_english", "code_german", "review") and strong:
                    detail.append(f"L{strong[0]['line']} {strong[0]['reason']}")
                if key == "code_german" and strong:
                    src_line = (en_root / p).read_text(
                        encoding="utf-8", errors="replace").splitlines()
                    ln = strong[0]["line"] - 1
                    snippet = src_line[ln].strip() if 0 <= ln < len(src_line) else ""
                    detail.append(f"Fundzeile: {snippet[:70]}")
                    detail.append("Bezeichner ausserhalb bleiben deutsch (ADR 0002)")
                if e.get("change_reason"):
                    detail.append(e["change_reason"])
                if e.get("kind") and len(e["kind"]) > 1:
                    detail.append("auch: " + ",".join(k for k in e["kind"] if k != key))
                note = notes.get(p)
                line = f"- [ ] `{p}` · {shown}"
                if plan and plan.get(p):
                    line += f" · Plan[{plan[p]}]"
                if detail:
                    line += " · " + " · ".join(detail)
                if note:
                    line += f" · Notiz: {note}"
                out.append(line)
            out.append("")

    if deleted:
        out.append(f"## 🗑️ Gelöscht – {len(deleted)}")
        out.append("")
        for p in sorted(deleted):
            out.append(f"- [x] `{p}` · nicht mehr im Baum")
        out.append("")

    if list_verified and verified:
        out.append(f"## ✅ Bestätigt – {len(verified)}")
        out.append("")
        for p, e in sorted(verified.items()):
            lv = (e.get("last_verified") or "?")[:10]
            note = notes.get(p)
            line = f"- [x] `{p}` · bestätigt {lv}"
            if e.get("note"):
                line += f" · Notiz: {e['note']}"
            elif note:
                line += f" · Notiz: {note}"
            out.append(line)
        out.append("")

    out.append("## Changelog")
    out.append("")
    for line in changelog[-CHANGELOG_KEEP:]:
        out.append(line)
    counts_txt = " ".join(f"{k}={counts[k]}" for k, _ in SECTION_ORDER if counts.get(k))
    summary = (f"Lauf: {len(entries)} verfolgt, {len(pending)} offen, "
               f"{len(verified)} bestätigt" + (f" · {counts_txt}" if counts_txt else ""))
    # Nothing moved since the last run: don't bloat the changelog with no-op lines.
    if not any(line.endswith(summary) for line in changelog[-1:]):
        out.append(f"- {now[:16].replace('T', ' ')} · {summary}")
    out.append("")
    path.write_text("\n".join(out), encoding="utf-8")


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="EN/DE doc sync (state-machine) + translation queue")
    parser.add_argument("--en", required=True)
    parser.add_argument("--de", required=True)
    parser.add_argument("--state", default="sync_state.json")
    parser.add_argument("--confirm", metavar="FILE", nargs="+",
                        help="Mark file(s) as VERIFIED (after review)")
    parser.add_argument("--unconfirm", metavar="FILE", nargs="+",
                        help="Push file(s) back to PENDING")
    parser.add_argument("--note", metavar="TEXT",
                        help="Note attached to --confirm/--unconfirm (kept in the queue)")
    parser.add_argument("--list", metavar="MD",
                        help="Write/regenerate the markdown translation queue here")
    parser.add_argument("--list-verified", action="store_true",
                        help="Also list VERIFIED files in the queue")
    parser.add_argument("--plan", default="temp/apps-plan.md",
                        help="Work plan whose [x]/[~] marks are shown as priority hints")
    parser.add_argument("--fix-boxes", metavar="FILE", nargs="+",
                        help="Normalise box frames of en/FILE to the dominant de/ box width")
    parser.add_argument("--gen-box", metavar="FILE",
                        help="Print box lines for en/FILE shaped like the de/ frame")
    parser.add_argument("--cell", metavar="TEXT", action="append", default=[],
                        help="Box row for --gen-box; use `a|b` for multi-column rows")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    en_root, de_root = Path(args.en), Path(args.de)
    state_path = Path(args.state)

    if not en_root.exists() or not de_root.exists():
        print("ERROR: root path not found")
        return 2

    state = load_state(state_path)
    en_scan = scan_tree(en_root)
    de_scan = scan_tree(de_root)
    now = datetime.now(timezone.utc).isoformat()

    # ── Confirm (review done: this file is OK) ──
    if args.confirm:
        missing = []
        for p in args.confirm:
            p = p.strip().strip("`")
            if p in state.get("entries", {}):
                e = state["entries"][p]
                e["status"] = "VERIFIED"
                e["last_verified"] = now
                e["change_reason"] = None
                if args.note:
                    e["note"] = args.note
                e["history"].append({"at": now, "event": "confirmed → VERIFIED"})
                print(f"✅ {p} → VERIFIED")
            else:
                missing.append(p)
        if missing:
            for p in missing:
                print(f"⚠️  {p} not in state yet. Run a scan first.")
        save_state(state_path, state)
        return 0 if not missing else 1

    if args.unconfirm:
        for p in args.unconfirm:
            p = p.strip().strip("`")
            e = state.get("entries", {}).get(p)
            if e:
                e["status"] = "PENDING"
                e["last_verified"] = None
                if args.note:
                    e["note"] = args.note
                e["history"].append({"at": now, "event": "unconfirmed → PENDING"})
                print(f"⏳ {p} → PENDING")
            else:
                print(f"⚠️  {p} not in state yet.")
        save_state(state_path, state)
        return 0

    # ── Build EN box lines shaped like the DE frame (replaces temp/boxgen.py) ──
    if args.gen_box:
        p = args.gen_box.strip().strip("`").removeprefix("docs/en/").removeprefix("en/")
        de_p = de_root / p
        if not de_p.exists():
            print(f"⚠️  {p}: no DE counterpart")
            return 2
        cells = [tuple(c.split("|")) if "|" in c else c for c in args.cell]
        if not cells:
            print("no --cell given")
            return 2
        for line in gen_box_lines(de_p.read_text(encoding="utf-8"), cells):
            print(line)
        return 0

    # ── Repair box frames (replaces temp/check-box-width.py --fix) ──
    # Opt-in: width drift exists on both sides of most files and is not always a
    # translation fault, so it never runs on its own.
    if args.fix_boxes:
        for p in args.fix_boxes:
            p = p.strip().strip("`").removeprefix("docs/en/").removeprefix("en/")
            en_p, de_p = en_root / p, de_root / p
            if not en_p.exists() or not de_p.exists():
                print(f"⚠️  {p}: needs both sides")
                continue
            targets = [max(set(run), key=run.count) for run in box_runs(de_p.read_text(encoding="utf-8"))]
            if not targets:
                print(f"⚠️  {p}: no box in DE")
                continue
            n = fix_box_width(en_p, targets)
            print(f"🔧 {p}: {n} box lines set to DE widths {targets}")
        # hashes are stale now – rescan before classify/list
        en_scan, de_scan = scan_tree(en_root), scan_tree(de_root)

    # ── Normal scan ──
    update_state(en_scan, de_scan, state)
    # remember sizes for the queue
    for p, e in state["entries"].items():
        e["en_bytes"] = (en_scan.get(p) or {}).get("bytes")
        e["de_bytes"] = (de_scan.get(p) or {}).get("bytes")
    classify(state["entries"], en_scan, de_scan, en_root, de_root)

    if args.json:
        output = {
            "generated": now,
            "summary": {
                "total": len(state["entries"]),
                "pending": sum(1 for e in state["entries"].values() if e["status"] == "PENDING"),
                "verified": sum(1 for e in state["entries"].values() if e["status"] == "VERIFIED"),
                "deleted": sum(1 for e in state["entries"].values() if e["status"] == "DELETED"),
            },
            "entries": state["entries"],
        }
        print(json.dumps(output, indent=2, ensure_ascii=False))
    else:
        print_report(state, en_scan, de_scan, verbose=args.verbose)
        pending_with_susp = [(p, e) for p, e in state["entries"].items()
                            if e["status"] == "PENDING" and
                            any(f["strength"] == "strong" for f in e.get("suspicion", []))]
        if pending_with_susp:
            print("\n  🔍 SUSPICION DETAILS (pending files with wrong-language prose)\n")
            for p, e in sorted(pending_with_susp):
                print(f"  📄 {p}")
                strong = [f for f in e["suspicion"] if f["strength"] == "strong"]
                for f in strong[:5]:
                    print(f"     L{f['line']:>4} {f['reason']}")
                if len(strong) > 5:
                    print(f"     … +{len(strong)-5} more")
                print()

    if args.list:
        write_queue(Path(args.list), state, en_scan, de_scan, en_root, de_root,
                    args.list_verified, read_plan(Path(args.plan)))
        print(f"\n📝 queue written: {args.list}")

    save_state(state_path, state)
    return 1 if any(e["status"] == "PENDING" for e in state["entries"].values()) else 0


if __name__ == "__main__":
    raise SystemExit(main())
