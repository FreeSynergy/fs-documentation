# Bottom Navigation (Mobile) - Aussehen

## Grundlayout

Bottom Navigation ist eine Navigation unten am Bildschirm, typisch für Mobile-First-Design.

## Layout-Varianten

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

## Größe-Varianten

| Größe | Höhe | Icon-Größe | Verwendung |
|-------|------|------------|------------|
| Small | 48px | 20px | Wenige Punkte |
| Medium | 56px | 24px | Standard |
| Large | 64px | 28px | Viele Punkte |

## Farb-Varianten

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Active** | Primärfarbe | Aktiver Punkt |
| **Inactive** | Grau | Inaktive Punkte |
| **Hover** | Heller | Hover-Zustand |

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `color` | Farbe ändert sich |
| `scale` | Vergrößerung |
| `shadow` | Schatten |

## Max 5 Punkte

```
┌─────────────────────────────────────────┐
│   🏠    📩   📅   👥   ⚙️              │
└─────────────────────────────────────────┘
```

## Animationen

| Effekt | Beschreibung |
|--------|--------------|
| `Fade In` | Einfade-Effekt |
| `Scale` | Skalierung |
| `Slide` | Schiebe-Effekt |
