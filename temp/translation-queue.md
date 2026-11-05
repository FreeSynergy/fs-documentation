# Übersetzungsliste – der Übersetzungs-Checker für den ganzen Baum

Stand: 2026-11-05 11:25 UTC · 1499 Dateien verfolgt · 689 offen · 803 bestätigt

Erzeugt von `python3 scripts/doc_sync.py --en docs/en --de docs/de \`
    `--state temp/sync_state.json --list temp/translation-queue.md`

Wahrheit ist `temp/sync_state.json`. Diese Liste ist seine Ansicht; sie darf
per Hand oder vom Agenten annotiert werden (`· Notiz: …`) – Anmerkungen und das
Changelog bleiben beim Neu-Erzeugen erhalten. Abhaken heißt: Datei ist übersetzt
und geprüft. Das Abhaken allein ist nichts wert – erst `--confirm <pfad>` setzt den
Eintrag im Zustand auf `VERIFIED`; beim nächsten Lauf verschwindet die Zeile.

| Befund | Heißt | Zu tun |
|--------|-------|--------|
| `needs_en` | Datei fehlt in `en/` | aus `de/` übersetzen, dann `--confirm` |
| `needs_de` | Datei fehlt in `de/` | aus `en/` rückübersetzen, dann `--confirm` |
| `copy` | `en/` == `de/` (Byte für Byte) | übersetzen, dann `--confirm` |
| `en_german` | `en/` hat deutschen Rest | Rest übersetzen, dann `--confirm` |
| `code_german` | deutscher Text im Codebeispiel | Beschriftungen im Beispiel englisch machen |
| `de_english` | `de/` hat englischen Rest | Rest rückübersetzen, dann `--confirm` |
| `parity` | Überschriften/Tabellen/Links ungleich | Form angleichen, dann `--confirm` |
| `rename` | Dateiname ist deutsch (ADR 0002) | umbenennen + Links nachziehen |
| `review` | kein Befund | lesen, dann `--confirm` |

Nie über Sprachbäume hinweg verlinken (CONVENTIONS §9): Links aus `en/` zeigen
nach `en/`, Links aus `de/` nach `de/`. Dateinamen bleiben englisch (ADR 0002).

**Reihenfolge:** A–G (inkl. D2) sind die eigentliche Arbeit, H ist nur Bestätigungs-Backlog.
`Plan[x]`/`Plan[~]` kommt aus `temp/apps-plan.md`: `[x]` = an Primärquellen verifiziert
(Übersetzung also sicher), `[~]` = vorhanden ohne Beleg. Eine Datei kann in mehreren
Abschnitten stehen (z. B. `needs_en` + `rename`); die Abschnittszahlen zählen deshalb
öfter als die Gesamtzahl offener Dateien.

## Offene Posten

| Abschnitt | Dateien |
|-----------|---------|
| A. `en/` fehlt – aus `de/` übersetzen | 502 |
| B. `de/` fehlt – englische Quelle nachziehen | 0 |
| C. `en/` ist eine Kopie von `de/` – unübersetzt | 0 |
| D. `en/` enthält noch deutschen Text – Rest übersetzen | 0 |
| D2. Deutscher Text in Codebeispielen/Boxen (ADR 0002: Code ist englisch) | 0 |
| E. `de/` enthält noch englischen Text – Rest rückübersetzen | 0 |
| F. Form nicht gleich – Struktur abgleichen | 42 |
| G. Deutscher Dateiname – Pfad englisch machen (ADR 0002) | 0 |
| H. Beide Seiten da, kein Befund – lesen und bestätigen | 145 |
| 🗑️ gelöscht (tombstone) | 7 |

## A. `en/` fehlt – aus `de/` übersetzen – 502 Dateien

### `interactions/animations/movement/` · 1

- [ ] `interactions/animations/movement/index.md` · 955b

### `interactions/animations/movement/parallax/` · 3

- [ ] `interactions/animations/movement/parallax/appearance.md` · 1.5k
- [ ] `interactions/animations/movement/parallax/attributes.md` · 1.3k
- [ ] `interactions/animations/movement/parallax/description.md` · 1.1k

### `interactions/animations/organization/` · 1

- [ ] `interactions/animations/organization/index.md` · 1.1k

### `interactions/animations/organization/cascade/` · 3

- [ ] `interactions/animations/organization/cascade/appearance.md` · 1.9k
- [ ] `interactions/animations/organization/cascade/attributes.md` · 1.7k
- [ ] `interactions/animations/organization/cascade/description.md` · 1.3k

### `interactions/animations/organization/stagger/` · 3

- [ ] `interactions/animations/organization/stagger/appearance.md` · 1.5k
- [ ] `interactions/animations/organization/stagger/attributes.md` · 1.3k
- [ ] `interactions/animations/organization/stagger/description.md` · 1.2k

### `interactions/animations/transition/` · 1

- [ ] `interactions/animations/transition/index.md` · 1.2k

### `interactions/animations/transition/cross-fade/` · 3

- [ ] `interactions/animations/transition/cross-fade/appearance.md` · 1.4k
- [ ] `interactions/animations/transition/cross-fade/attributes.md` · 1.3k
- [ ] `interactions/animations/transition/cross-fade/description.md` · 1001b

### `interactions/animations/transition/cross-slide/` · 3

- [ ] `interactions/animations/transition/cross-slide/appearance.md` · 1.8k
- [ ] `interactions/animations/transition/cross-slide/attributes.md` · 1.8k
- [ ] `interactions/animations/transition/cross-slide/description.md` · 1.2k

### `interactions/animations/transition/flip/` · 3

- [ ] `interactions/animations/transition/flip/appearance.md` · 1.3k
- [ ] `interactions/animations/transition/flip/attributes.md` · 1.7k
- [ ] `interactions/animations/transition/flip/description.md` · 972b

### `interactions/animations/transition/morph/` · 3

- [ ] `interactions/animations/transition/morph/appearance.md` · 1.4k
- [ ] `interactions/animations/transition/morph/attributes.md` · 1.4k
- [ ] `interactions/animations/transition/morph/description.md` · 1.0k

### `interactions/animations/transition/reorder/` · 3

- [ ] `interactions/animations/transition/reorder/appearance.md` · 1.8k
- [ ] `interactions/animations/transition/reorder/attributes.md` · 1.9k
- [ ] `interactions/animations/transition/reorder/description.md` · 1.3k

### `interactions/animations/transition/rotate/` · 3

- [ ] `interactions/animations/transition/rotate/appearance.md` · 1.2k
- [ ] `interactions/animations/transition/rotate/attributes.md` · 1.6k
- [ ] `interactions/animations/transition/rotate/description.md` · 927b

### `programs/` · 1

- [ ] `programs/index.md` · 3.4k · Plan[~]

### `programs/apps/calendar/frontends/` · 1

- [ ] `programs/apps/calendar/frontends/index.md` · 2.7k

### `programs/apps/projectmanagement/frontends/openproject/latest/` · 6

- [ ] `programs/apps/projectmanagement/frontends/openproject/latest/api.md` · 6.9k
- [ ] `programs/apps/projectmanagement/frontends/openproject/latest/description.md` · 3.6k
- [ ] `programs/apps/projectmanagement/frontends/openproject/latest/features.md` · 4.9k
- [ ] `programs/apps/projectmanagement/frontends/openproject/latest/layout.md` · 5.0k
- [ ] `programs/apps/projectmanagement/frontends/openproject/latest/menus.md` · 4.3k
- [ ] `programs/apps/projectmanagement/frontends/openproject/latest/shortcuts.md` · 5.3k

### `programs/apps/projectmanagement/frontends/planka/latest/` · 6

- [ ] `programs/apps/projectmanagement/frontends/planka/latest/api.md` · 2.9k
- [ ] `programs/apps/projectmanagement/frontends/planka/latest/description.md` · 3.5k
- [ ] `programs/apps/projectmanagement/frontends/planka/latest/features.md` · 4.5k
- [ ] `programs/apps/projectmanagement/frontends/planka/latest/layout.md` · 3.0k
- [ ] `programs/apps/projectmanagement/frontends/planka/latest/menus.md` · 4.0k
- [ ] `programs/apps/projectmanagement/frontends/planka/latest/shortcuts.md` · 1.1k

### `programs/apps/projectmanagement/frontends/redmine/latest/` · 6

- [ ] `programs/apps/projectmanagement/frontends/redmine/latest/api.md` · 7.0k
- [ ] `programs/apps/projectmanagement/frontends/redmine/latest/description.md` · 3.4k
- [ ] `programs/apps/projectmanagement/frontends/redmine/latest/features.md` · 5.1k
- [ ] `programs/apps/projectmanagement/frontends/redmine/latest/layout.md` · 4.9k
- [ ] `programs/apps/projectmanagement/frontends/redmine/latest/menus.md` · 3.6k
- [ ] `programs/apps/projectmanagement/frontends/redmine/latest/shortcuts.md` · 5.6k

### `programs/apps/projectmanagement/frontends/taiga/latest/` · 6

- [ ] `programs/apps/projectmanagement/frontends/taiga/latest/api.md` · 2.2k
- [ ] `programs/apps/projectmanagement/frontends/taiga/latest/description.md` · 1.3k
- [ ] `programs/apps/projectmanagement/frontends/taiga/latest/features.md` · 1.2k
- [ ] `programs/apps/projectmanagement/frontends/taiga/latest/layout.md` · 2.0k
- [ ] `programs/apps/projectmanagement/frontends/taiga/latest/menus.md` · 1.3k
- [ ] `programs/apps/projectmanagement/frontends/taiga/latest/shortcuts.md` · 546b

### `programs/apps/projectmanagement/frontends/wekan/latest/` · 6

- [ ] `programs/apps/projectmanagement/frontends/wekan/latest/api.md` · 2.5k
- [ ] `programs/apps/projectmanagement/frontends/wekan/latest/description.md` · 1.2k
- [ ] `programs/apps/projectmanagement/frontends/wekan/latest/features.md` · 1.3k
- [ ] `programs/apps/projectmanagement/frontends/wekan/latest/layout.md` · 2.5k
- [ ] `programs/apps/projectmanagement/frontends/wekan/latest/menus.md` · 1.2k
- [ ] `programs/apps/projectmanagement/frontends/wekan/latest/shortcuts.md` · 819b

### `programs/apps/streaming/frontends/ant-media-server/latest/` · 6

- [ ] `programs/apps/streaming/frontends/ant-media-server/latest/api.md` · 4.1k
- [ ] `programs/apps/streaming/frontends/ant-media-server/latest/description.md` · 2.8k
- [ ] `programs/apps/streaming/frontends/ant-media-server/latest/features.md` · 2.6k
- [ ] `programs/apps/streaming/frontends/ant-media-server/latest/layout.md` · 3.7k
- [ ] `programs/apps/streaming/frontends/ant-media-server/latest/menus.md` · 2.2k
- [ ] `programs/apps/streaming/frontends/ant-media-server/latest/shortcuts.md` · 1.9k

### `programs/apps/streaming/frontends/ffmpeg/latest/` · 6

- [ ] `programs/apps/streaming/frontends/ffmpeg/latest/api.md` · 3.9k
- [ ] `programs/apps/streaming/frontends/ffmpeg/latest/description.md` · 4.1k
- [ ] `programs/apps/streaming/frontends/ffmpeg/latest/features.md` · 3.3k
- [ ] `programs/apps/streaming/frontends/ffmpeg/latest/layout.md` · 2.7k
- [ ] `programs/apps/streaming/frontends/ffmpeg/latest/menus.md` · 2.6k
- [ ] `programs/apps/streaming/frontends/ffmpeg/latest/shortcuts.md` · 2.7k

### `programs/apps/streaming/frontends/gstreamer/latest/` · 6

- [ ] `programs/apps/streaming/frontends/gstreamer/latest/api.md` · 4.7k
- [ ] `programs/apps/streaming/frontends/gstreamer/latest/description.md` · 2.9k
- [ ] `programs/apps/streaming/frontends/gstreamer/latest/features.md` · 3.4k
- [ ] `programs/apps/streaming/frontends/gstreamer/latest/layout.md` · 3.6k
- [ ] `programs/apps/streaming/frontends/gstreamer/latest/menus.md` · 2.1k
- [ ] `programs/apps/streaming/frontends/gstreamer/latest/shortcuts.md` · 1.8k

### `programs/apps/streaming/frontends/mediamtx/latest/` · 6

- [ ] `programs/apps/streaming/frontends/mediamtx/latest/api.md` · 4.1k
- [ ] `programs/apps/streaming/frontends/mediamtx/latest/description.md` · 2.9k
- [ ] `programs/apps/streaming/frontends/mediamtx/latest/features.md` · 3.0k
- [ ] `programs/apps/streaming/frontends/mediamtx/latest/layout.md` · 3.8k
- [ ] `programs/apps/streaming/frontends/mediamtx/latest/menus.md` · 2.4k
- [ ] `programs/apps/streaming/frontends/mediamtx/latest/shortcuts.md` · 1.7k

### `programs/apps/streaming/frontends/mistserver/latest/` · 6

- [ ] `programs/apps/streaming/frontends/mistserver/latest/api.md` · 4.3k
- [ ] `programs/apps/streaming/frontends/mistserver/latest/description.md` · 2.8k
- [ ] `programs/apps/streaming/frontends/mistserver/latest/features.md` · 2.6k
- [ ] `programs/apps/streaming/frontends/mistserver/latest/layout.md` · 3.6k
- [ ] `programs/apps/streaming/frontends/mistserver/latest/menus.md` · 1.8k
- [ ] `programs/apps/streaming/frontends/mistserver/latest/shortcuts.md` · 2.0k

### `programs/apps/streaming/frontends/nginx-rtmp-module/latest/` · 6

- [ ] `programs/apps/streaming/frontends/nginx-rtmp-module/latest/api.md` · 3.8k
- [ ] `programs/apps/streaming/frontends/nginx-rtmp-module/latest/description.md` · 2.5k
- [ ] `programs/apps/streaming/frontends/nginx-rtmp-module/latest/features.md` · 2.5k
- [ ] `programs/apps/streaming/frontends/nginx-rtmp-module/latest/layout.md` · 3.5k
- [ ] `programs/apps/streaming/frontends/nginx-rtmp-module/latest/menus.md` · 2.4k
- [ ] `programs/apps/streaming/frontends/nginx-rtmp-module/latest/shortcuts.md` · 1.6k

### `programs/apps/streaming/frontends/obs-studio/latest/` · 6

- [ ] `programs/apps/streaming/frontends/obs-studio/latest/api.md` · 3.2k
- [ ] `programs/apps/streaming/frontends/obs-studio/latest/description.md` · 1.8k
- [ ] `programs/apps/streaming/frontends/obs-studio/latest/features.md` · 2.3k
- [ ] `programs/apps/streaming/frontends/obs-studio/latest/layout.md` · 3.0k
- [ ] `programs/apps/streaming/frontends/obs-studio/latest/menus.md` · 2.2k
- [ ] `programs/apps/streaming/frontends/obs-studio/latest/shortcuts.md` · 1.8k

### `programs/apps/streaming/frontends/restream/latest/` · 6

- [ ] `programs/apps/streaming/frontends/restream/latest/api.md` · 3.0k
- [ ] `programs/apps/streaming/frontends/restream/latest/description.md` · 2.5k
- [ ] `programs/apps/streaming/frontends/restream/latest/features.md` · 2.3k
- [ ] `programs/apps/streaming/frontends/restream/latest/layout.md` · 3.5k
- [ ] `programs/apps/streaming/frontends/restream/latest/menus.md` · 2.3k
- [ ] `programs/apps/streaming/frontends/restream/latest/shortcuts.md` · 1.4k

### `programs/apps/streaming/frontends/restreamer/latest/` · 6

- [ ] `programs/apps/streaming/frontends/restreamer/latest/api.md` · 3.8k
- [ ] `programs/apps/streaming/frontends/restreamer/latest/description.md` · 1.7k
- [ ] `programs/apps/streaming/frontends/restreamer/latest/features.md` · 1.4k
- [ ] `programs/apps/streaming/frontends/restreamer/latest/layout.md` · 3.7k
- [ ] `programs/apps/streaming/frontends/restreamer/latest/menus.md` · 1.3k
- [ ] `programs/apps/streaming/frontends/restreamer/latest/shortcuts.md` · 1.9k

### `programs/apps/streaming/frontends/wowza/latest/` · 6

- [ ] `programs/apps/streaming/frontends/wowza/latest/api.md` · 3.2k
- [ ] `programs/apps/streaming/frontends/wowza/latest/description.md` · 2.4k
- [ ] `programs/apps/streaming/frontends/wowza/latest/features.md` · 2.3k
- [ ] `programs/apps/streaming/frontends/wowza/latest/layout.md` · 3.8k
- [ ] `programs/apps/streaming/frontends/wowza/latest/menus.md` · 2.2k
- [ ] `programs/apps/streaming/frontends/wowza/latest/shortcuts.md` · 2.0k

### `programs/apps/whiteboards/frontends/drawio/latest/` · 6

- [ ] `programs/apps/whiteboards/frontends/drawio/latest/api.md` · 6.3k
- [ ] `programs/apps/whiteboards/frontends/drawio/latest/description.md` · 3.2k
- [ ] `programs/apps/whiteboards/frontends/drawio/latest/features.md` · 5.9k
- [ ] `programs/apps/whiteboards/frontends/drawio/latest/layout.md` · 6.3k
- [ ] `programs/apps/whiteboards/frontends/drawio/latest/menus.md` · 4.6k
- [ ] `programs/apps/whiteboards/frontends/drawio/latest/shortcuts.md` · 5.2k

### `programs/apps/whiteboards/frontends/excalidraw/latest/` · 6

- [ ] `programs/apps/whiteboards/frontends/excalidraw/latest/api.md` · 5.9k
- [ ] `programs/apps/whiteboards/frontends/excalidraw/latest/description.md` · 3.4k
- [ ] `programs/apps/whiteboards/frontends/excalidraw/latest/features.md` · 5.6k
- [ ] `programs/apps/whiteboards/frontends/excalidraw/latest/layout.md` · 6.7k
- [ ] `programs/apps/whiteboards/frontends/excalidraw/latest/menus.md` · 3.7k
- [ ] `programs/apps/whiteboards/frontends/excalidraw/latest/shortcuts.md` · 5.2k

### `programs/apps/whiteboards/frontends/miro/latest/` · 6

- [ ] `programs/apps/whiteboards/frontends/miro/latest/api.md` · 2.3k
- [ ] `programs/apps/whiteboards/frontends/miro/latest/description.md` · 1.2k
- [ ] `programs/apps/whiteboards/frontends/miro/latest/features.md` · 1.3k
- [ ] `programs/apps/whiteboards/frontends/miro/latest/layout.md` · 2.1k
- [ ] `programs/apps/whiteboards/frontends/miro/latest/menus.md` · 1.1k
- [ ] `programs/apps/whiteboards/frontends/miro/latest/shortcuts.md` · 1.0k

### `programs/apps/whiteboards/frontends/mural/latest/` · 6

- [ ] `programs/apps/whiteboards/frontends/mural/latest/api.md` · 1.3k
- [ ] `programs/apps/whiteboards/frontends/mural/latest/description.md` · 1.1k
- [ ] `programs/apps/whiteboards/frontends/mural/latest/features.md` · 1.1k
- [ ] `programs/apps/whiteboards/frontends/mural/latest/layout.md` · 1.8k
- [ ] `programs/apps/whiteboards/frontends/mural/latest/menus.md` · 1.1k
- [ ] `programs/apps/whiteboards/frontends/mural/latest/shortcuts.md` · 703b

### `programs/apps/whiteboards/frontends/openboard/latest/` · 6

- [ ] `programs/apps/whiteboards/frontends/openboard/latest/api.md` · 1.2k
- [ ] `programs/apps/whiteboards/frontends/openboard/latest/description.md` · 1.1k
- [ ] `programs/apps/whiteboards/frontends/openboard/latest/features.md` · 1.2k
- [ ] `programs/apps/whiteboards/frontends/openboard/latest/layout.md` · 1.7k
- [ ] `programs/apps/whiteboards/frontends/openboard/latest/menus.md` · 975b
- [ ] `programs/apps/whiteboards/frontends/openboard/latest/shortcuts.md` · 740b

### `programs/apps/whiteboards/frontends/tldraw/latest/` · 6

- [ ] `programs/apps/whiteboards/frontends/tldraw/latest/api.md` · 3.0k
- [ ] `programs/apps/whiteboards/frontends/tldraw/latest/description.md` · 3.2k
- [ ] `programs/apps/whiteboards/frontends/tldraw/latest/features.md` · 4.8k
- [ ] `programs/apps/whiteboards/frontends/tldraw/latest/layout.md` · 2.9k
- [ ] `programs/apps/whiteboards/frontends/tldraw/latest/menus.md` · 1.8k
- [ ] `programs/apps/whiteboards/frontends/tldraw/latest/shortcuts.md` · 1.7k

### `programs/apps/wiki/frontends/confluence/latest/` · 6

- [ ] `programs/apps/wiki/frontends/confluence/latest/api.md` · 6.0k
- [ ] `programs/apps/wiki/frontends/confluence/latest/description.md` · 1.9k
- [ ] `programs/apps/wiki/frontends/confluence/latest/features.md` · 5.4k
- [ ] `programs/apps/wiki/frontends/confluence/latest/layout.md` · 5.9k
- [ ] `programs/apps/wiki/frontends/confluence/latest/menus.md` · 2.4k
- [ ] `programs/apps/wiki/frontends/confluence/latest/shortcuts.md` · 7.0k

### `programs/apps/wiki/frontends/mediawiki/latest/` · 6

- [ ] `programs/apps/wiki/frontends/mediawiki/latest/api.md` · 5.3k
- [ ] `programs/apps/wiki/frontends/mediawiki/latest/description.md` · 1.9k
- [ ] `programs/apps/wiki/frontends/mediawiki/latest/features.md` · 4.1k
- [ ] `programs/apps/wiki/frontends/mediawiki/latest/layout.md` · 5.7k
- [ ] `programs/apps/wiki/frontends/mediawiki/latest/menus.md` · 2.3k
- [ ] `programs/apps/wiki/frontends/mediawiki/latest/shortcuts.md` · 6.7k

### `programs/apps/wiki/frontends/notion/latest/` · 6

- [ ] `programs/apps/wiki/frontends/notion/latest/api.md` · 5.3k
- [ ] `programs/apps/wiki/frontends/notion/latest/description.md` · 1.9k
- [ ] `programs/apps/wiki/frontends/notion/latest/features.md` · 7.2k
- [ ] `programs/apps/wiki/frontends/notion/latest/layout.md` · 5.4k
- [ ] `programs/apps/wiki/frontends/notion/latest/menus.md` · 4.2k
- [ ] `programs/apps/wiki/frontends/notion/latest/shortcuts.md` · 7.1k

### `programs/apps/wiki/frontends/tango.io/latest/` · 6

- [ ] `programs/apps/wiki/frontends/tango.io/latest/api.md` · 5.0k
- [ ] `programs/apps/wiki/frontends/tango.io/latest/description.md` · 1.8k
- [ ] `programs/apps/wiki/frontends/tango.io/latest/features.md` · 4.8k
- [ ] `programs/apps/wiki/frontends/tango.io/latest/layout.md` · 5.4k
- [ ] `programs/apps/wiki/frontends/tango.io/latest/menus.md` · 2.5k
- [ ] `programs/apps/wiki/frontends/tango.io/latest/shortcuts.md` · 6.7k

### `programs/apps/wiki/frontends/vscodium/latest/` · 6

- [ ] `programs/apps/wiki/frontends/vscodium/latest/api.md` · 5.1k
- [ ] `programs/apps/wiki/frontends/vscodium/latest/description.md` · 1.9k
- [ ] `programs/apps/wiki/frontends/vscodium/latest/features.md` · 6.4k
- [ ] `programs/apps/wiki/frontends/vscodium/latest/layout.md` · 6.8k
- [ ] `programs/apps/wiki/frontends/vscodium/latest/menus.md` · 2.0k
- [ ] `programs/apps/wiki/frontends/vscodium/latest/shortcuts.md` · 6.4k

### `programs/apps/wiki/frontends/wikijs/latest/` · 6

- [ ] `programs/apps/wiki/frontends/wikijs/latest/api.md` · 4.4k
- [ ] `programs/apps/wiki/frontends/wikijs/latest/description.md` · 2.1k
- [ ] `programs/apps/wiki/frontends/wikijs/latest/features.md` · 3.6k
- [ ] `programs/apps/wiki/frontends/wikijs/latest/layout.md` · 6.2k
- [ ] `programs/apps/wiki/frontends/wikijs/latest/menus.md` · 2.6k
- [ ] `programs/apps/wiki/frontends/wikijs/latest/shortcuts.md` · 5.1k

### `programs/apps/wiki/frontends/xwiki/latest/` · 6

- [ ] `programs/apps/wiki/frontends/xwiki/latest/api.md` · 5.1k
- [ ] `programs/apps/wiki/frontends/xwiki/latest/description.md` · 2.0k
- [ ] `programs/apps/wiki/frontends/xwiki/latest/features.md` · 3.4k
- [ ] `programs/apps/wiki/frontends/xwiki/latest/layout.md` · 6.7k
- [ ] `programs/apps/wiki/frontends/xwiki/latest/menus.md` · 2.4k
- [ ] `programs/apps/wiki/frontends/xwiki/latest/shortcuts.md` · 6.7k

### `programs/platform/crates/` · 1

- [ ] `programs/platform/crates/gui.md` · 11.7k

### `programs/platform/desktop/frontends/` · 1

- [ ] `programs/platform/desktop/frontends/index.md` · 7.4k

### `programs/platform/desktop/frontends/dashy/` · 1

- [ ] `programs/platform/desktop/frontends/dashy/index.md` · 925b

### `programs/platform/desktop/frontends/dashy/latest/` · 6

- [ ] `programs/platform/desktop/frontends/dashy/latest/api.md` · 7.5k
- [ ] `programs/platform/desktop/frontends/dashy/latest/description.md` · 3.7k
- [ ] `programs/platform/desktop/frontends/dashy/latest/features.md` · 7.0k
- [ ] `programs/platform/desktop/frontends/dashy/latest/layout.md` · 8.0k
- [ ] `programs/platform/desktop/frontends/dashy/latest/menus.md` · 5.0k
- [ ] `programs/platform/desktop/frontends/dashy/latest/shortcuts.md` · 6.2k

### `programs/platform/desktop/frontends/gethomepage/` · 1

- [ ] `programs/platform/desktop/frontends/gethomepage/index.md` · 1.1k

### `programs/platform/desktop/frontends/gethomepage/latest/` · 6

- [ ] `programs/platform/desktop/frontends/gethomepage/latest/api.md` · 8.4k
- [ ] `programs/platform/desktop/frontends/gethomepage/latest/description.md` · 4.6k
- [ ] `programs/platform/desktop/frontends/gethomepage/latest/features.md` · 6.5k
- [ ] `programs/platform/desktop/frontends/gethomepage/latest/layout.md` · 6.8k
- [ ] `programs/platform/desktop/frontends/gethomepage/latest/menus.md` · 5.7k
- [ ] `programs/platform/desktop/frontends/gethomepage/latest/shortcuts.md` · 6.8k

### `programs/platform/desktop/frontends/heimdall/` · 1

- [ ] `programs/platform/desktop/frontends/heimdall/index.md` · 877b

### `programs/platform/desktop/frontends/heimdall/latest/` · 6

- [ ] `programs/platform/desktop/frontends/heimdall/latest/api.md` · 7.2k
- [ ] `programs/platform/desktop/frontends/heimdall/latest/description.md` · 3.8k
- [ ] `programs/platform/desktop/frontends/heimdall/latest/features.md` · 6.2k
- [ ] `programs/platform/desktop/frontends/heimdall/latest/layout.md` · 7.7k
- [ ] `programs/platform/desktop/frontends/heimdall/latest/menus.md` · 4.6k
- [ ] `programs/platform/desktop/frontends/heimdall/latest/shortcuts.md` · 5.4k

### `programs/platform/desktop/frontends/homarr/` · 1

- [ ] `programs/platform/desktop/frontends/homarr/index.md` · 876b

### `programs/platform/desktop/frontends/homarr/latest/` · 6

- [ ] `programs/platform/desktop/frontends/homarr/latest/api.md` · 8.3k
- [ ] `programs/platform/desktop/frontends/homarr/latest/description.md` · 3.6k
- [ ] `programs/platform/desktop/frontends/homarr/latest/features.md` · 6.1k
- [ ] `programs/platform/desktop/frontends/homarr/latest/layout.md` · 7.8k
- [ ] `programs/platform/desktop/frontends/homarr/latest/menus.md` · 4.8k
- [ ] `programs/platform/desktop/frontends/homarr/latest/shortcuts.md` · 5.8k

### `programs/platform/desktop/frontends/homepage/` · 1

- [ ] `programs/platform/desktop/frontends/homepage/index.md` · 1.0k

### `programs/platform/desktop/frontends/homepage/latest/` · 6

- [ ] `programs/platform/desktop/frontends/homepage/latest/api.md` · 9.4k
- [ ] `programs/platform/desktop/frontends/homepage/latest/description.md` · 4.1k
- [ ] `programs/platform/desktop/frontends/homepage/latest/features.md` · 6.8k
- [ ] `programs/platform/desktop/frontends/homepage/latest/layout.md` · 7.2k
- [ ] `programs/platform/desktop/frontends/homepage/latest/menus.md` · 5.7k
- [ ] `programs/platform/desktop/frontends/homepage/latest/shortcuts.md` · 6.2k

### `programs/platform/desktop/frontends/homer/` · 1

- [ ] `programs/platform/desktop/frontends/homer/index.md` · 841b

### `programs/platform/desktop/frontends/homer/latest/` · 6

- [ ] `programs/platform/desktop/frontends/homer/latest/api.md` · 7.4k
- [ ] `programs/platform/desktop/frontends/homer/latest/description.md` · 3.3k
- [ ] `programs/platform/desktop/frontends/homer/latest/features.md` · 5.8k
- [ ] `programs/platform/desktop/frontends/homer/latest/layout.md` · 7.7k
- [ ] `programs/platform/desktop/frontends/homer/latest/menus.md` · 4.6k
- [ ] `programs/platform/desktop/frontends/homer/latest/shortcuts.md` · 5.5k

### `programs/platform/desktop/frontends/launchboard/` · 1

- [ ] `programs/platform/desktop/frontends/launchboard/index.md` · 1.2k

### `programs/platform/desktop/frontends/launchboard/latest/` · 6

- [ ] `programs/platform/desktop/frontends/launchboard/latest/api.md` · 9.2k
- [ ] `programs/platform/desktop/frontends/launchboard/latest/description.md` · 4.6k
- [ ] `programs/platform/desktop/frontends/launchboard/latest/features.md` · 6.7k
- [ ] `programs/platform/desktop/frontends/launchboard/latest/layout.md` · 8.8k
- [ ] `programs/platform/desktop/frontends/launchboard/latest/menus.md` · 5.1k
- [ ] `programs/platform/desktop/frontends/launchboard/latest/shortcuts.md` · 6.5k

### `programs/platform/desktop/frontends/opnsense/` · 1

- [ ] `programs/platform/desktop/frontends/opnsense/index.md` · 995b

### `programs/platform/desktop/frontends/opnsense/latest/` · 6

- [ ] `programs/platform/desktop/frontends/opnsense/latest/api.md` · 7.3k
- [ ] `programs/platform/desktop/frontends/opnsense/latest/description.md` · 3.7k
- [ ] `programs/platform/desktop/frontends/opnsense/latest/features.md` · 5.3k
- [ ] `programs/platform/desktop/frontends/opnsense/latest/layout.md` · 6.7k
- [ ] `programs/platform/desktop/frontends/opnsense/latest/menus.md` · 5.7k
- [ ] `programs/platform/desktop/frontends/opnsense/latest/shortcuts.md` · 5.6k

### `programs/platform/desktop/frontends/proxmox/` · 1

- [ ] `programs/platform/desktop/frontends/proxmox/index.md` · 994b

### `programs/platform/desktop/frontends/proxmox/latest/` · 6

- [ ] `programs/platform/desktop/frontends/proxmox/latest/api.md` · 6.5k
- [ ] `programs/platform/desktop/frontends/proxmox/latest/description.md` · 3.9k
- [ ] `programs/platform/desktop/frontends/proxmox/latest/features.md` · 5.6k
- [ ] `programs/platform/desktop/frontends/proxmox/latest/layout.md` · 7.3k
- [ ] `programs/platform/desktop/frontends/proxmox/latest/menus.md` · 5.1k
- [ ] `programs/platform/desktop/frontends/proxmox/latest/shortcuts.md` · 5.8k

### `programs/platform/desktop/frontends/synology-dsm/` · 1

- [ ] `programs/platform/desktop/frontends/synology-dsm/index.md` · 1001b

### `programs/platform/desktop/frontends/synology-dsm/latest/` · 6

- [ ] `programs/platform/desktop/frontends/synology-dsm/latest/api.md` · 8.3k
- [ ] `programs/platform/desktop/frontends/synology-dsm/latest/description.md` · 4.7k
- [ ] `programs/platform/desktop/frontends/synology-dsm/latest/features.md` · 7.0k
- [ ] `programs/platform/desktop/frontends/synology-dsm/latest/layout.md` · 8.4k
- [ ] `programs/platform/desktop/frontends/synology-dsm/latest/menus.md` · 5.5k
- [ ] `programs/platform/desktop/frontends/synology-dsm/latest/shortcuts.md` · 6.5k

### `programs/platform/desktop/frontends/truenas/` · 1

- [ ] `programs/platform/desktop/frontends/truenas/index.md` · 1.0k

### `programs/platform/desktop/frontends/truenas/latest/` · 6

- [ ] `programs/platform/desktop/frontends/truenas/latest/api.md` · 6.4k
- [ ] `programs/platform/desktop/frontends/truenas/latest/description.md` · 3.8k
- [ ] `programs/platform/desktop/frontends/truenas/latest/features.md` · 5.5k
- [ ] `programs/platform/desktop/frontends/truenas/latest/layout.md` · 6.4k
- [ ] `programs/platform/desktop/frontends/truenas/latest/menus.md` · 4.9k
- [ ] `programs/platform/desktop/frontends/truenas/latest/shortcuts.md` · 5.7k

### `programs/platform/desktop/frontends/unraid/` · 1

- [ ] `programs/platform/desktop/frontends/unraid/index.md` · 1.0k

### `programs/platform/desktop/frontends/unraid/latest/` · 6

- [ ] `programs/platform/desktop/frontends/unraid/latest/api.md` · 7.0k
- [ ] `programs/platform/desktop/frontends/unraid/latest/description.md` · 3.7k
- [ ] `programs/platform/desktop/frontends/unraid/latest/features.md` · 5.8k
- [ ] `programs/platform/desktop/frontends/unraid/latest/layout.md` · 8.1k
- [ ] `programs/platform/desktop/frontends/unraid/latest/menus.md` · 4.9k
- [ ] `programs/platform/desktop/frontends/unraid/latest/shortcuts.md` · 5.7k

### `programs/suites/crm/frontends/` · 1

- [ ] `programs/suites/crm/frontends/index.md` · 2.7k

### `programs/suites/crm/frontends/civicrm/` · 1

- [ ] `programs/suites/crm/frontends/civicrm/index.md` · 890b

### `programs/suites/crm/frontends/civicrm/latest/` · 6

- [ ] `programs/suites/crm/frontends/civicrm/latest/api.md` · 2.5k
- [ ] `programs/suites/crm/frontends/civicrm/latest/description.md` · 1.6k
- [ ] `programs/suites/crm/frontends/civicrm/latest/features.md` · 1.8k
- [ ] `programs/suites/crm/frontends/civicrm/latest/layout.md` · 2.5k
- [ ] `programs/suites/crm/frontends/civicrm/latest/menus.md` · 1.5k
- [ ] `programs/suites/crm/frontends/civicrm/latest/shortcuts.md` · 674b

### `programs/suites/crm/frontends/espocrm/` · 1

- [ ] `programs/suites/crm/frontends/espocrm/index.md` · 792b

### `programs/suites/crm/frontends/espocrm/latest/` · 6

- [ ] `programs/suites/crm/frontends/espocrm/latest/api.md` · 2.3k
- [ ] `programs/suites/crm/frontends/espocrm/latest/description.md` · 1.4k
- [ ] `programs/suites/crm/frontends/espocrm/latest/features.md` · 1.4k
- [ ] `programs/suites/crm/frontends/espocrm/latest/layout.md` · 2.1k
- [ ] `programs/suites/crm/frontends/espocrm/latest/menus.md` · 1.3k
- [ ] `programs/suites/crm/frontends/espocrm/latest/shortcuts.md` · 831b

### `programs/suites/crm/frontends/hubspot/` · 1

- [ ] `programs/suites/crm/frontends/hubspot/index.md` · 832b

### `programs/suites/crm/frontends/hubspot/latest/` · 6

- [ ] `programs/suites/crm/frontends/hubspot/latest/api.md` · 2.5k
- [ ] `programs/suites/crm/frontends/hubspot/latest/description.md` · 1.3k
- [ ] `programs/suites/crm/frontends/hubspot/latest/features.md` · 1.3k
- [ ] `programs/suites/crm/frontends/hubspot/latest/layout.md` · 2.1k
- [ ] `programs/suites/crm/frontends/hubspot/latest/menus.md` · 1.3k
- [ ] `programs/suites/crm/frontends/hubspot/latest/shortcuts.md` · 670b

### `programs/suites/crm/frontends/pipedrive/` · 1

- [ ] `programs/suites/crm/frontends/pipedrive/index.md` · 947b

### `programs/suites/crm/frontends/pipedrive/latest/` · 6

- [ ] `programs/suites/crm/frontends/pipedrive/latest/api.md` · 7.2k
- [ ] `programs/suites/crm/frontends/pipedrive/latest/description.md` · 3.5k
- [ ] `programs/suites/crm/frontends/pipedrive/latest/features.md` · 6.0k
- [ ] `programs/suites/crm/frontends/pipedrive/latest/layout.md` · 6.4k
- [ ] `programs/suites/crm/frontends/pipedrive/latest/menus.md` · 4.8k
- [ ] `programs/suites/crm/frontends/pipedrive/latest/shortcuts.md` · 6.9k

### `programs/suites/crm/frontends/salesforce/` · 1

- [ ] `programs/suites/crm/frontends/salesforce/index.md` · 827b

### `programs/suites/crm/frontends/salesforce/latest/` · 6

- [ ] `programs/suites/crm/frontends/salesforce/latest/api.md` · 2.7k
- [ ] `programs/suites/crm/frontends/salesforce/latest/description.md` · 1.6k
- [ ] `programs/suites/crm/frontends/salesforce/latest/features.md` · 1.5k
- [ ] `programs/suites/crm/frontends/salesforce/latest/layout.md` · 2.2k
- [ ] `programs/suites/crm/frontends/salesforce/latest/menus.md` · 1.5k
- [ ] `programs/suites/crm/frontends/salesforce/latest/shortcuts.md` · 1014b

### `programs/suites/crm/frontends/suitecrm/` · 1

- [ ] `programs/suites/crm/frontends/suitecrm/index.md` · 896b

### `programs/suites/crm/frontends/suitecrm/latest/` · 6

- [ ] `programs/suites/crm/frontends/suitecrm/latest/api.md` · 8.2k
- [ ] `programs/suites/crm/frontends/suitecrm/latest/description.md` · 3.4k
- [ ] `programs/suites/crm/frontends/suitecrm/latest/features.md` · 6.5k
- [ ] `programs/suites/crm/frontends/suitecrm/latest/layout.md` · 6.5k
- [ ] `programs/suites/crm/frontends/suitecrm/latest/menus.md` · 4.8k
- [ ] `programs/suites/crm/frontends/suitecrm/latest/shortcuts.md` · 7.0k

### `programs/suites/democracy/frontends/` · 1

- [ ] `programs/suites/democracy/frontends/index.md` · 2.7k

### `programs/suites/democracy/frontends/adhocracy4/` · 1

- [ ] `programs/suites/democracy/frontends/adhocracy4/index.md` · 816b

### `programs/suites/democracy/frontends/adhocracy4/latest/` · 6

- [ ] `programs/suites/democracy/frontends/adhocracy4/latest/api.md` · 1.8k
- [ ] `programs/suites/democracy/frontends/adhocracy4/latest/description.md` · 1.3k
- [ ] `programs/suites/democracy/frontends/adhocracy4/latest/features.md` · 1.3k
- [ ] `programs/suites/democracy/frontends/adhocracy4/latest/layout.md` · 1.6k
- [ ] `programs/suites/democracy/frontends/adhocracy4/latest/menus.md` · 982b
- [ ] `programs/suites/democracy/frontends/adhocracy4/latest/shortcuts.md` · 414b

### `programs/suites/democracy/frontends/circo/` · 1

- [ ] `programs/suites/democracy/frontends/circo/index.md` · 884b

### `programs/suites/democracy/frontends/circo/latest/` · 6

- [ ] `programs/suites/democracy/frontends/circo/latest/api.md` · 1.2k
- [ ] `programs/suites/democracy/frontends/circo/latest/description.md` · 1.2k
- [ ] `programs/suites/democracy/frontends/circo/latest/features.md` · 884b
- [ ] `programs/suites/democracy/frontends/circo/latest/layout.md` · 900b
- [ ] `programs/suites/democracy/frontends/circo/latest/menus.md` · 839b
- [ ] `programs/suites/democracy/frontends/circo/latest/shortcuts.md` · 310b

### `programs/suites/democracy/frontends/consul/` · 1

- [ ] `programs/suites/democracy/frontends/consul/index.md` · 811b

### `programs/suites/democracy/frontends/consul/latest/` · 6

- [ ] `programs/suites/democracy/frontends/consul/latest/api.md` · 1.7k
- [ ] `programs/suites/democracy/frontends/consul/latest/description.md` · 1.1k
- [ ] `programs/suites/democracy/frontends/consul/latest/features.md` · 1.1k
- [ ] `programs/suites/democracy/frontends/consul/latest/layout.md` · 1.5k
- [ ] `programs/suites/democracy/frontends/consul/latest/menus.md` · 1015b
- [ ] `programs/suites/democracy/frontends/consul/latest/shortcuts.md` · 373b

### `programs/suites/democracy/frontends/decidim/` · 1

- [ ] `programs/suites/democracy/frontends/decidim/index.md` · 863b

### `programs/suites/democracy/frontends/decidim/latest/` · 6

- [ ] `programs/suites/democracy/frontends/decidim/latest/api.md` · 1.8k
- [ ] `programs/suites/democracy/frontends/decidim/latest/description.md` · 1.3k
- [ ] `programs/suites/democracy/frontends/decidim/latest/features.md` · 1.3k
- [ ] `programs/suites/democracy/frontends/decidim/latest/layout.md` · 1.7k
- [ ] `programs/suites/democracy/frontends/decidim/latest/menus.md` · 920b
- [ ] `programs/suites/democracy/frontends/decidim/latest/shortcuts.md` · 452b

### `programs/suites/democracy/frontends/liquid-feedback/` · 1

- [ ] `programs/suites/democracy/frontends/liquid-feedback/index.md` · 806b

### `programs/suites/democracy/frontends/liquid-feedback/latest/` · 6

- [ ] `programs/suites/democracy/frontends/liquid-feedback/latest/api.md` · 1.4k
- [ ] `programs/suites/democracy/frontends/liquid-feedback/latest/description.md` · 1.2k
- [ ] `programs/suites/democracy/frontends/liquid-feedback/latest/features.md` · 1.2k
- [ ] `programs/suites/democracy/frontends/liquid-feedback/latest/layout.md` · 1.7k
- [ ] `programs/suites/democracy/frontends/liquid-feedback/latest/menus.md` · 1.1k
- [ ] `programs/suites/democracy/frontends/liquid-feedback/latest/shortcuts.md` · 365b

### `programs/suites/democracy/frontends/polis/` · 1

- [ ] `programs/suites/democracy/frontends/polis/index.md` · 797b

### `programs/suites/democracy/frontends/polis/latest/` · 6

- [ ] `programs/suites/democracy/frontends/polis/latest/api.md` · 1.7k
- [ ] `programs/suites/democracy/frontends/polis/latest/description.md` · 1.2k
- [ ] `programs/suites/democracy/frontends/polis/latest/features.md` · 1.2k
- [ ] `programs/suites/democracy/frontends/polis/latest/layout.md` · 1.6k
- [ ] `programs/suites/democracy/frontends/polis/latest/menus.md` · 872b
- [ ] `programs/suites/democracy/frontends/polis/latest/shortcuts.md` · 431b

### `programs/suites/erp/frontends/` · 1

- [ ] `programs/suites/erp/frontends/index.md` · 2.6k

### `programs/suites/erp/frontends/axelor/` · 1

- [ ] `programs/suites/erp/frontends/axelor/index.md` · 783b

### `programs/suites/erp/frontends/axelor/latest/` · 6

- [ ] `programs/suites/erp/frontends/axelor/latest/api.md` · 2.2k
- [ ] `programs/suites/erp/frontends/axelor/latest/description.md` · 1.2k
- [ ] `programs/suites/erp/frontends/axelor/latest/features.md` · 1.1k
- [ ] `programs/suites/erp/frontends/axelor/latest/layout.md` · 1.6k
- [ ] `programs/suites/erp/frontends/axelor/latest/menus.md` · 922b
- [ ] `programs/suites/erp/frontends/axelor/latest/shortcuts.md` · 438b

### `programs/suites/erp/frontends/dolibarr/` · 1

- [ ] `programs/suites/erp/frontends/dolibarr/index.md` · 748b

### `programs/suites/erp/frontends/dolibarr/latest/` · 6

- [ ] `programs/suites/erp/frontends/dolibarr/latest/api.md` · 2.6k
- [ ] `programs/suites/erp/frontends/dolibarr/latest/description.md` · 1.2k
- [ ] `programs/suites/erp/frontends/dolibarr/latest/features.md` · 1.2k
- [ ] `programs/suites/erp/frontends/dolibarr/latest/layout.md` · 1.8k
- [ ] `programs/suites/erp/frontends/dolibarr/latest/menus.md` · 1.1k
- [ ] `programs/suites/erp/frontends/dolibarr/latest/shortcuts.md` · 461b

### `programs/suites/erp/frontends/erpnext/` · 1

- [ ] `programs/suites/erp/frontends/erpnext/index.md` · 782b

### `programs/suites/erp/frontends/erpnext/latest/` · 6

- [ ] `programs/suites/erp/frontends/erpnext/latest/api.md` · 2.3k
- [ ] `programs/suites/erp/frontends/erpnext/latest/description.md` · 1.3k
- [ ] `programs/suites/erp/frontends/erpnext/latest/features.md` · 1.3k
- [ ] `programs/suites/erp/frontends/erpnext/latest/layout.md` · 1.8k
- [ ] `programs/suites/erp/frontends/erpnext/latest/menus.md` · 923b
- [ ] `programs/suites/erp/frontends/erpnext/latest/shortcuts.md` · 564b

### `programs/suites/erp/frontends/odoo/` · 1

- [ ] `programs/suites/erp/frontends/odoo/index.md` · 821b

### `programs/suites/erp/frontends/odoo/latest/` · 6

- [ ] `programs/suites/erp/frontends/odoo/latest/api.md` · 2.5k
- [ ] `programs/suites/erp/frontends/odoo/latest/description.md` · 1.4k
- [ ] `programs/suites/erp/frontends/odoo/latest/features.md` · 1.4k
- [ ] `programs/suites/erp/frontends/odoo/latest/layout.md` · 1.9k
- [ ] `programs/suites/erp/frontends/odoo/latest/menus.md` · 1.1k
- [ ] `programs/suites/erp/frontends/odoo/latest/shortcuts.md` · 870b

### `programs/suites/erp/frontends/sage/` · 1

- [ ] `programs/suites/erp/frontends/sage/index.md` · 911b

### `programs/suites/erp/frontends/sage/latest/` · 6

- [ ] `programs/suites/erp/frontends/sage/latest/api.md` · 1.8k
- [ ] `programs/suites/erp/frontends/sage/latest/description.md` · 1.3k
- [ ] `programs/suites/erp/frontends/sage/latest/features.md` · 1.1k
- [ ] `programs/suites/erp/frontends/sage/latest/layout.md` · 1.1k
- [ ] `programs/suites/erp/frontends/sage/latest/menus.md` · 954b
- [ ] `programs/suites/erp/frontends/sage/latest/shortcuts.md` · 797b

### `programs/suites/erp/frontends/tryton/` · 1

- [ ] `programs/suites/erp/frontends/tryton/index.md` · 787b

### `programs/suites/erp/frontends/tryton/latest/` · 6

- [ ] `programs/suites/erp/frontends/tryton/latest/api.md` · 2.2k
- [ ] `programs/suites/erp/frontends/tryton/latest/description.md` · 1.1k
- [ ] `programs/suites/erp/frontends/tryton/latest/features.md` · 1.0k
- [ ] `programs/suites/erp/frontends/tryton/latest/layout.md` · 1.7k
- [ ] `programs/suites/erp/frontends/tryton/latest/menus.md` · 992b
- [ ] `programs/suites/erp/frontends/tryton/latest/shortcuts.md` · 612b

### `programs/suites/marketplace/` · 1

- [ ] `programs/suites/marketplace/index.md` · 2.4k · Plan[~]

### `programs/suites/marketplace/frontends/` · 1

- [ ] `programs/suites/marketplace/frontends/index.md` · 2.7k

### `programs/suites/marketplace/frontends/arcemall/` · 1

- [ ] `programs/suites/marketplace/frontends/arcemall/index.md` · 901b

### `programs/suites/marketplace/frontends/arcemall/latest/` · 6

- [ ] `programs/suites/marketplace/frontends/arcemall/latest/api.md` · 1.4k
- [ ] `programs/suites/marketplace/frontends/arcemall/latest/description.md` · 1.2k
- [ ] `programs/suites/marketplace/frontends/arcemall/latest/features.md` · 963b
- [ ] `programs/suites/marketplace/frontends/arcemall/latest/layout.md` · 885b
- [ ] `programs/suites/marketplace/frontends/arcemall/latest/menus.md` · 765b
- [ ] `programs/suites/marketplace/frontends/arcemall/latest/shortcuts.md` · 314b

### `programs/suites/marketplace/frontends/cs-cart-multivendor/` · 1

- [ ] `programs/suites/marketplace/frontends/cs-cart-multivendor/index.md` · 819b

### `programs/suites/marketplace/frontends/cs-cart-multivendor/latest/` · 6

- [ ] `programs/suites/marketplace/frontends/cs-cart-multivendor/latest/api.md` · 1.8k
- [ ] `programs/suites/marketplace/frontends/cs-cart-multivendor/latest/description.md` · 1.1k
- [ ] `programs/suites/marketplace/frontends/cs-cart-multivendor/latest/features.md` · 889b
- [ ] `programs/suites/marketplace/frontends/cs-cart-multivendor/latest/layout.md` · 970b
- [ ] `programs/suites/marketplace/frontends/cs-cart-multivendor/latest/menus.md` · 945b
- [ ] `programs/suites/marketplace/frontends/cs-cart-multivendor/latest/shortcuts.md` · 409b

### `programs/suites/marketplace/frontends/ebay/` · 1

- [ ] `programs/suites/marketplace/frontends/ebay/index.md` · 856b

### `programs/suites/marketplace/frontends/ebay/latest/` · 6

- [ ] `programs/suites/marketplace/frontends/ebay/latest/api.md` · 2.5k
- [ ] `programs/suites/marketplace/frontends/ebay/latest/description.md` · 1.1k
- [ ] `programs/suites/marketplace/frontends/ebay/latest/features.md` · 1.1k
- [ ] `programs/suites/marketplace/frontends/ebay/latest/layout.md` · 949b
- [ ] `programs/suites/marketplace/frontends/ebay/latest/menus.md` · 971b
- [ ] `programs/suites/marketplace/frontends/ebay/latest/shortcuts.md` · 424b

### `programs/suites/marketplace/frontends/etsy/` · 1

- [ ] `programs/suites/marketplace/frontends/etsy/index.md` · 754b

### `programs/suites/marketplace/frontends/etsy/latest/` · 6

- [ ] `programs/suites/marketplace/frontends/etsy/latest/api.md` · 2.1k
- [ ] `programs/suites/marketplace/frontends/etsy/latest/description.md` · 1.1k
- [ ] `programs/suites/marketplace/frontends/etsy/latest/features.md` · 987b
- [ ] `programs/suites/marketplace/frontends/etsy/latest/layout.md` · 940b
- [ ] `programs/suites/marketplace/frontends/etsy/latest/menus.md` · 934b
- [ ] `programs/suites/marketplace/frontends/etsy/latest/shortcuts.md` · 378b

### `programs/suites/marketplace/frontends/kleinanzeigen/` · 1

- [ ] `programs/suites/marketplace/frontends/kleinanzeigen/index.md` · 914b

### `programs/suites/marketplace/frontends/kleinanzeigen/latest/` · 6

- [ ] `programs/suites/marketplace/frontends/kleinanzeigen/latest/api.md` · 1.3k
- [ ] `programs/suites/marketplace/frontends/kleinanzeigen/latest/description.md` · 1.1k
- [ ] `programs/suites/marketplace/frontends/kleinanzeigen/latest/features.md` · 1020b
- [ ] `programs/suites/marketplace/frontends/kleinanzeigen/latest/layout.md` · 1.5k
- [ ] `programs/suites/marketplace/frontends/kleinanzeigen/latest/menus.md` · 820b
- [ ] `programs/suites/marketplace/frontends/kleinanzeigen/latest/shortcuts.md` · 347b

### `programs/suites/marketplace/frontends/sharetribe/` · 1

- [ ] `programs/suites/marketplace/frontends/sharetribe/index.md` · 960b

### `programs/suites/marketplace/frontends/sharetribe/latest/` · 6

- [ ] `programs/suites/marketplace/frontends/sharetribe/latest/api.md` · 2.3k
- [ ] `programs/suites/marketplace/frontends/sharetribe/latest/description.md` · 1.4k
- [ ] `programs/suites/marketplace/frontends/sharetribe/latest/features.md` · 1.3k
- [ ] `programs/suites/marketplace/frontends/sharetribe/latest/layout.md` · 1.7k
- [ ] `programs/suites/marketplace/frontends/sharetribe/latest/menus.md` · 996b
- [ ] `programs/suites/marketplace/frontends/sharetribe/latest/shortcuts.md` · 395b

### `programs/suites/workflows/frontends/` · 1

- [ ] `programs/suites/workflows/frontends/index.md` · 2.6k

### `programs/suites/workflows/frontends/apache-airflow/` · 1

- [ ] `programs/suites/workflows/frontends/apache-airflow/index.md` · 860b

### `programs/suites/workflows/frontends/apache-airflow/latest/` · 6

- [ ] `programs/suites/workflows/frontends/apache-airflow/latest/api.md` · 2.5k
- [ ] `programs/suites/workflows/frontends/apache-airflow/latest/description.md` · 1.3k
- [ ] `programs/suites/workflows/frontends/apache-airflow/latest/features.md` · 1.3k
- [ ] `programs/suites/workflows/frontends/apache-airflow/latest/layout.md` · 2.1k
- [ ] `programs/suites/workflows/frontends/apache-airflow/latest/menus.md` · 1005b
- [ ] `programs/suites/workflows/frontends/apache-airflow/latest/shortcuts.md` · 773b

### `programs/suites/workflows/frontends/make/` · 1

- [ ] `programs/suites/workflows/frontends/make/index.md` · 795b

### `programs/suites/workflows/frontends/make/latest/` · 6

- [ ] `programs/suites/workflows/frontends/make/latest/api.md` · 2.1k
- [ ] `programs/suites/workflows/frontends/make/latest/description.md` · 1.2k
- [ ] `programs/suites/workflows/frontends/make/latest/features.md` · 1.3k
- [ ] `programs/suites/workflows/frontends/make/latest/layout.md` · 1.9k
- [ ] `programs/suites/workflows/frontends/make/latest/menus.md` · 981b
- [ ] `programs/suites/workflows/frontends/make/latest/shortcuts.md` · 481b

### `programs/suites/workflows/frontends/n8n/` · 1

- [ ] `programs/suites/workflows/frontends/n8n/index.md` · 771b

### `programs/suites/workflows/frontends/n8n/latest/` · 6

- [ ] `programs/suites/workflows/frontends/n8n/latest/api.md` · 2.3k
- [ ] `programs/suites/workflows/frontends/n8n/latest/description.md` · 1.3k
- [ ] `programs/suites/workflows/frontends/n8n/latest/features.md` · 1.3k
- [ ] `programs/suites/workflows/frontends/n8n/latest/layout.md` · 2.0k
- [ ] `programs/suites/workflows/frontends/n8n/latest/menus.md` · 1.3k
- [ ] `programs/suites/workflows/frontends/n8n/latest/shortcuts.md` · 771b

### `programs/suites/workflows/frontends/node-red/` · 1

- [ ] `programs/suites/workflows/frontends/node-red/index.md` · 832b

### `programs/suites/workflows/frontends/node-red/latest/` · 6

- [ ] `programs/suites/workflows/frontends/node-red/latest/api.md` · 2.1k
- [ ] `programs/suites/workflows/frontends/node-red/latest/description.md` · 1.2k
- [ ] `programs/suites/workflows/frontends/node-red/latest/features.md` · 1.4k
- [ ] `programs/suites/workflows/frontends/node-red/latest/layout.md` · 2.0k
- [ ] `programs/suites/workflows/frontends/node-red/latest/menus.md` · 1.2k
- [ ] `programs/suites/workflows/frontends/node-red/latest/shortcuts.md` · 806b

### `programs/suites/workflows/frontends/prefect/` · 1

- [ ] `programs/suites/workflows/frontends/prefect/index.md` · 736b

### `programs/suites/workflows/frontends/prefect/latest/` · 6

- [ ] `programs/suites/workflows/frontends/prefect/latest/api.md` · 2.3k
- [ ] `programs/suites/workflows/frontends/prefect/latest/description.md` · 1.2k
- [ ] `programs/suites/workflows/frontends/prefect/latest/features.md` · 1.3k
- [ ] `programs/suites/workflows/frontends/prefect/latest/layout.md` · 1.9k
- [ ] `programs/suites/workflows/frontends/prefect/latest/menus.md` · 969b
- [ ] `programs/suites/workflows/frontends/prefect/latest/shortcuts.md` · 727b

### `programs/suites/workflows/frontends/zapier/` · 1

- [ ] `programs/suites/workflows/frontends/zapier/index.md` · 801b

### `programs/suites/workflows/frontends/zapier/latest/` · 6

- [ ] `programs/suites/workflows/frontends/zapier/latest/api.md` · 2.2k
- [ ] `programs/suites/workflows/frontends/zapier/latest/description.md` · 1.1k
- [ ] `programs/suites/workflows/frontends/zapier/latest/features.md` · 1.1k
- [ ] `programs/suites/workflows/frontends/zapier/latest/layout.md` · 2.1k
- [ ] `programs/suites/workflows/frontends/zapier/latest/menus.md` · 1.1k
- [ ] `programs/suites/workflows/frontends/zapier/latest/shortcuts.md` · 449b

## F. Form nicht gleich – Struktur abgleichen – 42 Dateien

### `programs/apps/calendar/` · 1

- [ ] `programs/apps/calendar/index.md` · 3.6k · Plan[~] · Parität: links en-only=['../platform/desktop/masks/index.md', 'masks/index.md'] de-only=['../platform/desktop/frontends/index.md', 'frontends/index.md'] · hash changed since verification

### `programs/apps/contact/` · 1

- [ ] `programs/apps/contact/index.md` · 3.4k · Plan[~] · Parität: links en-only=['../platform/desktop/masks/index.md'] de-only=['../platform/desktop/frontends/index.md'] · hash changed since verification

### `programs/apps/gallery/` · 1

- [ ] `programs/apps/gallery/index.md` · 2.8k · Plan[~] · Parität: links en-only=['../platform/desktop/masks/index.md'] de-only=['../platform/desktop/frontends/index.md'] · hash changed since verification

### `programs/apps/helpdesk/` · 1

- [ ] `programs/apps/helpdesk/index.md` · 3.4k · Plan[~] · Parität: links en-only=['../platform/desktop/masks/index.md'] de-only=['../platform/desktop/frontends/index.md'] · hash changed since verification

### `programs/apps/maps/` · 1

- [ ] `programs/apps/maps/index.md` · 3.2k · Plan[~] · Parität: links en-only=['../platform/desktop/masks/index.md'] de-only=['../platform/desktop/frontends/index.md'] · hash changed since verification

### `programs/apps/marketing/` · 1

- [ ] `programs/apps/marketing/index.md` · 3.7k · Plan[~] · Parität: links en-only=['../platform/desktop/masks/index.md'] de-only=['../platform/desktop/frontends/index.md'] · hash changed since verification

### `programs/apps/projectmanagement/` · 1

- [ ] `programs/apps/projectmanagement/index.md` · 3.6k · Plan[~] · Parität: links en-only=['../platform/desktop/masks/index.md'] de-only=['../platform/desktop/frontends/index.md'] · hash changed since verification

### `programs/apps/projectmanagement/frontends/openproject/` · 1

- [ ] `programs/apps/projectmanagement/frontends/openproject/index.md` · 1009b · Parität: links en-only=['../masks/openproject/api.md', '../masks/openproject/description.md', '../masks/openproject/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/apps/projectmanagement/frontends/planka/` · 1

- [ ] `programs/apps/projectmanagement/frontends/planka/index.md` · 926b · Parität: links en-only=['../masks/planka/api.md', '../masks/planka/description.md', '../masks/planka/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/apps/projectmanagement/frontends/redmine/` · 1

- [ ] `programs/apps/projectmanagement/frontends/redmine/index.md` · 964b · Parität: links en-only=['../masks/redmine/api.md', '../masks/redmine/description.md', '../masks/redmine/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/apps/projectmanagement/frontends/taiga/` · 1

- [ ] `programs/apps/projectmanagement/frontends/taiga/index.md` · 832b · Parität: links en-only=['../masks/taiga/api.md', '../masks/taiga/description.md', '../masks/taiga/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/apps/projectmanagement/frontends/wekan/` · 1

- [ ] `programs/apps/projectmanagement/frontends/wekan/index.md` · 868b · Parität: links en-only=['../masks/wekan/api.md', '../masks/wekan/description.md', '../masks/wekan/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/apps/streaming/` · 1

- [ ] `programs/apps/streaming/index.md` · 3.3k · Plan[~] · Parität: links en-only=['../platform/desktop/masks/index.md'] de-only=['../platform/desktop/frontends/index.md'] · hash changed since verification

### `programs/apps/streaming/frontends/ant-media-server/` · 1

- [ ] `programs/apps/streaming/frontends/ant-media-server/index.md` · 1.1k · Parität: links en-only=['../masks/ant-media-server/api.md', '../masks/ant-media-server/description.md', '../masks/ant-media-server/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/apps/streaming/frontends/ffmpeg/` · 1

- [ ] `programs/apps/streaming/frontends/ffmpeg/index.md` · 2.2k · Parität: links en-only=['../masks/ffmpeg/api.md', '../masks/ffmpeg/description.md', '../masks/ffmpeg/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/apps/streaming/frontends/gstreamer/` · 1

- [ ] `programs/apps/streaming/frontends/gstreamer/index.md` · 1.1k · Parität: links en-only=['../masks/gstreamer/api.md', '../masks/gstreamer/description.md', '../masks/gstreamer/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/apps/streaming/frontends/mediamtx/` · 1

- [ ] `programs/apps/streaming/frontends/mediamtx/index.md` · 1.1k · Parität: links en-only=['../masks/mediamtx/api.md', '../masks/mediamtx/description.md', '../masks/mediamtx/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/apps/streaming/frontends/mistserver/` · 1

- [ ] `programs/apps/streaming/frontends/mistserver/index.md` · 1.1k · Parität: links en-only=['../masks/mistserver/api.md', '../masks/mistserver/description.md', '../masks/mistserver/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/apps/streaming/frontends/nginx-rtmp-module/` · 1

- [ ] `programs/apps/streaming/frontends/nginx-rtmp-module/index.md` · 1.2k · Parität: links en-only=['../masks/nginx-rtmp-module/api.md', '../masks/nginx-rtmp-module/description.md', '../masks/nginx-rtmp-module/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/apps/streaming/frontends/obs-studio/` · 1

- [ ] `programs/apps/streaming/frontends/obs-studio/index.md` · 947b · Parität: links en-only=['../masks/obs-studio/api.md', '../masks/obs-studio/description.md', '../masks/obs-studio/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/apps/streaming/frontends/restream/` · 1

- [ ] `programs/apps/streaming/frontends/restream/index.md` · 1.1k · Parität: links en-only=['../masks/restream/api.md', '../masks/restream/description.md', '../masks/restream/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/apps/streaming/frontends/restreamer/` · 1

- [ ] `programs/apps/streaming/frontends/restreamer/index.md` · 940b · Parität: links en-only=['../masks/restreamer/api.md', '../masks/restreamer/description.md', '../masks/restreamer/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/apps/streaming/frontends/wowza/` · 1

- [ ] `programs/apps/streaming/frontends/wowza/index.md` · 1.4k · Parität: links en-only=['../masks/wowza/api.md', '../masks/wowza/description.md', '../masks/wowza/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/apps/whiteboards/` · 1

- [ ] `programs/apps/whiteboards/index.md` · 3.3k · Plan[~] · Parität: links en-only=['../platform/desktop/masks/index.md'] de-only=['../platform/desktop/frontends/index.md'] · hash changed since verification

### `programs/apps/whiteboards/frontends/drawio/` · 1

- [ ] `programs/apps/whiteboards/frontends/drawio/index.md` · 925b · Parität: links en-only=['../masks/drawio/api.md', '../masks/drawio/description.md', '../masks/drawio/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/apps/whiteboards/frontends/excalidraw/` · 1

- [ ] `programs/apps/whiteboards/frontends/excalidraw/index.md` · 882b · Parität: links en-only=['../masks/excalidraw/api.md', '../masks/excalidraw/description.md', '../masks/excalidraw/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/apps/whiteboards/frontends/miro/` · 1

- [ ] `programs/apps/whiteboards/frontends/miro/index.md` · 812b · Parität: links en-only=['../masks/miro/api.md', '../masks/miro/description.md', '../masks/miro/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/apps/whiteboards/frontends/mural/` · 1

- [ ] `programs/apps/whiteboards/frontends/mural/index.md` · 792b · Parität: links en-only=['../masks/mural/api.md', '../masks/mural/description.md', '../masks/mural/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/apps/whiteboards/frontends/openboard/` · 1

- [ ] `programs/apps/whiteboards/frontends/openboard/index.md` · 876b · Parität: links en-only=['../masks/openboard/api.md', '../masks/openboard/description.md', '../masks/openboard/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/apps/whiteboards/frontends/tldraw/` · 1

- [ ] `programs/apps/whiteboards/frontends/tldraw/index.md` · 940b · Parität: links en-only=['../masks/tldraw/api.md', '../masks/tldraw/description.md', '../masks/tldraw/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/apps/wiki/frontends/confluence/` · 1

- [ ] `programs/apps/wiki/frontends/confluence/index.md` · 620b · Parität: links en-only=['../masks/confluence/api.md', '../masks/confluence/description.md', '../masks/confluence/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/apps/wiki/frontends/mediawiki/` · 1

- [ ] `programs/apps/wiki/frontends/mediawiki/index.md` · 611b · Parität: links en-only=['../masks/mediawiki/api.md', '../masks/mediawiki/description.md', '../masks/mediawiki/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/apps/wiki/frontends/notion/` · 1

- [ ] `programs/apps/wiki/frontends/notion/index.md` · 590b · Parität: links en-only=['../masks/notion/api.md', '../masks/notion/description.md', '../masks/notion/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/apps/wiki/frontends/tango.io/` · 1

- [ ] `programs/apps/wiki/frontends/tango.io/index.md` · 609b · Parität: links en-only=['../masks/tango.io/api.md', '../masks/tango.io/description.md', '../masks/tango.io/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/apps/wiki/frontends/vscodium/` · 1

- [ ] `programs/apps/wiki/frontends/vscodium/index.md` · 595b · Parität: links en-only=['../masks/vscodium/api.md', '../masks/vscodium/description.md', '../masks/vscodium/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/apps/wiki/frontends/wikijs/` · 1

- [ ] `programs/apps/wiki/frontends/wikijs/index.md` · 577b · Parität: links en-only=['../masks/wikijs/api.md', '../masks/wikijs/description.md', '../masks/wikijs/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/apps/wiki/frontends/xwiki/` · 1

- [ ] `programs/apps/wiki/frontends/xwiki/index.md` · 600b · Parität: links en-only=['../masks/xwiki/api.md', '../masks/xwiki/description.md', '../masks/xwiki/features.md'] de-only=['latest/api.md', 'latest/description.md', 'latest/features.md'] · hash changed since verification

### `programs/platform/desktop/` · 1

- [ ] `programs/platform/desktop/index.md` · 3.9k · Plan[~] · Parität: links en-only=['masks/index.md'] de-only=['frontends/index.md'] · hash changed since verification

### `programs/suites/crm/` · 1

- [ ] `programs/suites/crm/index.md` · 3.4k · Plan[~] · Parität: links en-only=['../platform/desktop/masks/index.md', 'masks/civicrm/index.md', 'masks/espocrm/index.md'] de-only=['../platform/desktop/frontends/index.md', 'frontends/civicrm/index.md', 'frontends/espocrm/index.md'] · hash changed since verification

### `programs/suites/democracy/` · 1

- [ ] `programs/suites/democracy/index.md` · 3.2k · Plan[~] · Parität: links en-only=['../platform/desktop/masks/index.md', 'masks/adhocracy4/index.md', 'masks/circo/index.md'] de-only=['../platform/desktop/frontends/index.md', 'frontends/adhocracy4/index.md', 'frontends/circo/index.md'] · hash changed since verification

### `programs/suites/erp/` · 1

- [ ] `programs/suites/erp/index.md` · 3.2k · Plan[~] · Parität: links en-only=['../platform/desktop/masks/index.md', 'masks/axelor/index.md', 'masks/dolibarr/index.md'] de-only=['../platform/desktop/frontends/index.md', 'frontends/axelor/index.md', 'frontends/dolibarr/index.md'] · hash changed since verification

### `programs/suites/workflows/` · 1

- [ ] `programs/suites/workflows/index.md` · 3.2k · Plan[~] · Parität: links en-only=['../platform/desktop/masks/index.md', 'masks/apache-airflow/index.md', 'masks/index.md'] de-only=['../platform/desktop/frontends/index.md', 'frontends/apache-airflow/index.md', 'frontends/index.md'] · hash changed since verification

## H. Beide Seiten da, kein Befund – lesen und bestätigen – 145 Dateien

### `(wurzel)/` · 1

- [ ] `index.md` · 2.0k · hash changed since verification

### `data/` · 2

- [ ] `data/api.md` · 8.7k · hash changed since verification
- [ ] `data/index.md` · 6.5k · hash changed since verification

### `interactions/animations/loop/` · 1

- [ ] `interactions/animations/loop/index.md` · 928b

### `interactions/animations/loop/glow/` · 3

- [ ] `interactions/animations/loop/glow/appearance.md` · 1.5k
- [ ] `interactions/animations/loop/glow/attributes.md` · 1.4k
- [ ] `interactions/animations/loop/glow/description.md` · 990b

### `interactions/animations/loop/heartbeat/` · 3

- [ ] `interactions/animations/loop/heartbeat/appearance.md` · 1.5k
- [ ] `interactions/animations/loop/heartbeat/attributes.md` · 1.7k
- [ ] `interactions/animations/loop/heartbeat/description.md` · 954b

### `interactions/animations/loop/pulse/` · 3

- [ ] `interactions/animations/loop/pulse/appearance.md` · 1.4k
- [ ] `interactions/animations/loop/pulse/attributes.md` · 1.7k
- [ ] `interactions/animations/loop/pulse/description.md` · 847b

### `interactions/animations/loop/spin/` · 3

- [ ] `interactions/animations/loop/spin/appearance.md` · 1.8k
- [ ] `interactions/animations/loop/spin/attributes.md` · 1.5k
- [ ] `interactions/animations/loop/spin/description.md` · 895b

### `programs/apps/calendar/frontends/davical/` · 1

- [ ] `programs/apps/calendar/frontends/davical/index.md` · 2.7k · hash changed since verification

### `programs/apps/calendar/frontends/davical/latest/` · 1

- [ ] `programs/apps/calendar/frontends/davical/latest/api.md` · 7.8k · hash changed since verification

### `programs/apps/calendar/frontends/google-calendar/` · 1

- [ ] `programs/apps/calendar/frontends/google-calendar/index.md` · 8.3k · hash changed since verification

### `programs/apps/calendar/frontends/google-calendar/latest/` · 2

- [ ] `programs/apps/calendar/frontends/google-calendar/latest/layout.md` · 7.6k · hash changed since verification
- [ ] `programs/apps/calendar/frontends/google-calendar/latest/menus.md` · 6.0k · hash changed since verification

### `programs/apps/calendar/frontends/merkuro/` · 1

- [ ] `programs/apps/calendar/frontends/merkuro/index.md` · 3.7k · hash changed since verification

### `programs/apps/calendar/frontends/merkuro/latest/` · 5

- [ ] `programs/apps/calendar/frontends/merkuro/latest/description.md` · 4.5k · hash changed since verification
- [ ] `programs/apps/calendar/frontends/merkuro/latest/features.md` · 4.3k · hash changed since verification
- [ ] `programs/apps/calendar/frontends/merkuro/latest/layout.md` · 6.1k · hash changed since verification
- [ ] `programs/apps/calendar/frontends/merkuro/latest/menus.md` · 3.4k · hash changed since verification
- [ ] `programs/apps/calendar/frontends/merkuro/latest/shortcuts.md` · 2.8k · hash changed since verification

### `programs/apps/calendar/frontends/nextcloud-calendar/` · 1

- [ ] `programs/apps/calendar/frontends/nextcloud-calendar/index.md` · 3.7k · hash changed since verification

### `programs/apps/calendar/frontends/nextcloud-calendar/latest/` · 5

- [ ] `programs/apps/calendar/frontends/nextcloud-calendar/latest/description.md` · 4.9k · hash changed since verification
- [ ] `programs/apps/calendar/frontends/nextcloud-calendar/latest/features.md` · 6.2k · hash changed since verification
- [ ] `programs/apps/calendar/frontends/nextcloud-calendar/latest/layout.md` · 7.4k · hash changed since verification
- [ ] `programs/apps/calendar/frontends/nextcloud-calendar/latest/menus.md` · 5.7k · hash changed since verification
- [ ] `programs/apps/calendar/frontends/nextcloud-calendar/latest/shortcuts.md` · 4.1k · hash changed since verification

### `programs/apps/calendar/frontends/outlook-calendar/` · 1

- [ ] `programs/apps/calendar/frontends/outlook-calendar/index.md` · 5.9k · hash changed since verification

### `programs/apps/calendar/frontends/outlook-calendar/latest/` · 5

- [ ] `programs/apps/calendar/frontends/outlook-calendar/latest/description.md` · 5.3k · hash changed since verification
- [ ] `programs/apps/calendar/frontends/outlook-calendar/latest/features.md` · 6.9k · hash changed since verification
- [ ] `programs/apps/calendar/frontends/outlook-calendar/latest/layout.md` · 5.9k · hash changed since verification
- [ ] `programs/apps/calendar/frontends/outlook-calendar/latest/menus.md` · 4.1k · hash changed since verification
- [ ] `programs/apps/calendar/frontends/outlook-calendar/latest/shortcuts.md` · 4.0k · hash changed since verification

### `programs/apps/calendar/frontends/planner/` · 1

- [ ] `programs/apps/calendar/frontends/planner/index.md` · 5.0k · hash changed since verification

### `programs/apps/calendar/frontends/planner/latest/` · 1

- [ ] `programs/apps/calendar/frontends/planner/latest/api.md` · 8.5k · hash changed since verification

### `programs/apps/contact/frontends/` · 1

- [ ] `programs/apps/contact/frontends/index.md` · 2.4k · hash changed since verification

### `programs/apps/contact/frontends/gnome-contacts/` · 1

- [ ] `programs/apps/contact/frontends/gnome-contacts/index.md` · 861b · hash changed since verification

### `programs/apps/contact/frontends/gnome-contacts/latest/` · 1

- [ ] `programs/apps/contact/frontends/gnome-contacts/latest/api.md` · 1.7k · hash changed since verification

### `programs/apps/contact/frontends/kaddressbook/` · 1

- [ ] `programs/apps/contact/frontends/kaddressbook/index.md` · 854b · hash changed since verification

### `programs/apps/contact/frontends/kaddressbook/latest/` · 1

- [ ] `programs/apps/contact/frontends/kaddressbook/latest/api.md` · 2.1k · hash changed since verification

### `programs/apps/contact/frontends/monica/` · 1

- [ ] `programs/apps/contact/frontends/monica/index.md` · 837b · hash changed since verification

### `programs/apps/contact/frontends/monica/latest/` · 1

- [ ] `programs/apps/contact/frontends/monica/latest/api.md` · 2.3k · hash changed since verification

### `programs/apps/contact/frontends/nextcloud-contacts/` · 1

- [ ] `programs/apps/contact/frontends/nextcloud-contacts/index.md` · 857b · hash changed since verification

### `programs/apps/contact/frontends/nextcloud-contacts/latest/` · 1

- [ ] `programs/apps/contact/frontends/nextcloud-contacts/latest/api.md` · 2.6k · hash changed since verification

### `programs/apps/gallery/frontends/` · 1

- [ ] `programs/apps/gallery/frontends/index.md` · 2.8k · hash changed since verification

### `programs/apps/gallery/frontends/coppermine/` · 1

- [ ] `programs/apps/gallery/frontends/coppermine/index.md` · 858b · hash changed since verification

### `programs/apps/gallery/frontends/coppermine/latest/` · 1

- [ ] `programs/apps/gallery/frontends/coppermine/latest/api.md` · 2.6k · hash changed since verification

### `programs/apps/gallery/frontends/damselfly/` · 1

- [ ] `programs/apps/gallery/frontends/damselfly/index.md` · 771b · hash changed since verification

### `programs/apps/gallery/frontends/damselfly/latest/` · 1

- [ ] `programs/apps/gallery/frontends/damselfly/latest/api.md` · 2.2k · hash changed since verification

### `programs/apps/gallery/frontends/immich/` · 1

- [ ] `programs/apps/gallery/frontends/immich/index.md` · 875b · hash changed since verification

### `programs/apps/gallery/frontends/immich/latest/` · 1

- [ ] `programs/apps/gallery/frontends/immich/latest/api.md` · 2.9k · hash changed since verification

### `programs/apps/gallery/frontends/librephotos/` · 1

- [ ] `programs/apps/gallery/frontends/librephotos/index.md` · 826b · hash changed since verification

### `programs/apps/gallery/frontends/librephotos/latest/` · 1

- [ ] `programs/apps/gallery/frontends/librephotos/latest/api.md` · 2.2k · hash changed since verification

### `programs/apps/gallery/frontends/lychee/` · 1

- [ ] `programs/apps/gallery/frontends/lychee/index.md` · 749b · hash changed since verification

### `programs/apps/gallery/frontends/lychee/latest/` · 1

- [ ] `programs/apps/gallery/frontends/lychee/latest/api.md` · 2.4k · hash changed since verification

### `programs/apps/gallery/frontends/nextcloud-photos/` · 1

- [ ] `programs/apps/gallery/frontends/nextcloud-photos/index.md` · 978b · hash changed since verification

### `programs/apps/gallery/frontends/nextcloud-photos/latest/` · 1

- [ ] `programs/apps/gallery/frontends/nextcloud-photos/latest/api.md` · 2.6k · hash changed since verification

### `programs/apps/gallery/frontends/photoprism/` · 1

- [ ] `programs/apps/gallery/frontends/photoprism/index.md` · 829b · hash changed since verification

### `programs/apps/gallery/frontends/photoprism/latest/` · 1

- [ ] `programs/apps/gallery/frontends/photoprism/latest/api.md` · 2.6k · hash changed since verification

### `programs/apps/gallery/frontends/piwigo/` · 1

- [ ] `programs/apps/gallery/frontends/piwigo/index.md` · 804b · hash changed since verification

### `programs/apps/gallery/frontends/piwigo/latest/` · 1

- [ ] `programs/apps/gallery/frontends/piwigo/latest/api.md` · 2.6k · hash changed since verification

### `programs/apps/helpdesk/frontends/` · 1

- [ ] `programs/apps/helpdesk/frontends/index.md` · 2.8k · hash changed since verification

### `programs/apps/helpdesk/frontends/freshdesk/` · 1

- [ ] `programs/apps/helpdesk/frontends/freshdesk/index.md` · 719b · hash changed since verification

### `programs/apps/helpdesk/frontends/freshdesk/latest/` · 1

- [ ] `programs/apps/helpdesk/frontends/freshdesk/latest/api.md` · 2.4k · hash changed since verification

### `programs/apps/helpdesk/frontends/glpi/` · 1

- [ ] `programs/apps/helpdesk/frontends/glpi/index.md` · 890b · hash changed since verification

### `programs/apps/helpdesk/frontends/glpi/latest/` · 1

- [ ] `programs/apps/helpdesk/frontends/glpi/latest/api.md` · 2.5k · hash changed since verification

### `programs/apps/helpdesk/frontends/helodesk/` · 1

- [ ] `programs/apps/helpdesk/frontends/helodesk/index.md` · 886b · hash changed since verification

### `programs/apps/helpdesk/frontends/helodesk/latest/` · 1

- [ ] `programs/apps/helpdesk/frontends/helodesk/latest/api.md` · 2.5k · hash changed since verification

### `programs/apps/helpdesk/frontends/helpscout/` · 1

- [ ] `programs/apps/helpdesk/frontends/helpscout/index.md` · 745b · hash changed since verification

### `programs/apps/helpdesk/frontends/helpscout/latest/` · 1

- [ ] `programs/apps/helpdesk/frontends/helpscout/latest/api.md` · 2.1k · hash changed since verification

### `programs/apps/helpdesk/frontends/osticket/` · 1

- [ ] `programs/apps/helpdesk/frontends/osticket/index.md` · 779b · hash changed since verification

### `programs/apps/helpdesk/frontends/osticket/latest/` · 1

- [ ] `programs/apps/helpdesk/frontends/osticket/latest/api.md` · 2.3k · hash changed since verification

### `programs/apps/helpdesk/frontends/request-tracker/` · 1

- [ ] `programs/apps/helpdesk/frontends/request-tracker/index.md` · 820b · hash changed since verification

### `programs/apps/helpdesk/frontends/request-tracker/latest/` · 1

- [ ] `programs/apps/helpdesk/frontends/request-tracker/latest/api.md` · 2.5k · hash changed since verification

### `programs/apps/helpdesk/frontends/zammad/` · 1

- [ ] `programs/apps/helpdesk/frontends/zammad/index.md` · 869b · hash changed since verification

### `programs/apps/helpdesk/frontends/zammad/latest/` · 1

- [ ] `programs/apps/helpdesk/frontends/zammad/latest/api.md` · 2.9k · hash changed since verification

### `programs/apps/helpdesk/frontends/zendesk/` · 1

- [ ] `programs/apps/helpdesk/frontends/zendesk/index.md` · 772b · hash changed since verification

### `programs/apps/helpdesk/frontends/zendesk/latest/` · 1

- [ ] `programs/apps/helpdesk/frontends/zendesk/latest/api.md` · 3.0k · hash changed since verification

### `programs/apps/maps/frontends/` · 1

- [ ] `programs/apps/maps/frontends/index.md` · 2.6k · hash changed since verification

### `programs/apps/maps/frontends/leaflet/` · 1

- [ ] `programs/apps/maps/frontends/leaflet/index.md` · 755b · hash changed since verification

### `programs/apps/maps/frontends/leaflet/latest/` · 2

- [ ] `programs/apps/maps/frontends/leaflet/latest/api.md` · 1.8k · hash changed since verification
- [ ] `programs/apps/maps/frontends/leaflet/latest/description.md` · 1.1k · hash changed since verification

### `programs/apps/maps/frontends/maplibre/` · 1

- [ ] `programs/apps/maps/frontends/maplibre/index.md` · 910b · hash changed since verification

### `programs/apps/maps/frontends/openstreetmap/` · 1

- [ ] `programs/apps/maps/frontends/openstreetmap/index.md` · 878b · hash changed since verification

### `programs/apps/maps/frontends/openstreetmap/latest/` · 2

- [ ] `programs/apps/maps/frontends/openstreetmap/latest/api.md` · 2.4k · hash changed since verification
- [ ] `programs/apps/maps/frontends/openstreetmap/latest/description.md` · 1.2k · hash changed since verification

### `programs/apps/maps/frontends/organic-maps/` · 1

- [ ] `programs/apps/maps/frontends/organic-maps/index.md` · 776b · hash changed since verification

### `programs/apps/maps/frontends/organic-maps/latest/` · 2

- [ ] `programs/apps/maps/frontends/organic-maps/latest/api.md` · 1.1k · hash changed since verification
- [ ] `programs/apps/maps/frontends/organic-maps/latest/description.md` · 1.0k · hash changed since verification

### `programs/apps/maps/frontends/osmand/` · 1

- [ ] `programs/apps/maps/frontends/osmand/index.md` · 879b · hash changed since verification

### `programs/apps/maps/frontends/osmand/latest/` · 2

- [ ] `programs/apps/maps/frontends/osmand/latest/api.md` · 1.7k · hash changed since verification
- [ ] `programs/apps/maps/frontends/osmand/latest/description.md` · 1.1k · hash changed since verification

### `programs/apps/maps/frontends/qgis/` · 1

- [ ] `programs/apps/maps/frontends/qgis/index.md` · 796b · hash changed since verification

### `programs/apps/maps/frontends/qgis/latest/` · 2

- [ ] `programs/apps/maps/frontends/qgis/latest/api.md` · 1.9k · hash changed since verification
- [ ] `programs/apps/maps/frontends/qgis/latest/description.md` · 1.1k · hash changed since verification

### `programs/apps/maps/frontends/umap/` · 1

- [ ] `programs/apps/maps/frontends/umap/index.md` · 787b · hash changed since verification

### `programs/apps/maps/frontends/umap/latest/` · 2

- [ ] `programs/apps/maps/frontends/umap/latest/api.md` · 1.8k · hash changed since verification
- [ ] `programs/apps/maps/frontends/umap/latest/description.md` · 1.1k · hash changed since verification

### `programs/apps/marketing/frontends/` · 1

- [ ] `programs/apps/marketing/frontends/index.md` · 2.5k · hash changed since verification

### `programs/apps/marketing/frontends/google-analytics/` · 1

- [ ] `programs/apps/marketing/frontends/google-analytics/index.md` · 800b · hash changed since verification

### `programs/apps/marketing/frontends/google-analytics/latest/` · 1

- [ ] `programs/apps/marketing/frontends/google-analytics/latest/api.md` · 2.2k · hash changed since verification

### `programs/apps/marketing/frontends/hotjar/` · 1

- [ ] `programs/apps/marketing/frontends/hotjar/index.md` · 781b · hash changed since verification

### `programs/apps/marketing/frontends/mailchimp/` · 1

- [ ] `programs/apps/marketing/frontends/mailchimp/index.md` · 735b · hash changed since verification

### `programs/apps/marketing/frontends/mailchimp/latest/` · 2

- [ ] `programs/apps/marketing/frontends/mailchimp/latest/api.md` · 2.2k · hash changed since verification
- [ ] `programs/apps/marketing/frontends/mailchimp/latest/description.md` · 1.2k · hash changed since verification

### `programs/apps/marketing/frontends/matomo/` · 1

- [ ] `programs/apps/marketing/frontends/matomo/index.md` · 791b · hash changed since verification

### `programs/apps/marketing/frontends/matomo/latest/` · 2

- [ ] `programs/apps/marketing/frontends/matomo/latest/api.md` · 2.1k · hash changed since verification
- [ ] `programs/apps/marketing/frontends/matomo/latest/description.md` · 1.3k · hash changed since verification

### `programs/apps/marketing/frontends/mautic/` · 1

- [ ] `programs/apps/marketing/frontends/mautic/index.md` · 794b · hash changed since verification

### `programs/apps/marketing/frontends/mautic/latest/` · 2

- [ ] `programs/apps/marketing/frontends/mautic/latest/api.md` · 2.4k · hash changed since verification
- [ ] `programs/apps/marketing/frontends/mautic/latest/description.md` · 1.2k · hash changed since verification

### `programs/apps/marketing/frontends/plausible/` · 1

- [ ] `programs/apps/marketing/frontends/plausible/index.md` · 728b · hash changed since verification

### `programs/apps/marketing/frontends/plausible/latest/` · 1

- [ ] `programs/apps/marketing/frontends/plausible/latest/api.md` · 2.0k · hash changed since verification

### `programs/apps/messenger/frontends/discord/` · 1

- [ ] `programs/apps/messenger/frontends/discord/index.md` · 553b · hash changed since verification

### `programs/apps/messenger/frontends/discord/latest/` · 1

- [ ] `programs/apps/messenger/frontends/discord/latest/api.md` · 7.0k · hash changed since verification

### `programs/apps/messenger/frontends/element/` · 1

- [ ] `programs/apps/messenger/frontends/element/index.md` · 563b · hash changed since verification

### `programs/apps/messenger/frontends/element/latest/` · 1

- [ ] `programs/apps/messenger/frontends/element/latest/api.md` · 7.0k · hash changed since verification

### `programs/apps/messenger/frontends/kontact/` · 1

- [ ] `programs/apps/messenger/frontends/kontact/index.md` · 572b · hash changed since verification

### `programs/apps/messenger/frontends/kontact/latest/` · 1

- [ ] `programs/apps/messenger/frontends/kontact/latest/api.md` · 5.6k · hash changed since verification

### `programs/apps/messenger/frontends/mastodon/` · 1

- [ ] `programs/apps/messenger/frontends/mastodon/index.md` · 550b · hash changed since verification

### `programs/apps/messenger/frontends/mastodon/latest/` · 1

- [ ] `programs/apps/messenger/frontends/mastodon/latest/api.md` · 7.0k · hash changed since verification

### `programs/apps/messenger/frontends/outlook/` · 1

- [ ] `programs/apps/messenger/frontends/outlook/index.md` · 513b · hash changed since verification

### `programs/apps/messenger/frontends/outlook/latest/` · 1

- [ ] `programs/apps/messenger/frontends/outlook/latest/api.md` · 6.4k · hash changed since verification

### `programs/apps/messenger/frontends/telegram/` · 1

- [ ] `programs/apps/messenger/frontends/telegram/index.md` · 533b · hash changed since verification

### `programs/apps/messenger/frontends/telegram/latest/` · 1

- [ ] `programs/apps/messenger/frontends/telegram/latest/api.md` · 6.8k · hash changed since verification

### `programs/apps/messenger/frontends/thunderbird/` · 1

- [ ] `programs/apps/messenger/frontends/thunderbird/index.md` · 529b · hash changed since verification

### `programs/apps/messenger/frontends/thunderbird/latest/` · 1

- [ ] `programs/apps/messenger/frontends/thunderbird/latest/api.md` · 6.2k · hash changed since verification

### `programs/apps/projectmanagement/frontends/` · 1

- [ ] `programs/apps/projectmanagement/frontends/index.md` · 2.7k · hash changed since verification

### `programs/apps/projectmanagement/frontends/asana/` · 1

- [ ] `programs/apps/projectmanagement/frontends/asana/index.md` · 783b · hash changed since verification

### `programs/apps/projectmanagement/frontends/asana/latest/` · 2

- [ ] `programs/apps/projectmanagement/frontends/asana/latest/api.md` · 2.3k · hash changed since verification
- [ ] `programs/apps/projectmanagement/frontends/asana/latest/description.md` · 1.2k · hash changed since verification

### `programs/apps/projectmanagement/frontends/jira/` · 1

- [ ] `programs/apps/projectmanagement/frontends/jira/index.md` · 768b · hash changed since verification

### `programs/apps/projectmanagement/frontends/jira/latest/` · 2

- [ ] `programs/apps/projectmanagement/frontends/jira/latest/api.md` · 2.5k · hash changed since verification
- [ ] `programs/apps/projectmanagement/frontends/jira/latest/description.md` · 1.3k · hash changed since verification

### `programs/apps/projectmanagement/frontends/trello/` · 1

- [ ] `programs/apps/projectmanagement/frontends/trello/index.md` · 739b · hash changed since verification

### `programs/apps/projectmanagement/frontends/trello/latest/` · 2

- [ ] `programs/apps/projectmanagement/frontends/trello/latest/api.md` · 2.5k · hash changed since verification
- [ ] `programs/apps/projectmanagement/frontends/trello/latest/description.md` · 1.3k · hash changed since verification

### `programs/apps/streaming/frontends/` · 1

- [ ] `programs/apps/streaming/frontends/index.md` · 3.1k · hash changed since verification

### `programs/apps/whiteboards/frontends/` · 1

- [ ] `programs/apps/whiteboards/frontends/index.md` · 2.5k · hash changed since verification

## 🗑️ Gelöscht – 7

- [x] `data/anforderungen.md` · nicht mehr im Baum
- [x] `data/contacts/jscontact/beschreibung.md` · nicht mehr im Baum
- [x] `data/contacts/jscontact/speicherung.md` · nicht mehr im Baum
- [x] `data/felder.md` · nicht mehr im Baum
- [x] `data/formate.md` · nicht mehr im Baum
- [x] `data/konventionen.md` · nicht mehr im Baum
- [x] `data/modelle.md` · nicht mehr im Baum

## Changelog

  Stil der Datei angepasst und gequotet). Bestaetigt mit `--confirm`. Variante-Namen wie `vorlage`,
  `anordbar`, `bericht` bleiben deutsch – Bezeichner, ADR 0002.
- 2026-11-04 20:45 · **Regel ergaenzt:** zitierte Stellen (…/"…/«…») zaehlen nicht als fremdsprachliche
  Prosa. Deutsche Produkt-Labels in `en/` und englische Spezifikat-Zitate in `de/` sind Belege,
  keine Uebersetzungsreste. Das allein hat 34 False-Positives in D/E beseitigt.
- 2026-11-04 20:29 · Lauf: 1492 verfolgt, 1492 offen, 0 bestätigt · needs_en=687 needs_de=1 en_german=5 de_english=3 parity=28 rename=15 review=771
- 2026-11-04 20:29 · Lauf: 1492 verfolgt, 1492 offen, 0 bestätigt · needs_en=687 needs_de=1 en_german=5 de_english=3 parity=28 rename=17 review=771
- 2026-11-04 20:32 · Lauf: 1492 verfolgt, 1492 offen, 0 bestätigt · needs_en=687 needs_de=1 en_german=5 de_english=3 parity=28 rename=17 review=771
- 2026-11-04 20:34 · Lauf: 1492 verfolgt, 1492 offen, 0 bestätigt · needs_en=687 needs_de=1 en_german=5 de_english=3 parity=28 rename=17 review=771
- 2026-11-04 20:36 · Lauf: 1492 verfolgt, 1492 offen, 0 bestätigt · needs_en=687 needs_de=1 en_german=5 de_english=3 parity=28 rename=17 review=771
- 2026-11-04 20:37 · Lauf: 1492 verfolgt, 1492 offen, 0 bestätigt · needs_en=687 needs_de=1 en_german=5 de_english=3 parity=28 rename=17 review=771
- 2026-11-04 20:44 · Lauf: 1492 verfolgt, 1492 offen, 0 bestätigt · needs_en=687 needs_de=1 en_german=4 parity=28 rename=17 review=773
- 2026-11-04 20:47 · Lauf: 1492 verfolgt, 1492 offen, 0 bestätigt · needs_en=687 needs_de=1 en_german=2 parity=28 rename=17 review=775
- 2026-11-04 20:49 · Lauf: 1492 verfolgt, 1492 offen, 0 bestätigt · needs_en=687 needs_de=1 en_german=1 parity=28 rename=17 review=776
- 2026-11-04 20:50 · Lauf: 1492 verfolgt, 1489 offen, 3 bestätigt · needs_en=687 needs_de=1 en_german=1 parity=28 rename=17 review=773
- 2026-11-05 00:45 · Lauf: 1492 verfolgt, 1489 offen, 3 bestätigt · needs_en=687 needs_de=1 en_german=3 parity=28 rename=17 review=771
- 2026-11-05 01:45 · Lauf: 1492 verfolgt, 1489 offen, 3 bestätigt · needs_en=687 needs_de=1 en_german=3 code_german=15 parity=28 rename=17 review=757
- 2026-11-05 01:47 · Lauf: 1492 verfolgt, 1489 offen, 3 bestätigt · needs_en=687 needs_de=1 en_german=3 code_german=15 parity=151 rename=17 review=635
- 2026-11-05 01:54 · Lauf: 1492 verfolgt, 1489 offen, 3 bestätigt · needs_en=687 needs_de=1 en_german=3 code_german=15 parity=29 rename=17 review=756
- 2026-11-05 02:24 · Lauf: 1492 verfolgt, 1489 offen, 3 bestätigt · needs_en=687 needs_de=1 en_german=3 code_german=15 parity=28 rename=17 review=757
- 2026-11-05 03:47 · Lauf: 1492 verfolgt, 1489 offen, 3 bestätigt · needs_en=687 needs_de=1 en_german=1 parity=28 rename=17 review=773
- 2026-11-05 04:01 · Lauf: 1492 verfolgt, 1474 offen, 18 bestätigt · needs_en=687 parity=28 rename=17 review=759
- 2026-11-05 04:51 · Lauf: 1492 verfolgt, 715 offen, 777 bestätigt · needs_en=682 parity=28 rename=17 review=5
- 2026-11-05 04:53 · Lauf: 1492 verfolgt, 710 offen, 782 bestätigt · needs_en=682 parity=28 rename=17
- 2026-11-05 05:06 · Lauf: 1492 verfolgt, 710 offen, 782 bestätigt · needs_en=682 parity=24 rename=17 review=4
- 2026-11-05 06:09 · Lauf: 1492 verfolgt, 706 offen, 786 bestätigt · needs_en=659 parity=17 rename=17 review=30
- 2026-11-05 06:10 · Lauf: 1492 verfolgt, 676 offen, 816 bestätigt · needs_en=659 parity=17 rename=17
- 2026-11-05 06:53 · Lauf: 1492 verfolgt, 676 offen, 816 bestätigt · needs_en=659 rename=17 review=17
- 2026-11-05 06:53 · Lauf: 1492 verfolgt, 659 offen, 833 bestätigt · needs_en=659 rename=17
- 2026-11-05 07:28 · Lauf: 1499 verfolgt, 702 offen, 790 bestätigt · needs_en=659 review=43
- 2026-11-05 07:28 · Lauf: 1499 verfolgt, 659 offen, 833 bestätigt · needs_en=659
- 2026-11-05 08:13 · Lauf: 1499 verfolgt, 660 offen, 832 bestätigt · needs_en=617 review=43
- 2026-11-05 08:13 · Lauf: 1499 verfolgt, 617 offen, 875 bestätigt · needs_en=617
- 2026-11-05 10:04 · Lauf: 1499 verfolgt, 617 offen, 875 bestätigt · needs_en=609 review=8
- 2026-11-05 10:04 · Lauf: 1499 verfolgt, 609 offen, 883 bestätigt · needs_en=609
- 2026-11-05 10:20 · Lauf: 1499 verfolgt, 609 offen, 883 bestätigt · needs_en=581 review=28
- 2026-11-05 10:31 · Lauf: 1499 verfolgt, 581 offen, 911 bestätigt · needs_en=556 review=25
- 2026-11-05 11:06 · Lauf: 1499 verfolgt, 557 offen, 935 bestätigt · needs_en=528 parity=1 review=28
- 2026-11-05 11:07 · Lauf: 1499 verfolgt, 529 offen, 963 bestätigt · needs_en=528 parity=1
- 2026-11-05 11:17 · Lauf: 1499 verfolgt, 529 offen, 963 bestätigt · needs_en=515 review=14
- 2026-11-05 11:25 · Lauf: 1499 verfolgt, 689 offen, 803 bestätigt · needs_en=502 parity=42 review=145
