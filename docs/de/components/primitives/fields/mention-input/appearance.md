# Mention Input - Erscheinungsbild

## Grundlayout
Ein Mention Input ist ein Textfeld mit Erwähnungen von Benutzern oder Kontakten.

```
┌─────────────────────────────────────────┐
│ @John Doe @Jane Smith                   │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **feld** | einzeilig, ausgewählte Personen als Chips mit Schließen-Button |
| **inline** | normaler Text, erwähnte Namen farbig hervorgehoben |
| **mehrzeilig** | Editorbereich, Chips und Text gemischt |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| small | 200px | inline |
| medium | 300px | Standard |
| large | 400px | hervorgehoben |
| full | 100% | volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **default** | hell | Standard |
| **mention** | Primärfarbe | erwähnte Benutzer |
| **active** | dunkel | aktiver Zustand |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|--------------|
| `border` | der Rahmen leuchtet auf |
| `shadow` | der Schatten wird stärker |

## Responsiv

- Die Vorschlagsliste folgt der Cursorposition. Sie klappt nach oben, wenn unten kein Platz ist.
- Auf schmalen Bildschirmen wird die Liste zu einer unten verankerten Leiste über der Tastatur.
- Chips brechen in die nächste Zeile um. Zu lange Namen werden mit Auslassungspunkten gekürzt.
  Der volle Name bleibt als Tooltip verfügbar.

## Autovervollständigung

```
┌─────────────────────────────────────────┐
│ @                                       │
├─────────────────────────────────────────┤
│  John Doe                               │
│  Jane Smith                             │
│  Bob Müller                             │
│  +                                      │
└─────────────────────────────────────────┘
```

## Ausgewählte Benutzer

```
┌─────────────────────────────────────────┐
│ @John Doe @Jane Smith (2 ausgewählt)    │
└─────────────────────────────────────────┘
```
