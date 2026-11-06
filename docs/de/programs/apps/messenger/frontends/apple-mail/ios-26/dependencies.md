# Apple Mail iOS 26 — Abhängigkeiten

Welche **unserer** Komponenten ein Frontend in diesem Stil benötigt. Namen aus `temp/messenger-components.md`;
**NEU** = nicht unter unseren 84 Komponenten.

| Bereich / Funktion | Komponente | Ebene |
|------------------|-----------|-----------|
| Großer Titel + Untertitel ✅ | `primitives/basics/heading` ⚠️ + `label` | Primitive |
| Schwebende runde Schaltflächen auf Glas ✅ | `primitives/actions/button` (rund, durchscheinende Variante — Änderung) | Primitive |
| Kategorie-Chips ✅ | `widgets/navigation/tabs` (Chip-Variante) oder `primitives/actions/button-group` | Widget |
| Erklär-Sheet der Kategorien ✅ | `widgets/overlays/drawer` + `widgets/containers/card` | Widget |
| Zeilen der Nachrichtenliste ✅ | `widgets/data/list-view` + `widgets/data/avatar` | Widget |
| VIP-Stern im Rand ✅ | `primitives/feedback/badge` (Symbol-Variante) | Primitive |
| Wisch-Aktionen (Mehr / Markieren / Löschen) ✅ | `widgets/data/list-view` + `interactions/gestures/swipe/swipe` | Widget + Geste |
| Langdruck-Vorschau + Menü ✅ | **NEU `peek-menu`** ⚠️ (Vorschaukarte + `context-menu`) — oder `context-menu` mit Vorschau-Platz (Änderung) | Widget |
| Untere Leiste: Filter, Suche, Verfassen ✅ | `primitives/fields/search-field` + `button` | Primitive |
| Nachrichtenansicht mit nächster/vorheriger ✅ | NEU `mail-view` + `button` | Widget |
| Zusammenfassen-Schaltfläche ✅ | `button` (nur wenn wir Zusammenfassungen anbieten — offen) | Primitive |
| Aktionsblatt (Kacheln + Liste + Farben) ✅ | `widgets/overlays/drawer` + **NEU `action-tiles`** ⚠️ + **NEU `color-swatch-row`** ⚠️ | Widget |
| Markierungsfarben ✅ | `message.flag` mit Farbe → `badge`-Farbvariante | Primitive |
| Verschieben-Sheet mit gestapelter Vorschau ✅ | `widgets/overlays/drawer` + `widgets/data/tree-view` + **NEU `selection-stack`** ⚠️ | Widget |
| Intelligente Mailbox-Liste, bearbeitbar ✅ | `widgets/data/list-view` (Häkchen + Ziehen zum Sortieren — Änderung) | Widget |
| Kontaktkarten-Sheet ✅ | Widget des Kontakte-Programms (übernommen, ADR 0020) | Widget |
| Mailinglisten-Banner mit Abmeldung ✅ | `primitives/feedback/alert` + `button` | Primitive |
| Suchbereich-Umschalter ✅ | `primitives/actions/button-group` | Primitive |
| Suchergebnisse (Top / weitere) ✅ | `widgets/data/list-view` mit Gruppen | Widget |
| Diktieren in der Suche ✅ | Plattform-Eingabe (Shell), keine Komponente ⚠️ | — |
| Einstellungsschalter (Mailaktivität schützen, Adressen markieren) ✅ | App-Einstellungen (`switch`, `tags-input`) | App |
| Sheet „Konto hinzufügen“ ✅ | `widgets/containers/wizard` | Widget |
| Verfasser (Mac) ✅ | NEU `composer` + `rich-text-editor` + `tags-input` (Empfänger) | Widget |
