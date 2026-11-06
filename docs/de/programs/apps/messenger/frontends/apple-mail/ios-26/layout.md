# Apple Mail iOS 26 — Layout

✅ = in einem Screenshot gesehen · ⚠️ = erschlossen.

## Fensteraufbau

```
┌──────────────────────────────┐
│ 09:41            ▮▮ ≋ ▭     │ status bar
│ (‹)          [Select] (…)    │ floating round glass buttons
│ Inbox                        │ large title
│ iCloud · updated just now    │ subtitle
│ [● Primary] (🛒) (💬) (📣) … │ category chips (scroll sideways)
├──────────────────────────────┤
│ (av) Sender           09:15 ›│
│      Subject 🍳              │ list rows
│      preview, two lines …    │
│ ★(av) Sender          08:32 ›│ VIP star outside the row
│ ……                           │
│                              │
│ (≡)  ( 🔍 Search      🎙 ) (✎)│ floating bottom bar: filter · search · compose
└──────────────────────────────┘
```

## Bereiche

### Kopfleiste
Schwebende runde Schaltflächen auf der Glasebene: zurück zu den Mailboxen, „Select“, Mehr (…) ✅. Keine feste Navigationsleiste; der Inhalt scrollt darunter ✅. Unsere Entsprechung: `widgets/navigation/toolbar` (schwebende Variante).

### Titelblock
Großer fetter Titel (Mailbox-Name) mit einem kleinen grauen Untertitel (Konto, letzte Aktualisierung) ✅.

### Kategorie-Chips
Eine waagerechte Reihe von Kapseln: Der aktive ist blau gefüllt mit Symbol und Beschriftung, die anderen grau nur mit Symbol ✅. Unsere Entsprechung: `widgets/navigation/tabs` (Chip-Variante) / `button-group`.

### Nachrichtenliste
Zeilen über die volle Breite mit rundem Avatar (Foto oder Memoji), Absender fett, Zeit und Chevron rechts, Betreff, zwei Zeilen Vorschau; feine Trennlinien, bis zum Text eingerückt ✅. Der VIP-Stern sitzt im linken Rand ✅. Unsere Entsprechung: `widgets/data/list-view`.

### Untere Leiste
Drei schwebende Elemente: Filter-Schaltfläche, Suchkapsel mit Mikrofon, Verfassen-Schaltfläche ✅. Unsere Entsprechung: `primitives/fields/search-field` + `primitives/actions/button` (rund).

### Nachrichtenansicht
Oben: Zurück-Schaltfläche mit einer Zähler-Kapsel (z. B. Anzahl im Posteingang), Pfeiltasten nach oben/unten ✅. Zeile „1 E-Mail“ und eine Schaltfläche Zusammenfassen ✅. Kopfzeile: Avatar, Absender, „an“ mit Chevron, Zeit, Markierung ✅. Darunter der Inhalt ✅. Unsere Entsprechung: NEU `mail-view`.

### Sheets
Untere Sheets mit abgerundeten oberen Ecken für: Nachrichtenaktionen (2×2-Kacheln + Liste + Farbzeile) ✅, Verschieben in Mailbox ✅, Kontaktkarte (in der Farbe des Kontakts getönt) ✅, Über Kategorien ✅. Unsere Entsprechung: `widgets/overlays/drawer` (unteres Sheet).

### Bildschirm Mailboxen
Großer Titel „Mailboxen“, Untertitel „gerade aktualisiert“, eine gruppierte Kartenliste; im Bearbeitungsmodus Häkchenfelder und Ziehgriffe, „Fertig“ als gefüllte blaue Kapsel, „Neue Mailbox“ als schwebende Kapsel ✅.

## Responsiv / mobil
Diese Version *ist* das Telefon-Layout. Am Mac ✅ (aktuelle Version): drei Spalten — Seitenleiste mit Abschnitten (Favoriten, Intelligente Mailboxen, Konten), Liste mit Kategorie-Reitern, Lesebereich — und eine Werkzeugleiste mit Symbolgruppen in Glaskapseln; Fenstersteuerung (Ampelknöpfe) oben links ✅. iPad ⚠️ (nicht gesehen).
