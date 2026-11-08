# Avatar - Erscheinungsbild

## Grundlayout

Avatare sind visuelle Darstellungen von Nutzern, die in verschiedenen Formen und
Größen gezeigt werden können.

## Varianten

```css
/* Rund - Standard */
.avatar-circular {
  border-radius: 50%;
  aspect-ratio: 1 / 1;
}

/* Quadratisch */
.avatar-square {
  border-radius: 4px;
}

/* Pille */
.avatar-pill {
  border-radius: 999px;
  aspect-ratio: auto;
}
```

## Größen

| Größe | Pixel | Verwendung |
|-------|-------|------------|
| XSmall | 24px | in Listeneinträgen, minimaler Chat |
| Small | 32px | Standard in Listen |
| Medium | 48px | Profile, Karten |
| Large | 64px | hervorgehobene Profile |
| XL | 96px | großzügige Darstellung |
| XXL | 128px+ | Blickfänge |

## Farben und Zustände

| Farbe | Initialen |
|-------|-----------|
| blau | A–D |
| grün | E–H |
| orange | I–L |
| rot | M–P |
| pink | Q–T |
| lila | U–Z |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `zoom` | der Avatar wird leicht größer (1,1-fach) |
| `border` | der Rand leuchtet auf |
| `shadow` | der Schatten wird stärker |
| `none` | kein Effekt |

## Responsiv

- In Listen bleibt der Avatar bei `small` (32 px), auch auf schmalen Bildschirmen;
  er wird nur in Profilansichten größer.
- Der Klickbereich um einen kleinen Avatar wächst auf 44 px, ohne dass sich die Bildgröße ändert.
- Lädt das Bild langsam, erscheinen zuerst die Initialen; danach blendet das Foto
  mit `fade-in` ein.

## Positionen des Status-Badges

| Position | Beschreibung |
|----------|--------------|
| **Unten rechts** | unten rechts (Standard) |
| **Oben rechts** | oben rechts |
| **Unten links** | unten links |
| **Mitte** | in der Mitte |

## Attribute für das Erscheinungsbild

| Attribut | Wert | Beschreibung |
|----------|------|--------------|
| `size` | `xsmall`, `small`, `medium`, `large`, `xl`, `xxl` | Größe |
| `shape` | `circular`, `square`, `pill` | Form |
| `variant` | `image`, `initials`, `icon`, `placeholder` | Inhalt |
| `status` | `online`, `offline`, `away`, `busy`, `in-meeting` | Status |
| `interactive` | `true`, `false` | anklickbar? |
