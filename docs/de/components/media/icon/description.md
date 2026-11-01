# Icon

| Feld | Wert |
|------|------|
| **Kategorie** | `media` |
| **Erbt von** | `base` |
| **Varianten** | `outline`, `gefüllt`, `animiert` |
| **Zustände** | `aktiv` |
| **Gesten** | `tap`, `long-press` |
| **Animationen** | `pulse`, `spin`, `highlight` |
| **Verwandt** | `avatar`, `button`, `badge`, `image`, `emoji-picker` |
| **Status** | dokumentiert |

## Beschreibung
Ein Icon ist ein symbolisches Grafikelement, das eine Funktion oder ein Objekt visuell repräsentiert. Im Gegensatz zu Icons in anderen Kontexten (z.B. Avatar) stehen Icons hier generisch für Funktionen, Dateitypen oder Aktionen.

## Verwendungszweck

- Funktionen visuell kennzeichnen (z.B. 🏠 für "Start")
- Dateitypen darstellen (z.B. 📄 für PDF, 📸 für Bilder)
- Aktionen symbolisieren (z.B. ✏️ für Bearbeiten, 🗑️ für Löschen)

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **outline** | Linienzeichnung, Standard in Werkzeugleisten |
| **gefüllt** | aktive oder betonte Darstellung |
| **animiert** | bewegt sich (`spin`, `pulse`), z. B. Laden oder Senden |

Form und Größe sind keine Varianten, sondern Attribute `shape` und `size`.

## Features

- SVG, damit stufenlos skalierbar und über die Textfarbe einfärbbar
- Ein Set pro Anwendung, gemischte Sets wirken unruhig
- Alt-Text oder `aria-label`, wenn das Icon die einzige Information trägt
- Reine Zier-Icons werden für Screenreader ausgeblendet

## Abgrenzung

- **Nicht verwechseln mit** [avatar](../../data/avatar/): ein Avatar stellt ein Subjekt dar,
  ein Icon eine Funktion oder einen Dateityp.
- **Nicht verwechseln mit** Emojis aus dem [emoji-picker](../../fields/emoji-picker/): Emojis sind
  Inhalt, Icons sind Bedienoberfläche.
- **Nicht verwechseln mit** [image](../image/): Icons sind klein, monochrom und Teil der Oberfläche.
- Ein klickbares Icon ist kein Icon-Element allein, sondern ein
  [button](../../actions/button/) in der Variante icon-only.

## Best Practices

- Konsistente Icon-Größe innerhalb einer Komponente
- Kontrast zum Hintergrund gewährleisten
- Hover-Effekt bei interaktiven Icons
- Alt-Text für Barrierefreiheit

## Form-Varianten

| Form | Beschreibung | Verwendung |
|------|-------------|------------|
| **Circular (Rund)** | Runde Form | Buttons, Avatare, Status-Indikatoren |
| **Square (Viereckig)** | Quadratische Form | Icons in Grids, List-Items |
| **Rectangular (Rechteckig)** | Rechteckige Form | Toolbar-Icons, Tab-Icons |
| **Hexagonal (Sechseckig)** | Sechseckige Form | Spezielle Status-Icons, Decorations |
| **Pill (Pillenform)** | Abgerundete Rechtecke | Tags, Badges, Chips |

## Größe-Varianten

| Größe | Pixel | Verwendung |
|-------|-------|------------|
| Small | 16px | Inline-Icons, List-Items |
| Medium | 24px | Navigation, Buttons |
| Large | 32px | Cards, Panels |
| XL | 48px | Hero-Sectionen, Featured-Items |
| XXL | 64px+ | Hero-Bereiche, Landing-Pages |

## Farb-Varianten

| Farbe | Verwendung |
|-------|------------|
| **Primär** | Hauptfarbe der Anwendung |
| **Sekundär** | Nebenaktionen |
| **Success** | Erfolgs-Meldungen |
| **Warning** | Warnungen |
| **Error** | Fehler-Meldungen |
| **Neutral** | Normale Icons |

## Siehe auch

- [media – Übersicht](../index.md)
- [Button](../../actions/button/) — icon-only-Buttons
- [Avatar](../../data/avatar/) — Personen statt Funktionen
- [Basiskomponente](../../basics/base/)
