# File Upload - Erscheinungsbild

## Grundlayout

Ein File Upload ist ein Element zum Auswählen und Hochladen von Dateien.

## Varianten

### Dateiauswahl

```
┌─────────────────────────────────────────┐
│ [📁 Datei wählen]                       │
└─────────────────────────────────────────┘
```

### Drag & Drop

```
┌─────────────────────────────────────────┐
│                                         │
│   Datei hier ablegen                    │
│                                         │
└─────────────────────────────────────────┘
```

### Bildvorschau

```
┌─────────────────────────────────────────┐
│  🖼️                                    │
│                                         │
│  [dateiname.jpg]     [✕]                │
└─────────────────────────────────────────┘
```

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| small | 200px | im Text |
| medium | 300px | Standard |
| large | 400px | hervorgehoben |
| full | 100% | volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Standard** | hell | Standard |
| **Primär** | Primärfarbe | primär |
| **Aktiv** | dunkel | aktiver Zustand |
| **Deaktiviert** | Grau | deaktiviert |

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
|--------|--------------|
| `border` | der Rahmen leuchtet auf |
| `shadow` | der Schatten wird stärker |
| `background` | der Hintergrund wechselt |

## Responsiv

- Die Ablagefläche wächst mit dem Inhalt: ohne Datei füllt sie die volle Breite,
  mit einer Dateiliste wird sie unter dem Auslöser zu einer Liste.
- Auf schmalen Bildschirmen stapeln sich Vorschau und Dateiname untereinander,
  die Entfernen-Schaltfläche bleibt oben rechts erreichbar.
- Unterhalb der Bildschirmbreite `small` wird die Ablagefläche auf `Full` gesetzt und der
  Auslöser wird zu einer Schaltfläche in voller Breite.

## Fortschrittsanzeige

```
┌─────────────────────────────────────────┐
│ datei.jpg                               │
│ ▓▓▓▓▓▓▓▓▓▓░░░░░░  75%                   │
└─────────────────────────────────────────┘
```
