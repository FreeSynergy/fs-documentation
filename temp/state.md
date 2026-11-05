# STATE – Apps translation de → en

- Current component number: 25 (parity section F done; messenger category done)
- Next component to do: data/ renames + data/* translation (then animations, desktop masks,
  streaming, suites, wiki, whiteboards, projectmanagement)
- Last 3 components completed: messenger masks (51 files), parity section F (17 files),
  asana/jira/trello projectmanagement masks
- Progress: 833 of 1492 files VERIFIED (doc_sync.py). Done:
  - calendar/masks/planner/api.md (repair), ALL index.md of the 9 categories
  - contact 30/30, gallery 56/56, helpdesk 56/56, maps 49/49 (incl. standpunkte.md),
    marketing 42/42
- Remaining apps (6 detail files each: api, description, features, menu, shortcuts, structure; index.md done):
  marketing: google-analytics, hotjar, mailchimp, matomo, mautic, plausible
  projectmanagement: asana, jira, openproject, planka, redmine, taiga, trello, wekan
  streaming: ant-media-server, ffmpeg, gstreamer, mediamtx, mistserver, nginx-rtmp-module,
             obs-studio, restream, restreamer, wowza
  whiteboards: drawio, excalidraw, miro, mural, openboard, tldraw
  wiki: confluence, mediawiki, notion, tango.io, vscodium, wikijs, xwiki
- Terminology (keep consistent):
  - Stand: -> "State:"; Übersicht -> "Overview"; Fundstellen -> "Locations";
    Skin-Hinweis -> "Skin note"; Abgrenzung -> "Differentiation"; Für wen geeignet -> "Who it suits";
    Hauptfunktionen -> "Main features"; "Was X NICHT kann" -> "What X does NOT do";
    Erweiterungen und Integrationen -> "Extensions and integrations"; Weg -> "Method";
    Menüs nach Rolle -> "Menus by role"; "Nicht vorhanden (bewusst)" -> "Not present (deliberately)";
    Angenommen -> "Assumed"; Kernendpunkte/Kernmethoden -> "Core endpoints"/"Core methods";
    SDKs und Client-Bibliotheken -> "SDKs and client libraries"; Struktur und UI/UX -> "Structure and UI/UX";
    Vorhanden -> "Present"; "Ausdrücklich nicht vorhanden" -> "Explicitly not present";
    Eingebaute Controls/Steuerelemente -> "Built-in controls"; Seitenleisten -> "Side bars";
    "entfällt" -> "Not applicable"; Betrieb -> "Operation/operator"; Instanz -> instance.
  - Standpunkte -> "location points (Standpunkte)" on first mention in prose; keep `standpunkte` in code/paths/links.
- ASCII boxes: build and verify EN boxes with `scripts/doc_sync.py` —
  `--gen-box <path> --cell "a|b"` prints rows shaped like the DE frame,
  `--fix-boxes <path>` normalises existing frames to the dominant DE width.
  A frame whose line widths differ is reported as a parity finding (only when
  `en/` is worse than `de/`).
- Tooling: `python3 scripts/doc_sync.py --en docs/en --de docs/de --state temp/sync_state.json
  --list temp/translation-queue.md` after every app/5 files; `--confirm <path>` marks a file done.
  Former helpers (`update-progress.py`, `mark-progress.py`, `check-box-width.py`, `boxgen.py`,
  `find_german_prose.py`, `find_untranslated*.py`, `check-translation.sh`,
  `translate-index-templates.py`) are superseded and archived in `scripts/_archive/`.
- Push status: PUSH FAILED at component 25 (DNS failure resolving github.com) — commits
  fc1bd19c and a1823700 are local; push when the network is back.
  Commit after ~5 components then push; if push fails: wait 5s, retry, retry once more, else note
  "PUSH FAILED at component <N>" here and keep working.
- Rename section G: done. `mappings`/`standards` are English identifiers – they were wrongly
  listed in `GERMAN_NAME_STEMS` of `doc_sync.py` and are removed there. The genuinely German
  names were renamed on **both** sides (ADR 0002) and every link/path text rewritten:
  felder→fields, formate→formats, modelle→models, konventionen→conventions,
  anforderungen→requirements, beschreibung→description, speicherung→storage
  (7 files, 411 link edits in 155 files, `mkdocs build` has zero `de/` link warnings).
  Renaming breaks verification: 43 previously VERIFIED files went back to PENDING
  ("hash changed") and were re-confirmed with a note. Expect that after every rename.
