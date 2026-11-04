# STATE – Apps translation de → en

- Current component number: 11 (gallery finished: coppermine, damselfly, immich, librephotos, lychee, nextcloud-photos, photoprism, piwigo)
- Next component to do: helpdesk / freshdesk (then glpi, helodesk, helpscout, osticket, request-tracker, zammad, zendesk)
- Last 3 components completed: photoprism (7/7), piwigo (7/7), gallery category complete
- Progress: 155 of 468 files translated. Done so far:
  - Step 4 repair: en/programs/apps/calendar/masks/planner/api.md (complete, 142 lines)
  - Step 5: ALL index.md of the 9 in-scope categories
  - contact: 30/30 complete
  - gallery: 56/56 complete (all 8 apps)
- Remaining apps (6 detail files each: api, description, features, menu, shortcuts, structure; index.md already done):
  helpdesk: freshdesk, glpi, helodesk, helpscout, osticket, request-tracker, zammad, zendesk
  maps: leaflet, maplibre, openstreetmap, organic-maps, osmand, qgis, umap
  marketing: google-analytics, hotjar, mailchimp, matomo, mautic, plausible
  projectmanagement: asana, jira, openproject, planka, redmine, taiga, trello, wekan
  streaming: ant-media-server, ffmpeg, gstreamer, mediamtx, mistserver, nginx-rtmp-module,
             obs-studio, restream, restreamer, wowza
  whiteboards: drawio, excalidraw, miro, mural, openboard, tldraw
  wiki: confluence, mediawiki, notion, tango.io, vscodium, wikijs, xwiki
- Rules / conventions to keep applying:
  - Mirror structure 1:1; never add or drop content.
  - Do NOT translate paths, filenames, CLI, code blocks, table pipes, example payloads.
  - ASCII boxes: normalise EN to the dominant DE width with
    `python3 temp/check-box-width.py --fix <de> <en>` after every structure.md.
  - Terminology: Skin-Hinweis -> "Skin note"; Abgrenzung -> "Differentiation" (description.md)
    / "How it differs from X" (app index); "Was X NICHT kann" -> "What X does NOT do";
    "Stand:" -> "State:"; "Fundstellen" -> "Locations"; "Übersicht" -> "Overview";
    "Verwandte Bereiche" -> "Related areas"; "Enthaltene Dokumentationen" -> "Included documentation";
    "Für wen geeignet" -> "Who it suits"; "Vorteile" -> "Advantages"; "Technische Details" -> "Technical details";
    "Hauptfunktionen" -> "Main features"; "Erweiterungen und Integrationen" -> "Extensions and integrations";
    "Weg" -> "Method"; "Menüs nach Rolle" -> "Menus by role"; "Nicht vorhanden (bewusst)" -> "Not present (deliberately)";
    "Angenommen" -> "Assumed"; "Kernendpunkte" -> "Core endpoints"; "Rate Limits" -> "Rate limits";
    "SDKs und Client-Bibliotheken" -> "SDKs and client libraries"; "Struktur und UI/UX" -> "Structure and UI/UX";
    "Oberfläche" -> "Interface"; "Tastatur-Shortcuts" -> "Keyboard shortcuts"; "Menüpunkte" -> "Menu items";
    "API Dokumentation" -> "API documentation"; "Funktionen" -> "Features"; "Beschreibung" -> "Description";
    "Was das Programm macht" -> "What the program does".
- Tooling: `python3 temp/update-progress.py` (run after every app). German check:
  `python3 temp/find_german_prose.py <file>` per file (0 = clean).
- Push status: OK (last push e76f9f57 -> origin/main). Commit after ~5 components, then push;
  if push fails: wait 5s, retry, retry once more, else note "PUSH FAILED" here and keep working.
