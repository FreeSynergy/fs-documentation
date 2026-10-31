# TrueNAS - Struktur & UI/UX

## Übersicht

Die TrueNAS-Weboberfläche (SCALE) ist eine Single-Page-Anwendung: links die Navigations-Sidebar, oben die Leiste mit Suchfeld, Job- und Alarm-Symbolen, rechts der Inhaltsbereich mit Karten, Tabellen und Assistenten. Statuswerte kommen live über WebSockets; lange Aktionen laufen als Jobs mit Fortschrittspanel.

## Fenster-Struktur

### Hauptansicht (Beispiel *Datasets*)

```
┌──────────────────────────────────────────────────────────────────────┐
│ Kopf: TrueNAS-Version | Suchleiste "Search" | Jobs | Glocke | User   │
├──────────────┬───────────────────────────────────────────────────────┤
│ Sidebar      │ Datasets                          [+ Create] [Manage] │
│ ▪ Dashboard  │ ┌───────────────────────────────────────────────────┐ │
│ ▪ Datasets   │ │ tank                 │ 42 % │ ZFS │ [⋮]          │ │
│ ▪ Pools      │ │  ├─ docs             │  3 % │     │ [⋮]          │ │
│ ▪ Shares     │ │  ├─ media            │ 31 % │     │ [⋮]          │ │
│ ▪ Apps       │ │  └─ app_configs      │  8 % │     │ [⋮]          │ │
│ ▪ System     │ └───────────────────────────────────────────────────┘ │
│              │ (Filter, Spaltenauswahl, Statusbanner)                │
└──────────────┴───────────────────────────────────────────────────────┘
```

### Assistent (Beispiel *Create Dataset*)

```
┌──────────────────────────────────────────┐
│  Dataset create            [X]           │
├──────────────────────────────────────────┤
│  Pool   [tank ▾]   Name  [____________]  │
│  (☑) Encryption   (☑) NFS/SMB-Presets    │
│  ▸ Advanced (compression, quota, …)      │
├──────────────────────────────────────────┤
│           [CANCEL]  [CREATE]             │
└──────────────────────────────────────────┘
```

### Job-Panel

```
┌──────────────────────────────────────────┐
│  Tasks                          [✕]      │
├──────────────────────────────────────────┤
│  ✅ Pool scrub      100 %   (2 h)        │
│  ⏳ Replication     42 %   [Abort]       │
│  ❌ Cloud Sync      error  [LOG]         │
└──────────────────────────────────────────┘
```

## Bereiche

| Bereich | Position | Inhalt |
|---------|----------|--------|
| Kopfzeile | Oben | Version/Build, globale Suche, Jobs, Alarme, Benutzer-/API-Menü |
| Sidebar | Links | Navigationspunkte (Datasets, Pools, Shares, Apps, System …) |
| inhaltsbereich | Rechts | Karten, Tabellen, Bäume, Formular-Wizards |
| Aktionsschalter | oben rechts im Inhalt | Create/Add/Manage des aktuellen Bereichs || Drei-Punkte-Menüs | Zeilen/objekte | Kontextaktionen (Snapshots, Edit, Delete) |
| Job-Panel | Overlay rechts | Laufende Middleware-Jobs mit Log-Links |
| Toasts | unten | Erfolg/Fehler nach Aktionen |

## UI/UX

### Design-Prinzipien

- **Ein Bereich pro Bildschirm**: keine Fensterverwaltung, Seitenwechsel über Sidebar
- **Geführte Assistenten**: Pool-/Dataset-/App-Anlage mit Defaults und Warnungen
- **Sichtbare Jobs**: lange Läufe nie unsichtbar — Job-Panel und Statusbanner
- **Zerstörungsschutz**: kritische Aktionen mit Bestätigungsdialog (Manuell tippen bei Gefahr, versionabhängig)

### Farbschema und Themes

- Helles Standard-Schema, Dark Mode je nach Version umschaltbar (Benutzermenü)
- Status: grün = ok/started, blau = Info, gelb = Warnung, rot = Fehler; Alarmglocke mit Zähler
- Akzentfarbe und Dichte bleiben konsistent über NG-ZORRO-Komponenten

### Interaktionen

- **Globale Suche**: findet Seiten, Datasets, Freigaben, Nutzer (seit 23.x, versionabhängig)
- **Bäume**: Dataset-/iSCSI-Bäume mit Aufklappen und Zeilen-Menüs
- **Formulare**: Inline-Validierung, Pflichtfeld-Markierung, Tooltips an Fachbegriffen
- **Live-Tabellen**: Status-Spalten aktualisieren ohne Neuaufbau (WebSocket-Push)
- **Drag & Drop**: praktisch nicht vorhanden — Ausnahmen wie App-Sortierung (versionabhängig)

### Responsive Design

- **Desktop**: Vollayout, Sidebar fix
- **Schmale Fenster**: Sidebar wird Icon-Leiste/Overlay, Tabellen bekommen horizontales Scrolling
- **Mobil**: Bedienung der Kernbereiche funktioniert, Formulare bleiben lang
- **Kioskbetrieb**: Web-UI auf Touch-Monitoren/Displays als gängiges Muster

### Zugänglichkeit

- **Tastatur**: Sidebar-Links, Tabellen und Dialoge per `Tab`/`Enter` erreichbar
- **Screenreader**: ARIA-Rollen auf Dialogen und Menüs; Live-Regionen für Toasts/Jobs
- **Fokusanzeige**: erkennbar, Assistenten setzen Fokus auf das erste Feld
- **Sprache**: UI in vielen Sprachen lokalisiert, DE enthält je nach Version unübersetzte Fachbegriffe

### Performance

- **SPA mit WebSocket-Backend**: Reiterwechsel ohne komplette Neulasten; Initial-Load spürbar (Angular-Bundle)
- **Tabellen-Paginierung**: große Dataset-/Snapshot-Listen werden seitig geladen
- **Job-basiert**: Scrub/Replikation blockieren die UI nicht; Logs bei Bedarf abrufen
- **Empfehlung**: Snapshot-Anzahl pro Dataset begrenzen, Report-Abfragen zeitlich eingrenzen

## Siehe auch

- [menu.md](menu.md) - Seitenstruktur und Rollen
- [features.md](features.md) - Funktionsbereiche
- [shortcuts.md](shortcuts.md) - Tastatur und Konsolenmenü
- [api.md](api.md) - Middleware-API und CLI
