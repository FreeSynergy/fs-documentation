# UI-Objekt-System (FsnObject)

[← Zurück zum Index](../INDEX.md) | [Desktop](../programme/desktop/README.md)

---

## Grundregel: Einmal definiert, überall identisch

JEDES sichtbare Element ist ein FsnObject. Fenster, Widgets, Modals, Panels — alles folgt denselben Regeln.

## Objekt-Typen

| Typ | Resize | Drag | Minimize | Close | Sidebar |
|---|---|---|---|---|---|
| Window | Immer | Immer (am Kopf) | Ja → wird Icon | Ja (mit Unsaved-Check) | Wenn Items > 0 |
| Widget | Nur im Edit-Mode | Nur im Edit-Mode | Nein | Nur im Edit-Mode | Nein |
| Modal | Nein | Nein | Nein | Ja (X oder Escape) | Nein |
| Panel | Nur Breite | Nein | Nein | Ja | Wenn Items > 0 |

## Resize (Größe ändern)

- **5px Toleranz** am Rand: Wenn die Maus innerhalb von 5px eines Randes ist, ändert sich der Cursor
- Cursor-Typen:
  - Links/Rechts: `ew-resize` (↔)
  - Oben/Unten: `ns-resize` (↕)
  - Ecke oben-links / unten-rechts: `nwse-resize`
  - Ecke oben-rechts / unten-links: `nesw-resize`
- Minimum-Größe wird eingehalten
- Bei Mousedown: Fullscreen-Overlay fängt alle Mouse-Events
- Bei Mouseup: Overlay weg, neue Größe gespeichert (SQLite)

## Drag (Verschieben)

- Am **Kopf/Titelleiste** anfassen → Drag beginnt
- Bei Widgets im Edit-Mode: Drag-Handle erscheint
- Fullscreen-Overlay während des Drags (verhindert "Verlieren")
- Position gespeichert (SQLite)

## Sidebar (Tab-Menü)

Jedes Fenster KANN eine Sidebar haben:
- **Nicht gehovert:** Nur SVG-Icons sichtbar (~40px breit)
- **Gehovert:** Öffnet sich mit Animation (~200px), zeigt Icon + Text
- **Keine Items:** Sidebar verschwindet komplett
- Einheitliches Look & Feel in JEDEM Fenster

## Minimize

- Klick auf Minimize-Button → Fenster wird zu einem **Icon auf dem Desktop**
- Das Icon hat einen **grünen pulsierenden Punkt** (oben rechts):
  - 1 Sekunde fade-in (0% → 100% Opacity)
  - 0.5 Sekunden warten
  - 1 Sekunde fade-out (100% → 0%)
  - Sofort wieder fade-in
- Das Icon kann verschoben werden (Drag & Drop)
- Klick auf Icon → Fenster wird wiederhergestellt

## Close mit Unsaved-Changes

Wenn `has_unsaved_changes == true`:
```
┌─ Unsaved Changes ─────────────┐
│                                │
│  You have unsaved changes.     │
│                                │
│  [Save] [Don't Save] [Cancel]  │
└────────────────────────────────┘
```

- **Save:** Änderungen speichern, dann schließen
- **Don't Save:** Änderungen verwerfen, schließen
- **Cancel:** Nichts tun, Fenster bleibt offen

## Widget-Bearbeitungsmodus

Rechtsklick auf Desktop-Hintergrund → "Edit Desktop":
1. Widgets werden draggable + resizable
2. "Add Widget" → scrollbare Liste (aus installierten Widgets)
3. "Background" → Bild hochladen, Farbe, Gradient
4. Weitere Einstellungen (Layout, etc.)
5. "Done" / "Apply" → speichern
6. "Cancel" → verwerfen

---

Weiter: [CSS-System](css.md) | [Themes](../konzepte/themes.md)
