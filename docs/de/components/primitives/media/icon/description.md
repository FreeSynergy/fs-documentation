# Icon (Symbol)

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
Ein Icon ist ein symbolisches Grafikelement. Es stellt eine Funktion oder ein Objekt
visuell dar. Anders als Icons in anderen Zusammenhängen (z. B. ein Avatar) stehen
die Icons hier allgemein für Funktionen, Dateitypen oder Aktionen.

## Verwendungszweck

- Funktionen visuell kennzeichnen (z. B. 🏠 für „Startseite“)
- Dateitypen zeigen (z. B. 📄 für PDF, 📸 für Bilder)
- Aktionen symbolisieren (z. B. ✏️ für Bearbeiten, 🗑️ für Löschen)

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **outline** | Linienzeichnung, Standard in Werkzeugleisten |
| **gefüllt** | aktive oder betonte Darstellung |
| **animiert** | bewegt sich (`spin`, `pulse`), z. B. beim Laden oder Senden |

Form und Größe sind keine Varianten, sondern die Attribute `shape` und `size`.

## Funktionen

- SVG. Dadurch skaliert es ohne Stufen und lässt sich über die Textfarbe einfärben.
- Ein Set pro Anwendung. Gemischte Sets wirken unruhig.
- Alternativtext oder `aria-label`, wenn das Icon die einzige Information trägt
- Rein dekorative Icons sind für Screenreader ausgeblendet

## Abgrenzung

- **Nicht verwechseln mit** [avatar](../../../widgets/data/avatar/): Ein Avatar steht für ein
  Subjekt, ein Icon für eine Funktion oder einen Dateityp.
- **Nicht verwechseln mit** Emojis aus dem [emoji-picker](../../../widgets/fields/emoji-picker/): Emojis sind
  Inhalt, Icons sind die Benutzeroberfläche.
- **Nicht verwechseln mit** [image](../image/): Icons sind klein, einfarbig und Teil der Fläche.
- Ein klickbares Icon ist für sich kein Icon-Element, sondern im Icon-only-Modus ein
  [Button](../../actions/button/).

## Best Practices

- Innerhalb einer Komponente einheitliche Icon-Größe
- Kontrast zum Hintergrund sicherstellen
- Hover-Effekt für interaktive Icons
- Alternativtext für Barrierefreiheit

## Formvarianten

| Form | Beschreibung | Verwendung |
|------|--------------|------------|
| **circular** | runde Form | Buttons, Avatare, Statusanzeigen |
| **square** | quadratische Form | Icons in Rastern, Listenelementen |
| **rectangular** | rechteckige Form | Icons in Werkzeugleisten, Tab-Icons |
| **hexagonal** | sechseckige Form | besondere Statussymbole, Dekorationen |
| **pill** | abgerundetes Rechteck | Tags, Badges, Chips |

## Größenvarianten

| Größe | Pixel | Verwendung |
|-------|-------|------------|
| small | 16px | Icons im Text, Listenelemente |
| medium | 24px | Navigation, Buttons |
| large | 32px | Cards, Panels |
| XL | 48px | Hero-Bereiche, hervorgehobene Elemente |
| XXL | 64px+ | Hero-Bereiche, Landingpages |

## Farbvarianten

| Farbe | Verwendung |
|-------|------------|
| **primary** | Hauptfarbe der Anwendung |
| **secondary** | sekundäre Aktionen |
| **success** | Erfolgsmeldungen |
| **warning** | Warnungen |
| **error** | Fehlermeldungen |
| **neutral** | gewöhnliche Icons |

## Siehe auch

- [media – Übersicht](../index.md)
- [Button](../../actions/button/) — Buttons nur mit Icon
- [Avatar](../../../widgets/data/avatar/) — Personen statt Funktionen
- [Base-Komponente](../../basics/base.md)
