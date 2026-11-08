# Context Menu - Erscheinungsbild

## Grundlayout
Ein Kontextmenü wird per Rechtsklick oder durch eine lange Berührung geöffnet.

```
┌─────────────────────────────────────────┐
│ 📋 Bearbeiten                           │
│ 📄 Kopieren                             │
│ 🗑️ Löschen                              │
│ ─────────────────────                   │
│ 🔄 Aktualisieren                        │
│ ℹ️ Eigenschaften                        │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Auslöser | Erscheinungsbild |
|----------|----------|------------------|
| **Standard** | Rechtsklick (Desktop) | Menü am Zeiger |
| **Long Press** | lange Berührung | Menü über dem Objekt, auf schmaler Fläche volle Breite |
| **Overflow Menu** | Klick auf drei Punkte | Menü unter dem Button |

## Größen

| Größe | Breite | Schriftgröße | Verwendung |
|-------|--------|--------------|------------|
| Small | 150px | 12px | wenige Optionen |
| Medium | 200px | 14px | Standard |
| Large | 250px | 16px | viele Optionen |

## Farben und Zustände

| Zustand | Farbe | Beschreibung |
|---------|-------|--------------|
| **Aktiv** | Primärfarbe | aktiver Menüeintrag |
| **Hover** | heller | Zustand beim Überfahren |
| **Deaktiviert** | Grau | deaktivierte Optionen |
| **Gefährlich** | Rot | gefährliche Aktionen |

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
|--------|--------------|
| `background` | der Hintergrund wechselt |
| `color` | die Farbe wechselt |
| `border-radius` | die Ecken sind abgerundet |

## Responsiv

Das Menü klappt vom Auslösepunkt weg auf und wechselt die Seite, wenn bis zum Bildschirmrand
zu wenig Platz ist (`pop-in` aus der jeweiligen Ecke). Ist es höher als der freie Platz,
scrollt es selbst; der Auslösepunkt bleibt sichtbar.

```css
.context-menu { position: fixed; min-width: 150px; max-height: 70vh; overflow: auto;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2); animation: pop-in 120ms; }
.context-menu--flip-x { transform-origin: right top; }  /* kein Platz rechts */
.context-menu--flip-y { transform-origin: left bottom; } /* kein Platz unten */
```

## Icons

| Icon | Bedeutung |
|------|-----------|
| 📋 | bearbeiten |
| 📄 | kopieren |
| 🗑️ | löschen |
| 🔄 | aktualisieren |
| ℹ️ | Information |

## Trennlinie

```
┌─────────────────────────────────────────┐
│ Aktionen                                │
│ ─────────────────────                   │
│ Weitere Aktionen                        │
└─────────────────────────────────────────┘
```
