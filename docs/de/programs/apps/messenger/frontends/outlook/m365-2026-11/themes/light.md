# Outlook m365-2026-11 — Theme „hell“

Werte sind beschrieben (aus Screenshots geschätzt), nicht als Dateien kopiert (ADR 0013). ✅ = gesehen.

## Farben
| Token (unser) | Rolle | Wert (ca.) |
|--------------|-----------------|-----------------|
| `color.surface` | Bereiche, Lesebereich, Liste | weiß, #FFFFFF ✅ |
| `color.surface.sunken` | Fensterhintergrund, Ordnerbereich, Titelleiste | sehr helles Grau, ~#F5F5F5 ✅ |
| `color.text` | Haupttext | nahezu schwarz, ~#242424 ✅ |
| `color.text.muted` | Vorschauzeile, Zeit, Hinweise | mittleres Grau, ~#616161 ✅ |
| `color.accent` | primäre Schaltflächen (Neue E-Mail, Senden), Unterstreichung des aktiven Reiters, ungelesener Betreff, Links | Microsoft-Blau, ~#0F6CBD ✅ |
| `color.accent.subtle` | ausgewählter Ordner / ausgewählte Zeile | blasses Blau, ~#DCE9F7 ✅ |
| `color.highlight` | markierte / hervorgehobene Zeile | blasses Gelb, ~#FFF8D6 ✅ |
| `color.danger` | Melden-Symbol, Markierung | rot, ~#C50F1F ✅ |
| `color.border` | Trennlinien zwischen Gruppen und Bereichen | helles Grau, ~#E0E0E0 ✅ |
| `color.accent` (Variante) | alternativer Theme-Akzent | violett, ~#8A4FD8 ✅ |

## Typografie
- Sans-Serif-UI-Schrift (Segoe UI Variable ⚠️), ~14 px in Listen und Menüband, Absender ~14 px regulär, Abschnittsüberschriften ~14 px halbfett ✅.
- Standardschrift des Verfassers „Aptos“, 11 pt ✅.
- Ungelesen: kein fetter Text, sondern blauer Betreff + linker Balken ✅.

## Abstände und Form
- Eckenradius ~4 px bei Schaltflächen und Chips, ~8 px bei Fenster und Dialogen ✅.
- Zeilen ~64–72 px hoch mit drei Zeilen (Absender, Betreff, Vorschau) ✅; Chips in Zeilen ✅.
- Dünne 1-px-Trennlinien; weicher Schatten bei Popovers und dem Einstellungsdialog ✅.
- Dichte einstellbar ✅.

## Bemerkenswerte Details
- Icons im Umriss-Stil mit wenigen farbigen (rotes Melden-Icon, violette Antwortpfeile, gelbe Schnellschritte) ✅.
- Die Copilot-Schaltfläche ist das einzige Verlaufselement ✅.
