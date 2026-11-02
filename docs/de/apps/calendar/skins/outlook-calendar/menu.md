# Outlook-Kalender – Menü- und Navigationsstruktur (Stand: 2026-11-02)

Belegt durch zwei offizielle support.microsoft.com-Artikel: „Keyboard shortcuts for Outlook“ (Reiter *New Outlook* / *Classic Outlook* / *Outlook on the web*) und „Use a screen reader to explore and navigate Outlook Calendar“ (beschreibt die Regionen/Layouts explizit). Englische Original-Labels zitiert, deutsche Übersetzung kann abweichen. Fundstellen in [index.md](index.md#quellen).

## Neues Outlook für Windows / Outlook on the web

```
Horizontale Navigationsleiste (oben: Suche mittig; rechts My Day, Benachrichtigungen, Hilfe, Einstellungen)
├── Registratorreiter (Ribbon tabs; "Home" vorausgewählt)
├── Linkes Navigationsfenster
│   ├── "New event"-Button (oben)
│   ├── Datumsauswahl (Date selector)
│   ├── Kalenderliste
│   └── ganz links: Ansichtsumschalter Mail / Calendar / Contacts / To Do
└── Aktueller Kalender (Hauptbereich)
    └── Toolbar oben: Monat/Jahr, zurück/vor, Monats-Picker,
        Ansicht (Day, Work week, Week, Month, Today), Freigabe (Share)
```

- **Registratorreiter „Home“:** u. a. neuer Termin (appointment), Meeting-Anfrage (meeting request), Kalender freigeben (share a calendar) – im Screenreader-Artikel namentlich genannt.
- **Reiter „View“ → „Calendar settings“:** öffnet das Einstellfenster mit Reiter *Calendar > View* und **Unterreitern** (Kategorie-Navigation per Pfeiltasten); belegte Einstellungen: **Arbeitszeiten und Arbeitstage**, **Abwesenheitsnotizen (out-of-office replies)**, **Standard-Erinnerungszeit**.
- **Suche** (oben mittig) findet auch Befehle/Aktionen („type the search words for the action“).
- **Termin-Editor:** `Ctrl+N` öffnet den **Event Composer als eigenes Fenster** (Feld „Add a title“, Tab durch Felder, „Save“-Button; Verwerfen: Alt+F4).
- **My Day / Benachrichtigungen / Hilfe / Einstellungen** in der Kopfzeile (Regionen-Liste des Artikels).
- **Ansichten:** Day, Work week, Week, Month (+ Today-Sprung); per Kürzel zusätzlich 3-Tage- und Listenansicht (siehe shortcuts.md).

## Klassisches Outlook für Windows (Kalendermodul)

```
Registratorreiter (Ribbon tabs oben)
├── Ordnerbereich (Folder pane, links) – "Calendar folders": eigene Kalender,
│   Feiertagskalender des Landes, freigegebene Kalender von Kollegen
├── Aktuelle Kalenderansicht (rechts)
└── Statusleiste (unten)
```

- **Home-Reiter:** neue Terminvereinbarung (appointment), Meeting-Anfrage, Kalender freigeben – namentlich im Artikel.
- **Ordnerbereich:** Kalender per Leertaste ein-/ausblenden, Ordner auf-/zuklappen (Pfeiltasten).
- **Datumsauswahl:** `Ctrl+G` öffnet Date Picker; zurück zu heute `Alt+H, O, D`.
- **Belegte Menüpunkte aus der Kürzel-Liste** (Access-Key-Pfade nennen die Menüs beim Namen):
  - *Freigegebenen Kalender hinzufügen / neuen Kalender anlegen:* `Alt+H,O,C`
  - **Kalender freigeben:** `Alt+H,S,C` · **Kalender online veröffentlichen:** `Alt+H,P,O`
  - **Freigabeberechtigungen des Ordners anzeigen/bearbeiten:** `Alt+H,F,P`
  - **Kalender per E-Mail senden:** `Alt+H,E`
  - **Assistent für die Terminplanung:** `Alt+X` (aus dem Meeting-Fenster)
  - **Erinnerungsfenster:** `Alt+V,M`; Snooze `Alt+S`, Verwerfen `Alt+D`
  - **Schedule nebeneinander (horizontales Layout):** `Alt+H,S,V`
  - **Ansichten:** Tagesraster 1–10 Tage `Alt+1`…`Alt+0`, Monat `Alt+ =`, ganze Woche `Alt+-`, Arbeitswoche `Ctrl+Alt+2`, „Nächste 7 Tage“ `Alt+H,X`
  - **Optionen-Dialog für Kalender:** `Alt+H,C,O`

## Mobile Clients (Outlook für iOS/Android)

- Kalenderansicht mit Monats-/Wochen-/Tagesumschalter und Kalenderliste; Detail-Menüs sind app-intern – **nicht** durch die zitierten Artikel belegt (nur „Outlook for iOS/Android“ als applies-to genannt). daher hier nicht im Detail dokumentiert.

## Server-/Admin-Ebene (Exchange Online)

- Kalender-Organisation erfolgt über **Exchange Admin Center / PowerShell** (Postfächer, Ressourcen, Freigaberichtlinien, Cross-Tenant-Verfügbarkeit) – eigene Produktfläche, nicht Teil der Kalender-App-Menüs; Beleg: Migrationsartikel „Migrate to Microsoft 365 Cross-Tenant Access Policy“ (learn.microsoft.com).

## Grenzen dieses Kapitels

- Die Web-/Client-Menüs ändern sich mit Microsoft-365-Schrittveröffentlichungen („released gradually“ – Hinweis im offiziellen Artikel). Die hier genannten Punkte sind ausschließlich den zitierten offiziellen Artikeln entnommen; nicht belegte Menüpunkte (z. B. „Abonnement hinzufügen“, Geburtstagskalender-Eintrag) wurden weggelassen.
