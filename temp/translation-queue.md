# Übersetzungsliste – der Übersetzungs-Checker für den ganzen Baum

Stand: 2026-11-05 17:28 UTC · 1537 Dateien verfolgt · 405 offen · 1125 bestätigt

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
| A. `en/` fehlt – aus `de/` übersetzen | 405 |
| B. `de/` fehlt – englische Quelle nachziehen | 0 |
| C. `en/` ist eine Kopie von `de/` – unübersetzt | 0 |
| D. `en/` enthält noch deutschen Text – Rest übersetzen | 0 |
| D2. Deutscher Text in Codebeispielen/Boxen (ADR 0002: Code ist englisch) | 0 |
| E. `de/` enthält noch englischen Text – Rest rückübersetzen | 0 |
| F. Form nicht gleich – Struktur abgleichen | 0 |
| G. Deutscher Dateiname – Pfad englisch machen (ADR 0002) | 0 |
| H. Beide Seiten da, kein Befund – lesen und bestätigen | 0 |
| 🗑️ gelöscht (tombstone) | 7 |

## A. `en/` fehlt – aus `de/` übersetzen – 405 Dateien

### `programs/` · 1

- [ ] `programs/index.md` · 3.4k · Plan[~]

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

## 🗑️ Gelöscht – 7

- [x] `data/anforderungen.md` · nicht mehr im Baum
- [x] `data/contacts/jscontact/beschreibung.md` · nicht mehr im Baum
- [x] `data/contacts/jscontact/speicherung.md` · nicht mehr im Baum
- [x] `data/felder.md` · nicht mehr im Baum
- [x] `data/formate.md` · nicht mehr im Baum
- [x] `data/konventionen.md` · nicht mehr im Baum
- [x] `data/modelle.md` · nicht mehr im Baum

## Changelog

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
- 2026-11-05 14:38 · Lauf: 1532 verfolgt, 638 offen, 887 bestätigt · needs_en=423 needs_de=17 parity=108 review=90
- 2026-11-05 14:41 · Lauf: 1532 verfolgt, 548 offen, 977 bestätigt · needs_en=423 needs_de=17 parity=108
- 2026-11-05 15:27 · Lauf: 1532 verfolgt, 554 offen, 971 bestätigt · needs_en=423 needs_de=17 parity=27 review=87
- 2026-11-05 15:28 · Lauf: 1532 verfolgt, 467 offen, 1058 bestätigt · needs_en=423 needs_de=17 parity=27
- 2026-11-05 15:43 · Lauf: 1537 verfolgt, 476 offen, 1054 bestätigt · needs_en=423 needs_de=22 parity=13 review=18
- 2026-11-05 16:18 · Lauf: 1537 verfolgt, 458 offen, 1072 bestätigt · needs_en=423 needs_de=22 parity=13
- 2026-11-05 16:19 · Lauf: 1537 verfolgt, 458 offen, 1072 bestätigt · needs_en=423 needs_de=5 parity=13 review=17
- 2026-11-05 16:19 · Lauf: 1537 verfolgt, 441 offen, 1089 bestätigt · needs_en=423 needs_de=5 parity=13
- 2026-11-05 16:21 · Lauf: 1537 verfolgt, 441 offen, 1089 bestätigt · needs_en=423 needs_de=2 parity=13 review=3
- 2026-11-05 16:23 · Lauf: 1537 verfolgt, 441 offen, 1089 bestätigt · needs_en=423 parity=13 review=5
- 2026-11-05 16:23 · Lauf: 1537 verfolgt, 436 offen, 1094 bestätigt · needs_en=423 parity=13
- 2026-11-05 16:43 · Lauf: 1537 verfolgt, 437 offen, 1093 bestätigt · needs_en=423 parity=1 review=13
- 2026-11-05 16:44 · Lauf: 1537 verfolgt, 437 offen, 1093 bestätigt · needs_en=423 review=14
- 2026-11-05 16:44 · Lauf: 1537 verfolgt, 423 offen, 1107 bestätigt · needs_en=423
- 2026-11-05 16:55 · Lauf: 1537 verfolgt, 431 offen, 1099 bestätigt · needs_en=417 parity=5 review=9
- 2026-11-05 17:01 · Lauf: 1537 verfolgt, 425 offen, 1105 bestätigt · needs_en=411 parity=5 review=9
- 2026-11-05 17:10 · Lauf: 1537 verfolgt, 419 offen, 1111 bestätigt · needs_en=405 parity=5 review=9
- 2026-11-05 17:20 · Lauf: 1537 verfolgt, 414 offen, 1116 bestätigt · needs_en=405 parity=1 review=8
- 2026-11-05 17:28 · Lauf: 1537 verfolgt, 414 offen, 1116 bestätigt · needs_en=405 review=9
- 2026-11-05 17:28 · Lauf: 1537 verfolgt, 405 offen, 1125 bestätigt · needs_en=405
