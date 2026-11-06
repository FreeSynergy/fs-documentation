# Outlook m365-2026-11 — Layout

✅ = in einem Screenshot gesehen · ⚠️ = erschlossen. Desktop = neues Outlook für Windows und Web (gleiche Oberfläche).

## Fensteraufbau

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│ [logo] Outlook        [ Search ……………… ]      ◇ ☑ 🔔 ⚙ 💡 (avatar)   [next event] │ title bar
├──┬───────────────────────────────────────────────────────────────────────────────┤
│  │ ≡  Home  View  Help                                                          │ ribbon tabs
│A │ [New mail ▾] Delete Archive Report Sweep Move… ↶ ↶↶ ↷ QuickSteps Read … [AI] │ ribbon (1 line)
│P ├───────────────┬────────────────────────┬────────────────────────────────────┤
│P │ Favourites    │ Focused | Other   ⚲ ⇅  │ Subject                      ⧉ ✕  │
│  │  Inbox     11 │ ▾ Pinned               │ ┌ AI summary card ────────────────┐ │
│R │  Invoices     │   row (pinned)         │ └─────────────────────────────────┘ │
│A │ ▾ account 1   │ ▾ Today                │ sender · to · time   ↶ ↶↶ ↷ …     │
│I │  Inbox     11 │   row  row  row        │ body                               │
│L │  Drafts …     │ ▾ Yesterday            │                                    │
│  │ ▸ account 2   │   row + [date · RSVP]  │                                    │
│  │ + Add account │                        │                                    │
└──┴───────────────┴────────────────────────┴────────────────────────────────────┘
  app rail          folder pane              message list              reading pane
```

## Bereiche

### Titelleiste
Produktname, ein breites **Suchfeld** in der Mitte, dann Symbol-Schaltflächen: Premium-Angebot, Mein Tag / Aufgaben, Benachrichtigungen (Glocke mit Punkt), Einstellungen, Tipps, Profilbild; ganz rechts ein **Chip für den nächsten Termin** („nächstes Meeting in 30 Min.“, mit 1/2-Pager bei mehreren Terminen) ✅.
Unsere Entsprechung: `widgets/navigation/toolbar` + `primitives/fields/search-field` + `widgets/data/avatar`.

### App-Leiste (ganz links)
Eine schmale Symbolspalte, die zwischen Mail, Kalender, Copilot, Personen, Gruppen, Aufgaben, Word, Excel, PowerPoint, OneDrive und „weitere Apps“ umschaltet ✅. Das ist der Suite-Umschalter (ADR 0038, Suite-Kontext).
Unsere Entsprechung: `widgets/navigation/sidebar` (eingeklappt) — bei FreeSynergy die Shell, nicht der Messenger ⚠️.

### Menüband
Drei Registerkarten am Desktop (Home, View, Help) ✅; der Verfasser ergänzt Nachricht, Einfügen, Text formatieren, Optionen ✅. Einzeiliges „vereinfachtes“ Menüband; Gruppen durch dünne Trennlinien getrennt; Überlauf unter „…“ und ein Chevron, um auf das klassische zweizeilige Menüband zu erweitern ✅. Geteilte Schaltflächen (Neue E-Mail ▾, Senden ▾, Löschen ▾) ✅. Klassisches Outlook: volles Menüband mit Datei, Start, Senden/Empfangen, Ordner, Ansicht, Hilfe (+ Add-in-Registerkarten) ✅.
Unsere Entsprechung: `widgets/navigation/toolbar` (Menüband-Variante mit `tabs`).

### Ordnerbereich
Einklappbare Abschnitte: **Favoriten** (kontoübergreifend), danach je ein Baum pro Konto mit Posteingang, Entwürfe, Gesendete Elemente, Gelöschte Elemente, Junk-E-Mail, Archiv, Notizen, Benutzerordner, Suchordner und dem Ordner „zurückgestellt“ ✅; Zähler für ungelesene Mails rechtsbündig ✅; Link „Konto hinzufügen“ unten ✅; kann im Reiter Ansicht ausgeblendet werden ✅.
Unsere Entsprechung: `widgets/data/tree-view` + `primitives/feedback/badge`.

### Nachrichtenliste
Kopfzeile mit den Reitern Fokussiert / Andere, einem Umschalter für den Auswahlmodus, Filter- und Sortiersymbolen ✅. Einklappbare Gruppen (Angeheftet, Heute, Gestern, Dieser Monat) ✅. Eine Zeile: Avatar, Absender, Betreff (blau bei ungelesen), Zeit, Vorschauzeile, optionale Chips (Besprechung mit RSVP, Kategorie-Tag), Statussymbole (angeheftet, markiert, Kalender, @, Anhang), Chevron zum Aufklappen der Unterhaltung, blauer linker Balken bei ungelesen ✅. Ausgewählte Zeile: hellblauer Hintergrund ✅; markierte bzw. hervorgehobene Zeile: blassgelber Hintergrund ✅.
Unsere Entsprechung: `widgets/data/list-view` (Zeilen `With Avatars` / `With Badges`) + `widgets/navigation/tabs`.

### Lesebereich
Betreffzeile mit Ausklappen und Schließen; optionale KI-Zusammenfassungskarte; pro Nachricht ein Kopf (Avatar mit Präsenz, Absender, Empfänger, Zeit) mit Antworten / Allen antworten / Weiterleiten / Mehr; Inhalt; Antwortblock für Einladungen ✅. Kann rechts, unten oder ausgeblendet platziert werden ⚠️ (Option Ansicht → Lesebereich gesehen ✅, Positionen nicht gesehen).
Unsere Entsprechung: NEU `mail-view` + `widgets/containers/panel`.

### Verfasser (eingebettet oder als eigenes Fenster)
Eingebettet im Lesebereich oder als eigenes Fenster ✅: Senden-Split-Schaltfläche, Auswahl „Von“, An/Cc (Bcc auf Abruf) mit Chips, Betreff, Hinweis „Entwurf gespeichert um …“, Inhalt; Zoom-, Ausklapp- und Verwerfen-Symbole rechts ✅.
Unsere Entsprechung: NEU `composer` + `rich-text-editor` + `tags-input` (Empfänger).

### Statusleiste (nur klassisch)
Anzahl der Elemente und ungelesenen Mails, Erinnerungen, Offline-Anzeige, Ansichtsumschalter und Zoom-Regler; jedes Element lässt sich über ein Kontextmenü ein- und ausblenden ✅.

### Einstellungsdialog
Ein großer modaler Dialog mit drei Spalten: Kategorien (Konten, Dateien, Allgemein, E-Mail, Kalender, Personen, Copilot) mit einem Suchfeld für Einstellungen, Unterseiten, Inhalt; Speichern / Verwerfen unten ✅.
Unsere Entsprechung: Einstellungen der App-Shell (`sidebar` + `field` + `switch` + `select`).

## Responsiv / mobil
Telefon-App ✅: farbiger Kopf (oder Bild-Theme) mit Kontotitel, Glocke und Suche; segmentierter Umschalter Fokussiert/Andere und eine Filter-Schaltfläche; einspaltige Liste; schwebende Schaltfläche „Neue E-Mail“ mit Chevron für weitere neue Elemente; untere Navigation (Mail, Kalender, Feed, Apps — oder Mail, Suche, Kalender in einem anderen Zustand) ✅. Hinweis unten im Toast-Stil („neues Design“, mit einer Aktion) ✅.
Ältere Tablet-/Web-Ansicht zeigt dieselben drei Bereiche mit farbiger oberer Leiste ✅.
