# TODO-Liste

[← Zurück zum Index](../INDEX.md) | [Bugs](BUGS.md)

**Regeln:**
- Jeder Punkt wird KOMPLETT umgesetzt. Keine Stubs.
- IMMER `cargo build` vor und nach jeder Änderung.
- Altes das nicht passt → LÖSCHEN und neu machen.
- Kein Menüpunkt ohne Funktion. Kein Button der nichts tut.

---

## Phase A: Fundament (MUSS ZUERST)

```
A1. [ ] SQLite-Speicherung implementieren
    - fsn-shared.db: übergreifende Settings (key/value, i18n-Auswahl, Audit-Log)
    - fsn-desktop.db: Widget-Positionen, Shortcuts, Profil, Layout, aktives Theme
    - fsn-conductor.db: Service-Konfigurationen, Quadlets, Variablen
    - fsn-store.db: Installierte Pakete, Versionen, Cache
    - fsn-core.db: Hosts, Projekte, Einladungen, Federation
    - Tabellen definieren, Migrations, SeaORM-Entities
    - JEDE Einstellung die der User macht MUSS in SQLite landen
    - Beim Start: DB lesen → UI befüllen

A2. [ ] Window X-Button fixen
    - Testen: Fenster bei jeder Größe schließbar
    - with_decorations(true) ODER Custom-Chrome korrekt implementieren

A3. [ ] FsnObject-System implementieren (siehe technik/ui-objekte.md)
    - Basis-Struct: Position, Größe, State, Sidebar-Items
    - Resize: 5px Toleranz, alle 4 Kanten + 4 Ecken, Fullscreen-Overlay
    - Drag: Am Kopf/Titelleiste, Fullscreen-Overlay
    - Minimize: → Icon mit pulsierendem grünem Punkt
    - Close: Unsaved-Changes-Dialog
    - Object-Sidebar: Icons wenn nicht gehovert, Icons+Text wenn gehovert
    - EINMAL definieren, für Window/Widget/Modal/Panel nutzen

A4. [ ] Scrollbars global
    - .fsn-scrollable CSS-Klasse (dünn, unauffällig)
    - Auf JEDEN Container anwenden der überlaufen kann
    - Settings, Store, Dropdowns, Modals, Listen, Sidebar, Hauptcontent
```

## Phase B: Theme-System reparieren

```
B1. [ ] CSS-Variablen-System bereinigen
    - Namenskonvention definieren (siehe technik/css.md)
    - Shared-Themes OHNE Prefix speichern
    - Programm-spezifische Themes MIT Prefix speichern
    - Parser: prüft ob alle Pflicht-Variablen gesetzt sind

B2. [ ] Kontraste fixen (WCAG AA minimum)
    - JEDE Theme prüfen: Text auf Hintergrund mindestens 4.5:1
    - Text-Muted mindestens 3:1
    - Alle 5 Themes überarbeiten
    - Kontrast-Check als Tool/Script

B3. [ ] Theme-Prefixing implementieren
    - Beim LADEN: Theme-Manager fügt Prefix hinzu (--fsn- für Desktop)
    - Beim SPEICHERN im Store: kein Prefix
    - Andere Programme (Wiki.rs) können eigenen Prefix nutzen (--wiki-)

B4. [ ] Theme-Editor in Settings
    - Einzelne Aspekte ändern (Farben, Button-Stil, etc.)
    - Live-Preview
    - Als neues Theme speichern
    - In den Store hochladen können (mit Metadaten)

B5. [ ] Theme-Aspekte konfigurierbar
    - Window-Chrome (MacOS, KDE, Windows, Minimal)
    - Button-Style (Rounded, Square, Pill, Flat)
    - Animationen (Dauer, Easing, an/aus)
    - Mauszeiger (Standard, Custom)
```

## Phase C: Store funktionsfähig machen

```
C1. [ ] Store-Catalog TOML fixen
    - Parse-Fehler beheben
    - Fehlerbehandlung: Freundliche Meldung + Retry

C2. [ ] Sprachen installierbar
    - .ftl-Dateien aus Store laden → in locales/{lang}/ speichern
    - In fsn-store.db registrieren
    - Nur installierte Sprachen im Dropdown
    - Englisch immer vorinstalliert

C3. [ ] Themes installierbar
    - Theme aus Store laden → In fsn-store.db registrieren
    - Live-Wechsel
    - Bei Wechsel: Fragen ob altes Theme gelöscht werden soll

C4. [ ] Widgets installierbar
    - Widget-Definition laden → registrieren
    - Im "Add Widget"-Dialog verfügbar

C5. [ ] Store-UI: Alle Pakettypen
    - Tabs: All | Modules | Languages | Themes | Widgets | Bots | Tasks
    - Jedes Paket: Icon, Name, Version, Tags, Beschreibung
    - Detail-View bei Klick
    - Install/Update/Remove Buttons
    - Suche über Tags
```

## Phase D: Widgets & Desktop

```
D1. [ ] DraggableWidget-Komponente (basierend auf FsnObject)
    - Position in SQLite speichern/laden

D2. [ ] ResizableContainer-Komponente (basierend auf FsnObject)
    - Größe in SQLite speichern/laden

D3. [ ] Widget-Bearbeitungsmodus
    - Rechtsklick → "Edit Desktop"
    - Drag, Resize, Add, Remove, Background
    - "Done" / "Cancel"

D4. [ ] Desktop-Hintergrund
    - Bild hochladen (FileEngine)
    - URL eingeben
    - Farbe/Gradient wählen
    - In SQLite speichern

D5. [ ] Basis-Widgets
    - Clock-Widget
    - System-Info-Widget
    - Messages-Widget (Placeholder)
    - My-Tasks-Widget (Placeholder)
```

## Phase E: Conductor neu bauen

```
E1. [ ] Alten Conductor-Code LÖSCHEN
    - Alles mit podman.sock → weg
    - Alles mit bollard → weg

E2. [ ] YAML-Parser
    - Docker-Compose YAML einlesen
    - Services, Subservices, Volumes, Networks, Ports
    - Subservices = gehören zum selben Paket

E3. [ ] Variablen-Analyse
    - Typ-Erkennung (*_HOST, *_PASSWORD, *_URL, ...)
    - Rollen-Erkennung mit Ober-/Unterrollen
    - Redis-kompatible: Redis, Dragonfly, KeyDB, Valkey
    - Datenbanken: Postgres, MySQL, MariaDB, MongoDB, SQLite, CockroachDB
    - Cache: Redis, Dragonfly, Memcached, KeyDB, Valkey
    - Konfidenz-Angabe
    - Einheitliches Pattern-Matching (mit _ und ohne _)

E4. [ ] Dry-Run + Validierung
    - Syntax-Check
    - Healthcheck vorhanden? (Warnung)
    - Netzwerke korrekt? (Warnung bei ungenutzten)
    - Port-Konflikte?

E5. [ ] Quadlet-Generator
    - YAML → .container-Dateien
    - Tera-Templates für Configs
    - Kein Podman-Socket — nur Dateien + systemctl

E6. [ ] Store-Integration (optional)
    - "Kennt Store diesen Service?" → Ergänzen, NICHT überschreiben
    - Bei Fehler: Fragen ob automatisch repariert werden soll
    - Offline: Funktioniert auch ohne Store
```

## Phase F: Lenses

```
F1. [ ] Lens-Datenmodell
    - Name, Suchbegriff/Thema, Service-Filter, Layout
    - In SQLite speichern

F2. [ ] Lens-View
    - Ergebnisse aus Services zusammenstellen
    - Gruppiert nach Service-Rolle
    - Jedes Ergebnis: Summary + Link zum Original

F3. [ ] Lens als Desktop-Icon
    - Lens auf Desktop platzieren
    - Klick → Lens öffnet sich als Fenster (FsnObject)
```

## Phase G: Search

```
G1. [ ] Search-View im Desktop
    - Suchfeld (global, Shortcut: Ctrl+K oder konfigurierbar)
    - Ergebnisse nach Service gruppiert
    - Relevanz-Sortierung
    - Preview + Link zum Original + Quelle (Service, Host, Projekt)

G2. [ ] Service-Suche (Ebene 1)
    - Jeder Service durchsucht seine eigenen Daten
    - Normalisiertes Ergebnis-Format

G3. [ ] Host-Suche (Ebene 2)
    - Bus aggregiert Service-Ergebnisse
    - Deduplizierung

G4. [ ] Föderale Suche (Ebene 3-4)
    - Nur Services mit search-Recht
    - Über API zwischen Projekten/Föderationen
```

## Phase H: Bots

```
H1. [ ] Bot-Framework Grundstruktur
    - BotDefinition laden, BotConfig in SQLite

H2. [ ] Broadcast-Bot
    - Telegram zuerst (teloxide)
    - Nachricht → an alle Gruppen senden

H3. [ ] Gatekeeper-Bot
    - Telegram-Join-Event → Verifikation → Approve/Deny
```

## Phase I: Tasks

```
I1. [ ] Data Offers/Accepts System
I2. [ ] Task Builder UI (Feld-Mapping)
I3. [ ] Task-Templates aus Store
```

## Phase J: Node (Invite, Federation)

```
J1. [ ] Invite-System
    - Token generieren + verschlüsselte TOML-Datei
    - Port pro Einladung (öffnen/schließen)
    - Validate + Join-Prozess

J2. [ ] Federation-Grundstruktur
    - Beitritt (Einladung oder Anfrage)
    - Domain-Pflicht für Föderationen
    - Subdomain-Routing
    - Auth-Broker (OAuth2 Proxy)

J3. [ ] Rechte-Kaskade
    - read, write, execute, search pro Service
    - Weitergabe: gleich oder weniger, nie mehr
    - Audit-Log für jede Änderung
    - Warnung bei umfangreichen Freigaben
```

## Phase K: Shortcuts, Menü, Profil, Polish

```
K1. [ ] Action Registry (jede Aktion hat ID + Default-Shortcut)
K2. [ ] Konfigurierbare Shortcuts in Settings
K3. [ ] Hilfe: Auto-generierte Shortcut-Referenz
K4. [ ] Menü: JEDER Punkt ruft echte Aktion auf
K5. [ ] Profil: IAM-Daten + editierbare Felder + Account-Linking
K6. [ ] Notification Bell
K7. [ ] Context-Menüs
K8. [ ] Animationen konfigurierbar
K9. [ ] Alle Stubs/toten Code entfernen
```

---

## Reihenfolge

```
Prio 1: A1-A4     (Fundament: SQLite, X-Button, FsnObject, Scrollbars)
Prio 2: B1-B5     (Theme-System reparieren + Kontraste)
Prio 3: C1-C5     (Store funktionsfähig)
Prio 4: D1-D5     (Widgets & Desktop)
Prio 5: E1-E6     (Conductor neu)
Prio 6: F1-F3     (Lenses)
Prio 7: G1-G4     (Search)
Prio 8: H1-H3     (Bots)
Prio 9: I1-I3     (Tasks)
Prio 10: J1-J3    (Node Invite + Federation)
Prio 11: K1-K9    (Polish)
```
