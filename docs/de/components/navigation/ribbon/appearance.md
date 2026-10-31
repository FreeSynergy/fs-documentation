# Ribbon - Aussehen

## Grundlayout

Das Ribbon ist eine tab-basierte Symbolleiste, bekannt aus Microsoft Office.

## Layout

```
┌─────────────────────────────────────────────────────────┐
│ Datei  Start  Einfügen  Layout  Referenzen  Übersicht   │  ← Tabs
├─────────────────────────────────────────────────────────┤
│ Schrift  Absatz  Stile                                  │  ← Groups
│ [A] [B] [I] [U]  [●] [1] [2] [→]  [A+] [T-]           │  ← Commands
├─────────────────────────────────────────────────────────┤
│ Schnellzugriff                                          │
│ [💾] [❌] [✔️] [Drucken]                                │
└─────────────────────────────────────────────────────────┘
```

## Größe-Varianten

| Größe | Höhe | Verwendung |
|-------|------|------------|
| Compact | 32px | Kompakte Darstellung |
| Standard | 48px | Standard |
| Large | 64px | Feature-Heavy |

## Farb-Varianten

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Active Tab** | Primärfarbe | Aktiver Tab |
| **Inactive Tab** | Grau | Inaktive Tabs |
| **Hover** | Heller | Hover-Zustand |
| **Command** | Neutral | Standard-Command |

## Group-Layout

```
┌─────────────────────────────────────────┐
│ Schrift                                 │  ← Group Label
├─────────────────────────────────────────┤
│ [A] [B] [I] [U]                         │  ← Commands
└─────────────────────────────────────────┘
```

## Command-Varianten

| Command | Beschreibung |
|---------|--------------|
| **Button** | Standard-Button |
| **Dropdown** | Dropdown-Button |
| **Split Button** | Button mit Dropdown-Arrow |
| **Gallery** | Gallery-Button |

## Minimized Ribbon

```
┌─────────────────────────────────────────┐
│ Datei │ Start │ Einfügen │ ...         │  ← Only Tabs
├─────────────────────────────────────────┤
│                                         │
│   (Content auf Klick erweiterbar)       │
│                                         │
└─────────────────────────────────────────┘
```

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `color` | Farbe ändert sich |
| `background` | Hintergrund ändert sich |
| `shadow` | Schatten erscheint |
