# Icon-Set erstellen — Formular & Workflow

> Teil des **Icon Managers** in FreeSynergy.Managers.

[← Icon Manager](README.md) | [Cursor Manager](cursor-manager.md) | [Synthesizer](../../konzepte/synthesizer.md) | [UI-Standards](../../konzepte/ui-standards.md)

---

## Sidebar-Einstiegspunkt

Im Icon Manager gibt es neben der Set-Liste den Punkt **"Neues Set erstellen"**. Der öffnet das Formular. Bestehende Sets können über den **"Bearbeiten"**-Button aus der Set-Liste geöffnet werden — das Formular ist identisch, nur mit vorausgefüllten Werten.

---

## Metadaten-Felder

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `id` | Text (slug) | ja | Eindeutige ID — Kleinbuchstaben, Bindestriche, keine Leerzeichen (z.B. `my-icons`) |
| `name` | Text | ja | Anzeigename (z.B. `My Icons`) |
| `description` | Textarea | nein | Kurzbeschreibung des Stils |
| `author` | Text | nein | Ersteller-Name oder Handle |
| `version` | Text (SemVer) | ja | z.B. `1.0.0` |
| `has_dark_variants` | Checkbox | nein | Enthält das Set `-dark.svg` Varianten? |
| `style` | Auswahl | nein | `outline` / `filled` / `duotone` / `flat` — Hinweis für den Synthesizer |
| `size` | Zahl (px) | nein | Standard-Größe der SVGs (z.B. `24`) |

---

## Icon-Slots

Anders als beim Cursor-Set gibt es keine feste Liste von Pflicht-Slots. Ein Icon-Set kann beliebige Icons enthalten — von einem einzigen bis zu tausenden.

Das Formular hat zwei Modi:

### Modus A — Freies Hochladen

Der Nutzer lädt SVG-Dateien einzeln hoch. Für jede Datei:

```
[Datei wählen]  →  [Vorschau]  Name: [__________]  Dark-Variante: [Datei wählen]
```

- **Name** = Icon-Name (= Dateiname ohne `.svg`), automatisch aus dem Dateinamen übernommen, editierbar
- **Dark-Variante** optional: eine zweite SVG für dunklen Hintergrund (wird als `name-dark.svg` gespeichert)
- **Löschen-Button** pro Slot

Es gibt einen **"Alle hochladen"**-Button — mehrere SVGs auf einmal auswählen, alle werden als Slots angelegt.

### Modus B — Synthesizer-gestützt

Wenn ein Dienst mit Rolle `synthesizer.structured` (oder `synthesizer.image`) aktiv ist, erscheint der Button **"Mit Synthesizer erstellen"** im Formular-Header.

→ Vollständige Beschreibung: [Synthesizer-Konzept](../../konzepte/synthesizer.md)

**Icon-Set-spezifisch:** Der Synthesizer bekommt als Kontext:

```toml
[context]
type    = "icon-set"
style   = "outline"     # aus dem Metadaten-Formular
size    = 24
names   = ["kanidm", "forgejo", "nextcloud", ...]  # optional: gewünschte Icons
```

Der Synthesizer gibt N Vorschläge zurück — jeder Vorschlag enthält SVG-Code für die angeforderten Icons. Der Nutzer sieht eine Grid-Vorschau pro Vorschlag und wählt per Checkbox aus, welchen er übernehmen möchte.

---

## Dark-Varianten

Das Formular zeigt immer zwei Spalten nebeneinander:

```
[Icon-Name]  [Light SVG]  [Vorschau hell]  │  [Dark SVG]  [Vorschau dunkel]
```

Wenn `has_dark_variants` aktiviert ist, wird die Dark-Spalte eingeblendet. Die Dark-Variante ist pro Icon optional — fehlt sie, zeigt das System die Light-Variante auf dunklem Hintergrund.

---

## Vorschau

Jeder hochgeladene Icon wird sofort inline als SVG gerendert — auf zwei Hintergründen:

```
[Hell ██] [Dunkel ██]
```

Damit sieht man sofort ob der Icon auf beiden Hintergründen lesbar ist.

---

## Minimum-Empfehlung

Es gibt keine Pflicht-Icons — aber das Formular zeigt einen Hinweis wenn weniger als 10 Icons hochgeladen wurden:

> "Ein Set mit weniger als 10 Icons ist normalerweise kein vollständiges Set. Das ist OK für ein Test-Set, aber nicht empfehlenswert für die Veröffentlichung."

---

## Speichern & Veröffentlichen

| Aktion | Voraussetzung |
|---|---|
| **Lokal speichern** | Immer möglich |
| **In Repository pushen** | Nutzer hat `icon-set.publish`-Berechtigung auf dem Ziel-Repository |

Beim Speichern:
1. Verzeichnis `{set-id}/` wird angelegt
2. Alle SVGs werden dort abgelegt (`name.svg`, `name-dark.svg`)
3. Der globale `manifest.toml` im Icons-Repo wird um einen `[[set]]`-Eintrag erweitert

Beim Pushen:
1. Git-Commit mit Autor-Info wird erzeugt
2. Push zum Ziel-Repository

---

## manifest.toml — generiertes Format

```toml
[[set]]
id              = "my-icons"
name            = "My Icons"
description     = "Clean outline icons for self-hosted services"
author          = "Username"
version         = "1.0.0"
has_dark_variants = true
source_repo_id  = "freesynergy-icons"
builtin         = false
```

---

## Verzeichnisstruktur

```
FreeSynergy.Icons/
├── manifest.toml
├── my-icons/
│   ├── kanidm.svg
│   ├── kanidm-dark.svg
│   ├── forgejo.svg
│   ├── forgejo-dark.svg
│   └── ...
```

---

Weiter: [Icon Manager](README.md) | [Cursor Manager erstellen](cursor-manager.md) | [Synthesizer-Konzept](../../konzepte/synthesizer.md)
