# KAddressBook - Struktur und UI/UX

## Fensterstruktur

```
┌───────────────────────────────────────────────────────────────────┐
│ Datei Bearbeiten Ansicht Adressbuch Werkzeuge Einstellungen Hilfe │
│ [🆕][✎][🗑]                    🔍 Suchen…                          │
├─────────────┬───────────────────────────┬─────────────────────────┤
│ Adressbuch- │ Kontaktliste (Tabelle)    │ Detailansicht           │
│ baum        │ ☐ Name  E-Mail  Tel       │ ┌─────────────────────┐ │
│ ● Persönlich│ ☐ Berg, A.  a@…   +49…    │ │ [Foto] Andrea Berg  │ │
│ ○ Arbeit    │ ☐ Klein, B. b@…   +49…    │ │ ✉ a@…               │ │
│ ☁ CardDAV   │                           │ │ ☎ +49…              │ │
│ ☁ LDAP      │                           │ │ ★ Geburtstag        │ │
│             │                           │ └─────────────────────┘ │
└─────────────┴───────────────────────────┴─────────────────────────┘
```

- Aufteilung 3-Spalten; Detailpanel mit Reiter „Details“, neuere Versionen mit Inline-Bearbeitung
- Schnellauswahl-Leiste (links unten) zeigt favorisierte Kontakte als Buttons

## UI/UX

- Qt-Widgets-Klassik, folgt Breeze/Fusion-Design; System-Hell/Dunkel
- Spalten frei wählbar und sortierbar (Klick auf Kopfzeile)
- Schriftgrößen-Adjustment wie im Rest von KDE

## Interaktionen

- **Drag & Drop**: Kontakte zwischen Adressbuch-Ordnern ziehen (Move/Copy je nach Rechte)
- **Rechtsklick**: Kontextmenü (Bearbeiten, vCard speichern, Löschen)
- **Doppelklick**: Detail-Editor
- **Animationen**: praktisch keine (Desktop-Klassik)

## Responsive Design

Nicht responsiv — Desktop-Fenster; auf hohen DPI skalieren Qt-Fonts automatisch.

## Accessibility

- Qt-Accessibility: Tabellen, Formulare, Menüs vollständig benannt; Access-Keys (`Alt+F` …)
- Screenreader-taugliche Editoren; Detailfeld-Beschriftungen vorhanden
- Shortcuts in [shortcuts.md](shortcuts.md) vollständig bedienbar — Mausalternativen stets vorhanden

## Editor-Struktur

- Kontakt-Editor mit Sektionsreitern; Felder mit „+“-Menü nach Kategorien (Telefon-Typen WORK/CELL, Adresse Typen)
- vCard-Rohansicht als Textfeld in „Kontakt importieren/Debug“ (Entwicklerpfad)
