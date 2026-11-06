# Apple Mail iOS 26 — Interaktion

✅ = gesehen · ⚠️ = erschlossen. Gesten gehören zum Frontend, nicht zum Verfasser (ADR 0037).

## Hover und Fokus
- Nicht anwendbar auf dem Telefon. Am Mac: Fokusring am Suchfeld ✅; Hover nicht gesehen ⚠️.
- Lupen-Callout in Apples Hilfebildern ist eine Illustration, kein UI-Merkmal ✅.

## Ziehen und Ablegen
- Intelligente Mailboxen per Ziehgriff im Bearbeitungsmodus neu ordnen ✅.
- Mails auf Mailboxen ziehen ⚠️ (bekannt auf iPad/Mac, nicht gesehen).

## Gesten

### Finger
- **Zeile nach links wischen** → die Zeile gleitet und zeigt drei runde Schaltflächen mit Beschriftung: Mehr (grau), Markieren (orange), Löschen (rot) ✅. Ein volles Wischen löst die letzte Aktion aus ⚠️.
- **Zeile nach rechts wischen** → als gelesen/ungelesen markieren ⚠️ (nicht gesehen).
- **Zeile lange drücken** → angehobene Vorschau der Mail plus ein Menü (Antworten, Allen antworten, Weiterleiten, Markieren, Benachrichtigen, Stummschalten) ✅.
- **„Auswählen“ antippen** → Mehrfachauswahl-Modus; danach öffnet „Verschieben“ ein Sheet mit gestapelter Vorschau ✅.
- **Kategorie-Chip antippen** → filtert den Posteingang ✅; Chips scrollen seitlich ⚠️.
- **Pfeiltasten nach oben/unten** in einer geöffneten Mail antippen → nächste/vorherige Mail ✅.
- **Absender antippen** → Kontaktkarten-Sheet ✅.
- **Markierungsfarbe** im Aktionsblatt antippen → Mail wird in dieser Farbe markiert ✅.
- **Mikrofon in der Suchkapsel** → Suche diktieren ✅.
- Sheet nach unten wischen zum Schließen; zum Aktualisieren herunterziehen ⚠️.

### Maus (macOS) ✅
- Werkzeugleisten-Schaltflächen, Menüs, Dropdown mit Suchvorschlägen; geteilte Ansicht aus Seitenleiste, Liste und Lesebereich.

### Stift
- „Skizze hinzufügen“ von einem nahen iPad in den Mac-Verfasser ✅ (Anhang-Menü) — Stifteingabe über Continuity.
