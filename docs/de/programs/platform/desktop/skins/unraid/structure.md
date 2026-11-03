# Unraid - Struktur & UI/UX

## Übersicht

Unraid zeigt im Browser eine klassische Server-Verwaltungsseite: oben die Tab-Leiste, darunter der Inhalt des aktiven Tabs als Abschnitt mit Tabellen und Formularen. Es gibt keine Fensterverwaltung und keine verschiebbaren Panels — jede Funktion ist eine eigene, komplett neu geladene Seite.

## Fenster-Struktur

### Standardseite (Beispiel Tab *Main*)

```
┌──────────────────────────────────────────────────────────────────────┐
│ Kopf: Unraid-Logo | Main Shares Users Docker VMs Apps Plugins ...    │
│                                   | Glocke | Connect | Hilfe | Logout│
├──────────────────────────────────────────────────────────────────────┤
│ Identification / Statusabschnitt (Gerätename, Update, Anmeldung)     │
├──────────────────────────────────────────────────────────────────────┤
│ Array-Übersicht                                                      │
│ ┌──────────┬──────────┬──────────┬──────────┬──────────┐             │
│ │ PARITY-1 │ DISK 1   │ DISK 2   │ ...      │ CACHE    │             │
│ │ Symbol   │ Symbol   │ Symbol   │          │ Symbol   │             │
│ │ used/tot │ used/tot │ used/tot │          │ used/tot │             │
│ └──────────┴──────────┴──────────┴──────────┴──────────┘             │
├──────────────────────────────────────────────────────────────────────┤
│ Meldungszone (Fehler/Warnungen als farbige Banner)                   │
└──────────────────────────────────────────────────────────────────────┘
```

### Dialog (Beispiel *Add New Share*)

```
┌──────────────────────────────────────────┐
│  Add New Share                    [X]    │
├──────────────────────────────────────────┤
│  Share Name        [____________]        │
│  Security          (public|secure|priv)  │
│  Include/Exclude   [Diskliste]           │
│  Allocation        [____________]        │
├──────────────────────────────────────────┤
│           [Cancel]        [Apply]        │
└──────────────────────────────────────────┘
```

### Container-Ansicht (Tab *Docker*)

```
┌──────────────────────────────────────────────────────────────────────┐
│ Docker: Anwendungssuche | Docker Settings | Add Container            │
├──────────────────────────────────────────────────────────────────────┤
│ ┌────────────┬─────────┬────────┬─────────────────────────────┐      │
│ │ Name       │ Pfad    │ Port   │ Aktionen                    │      │
│ ├────────────┼─────────┼────────┼─────────────────────────────┤      │
│ │ jellyfin   │ /mnt... │ 8096   │ WebPUI | Logs | Console | ..│      │
│ │ sonarr     │ /mnt... │ 8989   │ WebPUI | Logs | Console | ..│      │
│ └────────────┴─────────┴────────┴─────────────────────────────┘      │
└──────────────────────────────────────────────────────────────────────┘
```

## Bereiche

| Bereich | Position | Inhalt |
|---------|----------|--------|
| Tab-Leiste | Oben | Tabs (Main, Shares, Docker, VMs, …) als Seitenwechsel |
| Icon-Menü | Oben rechts | Benachrichtigungen, Connect, Hilfe, Abmelden |
| Status-/Identifikationsteil | Seitenanfang | Geräteinfos, Update- und Anmeldungsstatus |
| Tabellen-/Formularbereich | Mitte | Array-Tabelle, Share-Liste, Container- und VM-Listen |
| Meldungszone | Oben/Unten | Fehler, Warnungen, Erfolgsbanner |
| Dialoge | Overlay | Anlegen/Bearbeiten von Shares, Containern, VMs, Benutzern |
| webVNC-Fenster | Tab VMs | Browser-Konsole der virtuellen Maschine |

## UI/UX

### Design-Prinzipien

- **Tab statt Menübaum**: jeder Aufgabenbereich ist eine eigene Seite, kein verschachteltes Menü
- **Zustand zuerst**: Array-Farben (grün/gelb/rot) und Kapazitätsbalken dominieren die Main-Ansicht
- **Formulare statt Klick-Streaks**: Änderungen fast immer über Bearbeiten-Dialog mit Apply
- **Wenige Overlay-Ebenen**: max. ein Dialog gleichzeitig, keine verschachtelten Panels

### Farbschema und Themes

- Grund-Theme dunkelblau/orange; hell/dunkel und alternative Themes über Identification-Einstellung oder Dynamix-Plugins (versionabhängig)
- Statusfarben sind fest: grün = ok, gelb = Warnung/Anbau, rot = Fehler/Ausfall
- Tabellenzeilen und Buttons folgen einem einheitlichen Dynamix-Stil

### Interaktionen

- **Klick auf Laufwerksymbol**: Detailansicht mit SMART-Werten und Zuweisungsoptionen
- **Drag & Drop**: nur in Ausnahmefällen (Feinsystem-Layout von Plugins), nicht im Kern
- **Bestätigungsdialoge** bei riskanten Aktionen (Array stoppen, Share löschen, Disk zuweisen)
- **Fortschrittsbalken** für Parity Check, Mover und Formatierungen auf der Main-Seite
- **Autocomplete**: App-Store-Suche im Docker-/Apps-Tab

### Responsive Design

- **Desktop**: volle Tabellenbreite, alle Tabs sichtbar
- **Schmale Fenster**: Tabellen scrollen horizontal, Tab-Leiste bleibt oben (kein eigenes Mobil-Layout)
- **Mobil**: bedienbar, aber für Array-Arbeiten ungeeignet; webVNC auf kleinen Screens eingeschränkt
- Browser-Zoom hilft bei dichten Tabellen (versionabhängig)

### Zugänglichkeit

- **Tastatur**: Formularfelder per `Tab` erreichbar, `Enter` löst Standardbuttons aus, `Esc` schließt manche Dialoge
- **Screenreader**: einfache Tabellenstruktur, aber Status läuft stark über Farben und Symbole — Textalternativen ungleichmäßig
- **Fokusanzeige**: Browser-Standard, nicht zusätzlich gestaltet
- **Sprache**: Kern-UI englisch, Übersetzungen über Language-Plugins

### Performance

- **Serverseitiges Rendering**: jeder Tabwechsel lädt die ganze Seite neu — langsam bei vielen Shares/Containern
- **Poling**: Statuswerte (Temperaturen, Parity-Fortschritt) werden in Intervallen nachgeladen
- **Träge Platten**: SMART-Abfragen können Seiten spürbar bremsen, spin-up-verzögerte Laufwerke ebenso
- **Empfehlung**: Plugin-Anzahl und Monitoring-Intervalle bewusst wählen, Log-Suchen einschränken

## Siehe auch

- [menu.md](menu.md) - Tabs und Rollen im Detail
- [features.md](features.md) - Array, Docker, VMs, Plugins
- [shortcuts.md](shortcuts.md) - Tastatursteuerung
- [api.md](api.md) - GraphQL-API und Automatisierung
