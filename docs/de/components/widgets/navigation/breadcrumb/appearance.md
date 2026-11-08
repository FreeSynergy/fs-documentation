# Breadcrumb - Erscheinungsbild

## Grundlayout
Breadcrumbs zeigen den Pfad (Start > Wiki > Seite > Unterpunkt).

```
┌─────────────────────────────────────────┐
│ Start > Wiki > Seite > Unterpunkt       │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
| --------- | -------------- |
| **Default** | mit Pfeiltrennzeichen (>) |
| **Arrow** | mit Pfeil (→) |
| **Slash** | mit Schrägstrich (/) |
| **Chevron** | mit spitzen Klammern (›) |

## Größen

| Größe | Schriftgröße | Verwendung |
| ------- | ------------- | ------------ |
| Small | 12px | inline |
| Medium | 14px | Standard |
| Large | 16px | hervorgehoben |

## Farben und Zustände

| Zustand | Farbe | Beschreibung |
| -------- | ------- | -------------- |
| **Home** | Primärfarbe | Start |
| **Active** | dunkel | aktueller Pfad |
| **Inactive** | grau | inaktive Pfade |
| **Hover** | heller | Hover-Zustand |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
| -------- | -------------- |
| `color` | die Farbe ändert sich |
| `underline` | eine Unterstreichung erscheint |
| `opacity` | die Deckkraft ändert sich |

## Responsiv

- Der letzte Eintrag wird zuerst gekürzt, dann die Mitte: die Wurzel und der aktuelle Ort
  bleiben immer sichtbar, dazwischen erscheint `…` als aufklappbares Menü.
- Auf schmalen Bildschirmen reicht oft `zurueck` – ein Knopf mit dem vorherigen Namen.
- Der Pfad bricht nie um; er bleibt in einer Zeile und wächst mit der verfügbaren Breite.

## Mit Icons

```
┌─────────────────────────────────────────┐
│ 🏠 Start > 📚 Wiki > 📄 Seite > 📝 Text │
└─────────────────────────────────────────┘
```

## Eingeklappte Breadcrumbs (bei wenig Platz)

```
┌─────────────────────────────────────────┐
│ Start > ... > Seite > Unterpunkt        │
└─────────────────────────────────────────┘
```
