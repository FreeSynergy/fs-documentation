# Encryption State (Verschlüsselungsstatus) - Aussehen

## Grundlayout

```
 🔒 MLS      🔒 OpenPGP      🔓 transport only      ⚠ not encrypted
```

## Varianten

| Variante | Aussehen |
|---|---|
| **icon** | 16 px großes Schloss-Symbol |
| **icon-text** | Symbol und kurzer Name der Art |
| **warning** | Fläche in Fehlerfarbe mit dem Text „nicht verschlüsselt“ |

## Größen

| Größe | Höhe | Verwendung |
|---|---|---|
| `small` | 16 px | Nachrichtenkopf |
| `medium` | 20 px | Unterhaltungskopf (Standard) |
| `large` | 24 px | Detailpanel |

## Farben und Zustände

| Zustand | Aussehen |
|---|---|
| `encrypted` | neutraler oder Erfolgston, geschlossenes Schloss |
| `transport-only` | Warnton, halb geöffnetes Schloss |
| `unencrypted` | Fehlerton, offenes Schloss, Text |
| `unknown` | grau, Fragezeichen-Symbol |
| `focused` | Fokusring des Themes |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|---|---|
| `underline` | Text unterstrichen wie bei [link](../../basics/link/) |
| `tooltip` | erklärt die Art, siehe [tooltip](../../../widgets/overlays/tooltip/) |

## Reaktiv

- Unterhalb der Breite `small` wird nur das Symbol angezeigt; die Art bleibt im Tooltip.
- Die Berührungsfläche beträgt mindestens 44 px, auch wenn das Symbol 16 px groß ist.
