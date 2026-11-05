# Übersetzungsliste – der Übersetzungs-Checker für den ganzen Baum

Stand: 2026-11-05 14:28 UTC · 1532 Dateien verfolgt · 621 offen · 904 bestätigt

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
| A. `en/` fehlt – aus `de/` übersetzen | 423 |
| B. `de/` fehlt – englische Quelle nachziehen | 17 |
| C. `en/` ist eine Kopie von `de/` – unübersetzt | 0 |
| D. `en/` enthält noch deutschen Text – Rest übersetzen | 0 |
| D2. Deutscher Text in Codebeispielen/Boxen (ADR 0002: Code ist englisch) | 0 |
| E. `de/` enthält noch englischen Text – Rest rückübersetzen | 0 |
| F. Form nicht gleich – Struktur abgleichen | 107 |
| G. Deutscher Dateiname – Pfad englisch machen (ADR 0002) | 0 |
| H. Beide Seiten da, kein Befund – lesen und bestätigen | 74 |
| 🗑️ gelöscht (tombstone) | 7 |

## A. `en/` fehlt – aus `de/` übersetzen – 423 Dateien

### `programs/` · 1

- [ ] `programs/index.md` · 3.4k · Plan[~]

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

### `programs/platform/crates/` · 1

- [ ] `programs/platform/crates/gui.md` · 11.7k

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

## B. `de/` fehlt – englische Quelle nachziehen – 17 Dateien

### `programs/apps/calendar/` · 1

- [ ] `programs/apps/calendar/requirements.md` · 575b

### `programs/apps/contact/` · 1

- [ ] `programs/apps/contact/requirements.md` · 573b

### `programs/apps/gallery/` · 1

- [ ] `programs/apps/gallery/requirements.md` · 573b

### `programs/apps/helpdesk/` · 1

- [ ] `programs/apps/helpdesk/requirements.md` · 575b

### `programs/apps/maps/` · 1

- [ ] `programs/apps/maps/requirements.md` · 567b

### `programs/apps/marketing/` · 1

- [ ] `programs/apps/marketing/requirements.md` · 577b

### `programs/apps/messenger/` · 1

- [ ] `programs/apps/messenger/requirements.md` · 577b

### `programs/apps/projectmanagement/` · 1

- [ ] `programs/apps/projectmanagement/requirements.md` · 593b

### `programs/apps/streaming/` · 1

- [ ] `programs/apps/streaming/requirements.md` · 577b

### `programs/apps/whiteboards/` · 1

- [ ] `programs/apps/whiteboards/requirements.md` · 581b

### `programs/apps/wiki/` · 1

- [ ] `programs/apps/wiki/requirements.md` · 567b

### `programs/platform/desktop/` · 1

- [ ] `programs/platform/desktop/requirements.md` · 573b

### `programs/suites/crm/` · 1

- [ ] `programs/suites/crm/requirements.md` · 565b

### `programs/suites/democracy/` · 1

- [ ] `programs/suites/democracy/requirements.md` · 577b

### `programs/suites/erp/` · 1

- [ ] `programs/suites/erp/requirements.md` · 565b

### `programs/suites/marketplace/` · 1

- [ ] `programs/suites/marketplace/requirements.md` · 581b

### `programs/suites/workflows/` · 1

- [ ] `programs/suites/workflows/requirements.md` · 577b

## F. Form nicht gleich – Struktur abgleichen – 107 Dateien

### `data/` · 1

- [ ] `data/standards.md` · 23.6k · Parität: headings 20 vs 18; table rows 124 vs 107 · hash changed since verification

### `data/contacts/` · 3

- [ ] `data/contacts/index.md` · 1.5k · Parität: links en-only=['technical.md'] de-only=[] · hash changed since verification
- [ ] `data/contacts/standards.md` · 3.0k · Parität: links en-only=['technical.md'] de-only=[] · hash changed since verification
- [ ] `data/contacts/technical.md` · 3.0k · Parität: headings 7 vs 6; links en-only=['standards.md'] de-only=[] · hash changed since verification

### `data/identity/` · 2

- [ ] `data/identity/index.md` · 3.1k · Parität: table rows 13 vs 7 · hash changed since verification
- [ ] `data/identity/standards.md` · 2.5k · Parität: table rows 8 vs 9 · hash changed since verification

### `programs/apps/calendar/` · 1

- [ ] `programs/apps/calendar/index.md` · 4.3k · Plan[~] · Parität: links en-only=[] de-only=['../../data/api.md', '../platform/desktop/frontends/index.md', 'wiki/frontends/index.md'] · hash changed since verification

### `programs/apps/calendar/frontends/` · 1

- [ ] `programs/apps/calendar/frontends/index.md` · 3.5k · Parität: headings 3 vs 7; table rows 8 vs 0

### `programs/apps/calendar/frontends/davical/` · 1

- [ ] `programs/apps/calendar/frontends/davical/index.md` · 3.1k · Parität: headings 6 vs 4; table rows 27 vs 16 · hash changed since verification

### `programs/apps/calendar/frontends/google-calendar/` · 1

- [ ] `programs/apps/calendar/frontends/google-calendar/index.md` · 8.5k · Parität: headings 7 vs 5; table rows 50 vs 39 · hash changed since verification

### `programs/apps/calendar/frontends/merkuro/` · 1

- [ ] `programs/apps/calendar/frontends/merkuro/index.md` · 3.9k · Parität: headings 5 vs 3; table rows 11 vs 8 · hash changed since verification

### `programs/apps/calendar/frontends/nextcloud-calendar/` · 1

- [ ] `programs/apps/calendar/frontends/nextcloud-calendar/index.md` · 3.8k · Parität: headings 5 vs 3; table rows 11 vs 8 · hash changed since verification

### `programs/apps/calendar/frontends/outlook-calendar/` · 1

- [ ] `programs/apps/calendar/frontends/outlook-calendar/index.md` · 6.0k · Parität: headings 5 vs 3; table rows 11 vs 8 · hash changed since verification

### `programs/apps/calendar/frontends/planner/` · 1

- [ ] `programs/apps/calendar/frontends/planner/index.md` · 5.3k · Parität: headings 6 vs 4; table rows 30 vs 19 · hash changed since verification

### `programs/apps/contact/` · 1

- [ ] `programs/apps/contact/index.md` · 3.8k · Plan[~] · Parität: links en-only=[] de-only=['../../data/api.md', '../platform/desktop/frontends/index.md', 'wiki/frontends/index.md'] · hash changed since verification

### `programs/apps/contact/frontends/` · 1

- [ ] `programs/apps/contact/frontends/index.md` · 3.0k · Parität: headings 3 vs 7; table rows 6 vs 0 · hash changed since verification

### `programs/apps/contact/frontends/gnome-contacts/` · 1

- [ ] `programs/apps/contact/frontends/gnome-contacts/index.md` · 1.3k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/contact/frontends/kaddressbook/` · 1

- [ ] `programs/apps/contact/frontends/kaddressbook/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/contact/frontends/monica/` · 1

- [ ] `programs/apps/contact/frontends/monica/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/contact/frontends/nextcloud-contacts/` · 1

- [ ] `programs/apps/contact/frontends/nextcloud-contacts/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/gallery/frontends/` · 1

- [ ] `programs/apps/gallery/frontends/index.md` · 3.7k · Parität: headings 3 vs 7; table rows 10 vs 0 · hash changed since verification

### `programs/apps/gallery/frontends/coppermine/` · 1

- [ ] `programs/apps/gallery/frontends/coppermine/index.md` · 1.3k · Parität: headings 5 vs 3; table rows 12 vs 0 · hash changed since verification

### `programs/apps/gallery/frontends/damselfly/` · 1

- [ ] `programs/apps/gallery/frontends/damselfly/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/gallery/frontends/immich/` · 1

- [ ] `programs/apps/gallery/frontends/immich/index.md` · 1.3k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/gallery/frontends/librephotos/` · 1

- [ ] `programs/apps/gallery/frontends/librephotos/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/gallery/frontends/lychee/` · 1

- [ ] `programs/apps/gallery/frontends/lychee/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/gallery/frontends/nextcloud-photos/` · 1

- [ ] `programs/apps/gallery/frontends/nextcloud-photos/index.md` · 1.4k · Parität: headings 6 vs 4; table rows 11 vs 0 · hash changed since verification

### `programs/apps/gallery/frontends/photoprism/` · 1

- [ ] `programs/apps/gallery/frontends/photoprism/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/gallery/frontends/piwigo/` · 1

- [ ] `programs/apps/gallery/frontends/piwigo/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/helpdesk/` · 1

- [ ] `programs/apps/helpdesk/index.md` · 4.3k · Plan[~] · Parität: links en-only=[] de-only=['../../data/api.md', '../platform/desktop/frontends/index.md', 'wiki/frontends/index.md'] · hash changed since verification

### `programs/apps/helpdesk/frontends/` · 1

- [ ] `programs/apps/helpdesk/frontends/index.md` · 3.8k · Parität: headings 3 vs 7; table rows 10 vs 0 · hash changed since verification

### `programs/apps/helpdesk/frontends/freshdesk/` · 1

- [ ] `programs/apps/helpdesk/frontends/freshdesk/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/helpdesk/frontends/glpi/` · 1

- [ ] `programs/apps/helpdesk/frontends/glpi/index.md` · 1.3k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/helpdesk/frontends/helodesk/` · 1

- [ ] `programs/apps/helpdesk/frontends/helodesk/index.md` · 1.3k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/helpdesk/frontends/helpscout/` · 1

- [ ] `programs/apps/helpdesk/frontends/helpscout/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/helpdesk/frontends/osticket/` · 1

- [ ] `programs/apps/helpdesk/frontends/osticket/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/helpdesk/frontends/request-tracker/` · 1

- [ ] `programs/apps/helpdesk/frontends/request-tracker/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/helpdesk/frontends/zammad/` · 1

- [ ] `programs/apps/helpdesk/frontends/zammad/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/helpdesk/frontends/zendesk/` · 1

- [ ] `programs/apps/helpdesk/frontends/zendesk/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/maps/` · 1

- [ ] `programs/apps/maps/index.md` · 4.2k · Plan[~] · Parität: links en-only=[] de-only=['../../data/api.md', '../platform/desktop/frontends/index.md', 'wiki/frontends/index.md'] · hash changed since verification

### `programs/apps/maps/frontends/` · 1

- [ ] `programs/apps/maps/frontends/index.md` · 3.7k · Parität: headings 3 vs 7; table rows 9 vs 0 · hash changed since verification

### `programs/apps/maps/frontends/leaflet/` · 1

- [ ] `programs/apps/maps/frontends/leaflet/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/maps/frontends/maplibre/` · 1

- [ ] `programs/apps/maps/frontends/maplibre/index.md` · 1.3k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/maps/frontends/openstreetmap/` · 1

- [ ] `programs/apps/maps/frontends/openstreetmap/index.md` · 1.3k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/maps/frontends/organic-maps/` · 1

- [ ] `programs/apps/maps/frontends/organic-maps/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/maps/frontends/osmand/` · 1

- [ ] `programs/apps/maps/frontends/osmand/index.md` · 1.3k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/maps/frontends/qgis/` · 1

- [ ] `programs/apps/maps/frontends/qgis/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/maps/frontends/umap/` · 1

- [ ] `programs/apps/maps/frontends/umap/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/marketing/` · 1

- [ ] `programs/apps/marketing/index.md` · 4.5k · Plan[~] · Parität: links en-only=[] de-only=['../../data/api.md', '../platform/desktop/frontends/index.md', 'wiki/frontends/index.md'] · hash changed since verification

### `programs/apps/marketing/frontends/` · 1

- [ ] `programs/apps/marketing/frontends/index.md` · 3.5k · Parität: headings 3 vs 7; table rows 8 vs 0 · hash changed since verification

### `programs/apps/marketing/frontends/google-analytics/` · 1

- [ ] `programs/apps/marketing/frontends/google-analytics/index.md` · 1.3k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/marketing/frontends/hotjar/` · 1

- [ ] `programs/apps/marketing/frontends/hotjar/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/marketing/frontends/mailchimp/` · 1

- [ ] `programs/apps/marketing/frontends/mailchimp/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/marketing/frontends/matomo/` · 1

- [ ] `programs/apps/marketing/frontends/matomo/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/marketing/frontends/mautic/` · 1

- [ ] `programs/apps/marketing/frontends/mautic/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/marketing/frontends/plausible/` · 1

- [ ] `programs/apps/marketing/frontends/plausible/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/messenger/` · 1

- [ ] `programs/apps/messenger/index.md` · 3.9k · Plan[~] · Parität: headings 11 vs 10; links en-only=['frontends/discord/index.md', 'frontends/element/index.md', 'frontends/index.md'] de-only=[] · hash changed since verification

### `programs/apps/messenger/frontends/` · 1

- [ ] `programs/apps/messenger/frontends/index.md` · 3.2k · Parität: headings 3 vs 13; table rows 9 vs 0 · hash changed since verification

### `programs/apps/messenger/frontends/discord/` · 1

- [ ] `programs/apps/messenger/frontends/discord/index.md` · 1.1k · Parität: headings 5 vs 3; table rows 12 vs 0 · hash changed since verification

### `programs/apps/messenger/frontends/element/` · 1

- [ ] `programs/apps/messenger/frontends/element/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 12 vs 0 · hash changed since verification

### `programs/apps/messenger/frontends/kontact/` · 1

- [ ] `programs/apps/messenger/frontends/kontact/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 12 vs 0 · hash changed since verification

### `programs/apps/messenger/frontends/mastodon/` · 1

- [ ] `programs/apps/messenger/frontends/mastodon/index.md` · 1.1k · Parität: headings 5 vs 3; table rows 12 vs 0 · hash changed since verification

### `programs/apps/messenger/frontends/outlook/` · 1

- [ ] `programs/apps/messenger/frontends/outlook/index.md` · 1.1k · Parität: headings 5 vs 3; table rows 12 vs 0 · hash changed since verification

### `programs/apps/messenger/frontends/telegram/` · 1

- [ ] `programs/apps/messenger/frontends/telegram/index.md` · 1.1k · Parität: headings 5 vs 3; table rows 12 vs 0 · hash changed since verification

### `programs/apps/messenger/frontends/thunderbird/` · 1

- [ ] `programs/apps/messenger/frontends/thunderbird/index.md` · 1.1k · Parität: headings 5 vs 3; table rows 12 vs 0 · hash changed since verification

### `programs/apps/projectmanagement/` · 1

- [ ] `programs/apps/projectmanagement/index.md` · 4.7k · Plan[~] · Parität: links en-only=[] de-only=['../../data/api.md', '../platform/desktop/frontends/index.md', 'wiki/frontends/index.md'] · hash changed since verification

### `programs/apps/projectmanagement/frontends/` · 1

- [ ] `programs/apps/projectmanagement/frontends/index.md` · 4.0k · Parität: headings 3 vs 7; table rows 10 vs 0 · hash changed since verification

### `programs/apps/projectmanagement/frontends/asana/` · 1

- [ ] `programs/apps/projectmanagement/frontends/asana/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/projectmanagement/frontends/jira/` · 1

- [ ] `programs/apps/projectmanagement/frontends/jira/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/projectmanagement/frontends/openproject/` · 1

- [ ] `programs/apps/projectmanagement/frontends/openproject/index.md` · 964b · Parität: headings 5 vs 3; table rows 5 vs 0 · hash changed since verification

### `programs/apps/projectmanagement/frontends/planka/` · 1

- [ ] `programs/apps/projectmanagement/frontends/planka/index.md` · 888b · Parität: headings 5 vs 3; table rows 5 vs 0 · hash changed since verification

### `programs/apps/projectmanagement/frontends/redmine/` · 1

- [ ] `programs/apps/projectmanagement/frontends/redmine/index.md` · 941b · Parität: headings 5 vs 3; table rows 5 vs 0 · hash changed since verification

### `programs/apps/projectmanagement/frontends/taiga/` · 1

- [ ] `programs/apps/projectmanagement/frontends/taiga/index.md` · 856b · Parität: headings 5 vs 3; table rows 5 vs 0 · hash changed since verification

### `programs/apps/projectmanagement/frontends/trello/` · 1

- [ ] `programs/apps/projectmanagement/frontends/trello/index.md` · 1.2k · Parität: headings 5 vs 3; table rows 11 vs 0 · hash changed since verification

### `programs/apps/projectmanagement/frontends/wekan/` · 1

- [ ] `programs/apps/projectmanagement/frontends/wekan/index.md` · 887b · Parität: headings 5 vs 3; table rows 5 vs 0 · hash changed since verification

### `programs/apps/streaming/frontends/` · 1

- [ ] `programs/apps/streaming/frontends/index.md` · 4.6k · Parität: headings 3 vs 7; table rows 12 vs 0 · hash changed since verification

### `programs/apps/streaming/frontends/ant-media-server/` · 1

- [ ] `programs/apps/streaming/frontends/ant-media-server/index.md` · 937b · Parität: headings 5 vs 3; table rows 5 vs 0 · hash changed since verification

### `programs/apps/streaming/frontends/ffmpeg/` · 1

- [ ] `programs/apps/streaming/frontends/ffmpeg/index.md` · 2.1k · Parität: headings 6 vs 4; table rows 13 vs 8 · hash changed since verification

### `programs/apps/streaming/frontends/gstreamer/` · 1

- [ ] `programs/apps/streaming/frontends/gstreamer/index.md` · 1.0k · Parität: headings 5 vs 3; table rows 5 vs 0 · hash changed since verification

### `programs/apps/streaming/frontends/mediamtx/` · 1

- [ ] `programs/apps/streaming/frontends/mediamtx/index.md` · 996b · Parität: headings 5 vs 3; table rows 5 vs 0 · hash changed since verification

### `programs/apps/streaming/frontends/mistserver/` · 1

- [ ] `programs/apps/streaming/frontends/mistserver/index.md` · 1014b · Parität: headings 5 vs 3; table rows 5 vs 0 · hash changed since verification

### `programs/apps/streaming/frontends/nginx-rtmp-module/` · 1

- [ ] `programs/apps/streaming/frontends/nginx-rtmp-module/index.md` · 1006b · Parität: headings 5 vs 3; table rows 5 vs 0 · hash changed since verification

### `programs/apps/streaming/frontends/obs-studio/` · 1

- [ ] `programs/apps/streaming/frontends/obs-studio/index.md` · 882b · Parität: headings 5 vs 3; table rows 5 vs 0 · hash changed since verification

### `programs/apps/streaming/frontends/restream/` · 1

- [ ] `programs/apps/streaming/frontends/restream/index.md` · 963b · Parität: headings 5 vs 3; table rows 5 vs 0 · hash changed since verification

### `programs/apps/streaming/frontends/restreamer/` · 1

- [ ] `programs/apps/streaming/frontends/restreamer/index.md` · 884b · Parität: headings 5 vs 3; table rows 5 vs 0 · hash changed since verification

### `programs/apps/streaming/frontends/wowza/` · 1

- [ ] `programs/apps/streaming/frontends/wowza/index.md` · 1.1k · Parität: headings 5 vs 3; table rows 5 vs 0 · hash changed since verification

### `programs/apps/whiteboards/` · 1

- [ ] `programs/apps/whiteboards/index.md` · 3.9k · Plan[~] · Parität: links en-only=[] de-only=['../../data/api.md', '../platform/desktop/frontends/index.md', 'wiki/frontends/index.md'] · hash changed since verification

### `programs/apps/whiteboards/frontends/` · 1

- [ ] `programs/apps/whiteboards/frontends/index.md` · 3.3k · Parität: headings 3 vs 7; table rows 8 vs 0 · hash changed since verification

### `programs/apps/whiteboards/frontends/drawio/` · 1

- [ ] `programs/apps/whiteboards/frontends/drawio/index.md` · 840b · Parität: headings 5 vs 3; table rows 5 vs 0 · hash changed since verification

### `programs/apps/whiteboards/frontends/excalidraw/` · 1

- [ ] `programs/apps/whiteboards/frontends/excalidraw/index.md` · 801b · Parität: headings 5 vs 3; table rows 5 vs 0 · hash changed since verification

### `programs/apps/whiteboards/frontends/miro/` · 1

- [ ] `programs/apps/whiteboards/frontends/miro/index.md` · 876b · Parität: headings 5 vs 3; table rows 5 vs 0 · hash changed since verification

### `programs/apps/whiteboards/frontends/mural/` · 1

- [ ] `programs/apps/whiteboards/frontends/mural/index.md` · 846b · Parität: headings 5 vs 3; table rows 5 vs 0 · hash changed since verification

### `programs/apps/whiteboards/frontends/openboard/` · 1

- [ ] `programs/apps/whiteboards/frontends/openboard/index.md` · 897b · Parität: headings 5 vs 3; table rows 5 vs 0 · hash changed since verification

### `programs/apps/whiteboards/frontends/tldraw/` · 1

- [ ] `programs/apps/whiteboards/frontends/tldraw/index.md` · 885b · Parität: headings 5 vs 3; table rows 5 vs 0 · hash changed since verification

### `programs/apps/wiki/` · 1

- [ ] `programs/apps/wiki/index.md` · 3.3k · Plan[~] · Parität: headings 10 vs 9; links en-only=['frontends/confluence/index.md', 'frontends/index.md', 'frontends/mediawiki/index.md'] de-only=[] · hash changed since verification

### `programs/apps/wiki/frontends/` · 1

- [ ] `programs/apps/wiki/frontends/index.md` · 3.0k · Parität: headings 3 vs 13; table rows 9 vs 0 · hash changed since verification

### `programs/platform/desktop/` · 1

- [ ] `programs/platform/desktop/index.md` · 4.7k · Plan[~] · Parität: headings 14 vs 13; links en-only=['frontends/dashy/index.md', 'frontends/gethomepage/index.md', 'frontends/heimdall/index.md'] de-only=[] · hash changed since verification

### `programs/platform/desktop/frontends/` · 1

- [ ] `programs/platform/desktop/frontends/index.md` · 2.9k · Parität: headings 3 vs 16; table rows 14 vs 36

### `programs/suites/crm/` · 1

- [ ] `programs/suites/crm/index.md` · 3.1k · Plan[~] · Parität: links en-only=[] de-only=['../../data/api.md', '../apps/wiki/frontends/index.md', '../platform/desktop/frontends/index.md'] · hash changed since verification

### `programs/suites/crm/frontends/` · 1

- [ ] `programs/suites/crm/frontends/index.md` · 2.4k · Parität: headings 3 vs 7; table rows 8 vs 0

### `programs/suites/democracy/` · 1

- [ ] `programs/suites/democracy/index.md` · 3.0k · Plan[~] · Parität: links en-only=[] de-only=['../../data/api.md', '../apps/wiki/frontends/index.md', '../platform/desktop/frontends/index.md'] · hash changed since verification

### `programs/suites/democracy/frontends/` · 1

- [ ] `programs/suites/democracy/frontends/index.md` · 2.4k · Parität: headings 3 vs 7; table rows 8 vs 0

### `programs/suites/erp/` · 1

- [ ] `programs/suites/erp/index.md` · 2.9k · Plan[~] · Parität: links en-only=[] de-only=['../../data/api.md', '../apps/wiki/frontends/index.md', '../platform/desktop/frontends/index.md'] · hash changed since verification

### `programs/suites/erp/frontends/` · 1

- [ ] `programs/suites/erp/frontends/index.md` · 2.3k · Parität: headings 3 vs 7; table rows 8 vs 0

### `programs/suites/marketplace/frontends/` · 1

- [ ] `programs/suites/marketplace/frontends/index.md` · 2.4k · Parität: headings 3 vs 7; table rows 8 vs 0

### `programs/suites/workflows/` · 1

- [ ] `programs/suites/workflows/index.md` · 2.9k · Plan[~] · Parität: links en-only=[] de-only=['../../data/api.md', '../apps/wiki/frontends/index.md', '../platform/desktop/frontends/index.md'] · hash changed since verification

### `programs/suites/workflows/frontends/` · 1

- [ ] `programs/suites/workflows/frontends/index.md` · 2.4k · Parität: headings 3 vs 7; table rows 8 vs 0

## H. Beide Seiten da, kein Befund – lesen und bestätigen – 74 Dateien

### `data/contacts/jscontact/` · 1

- [ ] `data/contacts/jscontact/storage.md` · 2.8k · hash changed since verification

### `data/identity/` · 1

- [ ] `data/identity/technical.md` · 2.4k · hash changed since verification

### `data/login/` · 1

- [ ] `data/login/standards.md` · 2.0k · hash changed since verification

### `programs/apps/gallery/` · 1

- [ ] `programs/apps/gallery/index.md` · 3.7k · Plan[~] · hash changed since verification

### `programs/apps/gallery/frontends/coppermine/latest/` · 1

- [ ] `programs/apps/gallery/frontends/coppermine/latest/layout.md` · 1.3k · hash changed since verification

### `programs/apps/gallery/frontends/coppermine/latest/themes/` · 2

- [ ] `programs/apps/gallery/frontends/coppermine/latest/themes/default.md` · 1.5k · hash changed since verification
- [ ] `programs/apps/gallery/frontends/coppermine/latest/themes/index.md` · 216b · hash changed since verification

### `programs/apps/messenger/frontends/discord/latest/` · 1

- [ ] `programs/apps/messenger/frontends/discord/latest/layout.md` · 7.2k · hash changed since verification

### `programs/apps/messenger/frontends/discord/latest/themes/` · 2

- [ ] `programs/apps/messenger/frontends/discord/latest/themes/default.md` · 485b · hash changed since verification
- [ ] `programs/apps/messenger/frontends/discord/latest/themes/index.md` · 213b · hash changed since verification

### `programs/apps/messenger/frontends/element/latest/` · 1

- [ ] `programs/apps/messenger/frontends/element/latest/layout.md` · 6.4k · hash changed since verification

### `programs/apps/messenger/frontends/element/latest/themes/` · 2

- [ ] `programs/apps/messenger/frontends/element/latest/themes/default.md` · 481b · hash changed since verification
- [ ] `programs/apps/messenger/frontends/element/latest/themes/index.md` · 213b · hash changed since verification

### `programs/apps/messenger/frontends/kontact/latest/` · 1

- [ ] `programs/apps/messenger/frontends/kontact/latest/layout.md` · 10.2k · hash changed since verification

### `programs/apps/messenger/frontends/kontact/latest/themes/` · 2

- [ ] `programs/apps/messenger/frontends/kontact/latest/themes/default.md` · 566b · hash changed since verification
- [ ] `programs/apps/messenger/frontends/kontact/latest/themes/index.md` · 213b · hash changed since verification

### `programs/apps/messenger/frontends/mastodon/latest/` · 1

- [ ] `programs/apps/messenger/frontends/mastodon/latest/layout.md` · 7.7k · hash changed since verification

### `programs/apps/messenger/frontends/mastodon/latest/themes/` · 2

- [ ] `programs/apps/messenger/frontends/mastodon/latest/themes/default.md` · 479b · hash changed since verification
- [ ] `programs/apps/messenger/frontends/mastodon/latest/themes/index.md` · 214b · hash changed since verification

### `programs/apps/messenger/frontends/outlook/latest/` · 1

- [ ] `programs/apps/messenger/frontends/outlook/latest/layout.md` · 7.1k · hash changed since verification

### `programs/apps/messenger/frontends/outlook/latest/themes/` · 2

- [ ] `programs/apps/messenger/frontends/outlook/latest/themes/default.md` · 394b · hash changed since verification
- [ ] `programs/apps/messenger/frontends/outlook/latest/themes/index.md` · 213b · hash changed since verification

### `programs/apps/messenger/frontends/telegram/latest/` · 1

- [ ] `programs/apps/messenger/frontends/telegram/latest/layout.md` · 7.6k · hash changed since verification

### `programs/apps/messenger/frontends/telegram/latest/themes/` · 2

- [ ] `programs/apps/messenger/frontends/telegram/latest/themes/default.md` · 492b · hash changed since verification
- [ ] `programs/apps/messenger/frontends/telegram/latest/themes/index.md` · 214b · hash changed since verification

### `programs/apps/messenger/frontends/thunderbird/latest/` · 1

- [ ] `programs/apps/messenger/frontends/thunderbird/latest/layout.md` · 7.5k · hash changed since verification

### `programs/apps/messenger/frontends/thunderbird/latest/themes/` · 2

- [ ] `programs/apps/messenger/frontends/thunderbird/latest/themes/default.md` · 507b · hash changed since verification
- [ ] `programs/apps/messenger/frontends/thunderbird/latest/themes/index.md` · 217b · hash changed since verification

### `programs/apps/streaming/` · 1

- [ ] `programs/apps/streaming/index.md` · 4.8k · Plan[~] · hash changed since verification

### `programs/apps/wiki/frontends/confluence/` · 1

- [ ] `programs/apps/wiki/frontends/confluence/index.md` · 1.1k · hash changed since verification

### `programs/apps/wiki/frontends/confluence/latest/` · 6

- [ ] `programs/apps/wiki/frontends/confluence/latest/api.md` · 5.9k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/confluence/latest/description.md` · 1.9k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/confluence/latest/features.md` · 5.1k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/confluence/latest/layout.md` · 5.7k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/confluence/latest/menus.md` · 2.1k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/confluence/latest/shortcuts.md` · 6.7k · hash changed since verification

### `programs/apps/wiki/frontends/mediawiki/` · 1

- [ ] `programs/apps/wiki/frontends/mediawiki/index.md` · 1.0k · hash changed since verification

### `programs/apps/wiki/frontends/mediawiki/latest/` · 6

- [ ] `programs/apps/wiki/frontends/mediawiki/latest/api.md` · 5.1k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/mediawiki/latest/description.md` · 1.8k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/mediawiki/latest/features.md` · 3.8k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/mediawiki/latest/layout.md` · 5.6k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/mediawiki/latest/menus.md` · 2.0k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/mediawiki/latest/shortcuts.md` · 6.5k · hash changed since verification

### `programs/apps/wiki/frontends/notion/` · 1

- [ ] `programs/apps/wiki/frontends/notion/index.md` · 1.0k · hash changed since verification

### `programs/apps/wiki/frontends/notion/latest/` · 6

- [ ] `programs/apps/wiki/frontends/notion/latest/api.md` · 5.2k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/notion/latest/description.md` · 1.8k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/notion/latest/features.md` · 6.7k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/notion/latest/layout.md` · 5.2k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/notion/latest/menus.md` · 3.7k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/notion/latest/shortcuts.md` · 6.8k · hash changed since verification

### `programs/apps/wiki/frontends/tango.io/` · 1

- [ ] `programs/apps/wiki/frontends/tango.io/index.md` · 1.1k · hash changed since verification

### `programs/apps/wiki/frontends/tango.io/latest/` · 6

- [ ] `programs/apps/wiki/frontends/tango.io/latest/api.md` · 4.8k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/tango.io/latest/description.md` · 1.7k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/tango.io/latest/features.md` · 4.4k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/tango.io/latest/layout.md` · 5.3k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/tango.io/latest/menus.md` · 2.2k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/tango.io/latest/shortcuts.md` · 6.4k · hash changed since verification

### `programs/apps/wiki/frontends/vscodium/` · 1

- [ ] `programs/apps/wiki/frontends/vscodium/index.md` · 1.0k · hash changed since verification

### `programs/apps/wiki/frontends/vscodium/latest/` · 6

- [ ] `programs/apps/wiki/frontends/vscodium/latest/api.md` · 5.0k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/vscodium/latest/description.md` · 1.7k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/vscodium/latest/features.md` · 6.0k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/vscodium/latest/layout.md` · 6.6k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/vscodium/latest/menus.md` · 1.7k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/vscodium/latest/shortcuts.md` · 6.3k · hash changed since verification

### `programs/apps/wiki/frontends/wikijs/` · 1

- [ ] `programs/apps/wiki/frontends/wikijs/index.md` · 1.0k · hash changed since verification

### `programs/apps/wiki/frontends/wikijs/latest/` · 2

- [ ] `programs/apps/wiki/frontends/wikijs/latest/api.md` · 4.2k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/wikijs/latest/shortcuts.md` · 4.9k · hash changed since verification

### `programs/apps/wiki/frontends/xwiki/` · 1

- [ ] `programs/apps/wiki/frontends/xwiki/index.md` · 1.1k · hash changed since verification

### `programs/apps/wiki/frontends/xwiki/latest/` · 6

- [ ] `programs/apps/wiki/frontends/xwiki/latest/api.md` · 4.8k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/xwiki/latest/description.md` · 2.0k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/xwiki/latest/features.md` · 3.3k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/xwiki/latest/layout.md` · 6.6k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/xwiki/latest/menus.md` · 2.1k · hash changed since verification
- [ ] `programs/apps/wiki/frontends/xwiki/latest/shortcuts.md` · 6.4k · hash changed since verification

## 🗑️ Gelöscht – 7

- [x] `data/anforderungen.md` · nicht mehr im Baum
- [x] `data/contacts/jscontact/beschreibung.md` · nicht mehr im Baum
- [x] `data/contacts/jscontact/speicherung.md` · nicht mehr im Baum
- [x] `data/felder.md` · nicht mehr im Baum
- [x] `data/formate.md` · nicht mehr im Baum
- [x] `data/konventionen.md` · nicht mehr im Baum
- [x] `data/modelle.md` · nicht mehr im Baum

## Changelog

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
- 2026-11-05 11:28 · Lauf: 1499 verfolgt, 676 offen, 816 bestätigt · needs_en=498 review=178
- 2026-11-05 11:46 · Lauf: 1499 verfolgt, 714 offen, 778 bestätigt · needs_en=472 review=242
- 2026-11-05 11:46 · Lauf: 1499 verfolgt, 695 offen, 797 bestätigt · needs_en=472 review=223
- 2026-11-05 12:09 · Lauf: 1526 verfolgt, 605 offen, 914 bestätigt · needs_en=471 needs_de=27 parity=105 review=2
- 2026-11-05 12:38 · Lauf: 1526 verfolgt, 605 offen, 914 bestätigt · needs_en=467 needs_de=27 parity=105 review=6
- 2026-11-05 14:28 · Lauf: 1532 verfolgt, 621 offen, 904 bestätigt · needs_en=423 needs_de=17 parity=107 review=74
