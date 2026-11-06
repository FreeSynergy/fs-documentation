# Apple Mail iOS 26 — Theme „hell“

Werte sind beschrieben (aus Screenshots geschätzt), nicht als Dateien kopiert (ADR 0013). ✅ = gesehen.

## Farben
| Token (unser) | Rolle | Wert (ca.) |
|--------------|-----------------|-----------------|
| `color.surface` | Hintergrund der Liste | weiß, #FFFFFF ✅ |
| `color.surface.sunken` | gruppierter Hintergrund hinter Karten und Sheets | helles Grau, ~#F2F2F7 ✅ |
| `color.text` | Titel, Absender, Betreff | schwarz, ~#000000 ✅ |
| `color.text.muted` | Vorschau, Zeit, Untertitel | grau, ~#8A8A8E ✅ |
| `color.accent` | aktiver Chip, Fertig-Schaltfläche, Links, Icons | Systemblau, ~#007AFF (Chip ~#3E8EED) ✅ |
| `color.danger` | Löschen-Aktion | rot, ~#FF3B30 ✅ |
| `color.warning` | Markieren-Aktion, Markierungs-Icon | orange, ~#FF9500 ✅ |
| `color.neutral` | Aktion „Mehr“, inaktive Chips | grau, ~#C7C7CC / ~#E5E5EA ✅ |
| `color.vip` | VIP-Stern | gelb, ~#FFCC00 ✅ |
| Markierungs-Palette | Markierungsfarben | orange, rot, lila, cyan, gelb, grün, grau ✅ |
| Kategorie-Icons | Transaktionen / Updates / Werbung | grün / lila / pink ✅ |

## Typografie
- Großer Titel ~34 pt fett ✅; Absender ~17 pt halbfett; Betreff ~15 pt; Vorschau ~15 pt regulär grau ✅.
- Systemschrift ohne Serifen (SF Pro ⚠️).

## Abstände und Form
- Großzügige Zeilen (~100 pt mit zweizeiliger Vorschau) ✅; feine Trennlinien, eingerückt bis zum Text ✅.
- Kapseln überall: Chips, Suche, Schaltflächen ✅; Sheets und Karten mit großem Radius (~26–32 pt) ✅.
- Wisch-Aktionsschaltflächen sind Kreise (~56 pt) mit Beschriftung darunter ✅.
- Schwebende Bedienelemente mit weichem Schatten und durchscheinendem Glas ✅.

## Bemerkenswerte Details
- Keine sichtbaren Trennlinien zwischen Kopfbereich und Inhalt; der Inhalt scrollt unter den schwebenden Bedienelementen ✅.
- Das Kontaktkarten-Sheet ist im Beispiel mauve getönt, aus der vom Kontakt gewählten Farbe ✅.
