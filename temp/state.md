# STATE – Apps translation de → en

- Current component number: 19 (marketing category complete)
- Next component to do: projectmanagement / asana (then jira, openproject, planka, redmine, taiga, trello, wekan)
- Last 3 components completed: marketing/matomo, marketing/mautic, marketing/plausible (whole marketing category)
- Progress: 282 of 468 files translated. Done:
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
- Push status: OK (recovered; marketing pushed at c1d21988).
  Commit after ~5 components then push; if push fails: wait 5s, retry, retry once more, else note
  "PUSH FAILED at component <N>" here and keep working.
