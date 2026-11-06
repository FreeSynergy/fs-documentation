# Outlook m365-2026-11 — Theme „Bild“

Ein Bild-Theme legt ein Foto oder eine Illustration hinter das Fenster; die Bereiche liegen darüber als undurchsichtige oder leicht durchscheinende Karten. Werte geschätzt (ADR 0013). ✅ = gesehen.

## Farben
| Token (unser) | Rolle | Wert (ca.) |
|--------------|-----------------|-----------------|
| `color.backdrop` | Bild hinter den Bereichen (Landschaft, abstrakt) | Bild, keine Farbe ✅ |
| `color.surface` | Liste, Lesebereich | weiß (hell) oder dunkles Marineblau (dunkel) ✅ |
| `color.surface.sunken` | Ordnerbereich, Menüband | hell: ~#EEF3F8, aus dem Bild getönt ✅ |
| `color.accent` | Schaltflächen | passend zum Bild gewählt (in allen gesehenen Beispielen Blau) ✅ |

## Typografie
Wie [light](light.md) / [dark](dark.md).

## Abstände und Form
- Bereiche werden zu getrennten abgerundeten Karten mit Abständen, durch die das Bild hindurchscheint ✅.

## Bemerkenswerte Details
- Auf dem Telefon füllt das Bild den Kopfbereich hinter Titel, Glocke und Suche ✅.
- Nachbaubar: **teilweise** — ein Hintergrundbild-Token plus Kartenlayout ist möglich; aus dem Bild abgeleitete Akzentfarben brauchen einen Schritt zur Farbextraktion ⚠️; KI-generierte Bilder sind außerhalb des Umfangs.
