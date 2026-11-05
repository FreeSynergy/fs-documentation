# Übersetzungsliste – der Übersetzungs-Checker für den ganzen Baum

Stand: 2026-11-05 08:13 UTC · 1499 Dateien verfolgt · 617 offen · 875 bestätigt

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
| A. `en/` fehlt – aus `de/` übersetzen | 617 |
| B. `de/` fehlt – englische Quelle nachziehen | 0 |
| C. `en/` ist eine Kopie von `de/` – unübersetzt | 0 |
| D. `en/` enthält noch deutschen Text – Rest übersetzen | 0 |
| D2. Deutscher Text in Codebeispielen/Boxen (ADR 0002: Code ist englisch) | 0 |
| E. `de/` enthält noch englischen Text – Rest rückübersetzen | 0 |
| F. Form nicht gleich – Struktur abgleichen | 0 |
| G. Deutscher Dateiname – Pfad englisch machen (ADR 0002) | 0 |
| H. Beide Seiten da, kein Befund – lesen und bestätigen | 0 |
| 🗑️ gelöscht (tombstone) | 7 |

## A. `en/` fehlt – aus `de/` übersetzen – 617 Dateien

### `data/` · 8

- [ ] `data/api.md` · 8.8k
- [ ] `data/conventions.md` · 8.3k
- [ ] `data/fields.md` · 10.0k
- [ ] `data/formats.md` · 5.2k
- [ ] `data/mappings.md` · 14.9k
- [ ] `data/models.md` · 9.5k
- [ ] `data/requirements.md` · 7.1k
- [ ] `data/standards.md` · 21.2k

### `interactions/animations/entrance/` · 1

- [ ] `interactions/animations/entrance/index.md` · 1.4k

### `interactions/animations/entrance/bounce-in/` · 3

- [ ] `interactions/animations/entrance/bounce-in/appearance.md` · 1.3k
- [ ] `interactions/animations/entrance/bounce-in/attributes.md` · 1.5k
- [ ] `interactions/animations/entrance/bounce-in/description.md` · 1001b

### `interactions/animations/entrance/expand/` · 3

- [ ] `interactions/animations/entrance/expand/appearance.md` · 1.6k
- [ ] `interactions/animations/entrance/expand/attributes.md` · 1.7k
- [ ] `interactions/animations/entrance/expand/description.md` · 857b

### `interactions/animations/entrance/fade-in/` · 3

- [ ] `interactions/animations/entrance/fade-in/appearance.md` · 1.2k
- [ ] `interactions/animations/entrance/fade-in/attributes.md` · 1.5k
- [ ] `interactions/animations/entrance/fade-in/description.md` · 944b

### `interactions/animations/entrance/pop-in/` · 3

- [ ] `interactions/animations/entrance/pop-in/appearance.md` · 1.5k
- [ ] `interactions/animations/entrance/pop-in/attributes.md` · 1.6k
- [ ] `interactions/animations/entrance/pop-in/description.md` · 1.1k

### `interactions/animations/entrance/radial-out/` · 3

- [ ] `interactions/animations/entrance/radial-out/appearance.md` · 2.0k
- [ ] `interactions/animations/entrance/radial-out/attributes.md` · 1.9k
- [ ] `interactions/animations/entrance/radial-out/description.md` · 1.5k

### `interactions/animations/entrance/scale-in/` · 3

- [ ] `interactions/animations/entrance/scale-in/appearance.md` · 1.4k
- [ ] `interactions/animations/entrance/scale-in/attributes.md` · 1.6k
- [ ] `interactions/animations/entrance/scale-in/description.md` · 1.0k

### `interactions/animations/entrance/slide-in/` · 3

- [ ] `interactions/animations/entrance/slide-in/appearance.md` · 1.3k
- [ ] `interactions/animations/entrance/slide-in/attributes.md` · 1.6k
- [ ] `interactions/animations/entrance/slide-in/description.md` · 936b

### `interactions/animations/entrance/unfold/` · 3

- [ ] `interactions/animations/entrance/unfold/appearance.md` · 1.6k
- [ ] `interactions/animations/entrance/unfold/attributes.md` · 1.7k
- [ ] `interactions/animations/entrance/unfold/description.md` · 998b

### `interactions/animations/entrance/zoom-in/` · 3

- [ ] `interactions/animations/entrance/zoom-in/appearance.md` · 1.2k
- [ ] `interactions/animations/entrance/zoom-in/attributes.md` · 1.5k
- [ ] `interactions/animations/entrance/zoom-in/description.md` · 940b

### `interactions/animations/exit/` · 1

- [ ] `interactions/animations/exit/index.md` · 1.5k

### `interactions/animations/exit/bounce-out/` · 3

- [ ] `interactions/animations/exit/bounce-out/appearance.md` · 1.3k
- [ ] `interactions/animations/exit/bounce-out/attributes.md` · 1.7k
- [ ] `interactions/animations/exit/bounce-out/description.md` · 970b

### `interactions/animations/exit/collapse/` · 3

- [ ] `interactions/animations/exit/collapse/appearance.md` · 1.6k
- [ ] `interactions/animations/exit/collapse/attributes.md` · 1.7k
- [ ] `interactions/animations/exit/collapse/description.md` · 852b

### `interactions/animations/exit/fade-out/` · 3

- [ ] `interactions/animations/exit/fade-out/appearance.md` · 1.2k
- [ ] `interactions/animations/exit/fade-out/attributes.md` · 1.5k
- [ ] `interactions/animations/exit/fade-out/description.md` · 897b

### `interactions/animations/exit/pop-out/` · 3

- [ ] `interactions/animations/exit/pop-out/appearance.md` · 1.5k
- [ ] `interactions/animations/exit/pop-out/attributes.md` · 1.6k
- [ ] `interactions/animations/exit/pop-out/description.md` · 1.1k

### `interactions/animations/exit/radial-in/` · 3

- [ ] `interactions/animations/exit/radial-in/appearance.md` · 2.0k
- [ ] `interactions/animations/exit/radial-in/attributes.md` · 1.9k
- [ ] `interactions/animations/exit/radial-in/description.md` · 1.6k

### `interactions/animations/exit/scale-out/` · 3

- [ ] `interactions/animations/exit/scale-out/appearance.md` · 1.4k
- [ ] `interactions/animations/exit/scale-out/attributes.md` · 1.6k
- [ ] `interactions/animations/exit/scale-out/description.md` · 962b

### `interactions/animations/exit/slide-out/` · 3

- [ ] `interactions/animations/exit/slide-out/appearance.md` · 1.3k
- [ ] `interactions/animations/exit/slide-out/attributes.md` · 1.6k
- [ ] `interactions/animations/exit/slide-out/description.md` · 958b

### `interactions/animations/exit/zoom-out/` · 3

- [ ] `interactions/animations/exit/zoom-out/appearance.md` · 1.2k
- [ ] `interactions/animations/exit/zoom-out/attributes.md` · 1.6k
- [ ] `interactions/animations/exit/zoom-out/description.md` · 941b

### `interactions/animations/feedback/` · 1

- [ ] `interactions/animations/feedback/index.md` · 1.2k

### `interactions/animations/feedback/elastic/` · 3

- [ ] `interactions/animations/feedback/elastic/appearance.md` · 1.4k
- [ ] `interactions/animations/feedback/elastic/attributes.md` · 1.3k
- [ ] `interactions/animations/feedback/elastic/description.md` · 1012b

### `interactions/animations/feedback/highlight/` · 3

- [ ] `interactions/animations/feedback/highlight/appearance.md` · 1.4k
- [ ] `interactions/animations/feedback/highlight/attributes.md` · 1.6k
- [ ] `interactions/animations/feedback/highlight/description.md` · 892b

### `interactions/animations/feedback/lift/` · 3

- [ ] `interactions/animations/feedback/lift/appearance.md` · 1.7k
- [ ] `interactions/animations/feedback/lift/attributes.md` · 1.7k
- [ ] `interactions/animations/feedback/lift/description.md` · 1.3k

### `interactions/animations/feedback/press/` · 3

- [ ] `interactions/animations/feedback/press/appearance.md` · 1.5k
- [ ] `interactions/animations/feedback/press/attributes.md` · 1.7k
- [ ] `interactions/animations/feedback/press/description.md` · 1.3k

### `interactions/animations/feedback/ripple/` · 3

- [ ] `interactions/animations/feedback/ripple/appearance.md` · 1.4k
- [ ] `interactions/animations/feedback/ripple/attributes.md` · 1.7k
- [ ] `interactions/animations/feedback/ripple/description.md` · 973b

### `interactions/animations/feedback/rubber-band/` · 3

- [ ] `interactions/animations/feedback/rubber-band/appearance.md` · 1.5k
- [ ] `interactions/animations/feedback/rubber-band/attributes.md` · 1.3k
- [ ] `interactions/animations/feedback/rubber-band/description.md` · 1.0k

### `interactions/animations/feedback/shake/` · 3

- [ ] `interactions/animations/feedback/shake/appearance.md` · 1.4k
- [ ] `interactions/animations/feedback/shake/attributes.md` · 1.7k
- [ ] `interactions/animations/feedback/shake/description.md` · 1.1k

### `interactions/animations/feedback/tick-draw/` · 3

- [ ] `interactions/animations/feedback/tick-draw/appearance.md` · 1.8k
- [ ] `interactions/animations/feedback/tick-draw/attributes.md` · 1.8k
- [ ] `interactions/animations/feedback/tick-draw/description.md` · 1.2k

### `interactions/animations/feedback/wiggle/` · 3

- [ ] `interactions/animations/feedback/wiggle/appearance.md` · 1.5k
- [ ] `interactions/animations/feedback/wiggle/attributes.md` · 1.7k
- [ ] `interactions/animations/feedback/wiggle/description.md` · 966b

### `interactions/animations/loading/` · 1

- [ ] `interactions/animations/loading/index.md` · 963b

### `interactions/animations/loading/dots/` · 3

- [ ] `interactions/animations/loading/dots/appearance.md` · 1.6k
- [ ] `interactions/animations/loading/dots/attributes.md` · 1.8k
- [ ] `interactions/animations/loading/dots/description.md` · 1.2k

### `interactions/animations/loading/progress/` · 3

- [ ] `interactions/animations/loading/progress/appearance.md` · 1.4k
- [ ] `interactions/animations/loading/progress/attributes.md` · 1.3k
- [ ] `interactions/animations/loading/progress/description.md` · 929b

### `interactions/animations/loading/skeleton/` · 3

- [ ] `interactions/animations/loading/skeleton/appearance.md` · 1.6k
- [ ] `interactions/animations/loading/skeleton/attributes.md` · 1.4k
- [ ] `interactions/animations/loading/skeleton/description.md` · 1.2k

### `interactions/animations/loading/typing/` · 3

- [ ] `interactions/animations/loading/typing/appearance.md` · 1.4k
- [ ] `interactions/animations/loading/typing/attributes.md` · 1.4k
- [ ] `interactions/animations/loading/typing/description.md` · 938b

### `interactions/animations/loop/` · 1

- [ ] `interactions/animations/loop/index.md` · 991b

### `interactions/animations/loop/glow/` · 3

- [ ] `interactions/animations/loop/glow/appearance.md` · 1.5k
- [ ] `interactions/animations/loop/glow/attributes.md` · 1.4k
- [ ] `interactions/animations/loop/glow/description.md` · 1.0k

### `interactions/animations/loop/heartbeat/` · 3

- [ ] `interactions/animations/loop/heartbeat/appearance.md` · 1.5k
- [ ] `interactions/animations/loop/heartbeat/attributes.md` · 1.7k
- [ ] `interactions/animations/loop/heartbeat/description.md` · 981b

### `interactions/animations/loop/pulse/` · 3

- [ ] `interactions/animations/loop/pulse/appearance.md` · 1.5k
- [ ] `interactions/animations/loop/pulse/attributes.md` · 1.7k
- [ ] `interactions/animations/loop/pulse/description.md` · 895b

### `interactions/animations/loop/spin/` · 3

- [ ] `interactions/animations/loop/spin/appearance.md` · 1.9k
- [ ] `interactions/animations/loop/spin/attributes.md` · 1.6k
- [ ] `interactions/animations/loop/spin/description.md` · 961b

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

- [ ] `programs/index.md` · 3.3k · Plan[~]

### `programs/apps/calendar/masks/` · 1

- [ ] `programs/apps/calendar/masks/index.md` · 2.7k · Plan[~]

### `programs/apps/projectmanagement/masks/openproject/` · 6

- [ ] `programs/apps/projectmanagement/masks/openproject/api.md` · 6.9k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/openproject/description.md` · 3.6k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/openproject/features.md` · 4.9k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/openproject/menu.md` · 4.3k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/openproject/shortcuts.md` · 5.3k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/openproject/structure.md` · 5.0k · Plan[~]

### `programs/apps/projectmanagement/masks/planka/` · 6

- [ ] `programs/apps/projectmanagement/masks/planka/api.md` · 2.9k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/planka/description.md` · 3.5k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/planka/features.md` · 4.5k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/planka/menu.md` · 4.0k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/planka/shortcuts.md` · 1.1k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/planka/structure.md` · 3.0k · Plan[~]

### `programs/apps/projectmanagement/masks/redmine/` · 6

- [ ] `programs/apps/projectmanagement/masks/redmine/api.md` · 7.0k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/redmine/description.md` · 3.4k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/redmine/features.md` · 5.1k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/redmine/menu.md` · 3.6k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/redmine/shortcuts.md` · 5.6k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/redmine/structure.md` · 4.9k · Plan[~]

### `programs/apps/projectmanagement/masks/taiga/` · 6

- [ ] `programs/apps/projectmanagement/masks/taiga/api.md` · 2.2k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/taiga/description.md` · 1.3k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/taiga/features.md` · 1.2k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/taiga/menu.md` · 1.3k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/taiga/shortcuts.md` · 546b · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/taiga/structure.md` · 2.0k · Plan[~]

### `programs/apps/projectmanagement/masks/wekan/` · 6

- [ ] `programs/apps/projectmanagement/masks/wekan/api.md` · 2.5k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/wekan/description.md` · 1.2k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/wekan/features.md` · 1.3k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/wekan/menu.md` · 1.2k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/wekan/shortcuts.md` · 819b · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/wekan/structure.md` · 2.5k · Plan[~]

### `programs/apps/streaming/masks/ant-media-server/` · 6

- [ ] `programs/apps/streaming/masks/ant-media-server/api.md` · 4.1k · Plan[~]
- [ ] `programs/apps/streaming/masks/ant-media-server/description.md` · 2.8k · Plan[~]
- [ ] `programs/apps/streaming/masks/ant-media-server/features.md` · 2.6k · Plan[~]
- [ ] `programs/apps/streaming/masks/ant-media-server/menu.md` · 2.2k · Plan[~]
- [ ] `programs/apps/streaming/masks/ant-media-server/shortcuts.md` · 1.9k · Plan[~]
- [ ] `programs/apps/streaming/masks/ant-media-server/structure.md` · 3.7k · Plan[~]

### `programs/apps/streaming/masks/ffmpeg/` · 6

- [ ] `programs/apps/streaming/masks/ffmpeg/api.md` · 3.9k · Plan[~]
- [ ] `programs/apps/streaming/masks/ffmpeg/description.md` · 4.1k · Plan[~]
- [ ] `programs/apps/streaming/masks/ffmpeg/features.md` · 3.3k · Plan[~]
- [ ] `programs/apps/streaming/masks/ffmpeg/menu.md` · 2.6k · Plan[~]
- [ ] `programs/apps/streaming/masks/ffmpeg/shortcuts.md` · 2.7k · Plan[~]
- [ ] `programs/apps/streaming/masks/ffmpeg/structure.md` · 2.7k · Plan[~]

### `programs/apps/streaming/masks/gstreamer/` · 6

- [ ] `programs/apps/streaming/masks/gstreamer/api.md` · 4.7k · Plan[~]
- [ ] `programs/apps/streaming/masks/gstreamer/description.md` · 2.9k · Plan[~]
- [ ] `programs/apps/streaming/masks/gstreamer/features.md` · 3.4k · Plan[~]
- [ ] `programs/apps/streaming/masks/gstreamer/menu.md` · 2.1k · Plan[~]
- [ ] `programs/apps/streaming/masks/gstreamer/shortcuts.md` · 1.8k · Plan[~]
- [ ] `programs/apps/streaming/masks/gstreamer/structure.md` · 3.6k · Plan[~]

### `programs/apps/streaming/masks/mediamtx/` · 6

- [ ] `programs/apps/streaming/masks/mediamtx/api.md` · 4.1k · Plan[~]
- [ ] `programs/apps/streaming/masks/mediamtx/description.md` · 2.9k · Plan[~]
- [ ] `programs/apps/streaming/masks/mediamtx/features.md` · 3.0k · Plan[~]
- [ ] `programs/apps/streaming/masks/mediamtx/menu.md` · 2.4k · Plan[~]
- [ ] `programs/apps/streaming/masks/mediamtx/shortcuts.md` · 1.7k · Plan[~]
- [ ] `programs/apps/streaming/masks/mediamtx/structure.md` · 3.8k · Plan[~]

### `programs/apps/streaming/masks/mistserver/` · 6

- [ ] `programs/apps/streaming/masks/mistserver/api.md` · 4.3k · Plan[~]
- [ ] `programs/apps/streaming/masks/mistserver/description.md` · 2.8k · Plan[~]
- [ ] `programs/apps/streaming/masks/mistserver/features.md` · 2.6k · Plan[~]
- [ ] `programs/apps/streaming/masks/mistserver/menu.md` · 1.8k · Plan[~]
- [ ] `programs/apps/streaming/masks/mistserver/shortcuts.md` · 2.0k · Plan[~]
- [ ] `programs/apps/streaming/masks/mistserver/structure.md` · 3.6k · Plan[~]

### `programs/apps/streaming/masks/nginx-rtmp-module/` · 6

- [ ] `programs/apps/streaming/masks/nginx-rtmp-module/api.md` · 3.8k · Plan[~]
- [ ] `programs/apps/streaming/masks/nginx-rtmp-module/description.md` · 2.5k · Plan[~]
- [ ] `programs/apps/streaming/masks/nginx-rtmp-module/features.md` · 2.5k · Plan[~]
- [ ] `programs/apps/streaming/masks/nginx-rtmp-module/menu.md` · 2.4k · Plan[~]
- [ ] `programs/apps/streaming/masks/nginx-rtmp-module/shortcuts.md` · 1.6k · Plan[~]
- [ ] `programs/apps/streaming/masks/nginx-rtmp-module/structure.md` · 3.5k · Plan[~]

### `programs/apps/streaming/masks/obs-studio/` · 6

- [ ] `programs/apps/streaming/masks/obs-studio/api.md` · 3.2k · Plan[~]
- [ ] `programs/apps/streaming/masks/obs-studio/description.md` · 1.8k · Plan[~]
- [ ] `programs/apps/streaming/masks/obs-studio/features.md` · 2.3k · Plan[~]
- [ ] `programs/apps/streaming/masks/obs-studio/menu.md` · 2.2k · Plan[~]
- [ ] `programs/apps/streaming/masks/obs-studio/shortcuts.md` · 1.8k · Plan[~]
- [ ] `programs/apps/streaming/masks/obs-studio/structure.md` · 3.0k · Plan[~]

### `programs/apps/streaming/masks/restream/` · 6

- [ ] `programs/apps/streaming/masks/restream/api.md` · 3.0k · Plan[~]
- [ ] `programs/apps/streaming/masks/restream/description.md` · 2.5k · Plan[~]
- [ ] `programs/apps/streaming/masks/restream/features.md` · 2.3k · Plan[~]
- [ ] `programs/apps/streaming/masks/restream/menu.md` · 2.3k · Plan[~]
- [ ] `programs/apps/streaming/masks/restream/shortcuts.md` · 1.4k · Plan[~]
- [ ] `programs/apps/streaming/masks/restream/structure.md` · 3.5k · Plan[~]

### `programs/apps/streaming/masks/restreamer/` · 6

- [ ] `programs/apps/streaming/masks/restreamer/api.md` · 3.7k · Plan[~]
- [ ] `programs/apps/streaming/masks/restreamer/description.md` · 1.7k · Plan[~]
- [ ] `programs/apps/streaming/masks/restreamer/features.md` · 1.4k · Plan[~]
- [ ] `programs/apps/streaming/masks/restreamer/menu.md` · 1.3k · Plan[~]
- [ ] `programs/apps/streaming/masks/restreamer/shortcuts.md` · 1.9k · Plan[~]
- [ ] `programs/apps/streaming/masks/restreamer/structure.md` · 3.7k · Plan[~]

### `programs/apps/streaming/masks/wowza/` · 6

- [ ] `programs/apps/streaming/masks/wowza/api.md` · 3.2k · Plan[~]
- [ ] `programs/apps/streaming/masks/wowza/description.md` · 2.4k · Plan[~]
- [ ] `programs/apps/streaming/masks/wowza/features.md` · 2.3k · Plan[~]
- [ ] `programs/apps/streaming/masks/wowza/menu.md` · 2.2k · Plan[~]
- [ ] `programs/apps/streaming/masks/wowza/shortcuts.md` · 2.0k · Plan[~]
- [ ] `programs/apps/streaming/masks/wowza/structure.md` · 3.8k · Plan[~]

### `programs/apps/whiteboards/masks/drawio/` · 6

- [ ] `programs/apps/whiteboards/masks/drawio/api.md` · 6.3k · Plan[~]
- [ ] `programs/apps/whiteboards/masks/drawio/description.md` · 3.2k · Plan[~]
- [ ] `programs/apps/whiteboards/masks/drawio/features.md` · 5.9k · Plan[~]
- [ ] `programs/apps/whiteboards/masks/drawio/menu.md` · 4.6k · Plan[~]
- [ ] `programs/apps/whiteboards/masks/drawio/shortcuts.md` · 5.2k · Plan[~]
- [ ] `programs/apps/whiteboards/masks/drawio/structure.md` · 6.3k · Plan[~]

### `programs/apps/whiteboards/masks/excalidraw/` · 6

- [ ] `programs/apps/whiteboards/masks/excalidraw/api.md` · 5.9k · Plan[~]
- [ ] `programs/apps/whiteboards/masks/excalidraw/description.md` · 3.4k · Plan[~]
- [ ] `programs/apps/whiteboards/masks/excalidraw/features.md` · 5.6k · Plan[~]
- [ ] `programs/apps/whiteboards/masks/excalidraw/menu.md` · 3.7k · Plan[~]
- [ ] `programs/apps/whiteboards/masks/excalidraw/shortcuts.md` · 5.2k · Plan[~]
- [ ] `programs/apps/whiteboards/masks/excalidraw/structure.md` · 6.7k · Plan[~]

### `programs/apps/whiteboards/masks/miro/` · 6

- [ ] `programs/apps/whiteboards/masks/miro/api.md` · 2.3k · Plan[~]
- [ ] `programs/apps/whiteboards/masks/miro/description.md` · 1.2k · Plan[~]
- [ ] `programs/apps/whiteboards/masks/miro/features.md` · 1.3k · Plan[~]
- [ ] `programs/apps/whiteboards/masks/miro/menu.md` · 1.1k · Plan[~]
- [ ] `programs/apps/whiteboards/masks/miro/shortcuts.md` · 1.0k · Plan[~]
- [ ] `programs/apps/whiteboards/masks/miro/structure.md` · 2.1k · Plan[~]

### `programs/apps/whiteboards/masks/mural/` · 6

- [ ] `programs/apps/whiteboards/masks/mural/api.md` · 1.3k · Plan[~]
- [ ] `programs/apps/whiteboards/masks/mural/description.md` · 1.1k · Plan[~]
- [ ] `programs/apps/whiteboards/masks/mural/features.md` · 1.1k · Plan[~]
- [ ] `programs/apps/whiteboards/masks/mural/menu.md` · 1.1k · Plan[~]
- [ ] `programs/apps/whiteboards/masks/mural/shortcuts.md` · 703b · Plan[~]
- [ ] `programs/apps/whiteboards/masks/mural/structure.md` · 1.8k · Plan[~]

### `programs/apps/whiteboards/masks/openboard/` · 6

- [ ] `programs/apps/whiteboards/masks/openboard/api.md` · 1.2k · Plan[~]
- [ ] `programs/apps/whiteboards/masks/openboard/description.md` · 1.1k · Plan[~]
- [ ] `programs/apps/whiteboards/masks/openboard/features.md` · 1.2k · Plan[~]
- [ ] `programs/apps/whiteboards/masks/openboard/menu.md` · 975b · Plan[~]
- [ ] `programs/apps/whiteboards/masks/openboard/shortcuts.md` · 740b · Plan[~]
- [ ] `programs/apps/whiteboards/masks/openboard/structure.md` · 1.7k · Plan[~]

### `programs/apps/whiteboards/masks/tldraw/` · 6

- [ ] `programs/apps/whiteboards/masks/tldraw/api.md` · 3.0k · Plan[~]
- [ ] `programs/apps/whiteboards/masks/tldraw/description.md` · 3.2k · Plan[~]
- [ ] `programs/apps/whiteboards/masks/tldraw/features.md` · 4.8k · Plan[~]
- [ ] `programs/apps/whiteboards/masks/tldraw/menu.md` · 1.8k · Plan[~]
- [ ] `programs/apps/whiteboards/masks/tldraw/shortcuts.md` · 1.7k · Plan[~]
- [ ] `programs/apps/whiteboards/masks/tldraw/structure.md` · 2.9k · Plan[~]

### `programs/apps/wiki/masks/confluence/` · 6

- [ ] `programs/apps/wiki/masks/confluence/api.md` · 6.0k · Plan[~]
- [ ] `programs/apps/wiki/masks/confluence/description.md` · 1.9k · Plan[~]
- [ ] `programs/apps/wiki/masks/confluence/features.md` · 5.4k · Plan[~]
- [ ] `programs/apps/wiki/masks/confluence/menu.md` · 2.4k · Plan[~]
- [ ] `programs/apps/wiki/masks/confluence/shortcuts.md` · 7.0k · Plan[~]
- [ ] `programs/apps/wiki/masks/confluence/structure.md` · 5.9k · Plan[~]

### `programs/apps/wiki/masks/mediawiki/` · 6

- [ ] `programs/apps/wiki/masks/mediawiki/api.md` · 5.3k · Plan[~]
- [ ] `programs/apps/wiki/masks/mediawiki/description.md` · 1.9k · Plan[~]
- [ ] `programs/apps/wiki/masks/mediawiki/features.md` · 4.1k · Plan[~]
- [ ] `programs/apps/wiki/masks/mediawiki/menu.md` · 2.3k · Plan[~]
- [ ] `programs/apps/wiki/masks/mediawiki/shortcuts.md` · 6.7k · Plan[~]
- [ ] `programs/apps/wiki/masks/mediawiki/structure.md` · 5.7k · Plan[~]

### `programs/apps/wiki/masks/notion/` · 6

- [ ] `programs/apps/wiki/masks/notion/api.md` · 5.3k · Plan[~]
- [ ] `programs/apps/wiki/masks/notion/description.md` · 1.9k · Plan[~]
- [ ] `programs/apps/wiki/masks/notion/features.md` · 7.2k · Plan[~]
- [ ] `programs/apps/wiki/masks/notion/menu.md` · 4.2k · Plan[~]
- [ ] `programs/apps/wiki/masks/notion/shortcuts.md` · 7.1k · Plan[~]
- [ ] `programs/apps/wiki/masks/notion/structure.md` · 5.4k · Plan[~]

### `programs/apps/wiki/masks/tango.io/` · 6

- [ ] `programs/apps/wiki/masks/tango.io/api.md` · 5.0k · Plan[~]
- [ ] `programs/apps/wiki/masks/tango.io/description.md` · 1.8k · Plan[~]
- [ ] `programs/apps/wiki/masks/tango.io/features.md` · 4.8k · Plan[~]
- [ ] `programs/apps/wiki/masks/tango.io/menu.md` · 2.5k · Plan[~]
- [ ] `programs/apps/wiki/masks/tango.io/shortcuts.md` · 6.7k · Plan[~]
- [ ] `programs/apps/wiki/masks/tango.io/structure.md` · 5.4k · Plan[~]

### `programs/apps/wiki/masks/vscodium/` · 6

- [ ] `programs/apps/wiki/masks/vscodium/api.md` · 5.1k · Plan[~]
- [ ] `programs/apps/wiki/masks/vscodium/description.md` · 1.9k · Plan[~]
- [ ] `programs/apps/wiki/masks/vscodium/features.md` · 6.4k · Plan[~]
- [ ] `programs/apps/wiki/masks/vscodium/menu.md` · 2.0k · Plan[~]
- [ ] `programs/apps/wiki/masks/vscodium/shortcuts.md` · 6.4k · Plan[~]
- [ ] `programs/apps/wiki/masks/vscodium/structure.md` · 6.8k · Plan[~]

### `programs/apps/wiki/masks/wikijs/` · 6

- [ ] `programs/apps/wiki/masks/wikijs/api.md` · 4.4k · Plan[~]
- [ ] `programs/apps/wiki/masks/wikijs/description.md` · 2.1k · Plan[~]
- [ ] `programs/apps/wiki/masks/wikijs/features.md` · 3.6k · Plan[~]
- [ ] `programs/apps/wiki/masks/wikijs/menu.md` · 2.6k · Plan[~]
- [ ] `programs/apps/wiki/masks/wikijs/shortcuts.md` · 5.1k · Plan[~]
- [ ] `programs/apps/wiki/masks/wikijs/structure.md` · 6.2k · Plan[~]

### `programs/apps/wiki/masks/xwiki/` · 6

- [ ] `programs/apps/wiki/masks/xwiki/api.md` · 5.1k · Plan[~]
- [ ] `programs/apps/wiki/masks/xwiki/description.md` · 2.0k · Plan[~]
- [ ] `programs/apps/wiki/masks/xwiki/features.md` · 3.4k · Plan[~]
- [ ] `programs/apps/wiki/masks/xwiki/menu.md` · 2.4k · Plan[~]
- [ ] `programs/apps/wiki/masks/xwiki/shortcuts.md` · 6.7k · Plan[~]
- [ ] `programs/apps/wiki/masks/xwiki/structure.md` · 6.7k · Plan[~]

### `programs/platform/crates/` · 1

- [ ] `programs/platform/crates/gui.md` · 11.7k

### `programs/platform/desktop/masks/` · 1

- [ ] `programs/platform/desktop/masks/index.md` · 7.4k · Plan[~]

### `programs/platform/desktop/masks/dashy/` · 7

- [ ] `programs/platform/desktop/masks/dashy/api.md` · 7.5k · Plan[~]
- [ ] `programs/platform/desktop/masks/dashy/description.md` · 3.7k · Plan[~]
- [ ] `programs/platform/desktop/masks/dashy/features.md` · 7.0k · Plan[~]
- [ ] `programs/platform/desktop/masks/dashy/index.md` · 885b · Plan[~]
- [ ] `programs/platform/desktop/masks/dashy/menu.md` · 5.0k · Plan[~]
- [ ] `programs/platform/desktop/masks/dashy/shortcuts.md` · 6.2k · Plan[~]
- [ ] `programs/platform/desktop/masks/dashy/structure.md` · 8.0k · Plan[~]

### `programs/platform/desktop/masks/gethomepage/` · 7

- [ ] `programs/platform/desktop/masks/gethomepage/api.md` · 8.4k · Plan[~]
- [ ] `programs/platform/desktop/masks/gethomepage/description.md` · 4.6k · Plan[~]
- [ ] `programs/platform/desktop/masks/gethomepage/features.md` · 6.5k · Plan[~]
- [ ] `programs/platform/desktop/masks/gethomepage/index.md` · 1.0k · Plan[~]
- [ ] `programs/platform/desktop/masks/gethomepage/menu.md` · 5.7k · Plan[~]
- [ ] `programs/platform/desktop/masks/gethomepage/shortcuts.md` · 6.8k · Plan[~]
- [ ] `programs/platform/desktop/masks/gethomepage/structure.md` · 6.8k · Plan[~]

### `programs/platform/desktop/masks/heimdall/` · 7

- [ ] `programs/platform/desktop/masks/heimdall/api.md` · 7.2k · Plan[~]
- [ ] `programs/platform/desktop/masks/heimdall/description.md` · 3.8k · Plan[~]
- [ ] `programs/platform/desktop/masks/heimdall/features.md` · 6.2k · Plan[~]
- [ ] `programs/platform/desktop/masks/heimdall/index.md` · 837b · Plan[~]
- [ ] `programs/platform/desktop/masks/heimdall/menu.md` · 4.6k · Plan[~]
- [ ] `programs/platform/desktop/masks/heimdall/shortcuts.md` · 5.4k · Plan[~]
- [ ] `programs/platform/desktop/masks/heimdall/structure.md` · 7.7k · Plan[~]

### `programs/platform/desktop/masks/homarr/` · 7

- [ ] `programs/platform/desktop/masks/homarr/api.md` · 8.3k · Plan[~]
- [ ] `programs/platform/desktop/masks/homarr/description.md` · 3.6k · Plan[~]
- [ ] `programs/platform/desktop/masks/homarr/features.md` · 6.1k · Plan[~]
- [ ] `programs/platform/desktop/masks/homarr/index.md` · 836b · Plan[~]
- [ ] `programs/platform/desktop/masks/homarr/menu.md` · 4.8k · Plan[~]
- [ ] `programs/platform/desktop/masks/homarr/shortcuts.md` · 5.8k · Plan[~]
- [ ] `programs/platform/desktop/masks/homarr/structure.md` · 7.8k · Plan[~]

### `programs/platform/desktop/masks/homepage/` · 7

- [ ] `programs/platform/desktop/masks/homepage/api.md` · 9.3k · Plan[~]
- [ ] `programs/platform/desktop/masks/homepage/description.md` · 4.1k · Plan[~]
- [ ] `programs/platform/desktop/masks/homepage/features.md` · 6.8k · Plan[~]
- [ ] `programs/platform/desktop/masks/homepage/index.md` · 1010b · Plan[~]
- [ ] `programs/platform/desktop/masks/homepage/menu.md` · 5.7k · Plan[~]
- [ ] `programs/platform/desktop/masks/homepage/shortcuts.md` · 6.1k · Plan[~]
- [ ] `programs/platform/desktop/masks/homepage/structure.md` · 7.2k · Plan[~]

### `programs/platform/desktop/masks/homer/` · 7

- [ ] `programs/platform/desktop/masks/homer/api.md` · 7.4k · Plan[~]
- [ ] `programs/platform/desktop/masks/homer/description.md` · 3.3k · Plan[~]
- [ ] `programs/platform/desktop/masks/homer/features.md` · 5.8k · Plan[~]
- [ ] `programs/platform/desktop/masks/homer/index.md` · 801b · Plan[~]
- [ ] `programs/platform/desktop/masks/homer/menu.md` · 4.6k · Plan[~]
- [ ] `programs/platform/desktop/masks/homer/shortcuts.md` · 5.5k · Plan[~]
- [ ] `programs/platform/desktop/masks/homer/structure.md` · 7.7k · Plan[~]

### `programs/platform/desktop/masks/launchboard/` · 7

- [ ] `programs/platform/desktop/masks/launchboard/api.md` · 9.2k · Plan[~]
- [ ] `programs/platform/desktop/masks/launchboard/description.md` · 4.6k · Plan[~]
- [ ] `programs/platform/desktop/masks/launchboard/features.md` · 6.7k · Plan[~]
- [ ] `programs/platform/desktop/masks/launchboard/index.md` · 1.1k · Plan[~]
- [ ] `programs/platform/desktop/masks/launchboard/menu.md` · 5.1k · Plan[~]
- [ ] `programs/platform/desktop/masks/launchboard/shortcuts.md` · 6.5k · Plan[~]
- [ ] `programs/platform/desktop/masks/launchboard/structure.md` · 8.8k · Plan[~]

### `programs/platform/desktop/masks/opnsense/` · 7

- [ ] `programs/platform/desktop/masks/opnsense/api.md` · 7.3k · Plan[~]
- [ ] `programs/platform/desktop/masks/opnsense/description.md` · 3.7k · Plan[~]
- [ ] `programs/platform/desktop/masks/opnsense/features.md` · 5.3k · Plan[~]
- [ ] `programs/platform/desktop/masks/opnsense/index.md` · 955b · Plan[~]
- [ ] `programs/platform/desktop/masks/opnsense/menu.md` · 5.7k · Plan[~]
- [ ] `programs/platform/desktop/masks/opnsense/shortcuts.md` · 5.6k · Plan[~]
- [ ] `programs/platform/desktop/masks/opnsense/structure.md` · 6.7k · Plan[~]

### `programs/platform/desktop/masks/proxmox/` · 7

- [ ] `programs/platform/desktop/masks/proxmox/api.md` · 6.5k · Plan[~]
- [ ] `programs/platform/desktop/masks/proxmox/description.md` · 3.9k · Plan[~]
- [ ] `programs/platform/desktop/masks/proxmox/features.md` · 5.7k · Plan[~]
- [ ] `programs/platform/desktop/masks/proxmox/index.md` · 954b · Plan[~]
- [ ] `programs/platform/desktop/masks/proxmox/menu.md` · 5.1k · Plan[~]
- [ ] `programs/platform/desktop/masks/proxmox/shortcuts.md` · 5.8k · Plan[~]
- [ ] `programs/platform/desktop/masks/proxmox/structure.md` · 7.2k · Plan[~]

### `programs/platform/desktop/masks/synology-dsm/` · 7

- [ ] `programs/platform/desktop/masks/synology-dsm/api.md` · 8.3k · Plan[~]
- [ ] `programs/platform/desktop/masks/synology-dsm/description.md` · 4.7k · Plan[~]
- [ ] `programs/platform/desktop/masks/synology-dsm/features.md` · 7.0k · Plan[~]
- [ ] `programs/platform/desktop/masks/synology-dsm/index.md` · 961b · Plan[~]
- [ ] `programs/platform/desktop/masks/synology-dsm/menu.md` · 5.5k · Plan[~]
- [ ] `programs/platform/desktop/masks/synology-dsm/shortcuts.md` · 6.5k · Plan[~]
- [ ] `programs/platform/desktop/masks/synology-dsm/structure.md` · 8.4k · Plan[~]

### `programs/platform/desktop/masks/truenas/` · 7

- [ ] `programs/platform/desktop/masks/truenas/api.md` · 6.4k · Plan[~]
- [ ] `programs/platform/desktop/masks/truenas/description.md` · 3.8k · Plan[~]
- [ ] `programs/platform/desktop/masks/truenas/features.md` · 5.5k · Plan[~]
- [ ] `programs/platform/desktop/masks/truenas/index.md` · 1022b · Plan[~]
- [ ] `programs/platform/desktop/masks/truenas/menu.md` · 4.9k · Plan[~]
- [ ] `programs/platform/desktop/masks/truenas/shortcuts.md` · 5.7k · Plan[~]
- [ ] `programs/platform/desktop/masks/truenas/structure.md` · 6.4k · Plan[~]

### `programs/platform/desktop/masks/unraid/` · 7

- [ ] `programs/platform/desktop/masks/unraid/api.md` · 7.0k · Plan[~]
- [ ] `programs/platform/desktop/masks/unraid/description.md` · 3.7k · Plan[~]
- [ ] `programs/platform/desktop/masks/unraid/features.md` · 5.8k · Plan[~]
- [ ] `programs/platform/desktop/masks/unraid/index.md` · 1015b · Plan[~]
- [ ] `programs/platform/desktop/masks/unraid/menu.md` · 4.9k · Plan[~]
- [ ] `programs/platform/desktop/masks/unraid/shortcuts.md` · 5.7k · Plan[~]
- [ ] `programs/platform/desktop/masks/unraid/structure.md` · 8.1k · Plan[~]

### `programs/suites/crm/masks/` · 1

- [ ] `programs/suites/crm/masks/index.md` · 2.6k · Plan[~]

### `programs/suites/crm/masks/civicrm/` · 7

- [ ] `programs/suites/crm/masks/civicrm/api.md` · 2.5k · Plan[~]
- [ ] `programs/suites/crm/masks/civicrm/description.md` · 1.6k · Plan[~]
- [ ] `programs/suites/crm/masks/civicrm/features.md` · 1.8k · Plan[~]
- [ ] `programs/suites/crm/masks/civicrm/index.md` · 850b · Plan[~]
- [ ] `programs/suites/crm/masks/civicrm/menu.md` · 1.5k · Plan[~]
- [ ] `programs/suites/crm/masks/civicrm/shortcuts.md` · 674b · Plan[~]
- [ ] `programs/suites/crm/masks/civicrm/structure.md` · 2.5k · Plan[~]

### `programs/suites/crm/masks/espocrm/` · 7

- [ ] `programs/suites/crm/masks/espocrm/api.md` · 2.3k · Plan[~]
- [ ] `programs/suites/crm/masks/espocrm/description.md` · 1.4k · Plan[~]
- [ ] `programs/suites/crm/masks/espocrm/features.md` · 1.4k · Plan[~]
- [ ] `programs/suites/crm/masks/espocrm/index.md` · 752b · Plan[~]
- [ ] `programs/suites/crm/masks/espocrm/menu.md` · 1.3k · Plan[~]
- [ ] `programs/suites/crm/masks/espocrm/shortcuts.md` · 831b · Plan[~]
- [ ] `programs/suites/crm/masks/espocrm/structure.md` · 2.1k · Plan[~]

### `programs/suites/crm/masks/hubspot/` · 7

- [ ] `programs/suites/crm/masks/hubspot/api.md` · 2.5k · Plan[~]
- [ ] `programs/suites/crm/masks/hubspot/description.md` · 1.3k · Plan[~]
- [ ] `programs/suites/crm/masks/hubspot/features.md` · 1.3k · Plan[~]
- [ ] `programs/suites/crm/masks/hubspot/index.md` · 792b · Plan[~]
- [ ] `programs/suites/crm/masks/hubspot/menu.md` · 1.3k · Plan[~]
- [ ] `programs/suites/crm/masks/hubspot/shortcuts.md` · 670b · Plan[~]
- [ ] `programs/suites/crm/masks/hubspot/structure.md` · 2.1k · Plan[~]

### `programs/suites/crm/masks/pipedrive/` · 7

- [ ] `programs/suites/crm/masks/pipedrive/api.md` · 7.2k · Plan[~]
- [ ] `programs/suites/crm/masks/pipedrive/description.md` · 3.5k · Plan[~]
- [ ] `programs/suites/crm/masks/pipedrive/features.md` · 6.0k · Plan[~]
- [ ] `programs/suites/crm/masks/pipedrive/index.md` · 907b · Plan[~]
- [ ] `programs/suites/crm/masks/pipedrive/menu.md` · 4.8k · Plan[~]
- [ ] `programs/suites/crm/masks/pipedrive/shortcuts.md` · 6.9k · Plan[~]
- [ ] `programs/suites/crm/masks/pipedrive/structure.md` · 6.4k · Plan[~]

### `programs/suites/crm/masks/salesforce/` · 7

- [ ] `programs/suites/crm/masks/salesforce/api.md` · 2.7k · Plan[~]
- [ ] `programs/suites/crm/masks/salesforce/description.md` · 1.6k · Plan[~]
- [ ] `programs/suites/crm/masks/salesforce/features.md` · 1.5k · Plan[~]
- [ ] `programs/suites/crm/masks/salesforce/index.md` · 787b · Plan[~]
- [ ] `programs/suites/crm/masks/salesforce/menu.md` · 1.5k · Plan[~]
- [ ] `programs/suites/crm/masks/salesforce/shortcuts.md` · 1014b · Plan[~]
- [ ] `programs/suites/crm/masks/salesforce/structure.md` · 2.2k · Plan[~]

### `programs/suites/crm/masks/suitecrm/` · 7

- [ ] `programs/suites/crm/masks/suitecrm/api.md` · 8.2k · Plan[~]
- [ ] `programs/suites/crm/masks/suitecrm/description.md` · 3.4k · Plan[~]
- [ ] `programs/suites/crm/masks/suitecrm/features.md` · 6.5k · Plan[~]
- [ ] `programs/suites/crm/masks/suitecrm/index.md` · 856b · Plan[~]
- [ ] `programs/suites/crm/masks/suitecrm/menu.md` · 4.8k · Plan[~]
- [ ] `programs/suites/crm/masks/suitecrm/shortcuts.md` · 7.0k · Plan[~]
- [ ] `programs/suites/crm/masks/suitecrm/structure.md` · 6.5k · Plan[~]

### `programs/suites/democracy/masks/` · 1

- [ ] `programs/suites/democracy/masks/index.md` · 2.7k · Plan[~]

### `programs/suites/democracy/masks/adhocracy4/` · 7

- [ ] `programs/suites/democracy/masks/adhocracy4/api.md` · 1.8k · Plan[~]
- [ ] `programs/suites/democracy/masks/adhocracy4/description.md` · 1.3k · Plan[~]
- [ ] `programs/suites/democracy/masks/adhocracy4/features.md` · 1.3k · Plan[~]
- [ ] `programs/suites/democracy/masks/adhocracy4/index.md` · 776b · Plan[~]
- [ ] `programs/suites/democracy/masks/adhocracy4/menu.md` · 982b · Plan[~]
- [ ] `programs/suites/democracy/masks/adhocracy4/shortcuts.md` · 414b · Plan[~]
- [ ] `programs/suites/democracy/masks/adhocracy4/structure.md` · 1.6k · Plan[~]

### `programs/suites/democracy/masks/circo/` · 7

- [ ] `programs/suites/democracy/masks/circo/api.md` · 1.2k · Plan[~]
- [ ] `programs/suites/democracy/masks/circo/description.md` · 1.2k · Plan[~]
- [ ] `programs/suites/democracy/masks/circo/features.md` · 884b · Plan[~]
- [ ] `programs/suites/democracy/masks/circo/index.md` · 844b · Plan[~]
- [ ] `programs/suites/democracy/masks/circo/menu.md` · 839b · Plan[~]
- [ ] `programs/suites/democracy/masks/circo/shortcuts.md` · 310b · Plan[~]
- [ ] `programs/suites/democracy/masks/circo/structure.md` · 900b · Plan[~]

### `programs/suites/democracy/masks/consul/` · 7

- [ ] `programs/suites/democracy/masks/consul/api.md` · 1.7k · Plan[~]
- [ ] `programs/suites/democracy/masks/consul/description.md` · 1.1k · Plan[~]
- [ ] `programs/suites/democracy/masks/consul/features.md` · 1.1k · Plan[~]
- [ ] `programs/suites/democracy/masks/consul/index.md` · 771b · Plan[~]
- [ ] `programs/suites/democracy/masks/consul/menu.md` · 1015b · Plan[~]
- [ ] `programs/suites/democracy/masks/consul/shortcuts.md` · 373b · Plan[~]
- [ ] `programs/suites/democracy/masks/consul/structure.md` · 1.5k · Plan[~]

### `programs/suites/democracy/masks/decidim/` · 7

- [ ] `programs/suites/democracy/masks/decidim/api.md` · 1.8k · Plan[~]
- [ ] `programs/suites/democracy/masks/decidim/description.md` · 1.3k · Plan[~]
- [ ] `programs/suites/democracy/masks/decidim/features.md` · 1.3k · Plan[~]
- [ ] `programs/suites/democracy/masks/decidim/index.md` · 823b · Plan[~]
- [ ] `programs/suites/democracy/masks/decidim/menu.md` · 920b · Plan[~]
- [ ] `programs/suites/democracy/masks/decidim/shortcuts.md` · 452b · Plan[~]
- [ ] `programs/suites/democracy/masks/decidim/structure.md` · 1.7k · Plan[~]

### `programs/suites/democracy/masks/liquid-feedback/` · 7

- [ ] `programs/suites/democracy/masks/liquid-feedback/api.md` · 1.4k · Plan[~]
- [ ] `programs/suites/democracy/masks/liquid-feedback/description.md` · 1.2k · Plan[~]
- [ ] `programs/suites/democracy/masks/liquid-feedback/features.md` · 1.2k · Plan[~]
- [ ] `programs/suites/democracy/masks/liquid-feedback/index.md` · 766b · Plan[~]
- [ ] `programs/suites/democracy/masks/liquid-feedback/menu.md` · 1.1k · Plan[~]
- [ ] `programs/suites/democracy/masks/liquid-feedback/shortcuts.md` · 365b · Plan[~]
- [ ] `programs/suites/democracy/masks/liquid-feedback/structure.md` · 1.7k · Plan[~]

### `programs/suites/democracy/masks/polis/` · 7

- [ ] `programs/suites/democracy/masks/polis/api.md` · 1.7k · Plan[~]
- [ ] `programs/suites/democracy/masks/polis/description.md` · 1.2k · Plan[~]
- [ ] `programs/suites/democracy/masks/polis/features.md` · 1.2k · Plan[~]
- [ ] `programs/suites/democracy/masks/polis/index.md` · 757b · Plan[~]
- [ ] `programs/suites/democracy/masks/polis/menu.md` · 872b · Plan[~]
- [ ] `programs/suites/democracy/masks/polis/shortcuts.md` · 431b · Plan[~]
- [ ] `programs/suites/democracy/masks/polis/structure.md` · 1.6k · Plan[~]

### `programs/suites/erp/masks/` · 1

- [ ] `programs/suites/erp/masks/index.md` · 2.6k · Plan[~]

### `programs/suites/erp/masks/axelor/` · 7

- [ ] `programs/suites/erp/masks/axelor/api.md` · 2.2k · Plan[~]
- [ ] `programs/suites/erp/masks/axelor/description.md` · 1.2k · Plan[~]
- [ ] `programs/suites/erp/masks/axelor/features.md` · 1.1k · Plan[~]
- [ ] `programs/suites/erp/masks/axelor/index.md` · 743b · Plan[~]
- [ ] `programs/suites/erp/masks/axelor/menu.md` · 922b · Plan[~]
- [ ] `programs/suites/erp/masks/axelor/shortcuts.md` · 438b · Plan[~]
- [ ] `programs/suites/erp/masks/axelor/structure.md` · 1.6k · Plan[~]

### `programs/suites/erp/masks/dolibarr/` · 7

- [ ] `programs/suites/erp/masks/dolibarr/api.md` · 2.6k · Plan[~]
- [ ] `programs/suites/erp/masks/dolibarr/description.md` · 1.2k · Plan[~]
- [ ] `programs/suites/erp/masks/dolibarr/features.md` · 1.2k · Plan[~]
- [ ] `programs/suites/erp/masks/dolibarr/index.md` · 708b · Plan[~]
- [ ] `programs/suites/erp/masks/dolibarr/menu.md` · 1.1k · Plan[~]
- [ ] `programs/suites/erp/masks/dolibarr/shortcuts.md` · 461b · Plan[~]
- [ ] `programs/suites/erp/masks/dolibarr/structure.md` · 1.8k · Plan[~]

### `programs/suites/erp/masks/erpnext/` · 7

- [ ] `programs/suites/erp/masks/erpnext/api.md` · 2.3k · Plan[~]
- [ ] `programs/suites/erp/masks/erpnext/description.md` · 1.3k · Plan[~]
- [ ] `programs/suites/erp/masks/erpnext/features.md` · 1.3k · Plan[~]
- [ ] `programs/suites/erp/masks/erpnext/index.md` · 742b · Plan[~]
- [ ] `programs/suites/erp/masks/erpnext/menu.md` · 923b · Plan[~]
- [ ] `programs/suites/erp/masks/erpnext/shortcuts.md` · 564b · Plan[~]
- [ ] `programs/suites/erp/masks/erpnext/structure.md` · 1.8k · Plan[~]

### `programs/suites/erp/masks/odoo/` · 7

- [ ] `programs/suites/erp/masks/odoo/api.md` · 2.5k · Plan[~]
- [ ] `programs/suites/erp/masks/odoo/description.md` · 1.4k · Plan[~]
- [ ] `programs/suites/erp/masks/odoo/features.md` · 1.4k · Plan[~]
- [ ] `programs/suites/erp/masks/odoo/index.md` · 781b · Plan[~]
- [ ] `programs/suites/erp/masks/odoo/menu.md` · 1.1k · Plan[~]
- [ ] `programs/suites/erp/masks/odoo/shortcuts.md` · 870b · Plan[~]
- [ ] `programs/suites/erp/masks/odoo/structure.md` · 1.9k · Plan[~]

### `programs/suites/erp/masks/sage/` · 7

- [ ] `programs/suites/erp/masks/sage/api.md` · 1.8k · Plan[~]
- [ ] `programs/suites/erp/masks/sage/description.md` · 1.3k · Plan[~]
- [ ] `programs/suites/erp/masks/sage/features.md` · 1.1k · Plan[~]
- [ ] `programs/suites/erp/masks/sage/index.md` · 871b · Plan[~]
- [ ] `programs/suites/erp/masks/sage/menu.md` · 954b · Plan[~]
- [ ] `programs/suites/erp/masks/sage/shortcuts.md` · 797b · Plan[~]
- [ ] `programs/suites/erp/masks/sage/structure.md` · 1.1k · Plan[~]

### `programs/suites/erp/masks/tryton/` · 7

- [ ] `programs/suites/erp/masks/tryton/api.md` · 2.2k · Plan[~]
- [ ] `programs/suites/erp/masks/tryton/description.md` · 1.1k · Plan[~]
- [ ] `programs/suites/erp/masks/tryton/features.md` · 1.0k · Plan[~]
- [ ] `programs/suites/erp/masks/tryton/index.md` · 747b · Plan[~]
- [ ] `programs/suites/erp/masks/tryton/menu.md` · 992b · Plan[~]
- [ ] `programs/suites/erp/masks/tryton/shortcuts.md` · 612b · Plan[~]
- [ ] `programs/suites/erp/masks/tryton/structure.md` · 1.7k · Plan[~]

### `programs/suites/marketplace/` · 1

- [ ] `programs/suites/marketplace/index.md` · 2.4k · Plan[~]

### `programs/suites/marketplace/masks/` · 1

- [ ] `programs/suites/marketplace/masks/index.md` · 2.7k · Plan[~]

### `programs/suites/marketplace/masks/arcemall/` · 7

- [ ] `programs/suites/marketplace/masks/arcemall/api.md` · 1.4k · Plan[~]
- [ ] `programs/suites/marketplace/masks/arcemall/description.md` · 1.2k · Plan[~]
- [ ] `programs/suites/marketplace/masks/arcemall/features.md` · 963b · Plan[~]
- [ ] `programs/suites/marketplace/masks/arcemall/index.md` · 861b · Plan[~]
- [ ] `programs/suites/marketplace/masks/arcemall/menu.md` · 765b · Plan[~]
- [ ] `programs/suites/marketplace/masks/arcemall/shortcuts.md` · 314b · Plan[~]
- [ ] `programs/suites/marketplace/masks/arcemall/structure.md` · 885b · Plan[~]

### `programs/suites/marketplace/masks/cs-cart-multivendor/` · 7

- [ ] `programs/suites/marketplace/masks/cs-cart-multivendor/api.md` · 1.7k · Plan[~]
- [ ] `programs/suites/marketplace/masks/cs-cart-multivendor/description.md` · 1.1k · Plan[~]
- [ ] `programs/suites/marketplace/masks/cs-cart-multivendor/features.md` · 889b · Plan[~]
- [ ] `programs/suites/marketplace/masks/cs-cart-multivendor/index.md` · 779b · Plan[~]
- [ ] `programs/suites/marketplace/masks/cs-cart-multivendor/menu.md` · 945b · Plan[~]
- [ ] `programs/suites/marketplace/masks/cs-cart-multivendor/shortcuts.md` · 409b · Plan[~]
- [ ] `programs/suites/marketplace/masks/cs-cart-multivendor/structure.md` · 970b · Plan[~]

### `programs/suites/marketplace/masks/ebay/` · 7

- [ ] `programs/suites/marketplace/masks/ebay/api.md` · 2.5k · Plan[~]
- [ ] `programs/suites/marketplace/masks/ebay/description.md` · 1.1k · Plan[~]
- [ ] `programs/suites/marketplace/masks/ebay/features.md` · 1.1k · Plan[~]
- [ ] `programs/suites/marketplace/masks/ebay/index.md` · 816b · Plan[~]
- [ ] `programs/suites/marketplace/masks/ebay/menu.md` · 971b · Plan[~]
- [ ] `programs/suites/marketplace/masks/ebay/shortcuts.md` · 424b · Plan[~]
- [ ] `programs/suites/marketplace/masks/ebay/structure.md` · 949b · Plan[~]

### `programs/suites/marketplace/masks/etsy/` · 7

- [ ] `programs/suites/marketplace/masks/etsy/api.md` · 2.1k · Plan[~]
- [ ] `programs/suites/marketplace/masks/etsy/description.md` · 1.1k · Plan[~]
- [ ] `programs/suites/marketplace/masks/etsy/features.md` · 987b · Plan[~]
- [ ] `programs/suites/marketplace/masks/etsy/index.md` · 714b · Plan[~]
- [ ] `programs/suites/marketplace/masks/etsy/menu.md` · 934b · Plan[~]
- [ ] `programs/suites/marketplace/masks/etsy/shortcuts.md` · 378b · Plan[~]
- [ ] `programs/suites/marketplace/masks/etsy/structure.md` · 940b · Plan[~]

### `programs/suites/marketplace/masks/kleinanzeigen/` · 7

- [ ] `programs/suites/marketplace/masks/kleinanzeigen/api.md` · 1.3k · Plan[~]
- [ ] `programs/suites/marketplace/masks/kleinanzeigen/description.md` · 1.1k · Plan[~]
- [ ] `programs/suites/marketplace/masks/kleinanzeigen/features.md` · 1020b · Plan[~]
- [ ] `programs/suites/marketplace/masks/kleinanzeigen/index.md` · 874b · Plan[~]
- [ ] `programs/suites/marketplace/masks/kleinanzeigen/menu.md` · 820b · Plan[~]
- [ ] `programs/suites/marketplace/masks/kleinanzeigen/shortcuts.md` · 347b · Plan[~]
- [ ] `programs/suites/marketplace/masks/kleinanzeigen/structure.md` · 1.5k · Plan[~]

### `programs/suites/marketplace/masks/sharetribe/` · 7

- [ ] `programs/suites/marketplace/masks/sharetribe/api.md` · 2.3k · Plan[~]
- [ ] `programs/suites/marketplace/masks/sharetribe/description.md` · 1.4k · Plan[~]
- [ ] `programs/suites/marketplace/masks/sharetribe/features.md` · 1.3k · Plan[~]
- [ ] `programs/suites/marketplace/masks/sharetribe/index.md` · 920b · Plan[~]
- [ ] `programs/suites/marketplace/masks/sharetribe/menu.md` · 996b · Plan[~]
- [ ] `programs/suites/marketplace/masks/sharetribe/shortcuts.md` · 395b · Plan[~]
- [ ] `programs/suites/marketplace/masks/sharetribe/structure.md` · 1.7k · Plan[~]

### `programs/suites/workflows/masks/` · 1

- [ ] `programs/suites/workflows/masks/index.md` · 2.6k · Plan[~]

### `programs/suites/workflows/masks/apache-airflow/` · 7

- [ ] `programs/suites/workflows/masks/apache-airflow/api.md` · 2.5k · Plan[~]
- [ ] `programs/suites/workflows/masks/apache-airflow/description.md` · 1.3k · Plan[~]
- [ ] `programs/suites/workflows/masks/apache-airflow/features.md` · 1.3k · Plan[~]
- [ ] `programs/suites/workflows/masks/apache-airflow/index.md` · 820b · Plan[~]
- [ ] `programs/suites/workflows/masks/apache-airflow/menu.md` · 1005b · Plan[~]
- [ ] `programs/suites/workflows/masks/apache-airflow/shortcuts.md` · 773b · Plan[~]
- [ ] `programs/suites/workflows/masks/apache-airflow/structure.md` · 2.1k · Plan[~]

### `programs/suites/workflows/masks/make/` · 7

- [ ] `programs/suites/workflows/masks/make/api.md` · 2.1k · Plan[~]
- [ ] `programs/suites/workflows/masks/make/description.md` · 1.2k · Plan[~]
- [ ] `programs/suites/workflows/masks/make/features.md` · 1.3k · Plan[~]
- [ ] `programs/suites/workflows/masks/make/index.md` · 755b · Plan[~]
- [ ] `programs/suites/workflows/masks/make/menu.md` · 981b · Plan[~]
- [ ] `programs/suites/workflows/masks/make/shortcuts.md` · 481b · Plan[~]
- [ ] `programs/suites/workflows/masks/make/structure.md` · 1.9k · Plan[~]

### `programs/suites/workflows/masks/n8n/` · 7

- [ ] `programs/suites/workflows/masks/n8n/api.md` · 2.3k · Plan[~]
- [ ] `programs/suites/workflows/masks/n8n/description.md` · 1.3k · Plan[~]
- [ ] `programs/suites/workflows/masks/n8n/features.md` · 1.3k · Plan[~]
- [ ] `programs/suites/workflows/masks/n8n/index.md` · 731b · Plan[~]
- [ ] `programs/suites/workflows/masks/n8n/menu.md` · 1.3k · Plan[~]
- [ ] `programs/suites/workflows/masks/n8n/shortcuts.md` · 771b · Plan[~]
- [ ] `programs/suites/workflows/masks/n8n/structure.md` · 2.0k · Plan[~]

### `programs/suites/workflows/masks/node-red/` · 7

- [ ] `programs/suites/workflows/masks/node-red/api.md` · 2.1k · Plan[~]
- [ ] `programs/suites/workflows/masks/node-red/description.md` · 1.2k · Plan[~]
- [ ] `programs/suites/workflows/masks/node-red/features.md` · 1.4k · Plan[~]
- [ ] `programs/suites/workflows/masks/node-red/index.md` · 792b · Plan[~]
- [ ] `programs/suites/workflows/masks/node-red/menu.md` · 1.2k · Plan[~]
- [ ] `programs/suites/workflows/masks/node-red/shortcuts.md` · 806b · Plan[~]
- [ ] `programs/suites/workflows/masks/node-red/structure.md` · 2.0k · Plan[~]

### `programs/suites/workflows/masks/prefect/` · 7

- [ ] `programs/suites/workflows/masks/prefect/api.md` · 2.3k · Plan[~]
- [ ] `programs/suites/workflows/masks/prefect/description.md` · 1.2k · Plan[~]
- [ ] `programs/suites/workflows/masks/prefect/features.md` · 1.3k · Plan[~]
- [ ] `programs/suites/workflows/masks/prefect/index.md` · 696b · Plan[~]
- [ ] `programs/suites/workflows/masks/prefect/menu.md` · 969b · Plan[~]
- [ ] `programs/suites/workflows/masks/prefect/shortcuts.md` · 727b · Plan[~]
- [ ] `programs/suites/workflows/masks/prefect/structure.md` · 1.9k · Plan[~]

### `programs/suites/workflows/masks/zapier/` · 7

- [ ] `programs/suites/workflows/masks/zapier/api.md` · 2.2k · Plan[~]
- [ ] `programs/suites/workflows/masks/zapier/description.md` · 1.1k · Plan[~]
- [ ] `programs/suites/workflows/masks/zapier/features.md` · 1.1k · Plan[~]
- [ ] `programs/suites/workflows/masks/zapier/index.md` · 761b · Plan[~]
- [ ] `programs/suites/workflows/masks/zapier/menu.md` · 1.1k · Plan[~]
- [ ] `programs/suites/workflows/masks/zapier/shortcuts.md` · 449b · Plan[~]
- [ ] `programs/suites/workflows/masks/zapier/structure.md` · 2.1k · Plan[~]

## 🗑️ Gelöscht – 7

- [x] `data/anforderungen.md` · nicht mehr im Baum
- [x] `data/contacts/jscontact/beschreibung.md` · nicht mehr im Baum
- [x] `data/contacts/jscontact/speicherung.md` · nicht mehr im Baum
- [x] `data/felder.md` · nicht mehr im Baum
- [x] `data/formate.md` · nicht mehr im Baum
- [x] `data/konventionen.md` · nicht mehr im Baum
- [x] `data/modelle.md` · nicht mehr im Baum

## Changelog

  der `de`-Datei übernommen) und `--gen-box <pfad> --cell "a|b"`. Erster Fund gefixt:
  `en/components/primitives/fields/field/appearance.md` (Zeile 26 → 25 Zeichen, Frame bleibt heil).
- 2026-11-05 02:25 · **Festhaltungen:** `conventions/decisions/0010-ein-uebersetzungspruefer.md`,
  `temp/state.md` auf `doc_sync.py` umgestellt, `temp/translation-progress.md` stillgelegt.
  Abschnittszahlen jetzt: A 687 · B 1 · C 0 · D 3 · D2 15 · E 0 · F 29 · G 17 · H 756.
- 2026-11-04 20:45 · **Abschnitt D abgearbeitet (3 von 4):** `en/components/widgets/overlays/drawer/appearance.md`,
  `en/components/workbenches/special/dashboard/appearance.md` (deutsche Tabellenzellen in Groessen/Farben
  uebersetzt), `en/programs/apps/calendar/masks/google-calendar/menu.md` (deutsche Menue-Labels an den
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
