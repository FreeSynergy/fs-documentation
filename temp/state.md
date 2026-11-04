# STATE – Apps translation de → en

- Current component number: 6
- Next component to do: gallery / immich (files remaining: features, menu, structure, shortcuts, api; description.md already written)
- Last 3 components completed: coppermine (7/7), damselfly (7/7), immich-description
- Progress: 119 of 468 files translated. Done so far:
  - Step 4 repair: en/programs/apps/calendar/masks/planner/api.md (complete, 142 lines)
  - Step 5: ALL index.md of the 9 in-scope categories (category index + masks index + per-app index)
  - contact: 30/30 complete (gnome-contacts, kaddressbook, monica, nextcloud-contacts)
  - gallery: coppermine 7/7, damselfly 7/7, immich 1/7
- Remaining apps (6 detail files each: api, description, features, menu, shortcuts, structure):
  gallery: immich, librephotos, lychee, nextcloud-photos, photoprism, piwigo
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
  - Do NOT translate paths, filenames, CLI, code blocks, table pipes.
  - ASCII boxes: keep total line width byte-identical to DE (regenerate with python, verify len()).
  - Terminology: Skin-Hinweis -> "Skin note"; Abgrenzung zu X -> "How it differs from X" (app index)
    / "Differentiation" (description.md); "Was X NICHT kann" -> "What X does NOT do";
    "Stand:" -> "State:"; "Fundstellen" -> "Locations"; "Übersicht" -> "Overview";
    "Verwandte Bereiche" -> "Related areas"; "Enthaltene Dokumentationen" -> "Included documentation".
  - In category masks/index.md EN files keep the `docs/de/...` tree line and "written in German"
    verbatim (paths not translated).
- Tooling: `python3 temp/update-progress.py` regenerates temp/translation-progress.md from the
  filesystem (run after every app). German-prose check: temp/find_german_prose.py WORDS list.
- Push status: OK (origin/main == main after last push). Commit after ~5 components, then push;
  if push fails: wait 5s, retry, retry once more, else note "PUSH FAILED" here and keep working.
