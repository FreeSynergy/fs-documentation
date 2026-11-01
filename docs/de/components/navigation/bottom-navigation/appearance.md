# Bottom Navigation (Mobile) - Aussehen

## Grundlayout

Bottom Navigation ist eine Navigation unten am Bildschirm, typisch für Mobile-First-Design.

## Varianten

### Active Icon (Aktiver Punkt hervorgehoben)

```
┌─────────────────────────────────────────┐
│   🏠    📩   📅   👥   ⚙️              │
│   Home  Mail CalContactsSettings      │
└─────────────────────────────────────────┘
```

### Text Labels (Mit Text)

```
┌─────────────────────────────────────────┐
│ Home │ Mail │ Cal │ Cont. │ Settings    │
└─────────────────────────────────────────┘
```

### Icon Only (Nur Icons)

```
┌─────────────────────────────────────────┐
│ 🏠  📩  📅  👥  ⚙️                     │
└─────────────────────────────────────────┘
```

## Größen

| Größe | Höhe | Icon-Größe | Verwendung |
|-------|------|------------|------------|
| Small | 48px | 20px | Wenige Punkte |
| Medium | 56px | 24px | Standard |
| Large | 64px | 28px | Viele Punkte |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Active** | Primärfarbe | Aktiver Punkt |
| **Inactive** | Grau | Inaktive Punkte |
| **Hover** | Heller | Hover-Zustand |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `color` | Farbe ändert sich |
| `scale` | Vergrößerung |
| `shadow` | Schatten |

## Reaktiv

- Die Leiste ist immer vollbreit und bleibt am unteren Rand stehen; ihr Inhalt wird
  gleichmäßig auf die Punkte verteilt.
- Reicht der Platz für Beschriftungen nicht, fällt sie auf `icon only` zurück und der Name
  erscheint erst nach der Auswahl als Kurztext.
- Auf großen Bildschirmen wechselt die Anwendung üblicherweise auf
  [sidebar](../sidebar/) oder [toolbar](../toolbar/); die Leiste bleibt dann erhalten, wenn
  die Anwendung mobil bleibt, sonst entfällt sie.

## Max 5 Punkte

```
┌─────────────────────────────────────────┐
│   🏠    📩   📅   👥   ⚙️              │
└─────────────────────────────────────────┘
```

## Animationen

| Effekt | Beschreibung |
|--------|--------------|
| `fade-in` | Beschriftung blendet ein |
| `scale-in` | aktives Symbol wächst |
| `slide-in` | Indikator wandert zum aktiven Punkt |
