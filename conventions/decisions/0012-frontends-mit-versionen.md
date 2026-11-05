# 0012 – `masks/` wird `frontends/`, mit Versionsordner

Status: akzeptiert (2026-11-05) · ersetzt **0007**

## Kontext
Unter jeder Programmkategorie liegt pro analysiertem Fremdprogramm ein Ordner mit sieben Dateien
(`masks/<programm>/`). Zwei Lücken: (1) „Maske“ ist kein Begriff, den Außenstehende verstehen —
gemeint ist die Oberfläche, die jemand auf unsere Schnittstelle setzt, also ein **Frontend**.
(2) Programme ändern sich; ohne Version ist nicht erkennbar, *welcher* Stand beschrieben ist.
Der Dateisatz entstand aus einer Vorüberlegung mit Brave Leo und wurde angepasst.

## Entscheidung

### Begriff
- **Frontend** = Oberfläche (Aufteilung, Menüs, Interaktion, Tastenkürzel) auf unserer
  Schnittstelle. Austauschbar; das Programm kennt kein Frontend (Protokoll §2/§3 gelten weiter,
  dort „Maske“ → „Frontend“ lesen).
- **Theme** = Aussehen (Farben, Abstände, Typografie, Formen). Getrennt vom Frontend.

### Pfad
```
docs/en/programs/<level>/<category>/frontends/<program>/<version>/<files>
```
`<program>` = das analysierte Produkt (`element`, `outlook`), `<version>` so, wie der Hersteller
sie nennt (`1.11`, `2024`). **Protokolle sind keine Programme**: Matrix, IMAP, JMAP, CalDAV,
ActivityPub gehören nach `data/` (Standards), ihre Clients nach `frontends/`.

### Dateisatz eines Frontends
```
frontends/<program>/
├── index.md            Pflicht · was es ist, Einordnung, warum es hier steht (besondere Ideen),
│                                 Liste der dokumentierten Versionen
├── changelog.md        bei ≥2 Versionen · was sich zwischen den Versionen ändert
└── <version>/
    ├── description.md  Pflicht · ausführliche Beschreibung
    ├── features.md     Pflicht · was das Programm kann (ohne unseren Umsetzungsstatus)
    ├── layout.md       Pflicht · Raster, Panels, Spalten, Fensteraufbau
    ├── menus.md        Pflicht · Menüstruktur, Kontextmenüs, Menüs nach Rolle
    ├── shortcuts.md    Pflicht · Tastenkürzel
    ├── api.md          Pflicht · welche API/Protokolle, Auth, Rate-Limits
    ├── themes/         Pflicht · index.md + je Theme eine Datei: Farben, Typografie, Abstände,
    │                             CSS-Variablen/Tokens, was man nachbauen kann und was nicht
    ├── interaction.md  bei Bedarf · Hover, Fokus, Drag, Gesten (Finger, Maus, Stift)
    ├── states.md       bei Bedarf · UI-Zustände und Übergänge
    ├── events.md       bei Bedarf · Ereignisse nach außen (Webhooks, Push, Streams)
    ├── limits.md       bei Bedarf · bekannte Einschränkungen
    ├── i18n.md         bei Bedarf · Lokalisierung, Schriftrichtung
    └── dependencies.md bei Bedarf · welche **unserer** Components ein Frontend in diesem Stil braucht
```
- Kein `version.md` — der Ordnername ist die Version.
- `features.md` beschreibt das **Fremdprogramm**. Ob **wir** etwas umgesetzt haben, steht nur in
  `programs/<level>/<category>/requirements.md` (Status `implemented`/`planned`/`proposed`).
- Alte Namen: `menu.md` → `menus.md`, `structure.md` → `layout.md` (UI/UX-Teile nach
  `interaction.md`, Farbschema nach `themes/`).

### Suiten
```
docs/en/programs/suites/<category>/frontends/<suite>/
├── index.md       was die Suite ist, welche Apps, welche Plattform, Versionen
└── <version>/
    ├── apps.md    NUR Links auf die App-Frontends (../../../../../apps/<category>/frontends/<program>/)
    └── shared/    nur was die Suite NEU bringt: auth.md, sync.md, <service>-api.md, …
```
Keine Symlinks (Git/MkDocs-Probleme), keine Doppelbeschreibung.

## Folgen
- Umbau per Skript in `en/`: `masks/` → `frontends/`, Programmordner bekommen einen
  Versionsordner, Dateien werden umbenannt; danach `scripts/fix_links.py --force` und
  `mkdocs build`. `de/` folgt mit demselben Skript.
- `scripts/gen_skin_indexes.py` → `scripts/gen_frontend_indexes.py`.
- `conventions/doku-standard.md` Abschnitt „6-File-Per-Program“ wird durch diesen Dateisatz ersetzt.
- Vorlage: `conventions/templates/frontend/`.
