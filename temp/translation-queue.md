# Übersetzungsliste – der Übersetzungs-Checker für den ganzen Baum

Stand: 2026-11-05 02:57 UTC · 1492 Dateien verfolgt · 1489 offen · 3 bestätigt

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
| A. `en/` fehlt – aus `de/` übersetzen | 687 |
| B. `de/` fehlt – englische Quelle nachziehen | 1 |
| C. `en/` ist eine Kopie von `de/` – unübersetzt | 0 |
| D. `en/` enthält noch deutschen Text – Rest übersetzen | 3 |
| D2. Deutscher Text in Codebeispielen/Boxen (ADR 0002: Code ist englisch) | 15 |
| E. `de/` enthält noch englischen Text – Rest rückübersetzen | 0 |
| F. Form nicht gleich – Struktur abgleichen | 28 |
| G. Deutscher Dateiname – Pfad englisch machen (ADR 0002) | 17 |
| H. Beide Seiten da, kein Befund – lesen und bestätigen | 757 |
| 🗑️ gelöscht (tombstone) | 0 |

## A. `en/` fehlt – aus `de/` übersetzen – 687 Dateien

### `data/` · 8

- [ ] `data/anforderungen.md` · 7.1k · auch: rename
- [ ] `data/api.md` · 8.8k
- [ ] `data/felder.md` · 10.0k · auch: rename
- [ ] `data/formate.md` · 5.2k · auch: rename
- [ ] `data/konventionen.md` · 8.3k · auch: rename
- [ ] `data/mappings.md` · 14.9k · auch: rename
- [ ] `data/modelle.md` · 9.5k · auch: rename
- [ ] `data/standards.md` · 21.3k · auch: rename

### `data/contacts/` · 5

- [ ] `data/contacts/description.md` · 2.2k
- [ ] `data/contacts/examples.md` · 1.9k
- [ ] `data/contacts/index.md` · 1.3k
- [ ] `data/contacts/standards.md` · 2.4k · auch: rename
- [ ] `data/contacts/technical.md` · 2.4k

### `data/contacts/jscontact/` · 2

- [ ] `data/contacts/jscontact/beschreibung.md` · 4.1k · auch: rename
- [ ] `data/contacts/jscontact/speicherung.md` · 3.0k · auch: rename

### `data/events/` · 5

- [ ] `data/events/description.md` · 1.6k
- [ ] `data/events/examples.md` · 2.4k
- [ ] `data/events/index.md` · 1.3k
- [ ] `data/events/standards.md` · 2.8k · auch: rename
- [ ] `data/events/technical.md` · 2.4k

### `data/geodata/` · 5

- [ ] `data/geodata/description.md` · 1.6k
- [ ] `data/geodata/examples.md` · 1.8k
- [ ] `data/geodata/index.md` · 1.1k
- [ ] `data/geodata/standards.md` · 1.7k · auch: rename
- [ ] `data/geodata/technical.md` · 1.9k

### `data/identity/` · 5

- [ ] `data/identity/description.md` · 1.8k
- [ ] `data/identity/examples.md` · 2.3k
- [ ] `data/identity/index.md` · 2.1k
- [ ] `data/identity/standards.md` · 2.5k · auch: rename
- [ ] `data/identity/technical.md` · 2.4k

### `data/login/` · 5

- [ ] `data/login/description.md` · 1.1k
- [ ] `data/login/examples.md` · 2.0k
- [ ] `data/login/index.md` · 1.9k
- [ ] `data/login/standards.md` · 2.1k · auch: rename
- [ ] `data/login/technical.md` · 2.2k

### `data/messages/` · 5

- [ ] `data/messages/description.md` · 1.6k
- [ ] `data/messages/examples.md` · 2.4k
- [ ] `data/messages/index.md` · 1.1k
- [ ] `data/messages/standards.md` · 1.9k · auch: rename
- [ ] `data/messages/technical.md` · 2.1k

### `data/profile/` · 5

- [ ] `data/profile/description.md` · 1.6k
- [ ] `data/profile/examples.md` · 2.2k
- [ ] `data/profile/index.md` · 1.5k
- [ ] `data/profile/standards.md` · 2.2k · auch: rename
- [ ] `data/profile/technical.md` · 2.5k

### `data/projects/` · 5

- [ ] `data/projects/description.md` · 1.5k
- [ ] `data/projects/examples.md` · 1.8k
- [ ] `data/projects/index.md` · 1.9k
- [ ] `data/projects/standards.md` · 1.9k · auch: rename
- [ ] `data/projects/technical.md` · 2.1k

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

### `programs/apps/messenger/masks/` · 1

- [ ] `programs/apps/messenger/masks/index.md` · 4.5k · Plan[~]

### `programs/apps/messenger/masks/discord/` · 3

- [ ] `programs/apps/messenger/masks/discord/api.md` · 7.2k · Plan[~]
- [ ] `programs/apps/messenger/masks/discord/index.md` · 514b · Plan[~]
- [ ] `programs/apps/messenger/masks/discord/shortcuts.md` · 2.0k · Plan[~]

### `programs/apps/messenger/masks/element/` · 3

- [ ] `programs/apps/messenger/masks/element/api.md` · 7.2k · Plan[~]
- [ ] `programs/apps/messenger/masks/element/index.md` · 524b · Plan[~]
- [ ] `programs/apps/messenger/masks/element/shortcuts.md` · 1.9k · Plan[~]

### `programs/apps/messenger/masks/kontact/` · 3

- [ ] `programs/apps/messenger/masks/kontact/api.md` · 5.7k · Plan[~]
- [ ] `programs/apps/messenger/masks/kontact/index.md` · 539b · Plan[~]
- [ ] `programs/apps/messenger/masks/kontact/shortcuts.md` · 3.6k · Plan[~]

### `programs/apps/messenger/masks/mastodon/` · 3

- [ ] `programs/apps/messenger/masks/mastodon/api.md` · 7.1k · Plan[~]
- [ ] `programs/apps/messenger/masks/mastodon/index.md` · 509b · Plan[~]
- [ ] `programs/apps/messenger/masks/mastodon/shortcuts.md` · 2.0k · Plan[~]

### `programs/apps/messenger/masks/outlook/` · 4

- [ ] `programs/apps/messenger/masks/outlook/api.md` · 6.4k · Plan[~]
- [ ] `programs/apps/messenger/masks/outlook/index.md` · 479b · Plan[~]
- [ ] `programs/apps/messenger/masks/outlook/shortcuts.md` · 4.3k · Plan[~]
- [ ] `programs/apps/messenger/masks/outlook/structure.md` · 7.5k · Plan[~]

### `programs/apps/messenger/masks/telegram/` · 3

- [ ] `programs/apps/messenger/masks/telegram/api.md` · 6.9k · Plan[~]
- [ ] `programs/apps/messenger/masks/telegram/index.md` · 518b · Plan[~]
- [ ] `programs/apps/messenger/masks/telegram/shortcuts.md` · 1.7k · Plan[~]

### `programs/apps/messenger/masks/thunderbird/` · 3

- [ ] `programs/apps/messenger/masks/thunderbird/api.md` · 6.4k · Plan[~]
- [ ] `programs/apps/messenger/masks/thunderbird/index.md` · 500b · Plan[~]
- [ ] `programs/apps/messenger/masks/thunderbird/shortcuts.md` · 3.9k · Plan[~]

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

### `programs/apps/projectmanagement/masks/trello/` · 5

- [ ] `programs/apps/projectmanagement/masks/trello/api.md` · 2.5k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/trello/features.md` · 1.3k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/trello/menu.md` · 1.1k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/trello/shortcuts.md` · 959b · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/trello/structure.md` · 2.3k · Plan[~]

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

- [ ] `programs/apps/streaming/masks/restreamer/api.md` · 3.8k · Plan[~]
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

## B. `de/` fehlt – englische Quelle nachziehen – 1 Dateien

### `components/` · 1

- [ ] `components/blinc-cn-components.md` · 101.6k · auch: en_german

## D. `en/` enthält noch deutschen Text – Rest übersetzen – 3 Dateien

### `components/` · 1

- [ ] `components/blinc-cn-components.md` · 101.6k · L25 DE prose in EN: ['ein', 'das', 'einen', 'ist', 'der', 'hält'] · auch: needs_de

### `components/widgets/navigation/pagination/` · 2

- [ ] `components/widgets/navigation/pagination/appearance.md` · 2.5k · L81 German umlaut in EN word → "ändern" · auch: code_german
- [ ] `components/widgets/navigation/pagination/description.md` · 2.1k · L38 German umlaut in EN word → "ändern"

## D2. Deutscher Text in Codebeispielen/Boxen (ADR 0002: Code ist englisch) – 15 Dateien

### `components/widgets/navigation/pagination/` · 1

- [ ] `components/widgets/navigation/pagination/appearance.md` · 2.5k · L29 German word in code → "laden" · Fundzeile: │ [Mehr laden]                            │ · Bezeichner ausserhalb bleiben deutsch (ADR 0002) · auch: en_german

### `components/widgets/overlays/drawer/` · 1

- [ ] `components/widgets/overlays/drawer/usage.md` · 5.4k · L48 German in code/example → "Von" · Fundzeile: <DateInput label="Von" value={from} onChange={setFrom} /> · Bezeichner ausserhalb bleiben deutsch (ADR 0002)

### `components/widgets/overlays/modal/` · 1

- [ ] `components/widgets/overlays/modal/usage.md` · 4.5k · L48 German in code/example → "Hier" · Fundzeile: <p>Hier ist die Info...</p> · Bezeichner ausserhalb bleiben deutsch (ADR 0002)

### `programs/apps/gallery/masks/immich/` · 1

- [ ] `programs/apps/gallery/masks/immich/api.md` · 2.9k · Plan[~] · L52 German in code/example → "der" · Fundzeile: { "q": "Fahrrad in der Stadt", "size": 20 } · Bezeichner ausserhalb bleiben deutsch (ADR 0002)

### `programs/apps/gallery/masks/librephotos/` · 1

- [ ] `programs/apps/gallery/masks/librephotos/api.md` · 2.2k · Plan[~] · L47 German in code/example → "im" · Fundzeile: { "search_text": "Hund im Garten", "user": 3, "time": "all" } · Bezeichner ausserhalb bleiben deutsch (ADR 0002)

### `programs/apps/helpdesk/masks/freshdesk/` · 1

- [ ] `programs/apps/helpdesk/masks/freshdesk/api.md` · 2.4k · Plan[~] · L46 German in code/example → "haben" · Fundzeile: { "body": "Wir haben die Rechnung korrigiert.", "files": [] } · Bezeichner ausserhalb bleiben deutsch (ADR 0002)

### `programs/apps/helpdesk/masks/helpscout/` · 1

- [ ] `programs/apps/helpdesk/masks/helpscout/api.md` · 2.1k · Plan[~] · L43 German in code/example → "die" · Fundzeile: { "type": "reply", "body": "<p>Hallo, anbei die Korrektur.</p>", "assi · Bezeichner ausserhalb bleiben deutsch (ADR 0002)

### `programs/apps/helpdesk/masks/zammad/` · 1

- [ ] `programs/apps/helpdesk/masks/zammad/api.md` · 2.9k · Plan[~] · L48 German in code/example → "der" · Fundzeile: "body": "<p>Hallo, der Techniker kommt Donnerstag.</p>", · Bezeichner ausserhalb bleiben deutsch (ADR 0002)

### `programs/apps/helpdesk/masks/zendesk/` · 1

- [ ] `programs/apps/helpdesk/masks/zendesk/api.md` · 3.0k · Plan[~] · L51 German in code/example → "kein" · Fundzeile: "comment": { "body": "Seit 09:00 kein Druck.", "public": true }, · Bezeichner ausserhalb bleiben deutsch (ADR 0002)

### `programs/apps/maps/masks/leaflet/` · 1

- [ ] `programs/apps/maps/masks/leaflet/api.md` · 1.8k · Plan[~] · L37 German word in code → "beschreibung" · Fundzeile: onEachFeature: (f, l) => l.bindPopup(f.properties.beschreibung) · Bezeichner ausserhalb bleiben deutsch (ADR 0002)

### `programs/apps/maps/masks/maplibre/` · 1

- [ ] `programs/apps/maps/masks/maplibre/api.md` · 2.0k · Plan[~] · L39 German word in code → "eigener" · Fundzeile: // Polling/eigener Update-Kanal: · Bezeichner ausserhalb bleiben deutsch (ADR 0002)

### `programs/apps/maps/masks/organic-maps/` · 1

- [ ] `programs/apps/maps/masks/organic-maps/api.md` · 1.1k · Plan[~] · L19 German word in code → "öffnen" · Fundzeile: <a href="geo:48.530,9.058?q=48.530,9.058">In Organic Maps öffnen</a> · Bezeichner ausserhalb bleiben deutsch (ADR 0002)

### `programs/apps/maps/masks/osmand/` · 1

- [ ] `programs/apps/maps/masks/osmand/api.md` · 1.7k · Plan[~] · L22 German word in code → "öffnen" · Fundzeile: <a href="geo:48.530,9.058?q=48.530,9.058">In OsmAnd öffnen</a> · Bezeichner ausserhalb bleiben deutsch (ADR 0002)

### `programs/apps/marketing/masks/plausible/` · 1

- [ ] `programs/apps/marketing/masks/plausible/api.md` · 2.0k · Plan[~] · L40 German in code/example → "danke" · Fundzeile: { "name": "Spende", "url": "https://org/danke", · Bezeichner ausserhalb bleiben deutsch (ADR 0002)

### `programs/apps/projectmanagement/masks/asana/` · 1

- [ ] `programs/apps/projectmanagement/masks/asana/api.md` · 2.3k · Plan[~] · L47 German in code/example → "danach" · Fundzeile: "assignee": 9876, "notes": "Rechtsfreigabe danach" } } · Bezeichner ausserhalb bleiben deutsch (ADR 0002)

## F. Form nicht gleich – Struktur abgleichen – 28 Dateien

### `(wurzel)/` · 1

- [ ] `index.md` · 1.2k · Parität: headings 4 vs 5; table rows 0 vs 7

### `components/primitives/fields/color-input/` · 1

- [ ] `components/primitives/fields/color-input/appearance.md` · 2.8k · Parität: table rows 20 vs 25

### `components/primitives/fields/otp-input/` · 1

- [ ] `components/primitives/fields/otp-input/appearance.md` · 1.4k · Parität: links en-only=['../../../interactions/gestures/device/shake'] de-only=['../../../interactions/animations/feedback/shake']

### `data/` · 1

- [ ] `data/index.md` · 3.8k · Parität: headings 8 vs 9; table rows 38 vs 50

### `interactions/animations/` · 1

- [ ] `interactions/animations/index.md` · 5.2k · Parität: headings 15 vs 18; table rows 63 vs 137

### `interactions/gestures/` · 1

- [ ] `interactions/gestures/index.md` · 8.1k · Parität: table rows 91 vs 92; links en-only=['animations/index.md'] de-only=['../data/konventionen.md', 'animations']

### `interactions/gestures/device/` · 1

- [ ] `interactions/gestures/device/index.md` · 1.2k · Parität: links en-only=['shake/description.md'] de-only=['../animations/feedback/shake/description.md']

### `interactions/gestures/transform/` · 1

- [ ] `interactions/gestures/transform/index.md` · 1.1k · Parität: links en-only=['rotate/description.md'] de-only=['../animations/transition/rotate/description.md']

### `programs/apps/calendar/` · 1

- [ ] `programs/apps/calendar/index.md` · 2.7k · Plan[~] · Parität: headings 10 vs 12; links en-only=[] de-only=['../../data/api.md', '../platform/desktop/masks/index.md', 'masks/davical/index.md']

### `programs/apps/contact/` · 1

- [ ] `programs/apps/contact/index.md` · 2.6k · Plan[~] · Parität: headings 10 vs 12; links en-only=[] de-only=['../../data/api.md', '../platform/desktop/masks/index.md', 'masks/gnome-contacts/index.md']

### `programs/apps/helpdesk/` · 1

- [ ] `programs/apps/helpdesk/index.md` · 2.5k · Plan[~] · Parität: headings 10 vs 12; links en-only=[] de-only=['../../data/api.md', '../platform/desktop/masks/index.md', 'masks/freshdesk/index.md']

### `programs/apps/maps/` · 1

- [ ] `programs/apps/maps/index.md` · 2.4k · Plan[~] · Parität: headings 10 vs 12; links en-only=[] de-only=['../../data/api.md', '../platform/desktop/masks/index.md', 'masks/index.md']

### `programs/apps/marketing/` · 1

- [ ] `programs/apps/marketing/index.md` · 2.9k · Plan[~] · Parität: headings 10 vs 12; links en-only=[] de-only=['../../data/api.md', '../platform/desktop/masks/index.md', 'masks/google-analytics/index.md']

### `programs/apps/messenger/masks/discord/` · 1

- [ ] `programs/apps/messenger/masks/discord/features.md` · 3.4k · Plan[~] · Parität: table rows 10 vs 0; links en-only=[] de-only=['shortcuts.md']

### `programs/apps/messenger/masks/element/` · 1

- [ ] `programs/apps/messenger/masks/element/features.md` · 3.1k · Plan[~] · Parität: table rows 10 vs 0; links en-only=[] de-only=['shortcuts.md']

### `programs/apps/messenger/masks/kontact/` · 1

- [ ] `programs/apps/messenger/masks/kontact/features.md` · 3.6k · Plan[~] · Parität: table rows 15 vs 0; links en-only=[] de-only=['shortcuts.md']

### `programs/apps/messenger/masks/mastodon/` · 1

- [ ] `programs/apps/messenger/masks/mastodon/features.md` · 3.3k · Plan[~] · Parität: table rows 8 vs 0; links en-only=[] de-only=['shortcuts.md']

### `programs/apps/messenger/masks/outlook/` · 1

- [ ] `programs/apps/messenger/masks/outlook/features.md` · 2.3k · Plan[~] · Parität: table rows 14 vs 0; links en-only=[] de-only=['shortcuts.md']

### `programs/apps/messenger/masks/telegram/` · 1

- [ ] `programs/apps/messenger/masks/telegram/features.md` · 3.5k · Plan[~] · Parität: table rows 9 vs 0; links en-only=[] de-only=['shortcuts.md']

### `programs/apps/messenger/masks/thunderbird/` · 1

- [ ] `programs/apps/messenger/masks/thunderbird/features.md` · 3.4k · Plan[~] · Parität: table rows 13 vs 0; links en-only=[] de-only=['shortcuts.md']

### `programs/apps/projectmanagement/` · 1

- [ ] `programs/apps/projectmanagement/index.md` · 2.7k · Plan[~] · Parität: headings 10 vs 12; links en-only=[] de-only=['../../data/api.md', '../platform/desktop/masks/index.md', 'masks/asana/index.md']

### `programs/apps/whiteboards/` · 1

- [ ] `programs/apps/whiteboards/index.md` · 2.5k · Plan[~] · Parität: headings 10 vs 12; links en-only=[] de-only=['../../data/api.md', '../platform/desktop/masks/index.md', 'masks/drawio/index.md']

### `programs/apps/wiki/masks/` · 1

- [ ] `programs/apps/wiki/masks/index.md` · 2.9k · Plan[~] · Parität: headings 10 vs 13; links en-only=['programs/apps/wiki/masks/confluence/index.md', 'programs/apps/wiki/masks/mediawiki/index.md', 'programs/apps/wiki/masks/notion/index.md'] de-only=['confluence/index.md', 'mediawiki/index.md', 'notion/index.md']

### `programs/platform/desktop/` · 1

- [ ] `programs/platform/desktop/index.md` · 2.7k · Plan[~] · Parität: headings 10 vs 13; links en-only=[] de-only=['masks/index.md']

### `programs/suites/crm/` · 1

- [ ] `programs/suites/crm/index.md` · 959b · Plan[~] · Parität: headings 5 vs 12; links en-only=['programs/suites/crm/masks'] de-only=['../../data/api.md', '../apps/helpdesk', '../apps/marketing']

### `programs/suites/democracy/` · 1

- [ ] `programs/suites/democracy/index.md` · 2.5k · Plan[~] · Parität: headings 10 vs 12; links en-only=[] de-only=['../../data/api.md', '../apps/wiki/masks/index.md', '../platform/desktop/masks/index.md']

### `programs/suites/erp/` · 1

- [ ] `programs/suites/erp/index.md` · 2.5k · Plan[~] · Parität: headings 10 vs 12; links en-only=[] de-only=['../../data/api.md', '../apps/wiki/masks/index.md', '../platform/desktop/masks/index.md']

### `programs/suites/workflows/` · 1

- [ ] `programs/suites/workflows/index.md` · 2.5k · Plan[~] · Parität: headings 10 vs 12; links en-only=[] de-only=['../../data/api.md', '../apps/wiki/masks/index.md', '../platform/desktop/masks/index.md']

## G. Deutscher Dateiname – Pfad englisch machen (ADR 0002) – 17 Dateien

### `data/` · 7

- [ ] `data/anforderungen.md` · 7.1k · Zielpfad englisch, dann Links + `mkdocs.yml` nachziehen · auch: needs_en
- [ ] `data/felder.md` · 10.0k · Zielpfad englisch, dann Links + `mkdocs.yml` nachziehen · auch: needs_en
- [ ] `data/formate.md` · 5.2k · Zielpfad englisch, dann Links + `mkdocs.yml` nachziehen · auch: needs_en
- [ ] `data/konventionen.md` · 8.3k · Zielpfad englisch, dann Links + `mkdocs.yml` nachziehen · auch: needs_en
- [ ] `data/mappings.md` · 14.9k · Zielpfad englisch, dann Links + `mkdocs.yml` nachziehen · auch: needs_en
- [ ] `data/modelle.md` · 9.5k · Zielpfad englisch, dann Links + `mkdocs.yml` nachziehen · auch: needs_en
- [ ] `data/standards.md` · 21.3k · Zielpfad englisch, dann Links + `mkdocs.yml` nachziehen · auch: needs_en

### `data/contacts/` · 1

- [ ] `data/contacts/standards.md` · 2.4k · Zielpfad englisch, dann Links + `mkdocs.yml` nachziehen · auch: needs_en

### `data/contacts/jscontact/` · 2

- [ ] `data/contacts/jscontact/beschreibung.md` · 4.1k · Zielpfad englisch, dann Links + `mkdocs.yml` nachziehen · auch: needs_en
- [ ] `data/contacts/jscontact/speicherung.md` · 3.0k · Zielpfad englisch, dann Links + `mkdocs.yml` nachziehen · auch: needs_en

### `data/events/` · 1

- [ ] `data/events/standards.md` · 2.8k · Zielpfad englisch, dann Links + `mkdocs.yml` nachziehen · auch: needs_en

### `data/geodata/` · 1

- [ ] `data/geodata/standards.md` · 1.7k · Zielpfad englisch, dann Links + `mkdocs.yml` nachziehen · auch: needs_en

### `data/identity/` · 1

- [ ] `data/identity/standards.md` · 2.5k · Zielpfad englisch, dann Links + `mkdocs.yml` nachziehen · auch: needs_en

### `data/login/` · 1

- [ ] `data/login/standards.md` · 2.1k · Zielpfad englisch, dann Links + `mkdocs.yml` nachziehen · auch: needs_en

### `data/messages/` · 1

- [ ] `data/messages/standards.md` · 1.9k · Zielpfad englisch, dann Links + `mkdocs.yml` nachziehen · auch: needs_en

### `data/profile/` · 1

- [ ] `data/profile/standards.md` · 2.2k · Zielpfad englisch, dann Links + `mkdocs.yml` nachziehen · auch: needs_en

### `data/projects/` · 1

- [ ] `data/projects/standards.md` · 1.9k · Zielpfad englisch, dann Links + `mkdocs.yml` nachziehen · auch: needs_en

## H. Beide Seiten da, kein Befund – lesen und bestätigen – 757 Dateien

### `components/` · 1

- [ ] `components/index.md` · 6.1k

### `components/primitives/` · 1

- [ ] `components/primitives/index.md` · 2.4k

### `components/primitives/actions/` · 1

- [ ] `components/primitives/actions/index.md` · 1.1k

### `components/primitives/actions/button/` · 4

- [ ] `components/primitives/actions/button/appearance.md` · 2.3k
- [ ] `components/primitives/actions/button/attributes.md` · 1.7k
- [ ] `components/primitives/actions/button/description.md` · 2.3k
- [ ] `components/primitives/actions/button/usage.md` · 1.2k

### `components/primitives/actions/button-group/` · 4

- [ ] `components/primitives/actions/button-group/appearance.md` · 2.0k
- [ ] `components/primitives/actions/button-group/attributes.md` · 1.5k
- [ ] `components/primitives/actions/button-group/description.md` · 2.1k
- [ ] `components/primitives/actions/button-group/usage.md` · 1.3k

### `components/primitives/actions/floating-action-button/` · 4

- [ ] `components/primitives/actions/floating-action-button/appearance.md` · 2.4k
- [ ] `components/primitives/actions/floating-action-button/attributes.md` · 1.5k
- [ ] `components/primitives/actions/floating-action-button/description.md` · 1.9k
- [ ] `components/primitives/actions/floating-action-button/usage.md` · 1.6k

### `components/primitives/basics/` · 2

- [ ] `components/primitives/basics/base.md` · 5.9k
- [ ] `components/primitives/basics/index.md` · 1.3k

### `components/primitives/basics/kbd/` · 4

- [ ] `components/primitives/basics/kbd/appearance.md` · 1.1k
- [ ] `components/primitives/basics/kbd/attributes.md` · 919b
- [ ] `components/primitives/basics/kbd/description.md` · 1.7k
- [ ] `components/primitives/basics/kbd/usage.md` · 936b

### `components/primitives/basics/label/` · 4

- [ ] `components/primitives/basics/label/appearance.md` · 1.3k
- [ ] `components/primitives/basics/label/attributes.md` · 1007b
- [ ] `components/primitives/basics/label/description.md` · 1.8k
- [ ] `components/primitives/basics/label/usage.md` · 893b

### `components/primitives/basics/link/` · 4

- [ ] `components/primitives/basics/link/appearance.md` · 1.2k
- [ ] `components/primitives/basics/link/attributes.md` · 1.4k
- [ ] `components/primitives/basics/link/description.md` · 1.9k
- [ ] `components/primitives/basics/link/usage.md` · 940b

### `components/primitives/basics/separator/` · 4

- [ ] `components/primitives/basics/separator/appearance.md` · 1.4k
- [ ] `components/primitives/basics/separator/attributes.md` · 1.1k
- [ ] `components/primitives/basics/separator/description.md` · 2.0k
- [ ] `components/primitives/basics/separator/usage.md` · 1.0k

### `components/primitives/feedback/` · 1

- [ ] `components/primitives/feedback/index.md` · 1.8k

### `components/primitives/feedback/alert/` · 4

- [ ] `components/primitives/feedback/alert/appearance.md` · 2.6k
- [ ] `components/primitives/feedback/alert/attributes.md` · 1.5k
- [ ] `components/primitives/feedback/alert/description.md` · 1.6k
- [ ] `components/primitives/feedback/alert/usage.md` · 895b

### `components/primitives/feedback/badge/` · 4

- [ ] `components/primitives/feedback/badge/appearance.md` · 1.7k
- [ ] `components/primitives/feedback/badge/attributes.md` · 1.3k
- [ ] `components/primitives/feedback/badge/description.md` · 2.0k
- [ ] `components/primitives/feedback/badge/usage.md` · 1.0k

### `components/primitives/feedback/empty-state/` · 4

- [ ] `components/primitives/feedback/empty-state/appearance.md` · 1.6k
- [ ] `components/primitives/feedback/empty-state/attributes.md` · 1.5k
- [ ] `components/primitives/feedback/empty-state/description.md` · 1.7k
- [ ] `components/primitives/feedback/empty-state/usage.md` · 1004b

### `components/primitives/feedback/progress/` · 4

- [ ] `components/primitives/feedback/progress/appearance.md` · 1.6k
- [ ] `components/primitives/feedback/progress/attributes.md` · 1.4k
- [ ] `components/primitives/feedback/progress/description.md` · 1.8k
- [ ] `components/primitives/feedback/progress/usage.md` · 1.0k

### `components/primitives/feedback/skeleton/` · 4

- [ ] `components/primitives/feedback/skeleton/appearance.md` · 1.6k
- [ ] `components/primitives/feedback/skeleton/attributes.md` · 1.1k
- [ ] `components/primitives/feedback/skeleton/description.md` · 2.2k
- [ ] `components/primitives/feedback/skeleton/usage.md` · 1012b

### `components/primitives/feedback/spinner/` · 4

- [ ] `components/primitives/feedback/spinner/appearance.md` · 1.1k
- [ ] `components/primitives/feedback/spinner/attributes.md` · 963b
- [ ] `components/primitives/feedback/spinner/description.md` · 1.8k
- [ ] `components/primitives/feedback/spinner/usage.md` · 944b

### `components/primitives/feedback/toast/` · 4

- [ ] `components/primitives/feedback/toast/appearance.md` · 2.6k
- [ ] `components/primitives/feedback/toast/attributes.md` · 1.6k
- [ ] `components/primitives/feedback/toast/description.md` · 2.2k
- [ ] `components/primitives/feedback/toast/usage.md` · 633b

### `components/primitives/fields/` · 1

- [ ] `components/primitives/fields/index.md` · 3.9k

### `components/primitives/fields/checkbox/` · 4

- [ ] `components/primitives/fields/checkbox/appearance.md` · 1.9k
- [ ] `components/primitives/fields/checkbox/attributes.md` · 1.0k
- [ ] `components/primitives/fields/checkbox/description.md` · 1.6k
- [ ] `components/primitives/fields/checkbox/usage.md` · 2.8k

### `components/primitives/fields/color-input/` · 3

- [ ] `components/primitives/fields/color-input/attributes.md` · 1.3k
- [ ] `components/primitives/fields/color-input/description.md` · 1.7k
- [ ] `components/primitives/fields/color-input/usage.md` · 656b

### `components/primitives/fields/combobox/` · 4

- [ ] `components/primitives/fields/combobox/appearance.md` · 3.3k
- [ ] `components/primitives/fields/combobox/attributes.md` · 1.2k
- [ ] `components/primitives/fields/combobox/description.md` · 2.0k
- [ ] `components/primitives/fields/combobox/usage.md` · 615b

### `components/primitives/fields/date-input/` · 4

- [ ] `components/primitives/fields/date-input/appearance.md` · 2.8k
- [ ] `components/primitives/fields/date-input/attributes.md` · 1.7k
- [ ] `components/primitives/fields/date-input/description.md` · 2.1k
- [ ] `components/primitives/fields/date-input/usage.md` · 690b

### `components/primitives/fields/field/` · 4

- [ ] `components/primitives/fields/field/appearance.md` · 1.8k
- [ ] `components/primitives/fields/field/attributes.md` · 1.6k
- [ ] `components/primitives/fields/field/description.md` · 2.2k
- [ ] `components/primitives/fields/field/usage.md` · 1.1k

### `components/primitives/fields/input-group/` · 4

- [ ] `components/primitives/fields/input-group/appearance.md` · 2.6k
- [ ] `components/primitives/fields/input-group/attributes.md` · 1.7k
- [ ] `components/primitives/fields/input-group/description.md` · 2.8k
- [ ] `components/primitives/fields/input-group/usage.md` · 1.5k

### `components/primitives/fields/mention-input/` · 4

- [ ] `components/primitives/fields/mention-input/appearance.md` · 2.5k
- [ ] `components/primitives/fields/mention-input/attributes.md` · 1.2k
- [ ] `components/primitives/fields/mention-input/description.md` · 1.8k
- [ ] `components/primitives/fields/mention-input/usage.md` · 618b

### `components/primitives/fields/number-input/` · 4

- [ ] `components/primitives/fields/number-input/appearance.md` · 2.4k
- [ ] `components/primitives/fields/number-input/attributes.md` · 1.2k
- [ ] `components/primitives/fields/number-input/description.md` · 1.8k
- [ ] `components/primitives/fields/number-input/usage.md` · 536b

### `components/primitives/fields/otp-input/` · 3

- [ ] `components/primitives/fields/otp-input/attributes.md` · 1.5k
- [ ] `components/primitives/fields/otp-input/description.md` · 1.7k
- [ ] `components/primitives/fields/otp-input/usage.md` · 857b

### `components/primitives/fields/radio-group/` · 4

- [ ] `components/primitives/fields/radio-group/appearance.md` · 2.0k
- [ ] `components/primitives/fields/radio-group/attributes.md` · 1.1k
- [ ] `components/primitives/fields/radio-group/description.md` · 1.6k
- [ ] `components/primitives/fields/radio-group/usage.md` · 538b

### `components/primitives/fields/rating/` · 4

- [ ] `components/primitives/fields/rating/appearance.md` · 2.5k
- [ ] `components/primitives/fields/rating/attributes.md` · 1.1k
- [ ] `components/primitives/fields/rating/description.md` · 1.7k
- [ ] `components/primitives/fields/rating/usage.md` · 503b

### `components/primitives/fields/search-field/` · 4

- [ ] `components/primitives/fields/search-field/appearance.md` · 2.3k
- [ ] `components/primitives/fields/search-field/attributes.md` · 1.5k
- [ ] `components/primitives/fields/search-field/description.md` · 2.1k
- [ ] `components/primitives/fields/search-field/usage.md` · 3.5k

### `components/primitives/fields/select/` · 4

- [ ] `components/primitives/fields/select/appearance.md` · 2.1k
- [ ] `components/primitives/fields/select/attributes.md` · 1.5k
- [ ] `components/primitives/fields/select/description.md` · 1.9k
- [ ] `components/primitives/fields/select/usage.md` · 5.3k

### `components/primitives/fields/slider/` · 4

- [ ] `components/primitives/fields/slider/appearance.md` · 2.8k
- [ ] `components/primitives/fields/slider/attributes.md` · 1.3k
- [ ] `components/primitives/fields/slider/description.md` · 1.9k
- [ ] `components/primitives/fields/slider/usage.md` · 478b

### `components/primitives/fields/switch/` · 4

- [ ] `components/primitives/fields/switch/appearance.md` · 2.5k
- [ ] `components/primitives/fields/switch/attributes.md` · 1.0k
- [ ] `components/primitives/fields/switch/description.md` · 1.6k
- [ ] `components/primitives/fields/switch/usage.md` · 575b

### `components/primitives/fields/tags-input/` · 4

- [ ] `components/primitives/fields/tags-input/appearance.md` · 2.7k
- [ ] `components/primitives/fields/tags-input/attributes.md` · 1.5k
- [ ] `components/primitives/fields/tags-input/description.md` · 1.7k
- [ ] `components/primitives/fields/tags-input/usage.md` · 602b

### `components/primitives/fields/text-input/` · 4

- [ ] `components/primitives/fields/text-input/appearance.md` · 3.3k
- [ ] `components/primitives/fields/text-input/attributes.md` · 2.0k
- [ ] `components/primitives/fields/text-input/description.md` · 2.4k
- [ ] `components/primitives/fields/text-input/usage.md` · 3.4k

### `components/primitives/fields/textarea/` · 4

- [ ] `components/primitives/fields/textarea/appearance.md` · 2.8k
- [ ] `components/primitives/fields/textarea/attributes.md` · 1.4k
- [ ] `components/primitives/fields/textarea/description.md` · 1.9k
- [ ] `components/primitives/fields/textarea/usage.md` · 4.5k

### `components/primitives/media/` · 1

- [ ] `components/primitives/media/index.md` · 795b

### `components/primitives/media/icon/` · 4

- [ ] `components/primitives/media/icon/appearance.md` · 2.7k
- [ ] `components/primitives/media/icon/attributes.md` · 1.5k
- [ ] `components/primitives/media/icon/description.md` · 3.1k
- [ ] `components/primitives/media/icon/usage.md` · 3.5k

### `components/primitives/media/image/` · 4

- [ ] `components/primitives/media/image/appearance.md` · 2.8k
- [ ] `components/primitives/media/image/attributes.md` · 2.5k
- [ ] `components/primitives/media/image/description.md` · 3.5k
- [ ] `components/primitives/media/image/usage.md` · 7.3k

### `components/widgets/` · 1

- [ ] `components/widgets/index.md` · 3.2k

### `components/widgets/containers/` · 1

- [ ] `components/widgets/containers/index.md` · 1.7k

### `components/widgets/containers/accordion/` · 4

- [ ] `components/widgets/containers/accordion/appearance.md` · 2.5k
- [ ] `components/widgets/containers/accordion/attributes.md` · 1.3k
- [ ] `components/widgets/containers/accordion/description.md` · 2.6k
- [ ] `components/widgets/containers/accordion/usage.md` · 663b

### `components/widgets/containers/card/` · 4

- [ ] `components/widgets/containers/card/appearance.md` · 1.7k
- [ ] `components/widgets/containers/card/attributes.md` · 1.3k
- [ ] `components/widgets/containers/card/description.md` · 2.3k
- [ ] `components/widgets/containers/card/usage.md` · 830b

### `components/widgets/containers/panel/` · 4

- [ ] `components/widgets/containers/panel/appearance.md` · 2.2k
- [ ] `components/widgets/containers/panel/attributes.md` · 1.1k
- [ ] `components/widgets/containers/panel/description.md` · 2.8k
- [ ] `components/widgets/containers/panel/usage.md` · 642b

### `components/widgets/containers/scroll-area/` · 4

- [ ] `components/widgets/containers/scroll-area/appearance.md` · 1.6k
- [ ] `components/widgets/containers/scroll-area/attributes.md` · 1.5k
- [ ] `components/widgets/containers/scroll-area/description.md` · 1.8k
- [ ] `components/widgets/containers/scroll-area/usage.md` · 955b

### `components/widgets/containers/split-view/` · 4

- [ ] `components/widgets/containers/split-view/appearance.md` · 1.4k
- [ ] `components/widgets/containers/split-view/attributes.md` · 1.3k
- [ ] `components/widgets/containers/split-view/description.md` · 2.4k
- [ ] `components/widgets/containers/split-view/usage.md` · 633b

### `components/widgets/containers/wizard/` · 4

- [ ] `components/widgets/containers/wizard/appearance.md` · 2.2k
- [ ] `components/widgets/containers/wizard/attributes.md` · 1.7k
- [ ] `components/widgets/containers/wizard/description.md` · 2.7k
- [ ] `components/widgets/containers/wizard/usage.md` · 709b

### `components/widgets/data/` · 1

- [ ] `components/widgets/data/index.md` · 2.7k

### `components/widgets/data/avatar/` · 4

- [ ] `components/widgets/data/avatar/appearance.md` · 2.0k
- [ ] `components/widgets/data/avatar/attributes.md` · 1.5k
- [ ] `components/widgets/data/avatar/description.md` · 2.5k
- [ ] `components/widgets/data/avatar/usage.md` · 4.9k

### `components/widgets/data/calendar-view/` · 4

- [ ] `components/widgets/data/calendar-view/appearance.md` · 1.9k
- [ ] `components/widgets/data/calendar-view/attributes.md` · 1.3k
- [ ] `components/widgets/data/calendar-view/description.md` · 2.3k
- [ ] `components/widgets/data/calendar-view/usage.md` · 623b

### `components/widgets/data/chart/` · 4

- [ ] `components/widgets/data/chart/appearance.md` · 3.2k
- [ ] `components/widgets/data/chart/attributes.md` · 1.5k
- [ ] `components/widgets/data/chart/description.md` · 2.1k
- [ ] `components/widgets/data/chart/usage.md` · 540b

### `components/widgets/data/description-list/` · 4

- [ ] `components/widgets/data/description-list/appearance.md` · 1.3k
- [ ] `components/widgets/data/description-list/attributes.md` · 1.5k
- [ ] `components/widgets/data/description-list/description.md` · 1.8k
- [ ] `components/widgets/data/description-list/usage.md` · 841b

### `components/widgets/data/grid-view/` · 4

- [ ] `components/widgets/data/grid-view/appearance.md` · 1.9k
- [ ] `components/widgets/data/grid-view/attributes.md` · 1.4k
- [ ] `components/widgets/data/grid-view/description.md` · 2.0k
- [ ] `components/widgets/data/grid-view/usage.md` · 567b

### `components/widgets/data/list-view/` · 4

- [ ] `components/widgets/data/list-view/appearance.md` · 2.3k
- [ ] `components/widgets/data/list-view/attributes.md` · 1.5k
- [ ] `components/widgets/data/list-view/description.md` · 2.1k
- [ ] `components/widgets/data/list-view/usage.md` · 3.0k

### `components/widgets/data/repeater/` · 4

- [ ] `components/widgets/data/repeater/appearance.md` · 2.1k
- [ ] `components/widgets/data/repeater/attributes.md` · 1.4k
- [ ] `components/widgets/data/repeater/description.md` · 1.8k
- [ ] `components/widgets/data/repeater/usage.md` · 512b

### `components/widgets/data/table/` · 4

- [ ] `components/widgets/data/table/appearance.md` · 2.6k
- [ ] `components/widgets/data/table/attributes.md` · 1.9k
- [ ] `components/widgets/data/table/description.md` · 2.2k
- [ ] `components/widgets/data/table/usage.md` · 4.4k

### `components/widgets/data/table-of-contents/` · 4

- [ ] `components/widgets/data/table-of-contents/appearance.md` · 2.5k
- [ ] `components/widgets/data/table-of-contents/attributes.md` · 1.3k
- [ ] `components/widgets/data/table-of-contents/description.md` · 2.7k
- [ ] `components/widgets/data/table-of-contents/usage.md` · 594b

### `components/widgets/data/timeline/` · 4

- [ ] `components/widgets/data/timeline/appearance.md` · 2.0k
- [ ] `components/widgets/data/timeline/attributes.md` · 1.0k
- [ ] `components/widgets/data/timeline/description.md` · 2.9k
- [ ] `components/widgets/data/timeline/usage.md` · 549b

### `components/widgets/data/tree-view/` · 4

- [ ] `components/widgets/data/tree-view/appearance.md` · 2.2k
- [ ] `components/widgets/data/tree-view/attributes.md` · 1.6k
- [ ] `components/widgets/data/tree-view/description.md` · 2.0k
- [ ] `components/widgets/data/tree-view/usage.md` · 4.5k

### `components/widgets/fields/` · 1

- [ ] `components/widgets/fields/index.md` · 1.5k

### `components/widgets/fields/date-picker/` · 4

- [ ] `components/widgets/fields/date-picker/appearance.md` · 3.5k
- [ ] `components/widgets/fields/date-picker/attributes.md` · 4.8k
- [ ] `components/widgets/fields/date-picker/description.md` · 5.3k
- [ ] `components/widgets/fields/date-picker/usage.md` · 3.9k

### `components/widgets/fields/emoji-picker/` · 4

- [ ] `components/widgets/fields/emoji-picker/appearance.md` · 2.8k
- [ ] `components/widgets/fields/emoji-picker/attributes.md` · 1.3k
- [ ] `components/widgets/fields/emoji-picker/description.md` · 1.9k
- [ ] `components/widgets/fields/emoji-picker/usage.md` · 613b

### `components/widgets/fields/file-upload/` · 4

- [ ] `components/widgets/fields/file-upload/appearance.md` · 2.7k
- [ ] `components/widgets/fields/file-upload/attributes.md` · 1.3k
- [ ] `components/widgets/fields/file-upload/description.md` · 1.8k
- [ ] `components/widgets/fields/file-upload/usage.md` · 558b

### `components/widgets/fields/range-calendar/` · 4

- [ ] `components/widgets/fields/range-calendar/appearance.md` · 1.8k
- [ ] `components/widgets/fields/range-calendar/attributes.md` · 1.4k
- [ ] `components/widgets/fields/range-calendar/description.md` · 1.7k
- [ ] `components/widgets/fields/range-calendar/usage.md` · 832b

### `components/widgets/fields/time-picker/` · 4

- [ ] `components/widgets/fields/time-picker/appearance.md` · 1.3k
- [ ] `components/widgets/fields/time-picker/attributes.md` · 1.3k
- [ ] `components/widgets/fields/time-picker/description.md` · 1.6k
- [ ] `components/widgets/fields/time-picker/usage.md` · 855b

### `components/widgets/media/` · 1

- [ ] `components/widgets/media/index.md` · 1.4k

### `components/widgets/media/audio/` · 4

- [ ] `components/widgets/media/audio/appearance.md` · 2.3k
- [ ] `components/widgets/media/audio/attributes.md` · 2.1k
- [ ] `components/widgets/media/audio/description.md` · 2.7k
- [ ] `components/widgets/media/audio/usage.md` · 7.4k

### `components/widgets/media/carousel/` · 4

- [ ] `components/widgets/media/carousel/appearance.md` · 1.8k
- [ ] `components/widgets/media/carousel/attributes.md` · 1.3k
- [ ] `components/widgets/media/carousel/description.md` · 2.0k
- [ ] `components/widgets/media/carousel/usage.md` · 616b

### `components/widgets/media/gallery/` · 4

- [ ] `components/widgets/media/gallery/appearance.md` · 3.7k
- [ ] `components/widgets/media/gallery/attributes.md` · 2.3k
- [ ] `components/widgets/media/gallery/description.md` · 3.0k
- [ ] `components/widgets/media/gallery/usage.md` · 8.4k

### `components/widgets/media/media-player/` · 4

- [ ] `components/widgets/media/media-player/appearance.md` · 2.5k
- [ ] `components/widgets/media/media-player/attributes.md` · 1.5k
- [ ] `components/widgets/media/media-player/description.md` · 2.0k
- [ ] `components/widgets/media/media-player/usage.md` · 515b

### `components/widgets/media/video/` · 4

- [ ] `components/widgets/media/video/appearance.md` · 4.0k
- [ ] `components/widgets/media/video/attributes.md` · 2.7k
- [ ] `components/widgets/media/video/description.md` · 2.8k
- [ ] `components/widgets/media/video/usage.md` · 6.9k

### `components/widgets/navigation/` · 1

- [ ] `components/widgets/navigation/index.md` · 2.5k

### `components/widgets/navigation/bottom-navigation/` · 4

- [ ] `components/widgets/navigation/bottom-navigation/appearance.md` · 2.8k
- [ ] `components/widgets/navigation/bottom-navigation/attributes.md` · 1.4k
- [ ] `components/widgets/navigation/bottom-navigation/description.md` · 2.1k
- [ ] `components/widgets/navigation/bottom-navigation/usage.md` · 2.8k

### `components/widgets/navigation/breadcrumb/` · 4

- [ ] `components/widgets/navigation/breadcrumb/appearance.md` · 2.2k
- [ ] `components/widgets/navigation/breadcrumb/attributes.md` · 1.6k
- [ ] `components/widgets/navigation/breadcrumb/description.md` · 1.9k
- [ ] `components/widgets/navigation/breadcrumb/usage.md` · 3.9k

### `components/widgets/navigation/command/` · 4

- [ ] `components/widgets/navigation/command/appearance.md` · 1.9k
- [ ] `components/widgets/navigation/command/attributes.md` · 1.5k
- [ ] `components/widgets/navigation/command/description.md` · 1.8k
- [ ] `components/widgets/navigation/command/usage.md` · 849b

### `components/widgets/navigation/language-switcher/` · 4

- [ ] `components/widgets/navigation/language-switcher/appearance.md` · 2.3k
- [ ] `components/widgets/navigation/language-switcher/attributes.md` · 1.5k
- [ ] `components/widgets/navigation/language-switcher/description.md` · 2.5k
- [ ] `components/widgets/navigation/language-switcher/usage.md` · 4.0k

### `components/widgets/navigation/menu/` · 4

- [ ] `components/widgets/navigation/menu/appearance.md` · 2.0k
- [ ] `components/widgets/navigation/menu/attributes.md` · 2.0k
- [ ] `components/widgets/navigation/menu/description.md` · 2.5k
- [ ] `components/widgets/navigation/menu/usage.md` · 3.1k

### `components/widgets/navigation/pagination/` · 2

- [ ] `components/widgets/navigation/pagination/attributes.md` · 1.3k
- [ ] `components/widgets/navigation/pagination/usage.md` · 3.8k

### `components/widgets/navigation/radial-menu/` · 4

- [ ] `components/widgets/navigation/radial-menu/appearance.md` · 8.2k
- [ ] `components/widgets/navigation/radial-menu/attributes.md` · 4.0k
- [ ] `components/widgets/navigation/radial-menu/description.md` · 7.0k
- [ ] `components/widgets/navigation/radial-menu/usage.md` · 3.6k

### `components/widgets/navigation/sidebar/` · 4

- [ ] `components/widgets/navigation/sidebar/appearance.md` · 2.3k
- [ ] `components/widgets/navigation/sidebar/attributes.md` · 1.5k
- [ ] `components/widgets/navigation/sidebar/description.md` · 2.7k
- [ ] `components/widgets/navigation/sidebar/usage.md` · 4.9k

### `components/widgets/navigation/tabs/` · 4

- [ ] `components/widgets/navigation/tabs/appearance.md` · 3.7k
- [ ] `components/widgets/navigation/tabs/attributes.md` · 1.5k
- [ ] `components/widgets/navigation/tabs/description.md` · 2.0k
- [ ] `components/widgets/navigation/tabs/usage.md` · 4.1k

### `components/widgets/navigation/toolbar/` · 4

- [ ] `components/widgets/navigation/toolbar/appearance.md` · 3.3k
- [ ] `components/widgets/navigation/toolbar/attributes.md` · 2.2k
- [ ] `components/widgets/navigation/toolbar/description.md` · 2.9k
- [ ] `components/widgets/navigation/toolbar/usage.md` · 3.1k

### `components/widgets/overlays/` · 1

- [ ] `components/widgets/overlays/index.md` · 2.0k

### `components/widgets/overlays/alert-dialog/` · 4

- [ ] `components/widgets/overlays/alert-dialog/appearance.md` · 1.6k
- [ ] `components/widgets/overlays/alert-dialog/attributes.md` · 1.6k
- [ ] `components/widgets/overlays/alert-dialog/description.md` · 1.9k
- [ ] `components/widgets/overlays/alert-dialog/usage.md` · 1.0k

### `components/widgets/overlays/context-menu/` · 4

- [ ] `components/widgets/overlays/context-menu/appearance.md` · 2.8k
- [ ] `components/widgets/overlays/context-menu/attributes.md` · 1.4k
- [ ] `components/widgets/overlays/context-menu/description.md` · 2.2k
- [ ] `components/widgets/overlays/context-menu/usage.md` · 3.7k

### `components/widgets/overlays/drawer/` · 2

- [ ] `components/widgets/overlays/drawer/attributes.md` · 1.3k
- [ ] `components/widgets/overlays/drawer/description.md` · 1.9k

### `components/widgets/overlays/hover-card/` · 4

- [ ] `components/widgets/overlays/hover-card/appearance.md` · 1.4k
- [ ] `components/widgets/overlays/hover-card/attributes.md` · 1.5k
- [ ] `components/widgets/overlays/hover-card/description.md` · 1.8k
- [ ] `components/widgets/overlays/hover-card/usage.md` · 871b

### `components/widgets/overlays/modal/` · 3

- [ ] `components/widgets/overlays/modal/appearance.md` · 3.2k
- [ ] `components/widgets/overlays/modal/attributes.md` · 1.4k
- [ ] `components/widgets/overlays/modal/description.md` · 1.8k

### `components/widgets/overlays/popover/` · 4

- [ ] `components/widgets/overlays/popover/appearance.md` · 1.5k
- [ ] `components/widgets/overlays/popover/attributes.md` · 1.9k
- [ ] `components/widgets/overlays/popover/description.md` · 2.1k
- [ ] `components/widgets/overlays/popover/usage.md` · 1.1k

### `components/widgets/overlays/tooltip/` · 4

- [ ] `components/widgets/overlays/tooltip/appearance.md` · 1.4k
- [ ] `components/widgets/overlays/tooltip/attributes.md` · 1.6k
- [ ] `components/widgets/overlays/tooltip/description.md` · 1.9k
- [ ] `components/widgets/overlays/tooltip/usage.md` · 1.0k

### `components/widgets/special/` · 1

- [ ] `components/widgets/special/index.md` · 661b

### `components/widgets/special/map-view/` · 4

- [ ] `components/widgets/special/map-view/appearance.md` · 2.7k
- [ ] `components/widgets/special/map-view/attributes.md` · 1.6k
- [ ] `components/widgets/special/map-view/description.md` · 1.9k
- [ ] `components/widgets/special/map-view/usage.md` · 601b

### `components/workbenches/` · 1

- [ ] `components/workbenches/index.md` · 1.0k

### `components/workbenches/fields/` · 1

- [ ] `components/workbenches/fields/index.md` · 687b

### `components/workbenches/fields/rich-text-editor/` · 4

- [ ] `components/workbenches/fields/rich-text-editor/appearance.md` · 2.9k
- [ ] `components/workbenches/fields/rich-text-editor/attributes.md` · 1.4k
- [ ] `components/workbenches/fields/rich-text-editor/description.md` · 2.0k
- [ ] `components/workbenches/fields/rich-text-editor/usage.md` · 636b

### `components/workbenches/special/` · 1

- [ ] `components/workbenches/special/index.md` · 1.2k

### `components/workbenches/special/code-editor/` · 4

- [ ] `components/workbenches/special/code-editor/appearance.md` · 2.1k
- [ ] `components/workbenches/special/code-editor/attributes.md` · 1.4k
- [ ] `components/workbenches/special/code-editor/description.md` · 1.9k
- [ ] `components/workbenches/special/code-editor/usage.md` · 517b

### `components/workbenches/special/dashboard/` · 3

- [ ] `components/workbenches/special/dashboard/attributes.md` · 1.4k
- [ ] `components/workbenches/special/dashboard/description.md` · 1.9k
- [ ] `components/workbenches/special/dashboard/usage.md` · 534b

### `components/workbenches/special/embed/` · 4

- [ ] `components/workbenches/special/embed/appearance.md` · 2.2k
- [ ] `components/workbenches/special/embed/attributes.md` · 2.0k
- [ ] `components/workbenches/special/embed/description.md` · 2.6k
- [ ] `components/workbenches/special/embed/usage.md` · 1.0k

### `components/workbenches/special/whiteboard/` · 4

- [ ] `components/workbenches/special/whiteboard/appearance.md` · 2.9k
- [ ] `components/workbenches/special/whiteboard/attributes.md` · 1.3k
- [ ] `components/workbenches/special/whiteboard/description.md` · 2.0k
- [ ] `components/workbenches/special/whiteboard/usage.md` · 553b

### `interactions/gestures/combined/` · 1

- [ ] `interactions/gestures/combined/index.md` · 1.2k

### `interactions/gestures/combined/drag-and-drop/` · 3

- [ ] `interactions/gestures/combined/drag-and-drop/appearance.md` · 1.9k
- [ ] `interactions/gestures/combined/drag-and-drop/attributes.md` · 2.2k
- [ ] `interactions/gestures/combined/drag-and-drop/description.md` · 1.9k

### `interactions/gestures/combined/pull-to-refresh/` · 3

- [ ] `interactions/gestures/combined/pull-to-refresh/appearance.md` · 1.4k
- [ ] `interactions/gestures/combined/pull-to-refresh/attributes.md` · 1.9k
- [ ] `interactions/gestures/combined/pull-to-refresh/description.md` · 1.8k

### `interactions/gestures/device/flip/` · 3

- [ ] `interactions/gestures/device/flip/appearance.md` · 1.2k
- [ ] `interactions/gestures/device/flip/attributes.md` · 1.6k
- [ ] `interactions/gestures/device/flip/description.md` · 1.6k

### `interactions/gestures/device/shake/` · 3

- [ ] `interactions/gestures/device/shake/appearance.md` · 1.3k
- [ ] `interactions/gestures/device/shake/attributes.md` · 1.7k
- [ ] `interactions/gestures/device/shake/description.md` · 1.2k

### `interactions/gestures/device/tilt/` · 3

- [ ] `interactions/gestures/device/tilt/appearance.md` · 1.3k
- [ ] `interactions/gestures/device/tilt/attributes.md` · 1.7k
- [ ] `interactions/gestures/device/tilt/description.md` · 1.4k

### `interactions/gestures/device/wave/` · 3

- [ ] `interactions/gestures/device/wave/appearance.md` · 1.3k
- [ ] `interactions/gestures/device/wave/attributes.md` · 1.6k
- [ ] `interactions/gestures/device/wave/description.md` · 1.7k

### `interactions/gestures/special/` · 1

- [ ] `interactions/gestures/special/index.md` · 1.0k

### `interactions/gestures/special/fingerprint/` · 3

- [ ] `interactions/gestures/special/fingerprint/appearance.md` · 1.5k
- [ ] `interactions/gestures/special/fingerprint/attributes.md` · 1.3k
- [ ] `interactions/gestures/special/fingerprint/description.md` · 1.4k

### `interactions/gestures/special/hover/` · 3

- [ ] `interactions/gestures/special/hover/appearance.md` · 1.6k
- [ ] `interactions/gestures/special/hover/attributes.md` · 1.6k
- [ ] `interactions/gestures/special/hover/description.md` · 1.7k

### `interactions/gestures/swipe/` · 1

- [ ] `interactions/gestures/swipe/index.md` · 1.7k

### `interactions/gestures/swipe/drag/` · 3

- [ ] `interactions/gestures/swipe/drag/appearance.md` · 1010b
- [ ] `interactions/gestures/swipe/drag/attributes.md` · 1.1k
- [ ] `interactions/gestures/swipe/drag/description.md` · 409b

### `interactions/gestures/swipe/draw-gesture/` · 3

- [ ] `interactions/gestures/swipe/draw-gesture/appearance.md` · 1.6k
- [ ] `interactions/gestures/swipe/draw-gesture/attributes.md` · 1.9k
- [ ] `interactions/gestures/swipe/draw-gesture/description.md` · 1.8k

### `interactions/gestures/swipe/edge-swipe/` · 3

- [ ] `interactions/gestures/swipe/edge-swipe/appearance.md` · 1.8k
- [ ] `interactions/gestures/swipe/edge-swipe/attributes.md` · 1.8k
- [ ] `interactions/gestures/swipe/edge-swipe/description.md` · 1.7k

### `interactions/gestures/swipe/flick/` · 3

- [ ] `interactions/gestures/swipe/flick/appearance.md` · 1.8k
- [ ] `interactions/gestures/swipe/flick/attributes.md` · 1.8k
- [ ] `interactions/gestures/swipe/flick/description.md` · 1.6k

### `interactions/gestures/swipe/multi-finger-swipe/` · 3

- [ ] `interactions/gestures/swipe/multi-finger-swipe/appearance.md` · 1.5k
- [ ] `interactions/gestures/swipe/multi-finger-swipe/attributes.md` · 1.8k
- [ ] `interactions/gestures/swipe/multi-finger-swipe/description.md` · 1.8k

### `interactions/gestures/swipe/swipe/` · 3

- [ ] `interactions/gestures/swipe/swipe/appearance.md` · 1.0k
- [ ] `interactions/gestures/swipe/swipe/attributes.md` · 1008b
- [ ] `interactions/gestures/swipe/swipe/description.md` · 538b

### `interactions/gestures/tap/` · 1

- [ ] `interactions/gestures/tap/index.md` · 1.6k

### `interactions/gestures/tap/double-tap/` · 3

- [ ] `interactions/gestures/tap/double-tap/appearance.md` · 860b
- [ ] `interactions/gestures/tap/double-tap/attributes.md` · 869b
- [ ] `interactions/gestures/tap/double-tap/description.md` · 421b

### `interactions/gestures/tap/force-press/` · 3

- [ ] `interactions/gestures/tap/force-press/appearance.md` · 1.5k
- [ ] `interactions/gestures/tap/force-press/attributes.md` · 1.8k
- [ ] `interactions/gestures/tap/force-press/description.md` · 1.8k

### `interactions/gestures/tap/long-press/` · 3

- [ ] `interactions/gestures/tap/long-press/appearance.md` · 868b
- [ ] `interactions/gestures/tap/long-press/attributes.md` · 875b
- [ ] `interactions/gestures/tap/long-press/description.md` · 409b

### `interactions/gestures/tap/multi-finger-long-press/` · 3

- [ ] `interactions/gestures/tap/multi-finger-long-press/appearance.md` · 1.4k
- [ ] `interactions/gestures/tap/multi-finger-long-press/attributes.md` · 1.8k
- [ ] `interactions/gestures/tap/multi-finger-long-press/description.md` · 1.6k

### `interactions/gestures/tap/multi-finger-tap/` · 3

- [ ] `interactions/gestures/tap/multi-finger-tap/appearance.md` · 1.5k
- [ ] `interactions/gestures/tap/multi-finger-tap/attributes.md` · 1.6k
- [ ] `interactions/gestures/tap/multi-finger-tap/description.md` · 1.6k

### `interactions/gestures/tap/tap/` · 3

- [ ] `interactions/gestures/tap/tap/appearance.md` · 827b
- [ ] `interactions/gestures/tap/tap/attributes.md` · 836b
- [ ] `interactions/gestures/tap/tap/description.md` · 396b

### `interactions/gestures/transform/pinch/` · 3

- [ ] `interactions/gestures/transform/pinch/appearance.md` · 905b
- [ ] `interactions/gestures/transform/pinch/attributes.md` · 902b
- [ ] `interactions/gestures/transform/pinch/description.md` · 508b

### `interactions/gestures/transform/rotate/` · 3

- [ ] `interactions/gestures/transform/rotate/appearance.md` · 1.0k
- [ ] `interactions/gestures/transform/rotate/attributes.md` · 888b
- [ ] `interactions/gestures/transform/rotate/description.md` · 522b

### `interactions/gestures/transform/spread/` · 3

- [ ] `interactions/gestures/transform/spread/appearance.md` · 920b
- [ ] `interactions/gestures/transform/spread/attributes.md` · 906b
- [ ] `interactions/gestures/transform/spread/description.md` · 521b

### `programs/apps/calendar/masks/davical/` · 7

- [ ] `programs/apps/calendar/masks/davical/api.md` · 7.8k · Plan[x]
- [ ] `programs/apps/calendar/masks/davical/description.md` · 3.1k · Plan[x]
- [ ] `programs/apps/calendar/masks/davical/features.md` · 3.4k · Plan[x]
- [ ] `programs/apps/calendar/masks/davical/index.md` · 2.7k · Plan[x]
- [ ] `programs/apps/calendar/masks/davical/menu.md` · 2.6k · Plan[x]
- [ ] `programs/apps/calendar/masks/davical/shortcuts.md` · 1.8k · Plan[x]
- [ ] `programs/apps/calendar/masks/davical/structure.md` · 2.9k · Plan[x]

### `programs/apps/calendar/masks/google-calendar/` · 6

- [ ] `programs/apps/calendar/masks/google-calendar/api.md` · 11.7k · Plan[x]
- [ ] `programs/apps/calendar/masks/google-calendar/description.md` · 5.2k · Plan[x]
- [ ] `programs/apps/calendar/masks/google-calendar/features.md` · 6.0k · Plan[x]
- [ ] `programs/apps/calendar/masks/google-calendar/index.md` · 8.3k · Plan[x]
- [ ] `programs/apps/calendar/masks/google-calendar/shortcuts.md` · 3.2k · Plan[x]
- [ ] `programs/apps/calendar/masks/google-calendar/structure.md` · 7.6k · Plan[x]

### `programs/apps/calendar/masks/merkuro/` · 7

- [ ] `programs/apps/calendar/masks/merkuro/api.md` · 6.5k · Plan[x]
- [ ] `programs/apps/calendar/masks/merkuro/description.md` · 4.5k · Plan[x]
- [ ] `programs/apps/calendar/masks/merkuro/features.md` · 4.3k · Plan[x]
- [ ] `programs/apps/calendar/masks/merkuro/index.md` · 3.7k · Plan[x]
- [ ] `programs/apps/calendar/masks/merkuro/menu.md` · 3.4k · Plan[x]
- [ ] `programs/apps/calendar/masks/merkuro/shortcuts.md` · 2.8k · Plan[x]
- [ ] `programs/apps/calendar/masks/merkuro/structure.md` · 6.1k · Plan[x]

### `programs/apps/calendar/masks/nextcloud-calendar/` · 7

- [ ] `programs/apps/calendar/masks/nextcloud-calendar/api.md` · 11.9k · Plan[x]
- [ ] `programs/apps/calendar/masks/nextcloud-calendar/description.md` · 4.9k · Plan[x]
- [ ] `programs/apps/calendar/masks/nextcloud-calendar/features.md` · 6.2k · Plan[x]
- [ ] `programs/apps/calendar/masks/nextcloud-calendar/index.md` · 3.7k · Plan[x]
- [ ] `programs/apps/calendar/masks/nextcloud-calendar/menu.md` · 5.7k · Plan[x]
- [ ] `programs/apps/calendar/masks/nextcloud-calendar/shortcuts.md` · 4.1k · Plan[x]
- [ ] `programs/apps/calendar/masks/nextcloud-calendar/structure.md` · 7.4k · Plan[x]

### `programs/apps/calendar/masks/outlook-calendar/` · 7

- [ ] `programs/apps/calendar/masks/outlook-calendar/api.md` · 12.9k · Plan[x]
- [ ] `programs/apps/calendar/masks/outlook-calendar/description.md` · 5.3k · Plan[x]
- [ ] `programs/apps/calendar/masks/outlook-calendar/features.md` · 6.9k · Plan[x]
- [ ] `programs/apps/calendar/masks/outlook-calendar/index.md` · 5.9k · Plan[x]
- [ ] `programs/apps/calendar/masks/outlook-calendar/menu.md` · 4.1k · Plan[x]
- [ ] `programs/apps/calendar/masks/outlook-calendar/shortcuts.md` · 4.0k · Plan[x]
- [ ] `programs/apps/calendar/masks/outlook-calendar/structure.md` · 5.9k · Plan[x]

### `programs/apps/calendar/masks/planner/` · 7

- [ ] `programs/apps/calendar/masks/planner/api.md` · 8.5k · Plan[x]
- [ ] `programs/apps/calendar/masks/planner/description.md` · 4.4k · Plan[x]
- [ ] `programs/apps/calendar/masks/planner/features.md` · 6.4k · Plan[x]
- [ ] `programs/apps/calendar/masks/planner/index.md` · 5.0k · Plan[x]
- [ ] `programs/apps/calendar/masks/planner/menu.md` · 4.0k · Plan[x]
- [ ] `programs/apps/calendar/masks/planner/shortcuts.md` · 3.3k · Plan[x]
- [ ] `programs/apps/calendar/masks/planner/structure.md` · 8.6k · Plan[x]

### `programs/apps/contact/masks/` · 1

- [ ] `programs/apps/contact/masks/index.md` · 2.3k · Plan[~]

### `programs/apps/contact/masks/gnome-contacts/` · 7

- [ ] `programs/apps/contact/masks/gnome-contacts/api.md` · 1.7k · Plan[~]
- [ ] `programs/apps/contact/masks/gnome-contacts/description.md` · 1.7k · Plan[~]
- [ ] `programs/apps/contact/masks/gnome-contacts/features.md` · 1.3k · Plan[~]
- [ ] `programs/apps/contact/masks/gnome-contacts/index.md` · 821b · Plan[~]
- [ ] `programs/apps/contact/masks/gnome-contacts/menu.md` · 1.1k · Plan[~]
- [ ] `programs/apps/contact/masks/gnome-contacts/shortcuts.md` · 997b · Plan[~]
- [ ] `programs/apps/contact/masks/gnome-contacts/structure.md` · 2.4k · Plan[~]

### `programs/apps/contact/masks/kaddressbook/` · 7

- [ ] `programs/apps/contact/masks/kaddressbook/api.md` · 2.1k · Plan[~]
- [ ] `programs/apps/contact/masks/kaddressbook/description.md` · 1.7k · Plan[~]
- [ ] `programs/apps/contact/masks/kaddressbook/features.md` · 1.7k · Plan[~]
- [ ] `programs/apps/contact/masks/kaddressbook/index.md` · 814b · Plan[~]
- [ ] `programs/apps/contact/masks/kaddressbook/menu.md` · 1.5k · Plan[~]
- [ ] `programs/apps/contact/masks/kaddressbook/shortcuts.md` · 1.3k · Plan[~]
- [ ] `programs/apps/contact/masks/kaddressbook/structure.md` · 2.7k · Plan[~]

### `programs/apps/contact/masks/monica/` · 7

- [ ] `programs/apps/contact/masks/monica/api.md` · 2.3k · Plan[~]
- [ ] `programs/apps/contact/masks/monica/description.md` · 1.6k · Plan[~]
- [ ] `programs/apps/contact/masks/monica/features.md` · 1.4k · Plan[~]
- [ ] `programs/apps/contact/masks/monica/index.md` · 797b · Plan[~]
- [ ] `programs/apps/contact/masks/monica/menu.md` · 1.6k · Plan[~]
- [ ] `programs/apps/contact/masks/monica/shortcuts.md` · 723b · Plan[~]
- [ ] `programs/apps/contact/masks/monica/structure.md` · 2.9k · Plan[~]

### `programs/apps/contact/masks/nextcloud-contacts/` · 7

- [ ] `programs/apps/contact/masks/nextcloud-contacts/api.md` · 2.6k · Plan[~]
- [ ] `programs/apps/contact/masks/nextcloud-contacts/description.md` · 1.7k · Plan[~]
- [ ] `programs/apps/contact/masks/nextcloud-contacts/features.md` · 1.7k · Plan[~]
- [ ] `programs/apps/contact/masks/nextcloud-contacts/index.md` · 817b · Plan[~]
- [ ] `programs/apps/contact/masks/nextcloud-contacts/menu.md` · 1.5k · Plan[~]
- [ ] `programs/apps/contact/masks/nextcloud-contacts/shortcuts.md` · 932b · Plan[~]
- [ ] `programs/apps/contact/masks/nextcloud-contacts/structure.md` · 2.4k · Plan[~]

### `programs/apps/gallery/` · 1

- [ ] `programs/apps/gallery/index.md` · 2.7k · Plan[~]

### `programs/apps/gallery/masks/` · 1

- [ ] `programs/apps/gallery/masks/index.md` · 2.8k · Plan[~]

### `programs/apps/gallery/masks/coppermine/` · 7

- [ ] `programs/apps/gallery/masks/coppermine/api.md` · 2.6k · Plan[~]
- [ ] `programs/apps/gallery/masks/coppermine/description.md` · 1.4k · Plan[~]
- [ ] `programs/apps/gallery/masks/coppermine/features.md` · 1.2k · Plan[~]
- [ ] `programs/apps/gallery/masks/coppermine/index.md` · 818b · Plan[~]
- [ ] `programs/apps/gallery/masks/coppermine/menu.md` · 1.3k · Plan[~]
- [ ] `programs/apps/gallery/masks/coppermine/shortcuts.md` · 1.0k · Plan[~]
- [ ] `programs/apps/gallery/masks/coppermine/structure.md` · 2.5k · Plan[~]

### `programs/apps/gallery/masks/damselfly/` · 7

- [ ] `programs/apps/gallery/masks/damselfly/api.md` · 2.2k · Plan[~]
- [ ] `programs/apps/gallery/masks/damselfly/description.md` · 1.3k · Plan[~]
- [ ] `programs/apps/gallery/masks/damselfly/features.md` · 1.1k · Plan[~]
- [ ] `programs/apps/gallery/masks/damselfly/index.md` · 731b · Plan[~]
- [ ] `programs/apps/gallery/masks/damselfly/menu.md` · 1.2k · Plan[~]
- [ ] `programs/apps/gallery/masks/damselfly/shortcuts.md` · 941b · Plan[~]
- [ ] `programs/apps/gallery/masks/damselfly/structure.md` · 2.5k · Plan[~]

### `programs/apps/gallery/masks/immich/` · 6

- [ ] `programs/apps/gallery/masks/immich/description.md` · 1.8k · Plan[~]
- [ ] `programs/apps/gallery/masks/immich/features.md` · 1.9k · Plan[~]
- [ ] `programs/apps/gallery/masks/immich/index.md` · 835b · Plan[~]
- [ ] `programs/apps/gallery/masks/immich/menu.md` · 1.8k · Plan[~]
- [ ] `programs/apps/gallery/masks/immich/shortcuts.md` · 1.4k · Plan[~]
- [ ] `programs/apps/gallery/masks/immich/structure.md` · 2.6k · Plan[~]

### `programs/apps/gallery/masks/librephotos/` · 6

- [ ] `programs/apps/gallery/masks/librephotos/description.md` · 1.4k · Plan[~]
- [ ] `programs/apps/gallery/masks/librephotos/features.md` · 1.3k · Plan[~]
- [ ] `programs/apps/gallery/masks/librephotos/index.md` · 786b · Plan[~]
- [ ] `programs/apps/gallery/masks/librephotos/menu.md` · 1.5k · Plan[~]
- [ ] `programs/apps/gallery/masks/librephotos/shortcuts.md` · 860b · Plan[~]
- [ ] `programs/apps/gallery/masks/librephotos/structure.md` · 2.6k · Plan[~]

### `programs/apps/gallery/masks/lychee/` · 7

- [ ] `programs/apps/gallery/masks/lychee/api.md` · 2.4k · Plan[~]
- [ ] `programs/apps/gallery/masks/lychee/description.md` · 1.4k · Plan[~]
- [ ] `programs/apps/gallery/masks/lychee/features.md` · 1.1k · Plan[~]
- [ ] `programs/apps/gallery/masks/lychee/index.md` · 709b · Plan[~]
- [ ] `programs/apps/gallery/masks/lychee/menu.md` · 1.2k · Plan[~]
- [ ] `programs/apps/gallery/masks/lychee/shortcuts.md` · 1006b · Plan[~]
- [ ] `programs/apps/gallery/masks/lychee/structure.md` · 2.3k · Plan[~]

### `programs/apps/gallery/masks/nextcloud-photos/` · 7

- [ ] `programs/apps/gallery/masks/nextcloud-photos/api.md` · 2.6k · Plan[~]
- [ ] `programs/apps/gallery/masks/nextcloud-photos/description.md` · 1.6k · Plan[~]
- [ ] `programs/apps/gallery/masks/nextcloud-photos/features.md` · 1.4k · Plan[~]
- [ ] `programs/apps/gallery/masks/nextcloud-photos/index.md` · 938b · Plan[~]
- [ ] `programs/apps/gallery/masks/nextcloud-photos/menu.md` · 1.4k · Plan[~]
- [ ] `programs/apps/gallery/masks/nextcloud-photos/shortcuts.md` · 1007b · Plan[~]
- [ ] `programs/apps/gallery/masks/nextcloud-photos/structure.md` · 2.5k · Plan[~]

### `programs/apps/gallery/masks/photoprism/` · 7

- [ ] `programs/apps/gallery/masks/photoprism/api.md` · 2.6k · Plan[~]
- [ ] `programs/apps/gallery/masks/photoprism/description.md` · 1.6k · Plan[~]
- [ ] `programs/apps/gallery/masks/photoprism/features.md` · 1.7k · Plan[~]
- [ ] `programs/apps/gallery/masks/photoprism/index.md` · 789b · Plan[~]
- [ ] `programs/apps/gallery/masks/photoprism/menu.md` · 1.8k · Plan[~]
- [ ] `programs/apps/gallery/masks/photoprism/shortcuts.md` · 1.3k · Plan[~]
- [ ] `programs/apps/gallery/masks/photoprism/structure.md` · 2.8k · Plan[~]

### `programs/apps/gallery/masks/piwigo/` · 7

- [ ] `programs/apps/gallery/masks/piwigo/api.md` · 2.6k · Plan[~]
- [ ] `programs/apps/gallery/masks/piwigo/description.md` · 1.5k · Plan[~]
- [ ] `programs/apps/gallery/masks/piwigo/features.md` · 1.5k · Plan[~]
- [ ] `programs/apps/gallery/masks/piwigo/index.md` · 764b · Plan[~]
- [ ] `programs/apps/gallery/masks/piwigo/menu.md` · 1.7k · Plan[~]
- [ ] `programs/apps/gallery/masks/piwigo/shortcuts.md` · 1.0k · Plan[~]
- [ ] `programs/apps/gallery/masks/piwigo/structure.md` · 2.4k · Plan[~]

### `programs/apps/helpdesk/masks/` · 1

- [ ] `programs/apps/helpdesk/masks/index.md` · 2.8k · Plan[~]

### `programs/apps/helpdesk/masks/freshdesk/` · 6

- [ ] `programs/apps/helpdesk/masks/freshdesk/description.md` · 1.3k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/freshdesk/features.md` · 1.4k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/freshdesk/index.md` · 679b · Plan[~]
- [ ] `programs/apps/helpdesk/masks/freshdesk/menu.md` · 1.4k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/freshdesk/shortcuts.md` · 695b · Plan[~]
- [ ] `programs/apps/helpdesk/masks/freshdesk/structure.md` · 2.0k · Plan[~]

### `programs/apps/helpdesk/masks/glpi/` · 7

- [ ] `programs/apps/helpdesk/masks/glpi/api.md` · 2.5k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/glpi/description.md` · 1.5k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/glpi/features.md` · 1.6k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/glpi/index.md` · 850b · Plan[~]
- [ ] `programs/apps/helpdesk/masks/glpi/menu.md` · 1.3k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/glpi/shortcuts.md` · 645b · Plan[~]
- [ ] `programs/apps/helpdesk/masks/glpi/structure.md` · 2.5k · Plan[~]

### `programs/apps/helpdesk/masks/helodesk/` · 7

- [ ] `programs/apps/helpdesk/masks/helodesk/api.md` · 2.5k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/helodesk/description.md` · 1.5k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/helodesk/features.md` · 1.6k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/helodesk/index.md` · 846b · Plan[~]
- [ ] `programs/apps/helpdesk/masks/helodesk/menu.md` · 1.3k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/helodesk/shortcuts.md` · 713b · Plan[~]
- [ ] `programs/apps/helpdesk/masks/helodesk/structure.md` · 2.3k · Plan[~]

### `programs/apps/helpdesk/masks/helpscout/` · 6

- [ ] `programs/apps/helpdesk/masks/helpscout/description.md` · 1.2k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/helpscout/features.md` · 1.4k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/helpscout/index.md` · 705b · Plan[~]
- [ ] `programs/apps/helpdesk/masks/helpscout/menu.md` · 1.1k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/helpscout/shortcuts.md` · 638b · Plan[~]
- [ ] `programs/apps/helpdesk/masks/helpscout/structure.md` · 2.0k · Plan[~]

### `programs/apps/helpdesk/masks/osticket/` · 7

- [ ] `programs/apps/helpdesk/masks/osticket/api.md` · 2.3k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/osticket/description.md` · 1.4k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/osticket/features.md` · 1.7k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/osticket/index.md` · 739b · Plan[~]
- [ ] `programs/apps/helpdesk/masks/osticket/menu.md` · 1.3k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/osticket/shortcuts.md` · 631b · Plan[~]
- [ ] `programs/apps/helpdesk/masks/osticket/structure.md` · 2.3k · Plan[~]

### `programs/apps/helpdesk/masks/request-tracker/` · 7

- [ ] `programs/apps/helpdesk/masks/request-tracker/api.md` · 2.5k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/request-tracker/description.md` · 1.5k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/request-tracker/features.md` · 1.7k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/request-tracker/index.md` · 780b · Plan[~]
- [ ] `programs/apps/helpdesk/masks/request-tracker/menu.md` · 1.2k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/request-tracker/shortcuts.md` · 997b · Plan[~]
- [ ] `programs/apps/helpdesk/masks/request-tracker/structure.md` · 2.3k · Plan[~]

### `programs/apps/helpdesk/masks/zammad/` · 6

- [ ] `programs/apps/helpdesk/masks/zammad/description.md` · 1.7k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/zammad/features.md` · 1.7k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/zammad/index.md` · 829b · Plan[~]
- [ ] `programs/apps/helpdesk/masks/zammad/menu.md` · 1.7k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/zammad/shortcuts.md` · 1005b · Plan[~]
- [ ] `programs/apps/helpdesk/masks/zammad/structure.md` · 2.6k · Plan[~]

### `programs/apps/helpdesk/masks/zendesk/` · 6

- [ ] `programs/apps/helpdesk/masks/zendesk/description.md` · 1.4k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/zendesk/features.md` · 1.6k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/zendesk/index.md` · 732b · Plan[~]
- [ ] `programs/apps/helpdesk/masks/zendesk/menu.md` · 1.3k · Plan[~]
- [ ] `programs/apps/helpdesk/masks/zendesk/shortcuts.md` · 915b · Plan[~]
- [ ] `programs/apps/helpdesk/masks/zendesk/structure.md` · 2.4k · Plan[~]

### `programs/apps/maps/` · 1

- [ ] `programs/apps/maps/standpunkte.md` · 2.2k · Plan[~]

### `programs/apps/maps/masks/` · 1

- [ ] `programs/apps/maps/masks/index.md` · 2.6k · Plan[~]

### `programs/apps/maps/masks/leaflet/` · 6

- [ ] `programs/apps/maps/masks/leaflet/description.md` · 1.1k · Plan[~]
- [ ] `programs/apps/maps/masks/leaflet/features.md` · 1.1k · Plan[~]
- [ ] `programs/apps/maps/masks/leaflet/index.md` · 715b · Plan[~]
- [ ] `programs/apps/maps/masks/leaflet/menu.md` · 581b · Plan[~]
- [ ] `programs/apps/maps/masks/leaflet/shortcuts.md` · 499b · Plan[~]
- [ ] `programs/apps/maps/masks/leaflet/structure.md` · 996b · Plan[~]

### `programs/apps/maps/masks/maplibre/` · 6

- [ ] `programs/apps/maps/masks/maplibre/description.md` · 1.1k · Plan[~]
- [ ] `programs/apps/maps/masks/maplibre/features.md` · 1.2k · Plan[~]
- [ ] `programs/apps/maps/masks/maplibre/index.md` · 870b · Plan[~]
- [ ] `programs/apps/maps/masks/maplibre/menu.md` · 640b · Plan[~]
- [ ] `programs/apps/maps/masks/maplibre/shortcuts.md` · 606b · Plan[~]
- [ ] `programs/apps/maps/masks/maplibre/structure.md` · 1.6k · Plan[~]

### `programs/apps/maps/masks/openstreetmap/` · 7

- [ ] `programs/apps/maps/masks/openstreetmap/api.md` · 2.3k · Plan[~]
- [ ] `programs/apps/maps/masks/openstreetmap/description.md` · 1.2k · Plan[~]
- [ ] `programs/apps/maps/masks/openstreetmap/features.md` · 1.3k · Plan[~]
- [ ] `programs/apps/maps/masks/openstreetmap/index.md` · 838b · Plan[~]
- [ ] `programs/apps/maps/masks/openstreetmap/menu.md` · 1.0k · Plan[~]
- [ ] `programs/apps/maps/masks/openstreetmap/shortcuts.md` · 1.2k · Plan[~]
- [ ] `programs/apps/maps/masks/openstreetmap/structure.md` · 2.1k · Plan[~]

### `programs/apps/maps/masks/organic-maps/` · 6

- [ ] `programs/apps/maps/masks/organic-maps/description.md` · 1.0k · Plan[~]
- [ ] `programs/apps/maps/masks/organic-maps/features.md` · 946b · Plan[~]
- [ ] `programs/apps/maps/masks/organic-maps/index.md` · 736b · Plan[~]
- [ ] `programs/apps/maps/masks/organic-maps/menu.md` · 804b · Plan[~]
- [ ] `programs/apps/maps/masks/organic-maps/shortcuts.md` · 548b · Plan[~]
- [ ] `programs/apps/maps/masks/organic-maps/structure.md` · 1.2k · Plan[~]

### `programs/apps/maps/masks/osmand/` · 6

- [ ] `programs/apps/maps/masks/osmand/description.md` · 1.1k · Plan[~]
- [ ] `programs/apps/maps/masks/osmand/features.md` · 1.3k · Plan[~]
- [ ] `programs/apps/maps/masks/osmand/index.md` · 839b · Plan[~]
- [ ] `programs/apps/maps/masks/osmand/menu.md` · 893b · Plan[~]
- [ ] `programs/apps/maps/masks/osmand/shortcuts.md` · 604b · Plan[~]
- [ ] `programs/apps/maps/masks/osmand/structure.md` · 1.4k · Plan[~]

### `programs/apps/maps/masks/qgis/` · 7

- [ ] `programs/apps/maps/masks/qgis/api.md` · 1.9k · Plan[~]
- [ ] `programs/apps/maps/masks/qgis/description.md` · 1.1k · Plan[~]
- [ ] `programs/apps/maps/masks/qgis/features.md` · 1.3k · Plan[~]
- [ ] `programs/apps/maps/masks/qgis/index.md` · 756b · Plan[~]
- [ ] `programs/apps/maps/masks/qgis/menu.md` · 947b · Plan[~]
- [ ] `programs/apps/maps/masks/qgis/shortcuts.md` · 766b · Plan[~]
- [ ] `programs/apps/maps/masks/qgis/structure.md` · 2.0k · Plan[~]

### `programs/apps/maps/masks/umap/` · 7

- [ ] `programs/apps/maps/masks/umap/api.md` · 1.8k · Plan[~]
- [ ] `programs/apps/maps/masks/umap/description.md` · 1.1k · Plan[~]
- [ ] `programs/apps/maps/masks/umap/features.md` · 1.0k · Plan[~]
- [ ] `programs/apps/maps/masks/umap/index.md` · 747b · Plan[~]
- [ ] `programs/apps/maps/masks/umap/menu.md` · 1004b · Plan[~]
- [ ] `programs/apps/maps/masks/umap/shortcuts.md` · 427b · Plan[~]
- [ ] `programs/apps/maps/masks/umap/structure.md` · 1.8k · Plan[~]

### `programs/apps/marketing/masks/` · 1

- [ ] `programs/apps/marketing/masks/index.md` · 2.5k · Plan[~]

### `programs/apps/marketing/masks/google-analytics/` · 7

- [ ] `programs/apps/marketing/masks/google-analytics/api.md` · 2.2k · Plan[~]
- [ ] `programs/apps/marketing/masks/google-analytics/description.md` · 1.1k · Plan[~]
- [ ] `programs/apps/marketing/masks/google-analytics/features.md` · 1.2k · Plan[~]
- [ ] `programs/apps/marketing/masks/google-analytics/index.md` · 760b · Plan[~]
- [ ] `programs/apps/marketing/masks/google-analytics/menu.md` · 971b · Plan[~]
- [ ] `programs/apps/marketing/masks/google-analytics/shortcuts.md` · 413b · Plan[~]
- [ ] `programs/apps/marketing/masks/google-analytics/structure.md` · 1.7k · Plan[~]

### `programs/apps/marketing/masks/hotjar/` · 7

- [ ] `programs/apps/marketing/masks/hotjar/api.md` · 1.7k · Plan[~]
- [ ] `programs/apps/marketing/masks/hotjar/description.md` · 1.1k · Plan[~]
- [ ] `programs/apps/marketing/masks/hotjar/features.md` · 1013b · Plan[~]
- [ ] `programs/apps/marketing/masks/hotjar/index.md` · 741b · Plan[~]
- [ ] `programs/apps/marketing/masks/hotjar/menu.md` · 849b · Plan[~]
- [ ] `programs/apps/marketing/masks/hotjar/shortcuts.md` · 411b · Plan[~]
- [ ] `programs/apps/marketing/masks/hotjar/structure.md` · 1.0k · Plan[~]

### `programs/apps/marketing/masks/mailchimp/` · 7

- [ ] `programs/apps/marketing/masks/mailchimp/api.md` · 2.2k · Plan[~]
- [ ] `programs/apps/marketing/masks/mailchimp/description.md` · 1.2k · Plan[~]
- [ ] `programs/apps/marketing/masks/mailchimp/features.md` · 1.0k · Plan[~]
- [ ] `programs/apps/marketing/masks/mailchimp/index.md` · 695b · Plan[~]
- [ ] `programs/apps/marketing/masks/mailchimp/menu.md` · 914b · Plan[~]
- [ ] `programs/apps/marketing/masks/mailchimp/shortcuts.md` · 475b · Plan[~]
- [ ] `programs/apps/marketing/masks/mailchimp/structure.md` · 1.7k · Plan[~]

### `programs/apps/marketing/masks/matomo/` · 7

- [ ] `programs/apps/marketing/masks/matomo/api.md` · 2.1k · Plan[~]
- [ ] `programs/apps/marketing/masks/matomo/description.md` · 1.3k · Plan[~]
- [ ] `programs/apps/marketing/masks/matomo/features.md` · 1.1k · Plan[~]
- [ ] `programs/apps/marketing/masks/matomo/index.md` · 751b · Plan[~]
- [ ] `programs/apps/marketing/masks/matomo/menu.md` · 972b · Plan[~]
- [ ] `programs/apps/marketing/masks/matomo/shortcuts.md` · 375b · Plan[~]
- [ ] `programs/apps/marketing/masks/matomo/structure.md` · 1.6k · Plan[~]

### `programs/apps/marketing/masks/mautic/` · 7

- [ ] `programs/apps/marketing/masks/mautic/api.md` · 2.4k · Plan[~]
- [ ] `programs/apps/marketing/masks/mautic/description.md` · 1.2k · Plan[~]
- [ ] `programs/apps/marketing/masks/mautic/features.md` · 1.1k · Plan[~]
- [ ] `programs/apps/marketing/masks/mautic/index.md` · 754b · Plan[~]
- [ ] `programs/apps/marketing/masks/mautic/menu.md` · 1.0k · Plan[~]
- [ ] `programs/apps/marketing/masks/mautic/shortcuts.md` · 378b · Plan[~]
- [ ] `programs/apps/marketing/masks/mautic/structure.md` · 1.6k · Plan[~]

### `programs/apps/marketing/masks/plausible/` · 6

- [ ] `programs/apps/marketing/masks/plausible/description.md` · 1.1k · Plan[~]
- [ ] `programs/apps/marketing/masks/plausible/features.md` · 1020b · Plan[~]
- [ ] `programs/apps/marketing/masks/plausible/index.md` · 688b · Plan[~]
- [ ] `programs/apps/marketing/masks/plausible/menu.md` · 768b · Plan[~]
- [ ] `programs/apps/marketing/masks/plausible/shortcuts.md` · 392b · Plan[~]
- [ ] `programs/apps/marketing/masks/plausible/structure.md` · 1.6k · Plan[~]

### `programs/apps/messenger/` · 1

- [ ] `programs/apps/messenger/index.md` · 2.6k · Plan[~]

### `programs/apps/messenger/masks/discord/` · 3

- [ ] `programs/apps/messenger/masks/discord/description.md` · 2.7k · Plan[~]
- [ ] `programs/apps/messenger/masks/discord/menu.md` · 1.9k · Plan[~]
- [ ] `programs/apps/messenger/masks/discord/structure.md` · 7.4k · Plan[~]

### `programs/apps/messenger/masks/element/` · 3

- [ ] `programs/apps/messenger/masks/element/description.md` · 2.9k · Plan[~]
- [ ] `programs/apps/messenger/masks/element/menu.md` · 1.7k · Plan[~]
- [ ] `programs/apps/messenger/masks/element/structure.md` · 6.7k · Plan[~]

### `programs/apps/messenger/masks/kontact/` · 3

- [ ] `programs/apps/messenger/masks/kontact/description.md` · 2.9k · Plan[~]
- [ ] `programs/apps/messenger/masks/kontact/menu.md` · 2.9k · Plan[~]
- [ ] `programs/apps/messenger/masks/kontact/structure.md` · 10.6k · Plan[~]

### `programs/apps/messenger/masks/mastodon/` · 3

- [ ] `programs/apps/messenger/masks/mastodon/description.md` · 2.7k · Plan[~]
- [ ] `programs/apps/messenger/masks/mastodon/menu.md` · 2.0k · Plan[~]
- [ ] `programs/apps/messenger/masks/mastodon/structure.md` · 8.0k · Plan[~]

### `programs/apps/messenger/masks/outlook/` · 2

- [ ] `programs/apps/messenger/masks/outlook/description.md` · 2.3k · Plan[~]
- [ ] `programs/apps/messenger/masks/outlook/menu.md` · 2.1k · Plan[~]

### `programs/apps/messenger/masks/telegram/` · 3

- [ ] `programs/apps/messenger/masks/telegram/description.md` · 2.7k · Plan[~]
- [ ] `programs/apps/messenger/masks/telegram/menu.md` · 1.9k · Plan[~]
- [ ] `programs/apps/messenger/masks/telegram/structure.md` · 7.9k · Plan[~]

### `programs/apps/messenger/masks/thunderbird/` · 3

- [ ] `programs/apps/messenger/masks/thunderbird/description.md` · 2.8k · Plan[~]
- [ ] `programs/apps/messenger/masks/thunderbird/menu.md` · 2.8k · Plan[~]
- [ ] `programs/apps/messenger/masks/thunderbird/structure.md` · 7.8k · Plan[~]

### `programs/apps/projectmanagement/masks/` · 1

- [ ] `programs/apps/projectmanagement/masks/index.md` · 2.7k · Plan[~]

### `programs/apps/projectmanagement/masks/asana/` · 6

- [ ] `programs/apps/projectmanagement/masks/asana/description.md` · 1.2k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/asana/features.md` · 1.3k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/asana/index.md` · 743b · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/asana/menu.md` · 1.1k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/asana/shortcuts.md` · 763b · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/asana/structure.md` · 2.0k · Plan[~]

### `programs/apps/projectmanagement/masks/jira/` · 7

- [ ] `programs/apps/projectmanagement/masks/jira/api.md` · 2.5k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/jira/description.md` · 1.3k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/jira/features.md` · 1.5k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/jira/index.md` · 728b · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/jira/menu.md` · 1.2k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/jira/shortcuts.md` · 1.1k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/jira/structure.md` · 2.4k · Plan[~]

### `programs/apps/projectmanagement/masks/openproject/` · 1

- [ ] `programs/apps/projectmanagement/masks/openproject/index.md` · 865b · Plan[~]

### `programs/apps/projectmanagement/masks/planka/` · 1

- [ ] `programs/apps/projectmanagement/masks/planka/index.md` · 812b · Plan[~]

### `programs/apps/projectmanagement/masks/redmine/` · 1

- [ ] `programs/apps/projectmanagement/masks/redmine/index.md` · 844b · Plan[~]

### `programs/apps/projectmanagement/masks/taiga/` · 1

- [ ] `programs/apps/projectmanagement/masks/taiga/index.md` · 724b · Plan[~]

### `programs/apps/projectmanagement/masks/trello/` · 2

- [ ] `programs/apps/projectmanagement/masks/trello/description.md` · 1.3k · Plan[~]
- [ ] `programs/apps/projectmanagement/masks/trello/index.md` · 699b · Plan[~]

### `programs/apps/projectmanagement/masks/wekan/` · 1

- [ ] `programs/apps/projectmanagement/masks/wekan/index.md` · 760b · Plan[~]

### `programs/apps/streaming/` · 1

- [ ] `programs/apps/streaming/index.md` · 3.2k · Plan[~]

### `programs/apps/streaming/masks/` · 1

- [ ] `programs/apps/streaming/masks/index.md` · 3.1k · Plan[~]

### `programs/apps/streaming/masks/ant-media-server/` · 1

- [ ] `programs/apps/streaming/masks/ant-media-server/index.md` · 904b · Plan[~]

### `programs/apps/streaming/masks/ffmpeg/` · 1

- [ ] `programs/apps/streaming/masks/ffmpeg/index.md` · 2.1k · Plan[~]

### `programs/apps/streaming/masks/gstreamer/` · 1

- [ ] `programs/apps/streaming/masks/gstreamer/index.md` · 1008b · Plan[~]

### `programs/apps/streaming/masks/mediamtx/` · 1

- [ ] `programs/apps/streaming/masks/mediamtx/index.md` · 970b · Plan[~]

### `programs/apps/streaming/masks/mistserver/` · 1

- [ ] `programs/apps/streaming/masks/mistserver/index.md` · 954b · Plan[~]

### `programs/apps/streaming/masks/nginx-rtmp-module/` · 1

- [ ] `programs/apps/streaming/masks/nginx-rtmp-module/index.md` · 1014b · Plan[~]

### `programs/apps/streaming/masks/obs-studio/` · 1

- [ ] `programs/apps/streaming/masks/obs-studio/index.md` · 809b · Plan[~]

### `programs/apps/streaming/masks/restream/` · 1

- [ ] `programs/apps/streaming/masks/restream/index.md` · 981b · Plan[~]

### `programs/apps/streaming/masks/restreamer/` · 1

- [ ] `programs/apps/streaming/masks/restreamer/index.md` · 802b · Plan[~]

### `programs/apps/streaming/masks/wowza/` · 1

- [ ] `programs/apps/streaming/masks/wowza/index.md` · 1.3k · Plan[~]

### `programs/apps/whiteboards/masks/` · 1

- [ ] `programs/apps/whiteboards/masks/index.md` · 2.5k · Plan[~]

### `programs/apps/whiteboards/masks/drawio/` · 1

- [ ] `programs/apps/whiteboards/masks/drawio/index.md` · 811b · Plan[~]

### `programs/apps/whiteboards/masks/excalidraw/` · 1

- [ ] `programs/apps/whiteboards/masks/excalidraw/index.md` · 744b · Plan[~]

### `programs/apps/whiteboards/masks/miro/` · 1

- [ ] `programs/apps/whiteboards/masks/miro/index.md` · 710b · Plan[~]

### `programs/apps/whiteboards/masks/mural/` · 1

- [ ] `programs/apps/whiteboards/masks/mural/index.md` · 684b · Plan[~]

### `programs/apps/whiteboards/masks/openboard/` · 1

- [ ] `programs/apps/whiteboards/masks/openboard/index.md` · 744b · Plan[~]

### `programs/apps/whiteboards/masks/tldraw/` · 1

- [ ] `programs/apps/whiteboards/masks/tldraw/index.md` · 826b · Plan[~]

### `programs/apps/wiki/` · 1

- [ ] `programs/apps/wiki/index.md` · 2.3k · Plan[~]

### `programs/apps/wiki/masks/confluence/` · 1

- [ ] `programs/apps/wiki/masks/confluence/index.md` · 482b · Plan[~]

### `programs/apps/wiki/masks/mediawiki/` · 1

- [ ] `programs/apps/wiki/masks/mediawiki/index.md` · 479b · Plan[~]

### `programs/apps/wiki/masks/notion/` · 1

- [ ] `programs/apps/wiki/masks/notion/index.md` · 476b · Plan[~]

### `programs/apps/wiki/masks/tango.io/` · 1

- [ ] `programs/apps/wiki/masks/tango.io/index.md` · 483b · Plan[~]

### `programs/apps/wiki/masks/vscodium/` · 1

- [ ] `programs/apps/wiki/masks/vscodium/index.md` · 469b · Plan[~]

### `programs/apps/wiki/masks/wikijs/` · 1

- [ ] `programs/apps/wiki/masks/wikijs/index.md` · 463b · Plan[~]

### `programs/apps/wiki/masks/xwiki/` · 1

- [ ] `programs/apps/wiki/masks/xwiki/index.md` · 492b · Plan[~]

## Changelog

  `find_untranslated.py`, `find_untranslated_ger_lines.py`, `check-translation.sh`,
  `check-box-width.py`, `boxgen.py`, `update-progress.py`, `mark-progress.py`,
  `translate-index-templates.py`. Abgleich gelaufen: alle Funde der drei Sprachdetektoren werden
  jetzt von `doc_sync.py` gemeldet.
- 2026-11-05 02:25 · **Prüfer erweitert, nicht neu geschrieben:** neuer Abschnitt D2
  (`code_german`) – deutscher Text in Codebeispielen und Boxen, weil ADR 0002 Code englisch hält.
  Kein alter Detektor hat Codezeilen gesehen. Zwei Parser-Fehler behoben: ``` ```jsx ``` wurde als
  Inline-Code geparst und machte ganze Codeblöcke Ausnahme-frei; Umlaute am Wortanfang (`ändern`)
  galten nicht als Indiz. Box-Prüfung (`box frames broken`) meldet nur, wenn `en/` schlechter ist
  als `de/` – die Breitenfehler existieren sonst beidseitig (en 123 / de 227 Dateien) und sind
  kein Übersetzungsproblem.
- 2026-11-05 02:25 · **Reparatur im selben Skript:** `--fix-boxes <pfad>` (Zielbreite je Box, aus
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
