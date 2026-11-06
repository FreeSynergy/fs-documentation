# Outlook m365-2026-11 — Abhängigkeiten

Welche **unserer** Komponenten ein Frontend in diesem Stil benötigt. Namen aus `temp/messenger-components.md`;
**NEU** = nicht unter unseren 84 Komponenten. ✅/⚠️ beziehen sich auf die gesehene Outlook-Funktion.

| Bereich / Funktion | Komponente | Ebene |
|------------------|-----------|-----------|
| Fenster mit 3–4 größenveränderlichen Bereichen ✅ | `widgets/containers/split-view` + App-Shell | Widget / App |
| App-Leiste (Suite-Umschalter) ✅ | `widgets/navigation/sidebar` (eingeklappt) — Shell, nicht Messenger | Widget |
| Suche in der Titelleiste ✅ | `primitives/fields/search-field` | Primitive |
| Chip für den nächsten Termin in der Titelleiste ✅ | **NEU `next-event-chip`** (übernommenes Kalender-Widget, kompakt) | Widget |
| Menüband mit Registerkarten, geteilte Schaltflächen ✅ | `widgets/navigation/toolbar` (Menüband-Variante) + `widgets/navigation/tabs` + **NEU `split-button`** ⚠️ (oder `button-group`-Variante) | Widget |
| Ordnerbaum mit Favoriten, Zählern ✅ | `widgets/data/tree-view` + `primitives/feedback/badge` | Widget |
| Fokussiert / Andere ✅ | `widgets/navigation/tabs` | Widget |
| Nachrichtenliste, Datumsgruppen, Gruppe „Angeheftet“ ✅ | `widgets/data/list-view` (Gruppierung mit einklappbaren Überschriften — Änderung) | Widget |
| Zeile mit Chips (RSVP, Kategorie, @) ✅ | `widgets/data/list-view`-Zeile + `primitives/feedback/badge` + übernommener Kalender-Einladungs-Chip | Widget |
| Lesebereich ✅ | NEU `mail-view` | Widget |
| HTML-Inhalt | NEU `html-view` ⚠️ / `workbenches/special/embed` | Workbench |
| KI-Zusammenfassungskarte ✅ | `widgets/containers/card` (nur wenn wir Zusammenfassungen anbieten — offen) | Widget |
| Reaktionen auf Mails ✅ | NEU `reaction-bar` | Widget |
| Präsenzpunkt ✅ | `widgets/data/avatar` | Widget |
| Kontakt-Hover-Karte ✅ | `widgets/overlays/hover-card` + Kontakte-Karten-Widget | Widget |
| Antwortblock für Einladungen ✅ | Widget des Kalender-Programms (übernommen) | Widget |
| Verfasser eingebettet / als eigenes Fenster ✅ | NEU `composer` + `workbenches/fields/rich-text-editor` | Widget / Workbench |
| Empfänger mit Chips ✅ | `primitives/fields/tags-input` (Variante `recipients`) + `combobox` | Primitive |
| Grammatik-Popover ✅ | `widgets/overlays/popover` ⚠️ (nur mit einem lokalen Prüfer) | Widget |
| Versand terminieren / zurückstellen / Nachverfolgungszeit ✅ | `widgets/fields/date-picker` + `widgets/fields/time-picker` + **NEU `time-preset-menu`** (später heute / morgen / Wochenende / nächste Woche + benutzerdefiniert) | Widget |
| Leiste „Senden rückgängig“ ✅ | `primitives/feedback/toast` mit Aktion + Countdown (Änderung) | Primitive |
| Regler für die Rückgängig-Verzögerung ✅ | `primitives/fields/slider` ⚠️ | Primitive |
| Kontextmenüs mit Untermenüs ✅ | `widgets/overlays/context-menu` | Widget |
| Kategorien mit Farbe ✅ | **NEU `category-chip`** ⚠️ (oder `badge`-Farbvariante) + Einstellungsliste | Primitive |
| Kategorie- / intelligente Suchordner ✅ | `tree-view`-Eintrag, gebunden an eine gespeicherte Abfrage (Änderung) | Widget |
| Regeln ✅ | NEU `rule-editor` | Widget |
| Offline-Einstellungen ✅ | Einstellungsseite (`switch`, `select`) | App |
| Offline- / Sync-Anzeige ✅ (klassische Statusleiste) | **NEU `sync-state`** ⚠️ (oder `badge`) | Primitive |
| Einstellungsdialog mit 3 Spalten ✅ | `widgets/overlays/modal` + `sidebar` + `field` | App |
| Dialog „Konto hinzufügen“ ✅ | `widgets/containers/wizard` | Widget |
| Mobile untere Navigation, schwebende Neue-Mail-Schaltfläche ✅ | `widgets/navigation/bottom-navigation` + **NEU `floating-action-button`** ⚠️ (oder `button`-Variante) | Widget |
| Mobile Wisch-Aktionen ⚠️ | `list-view` + `interactions/gestures/swipe` | Geste |
| Theme-Auswahl mit Vorschauen ✅ | Einstellungsseite + `primitives/media/image` | App |
