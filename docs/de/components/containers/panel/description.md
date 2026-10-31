# Panel (Container)

## Beschreibung

Ein Panel ist ein großer Container mit Header, Inhalt und Footer. Unterscheidet sich von Card durch größere Größe und Layout-Verwendung.

## Verwendungszweck

- Große Inhalt Blöcke
- Layout-Container
- Filter-Panel
- Dashboard-Widget

## Struktur

```
┌─────────────────────────────────────────┐
│ Header / Titel                          │  ← Header
├─────────────────────────────────────────┤
│                                         │
│   Inhalt                                │
│   ...                                   │
│                                         │  ← Body
├─────────────────────────────────────────┤
│ Footer / Aktionen                       │  ← Footer
└─────────────────────────────────────────┘
```

## Varianten

| Variant | Beschreibung |
|---------|--------------|
| **Default** | Standard-Panel mit Header |
| **Collapsible** | Header klappt Inhalt ein/aus |
| **Draggable** | Verschiebbar |
| **Filter** | Mit Filter-Optionen |

## Features

- Collapsible (Ein/Ausklappen)
- Draggable (Verschieben)
- Resize (Größe ändern)
- Custom Header (benutzerdefinierter Header)

## Best Practices

- Clear-Header-Text
- Konsistente Größe
- Hover-Effect
- Accessibility
