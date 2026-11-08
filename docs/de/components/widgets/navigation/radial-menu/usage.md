# Radial Menu - Verwendung

## Eckmenü mit Hover (oben rechts)

Der Klassiker: Die Punkte sitzen in der Ecke, wachsen beim Überfahren und schieben ihre
Unterpunkte nach innen in die Fläche (`clamp` macht aus dem Vollkreis einen Fächer).

```jsx
<RadialMenu
  anchor="top-right"
  variant="facher"
  trigger="hover"
  items={[
    { id: 'new', icon: 'plus', label: 'Neu' },
    { id: 'share', icon: 'share', label: 'Teilen',
      children: [
        { id: 'link', icon: 'link', label: 'Link kopieren' },
        { id: 'mail', icon: 'mail', label: 'E-Mail' }
      ] },
    { id: 'settings', icon: 'cog', label: 'Einstellungen' }
  ]}
  onSelect={(id) => run(id)}
/>
```

## Freier Anker in der Mitte der Fläche

Den Anker auf freie Koordinaten oder ein anderes Element setzen. Das Menü erscheint dort,
wo der Nutzer arbeitet (Whiteboard, Karte, Editor).

```jsx
<RadialMenu
  variant="launcher"
  anchor={{ x: cursor.x, y: cursor.y }}
  size="large"
  items={palette}
/>

<RadialMenu anchor="#avatar-42" items={personActions} />
```

## Unterpunkte im nächsten Ring

Beim Überfahren eines Punktes öffnen sich dessen `children` im zweiten Ring. Bei drei Ebenen
entspricht `levels={3}` drei Ringen.

```jsx
<RadialMenu
  anchor="center"
  levels={3}
  activeItem={hoveredItem}      // Unterpunkte erscheinen im nächsten Ring
  dimInactive
  items={[
    { id: 'document', icon: 'file', children: [
        { id: 'rename', icon: 'pencil' },
        { id: 'versions', icon: 'history', children: [
            { id: 'v1', label: 'v1' },
            { id: 'v2', label: 'v2' }
        ] }
    ] }
  ]}
/>
```

## Sektoren statt Punkte (Pie Menu)

Große Trefferflächen, Auswahl allein über die Richtung — gut auf Touch und Controllern.

```jsx
<RadialMenu
  variant="sektoren"
  trigger="long-press"
  items={toolModes}
/>
```

## Kontextmenü am Zeiger

Ein Rechtsklick öffnet dasselbe Menü an der Zeigerposition — die runde Variante des
[context-menu](../../overlays/context-menu/).

```jsx
<RadialMenu variant="kontext" items={contextActions} />
```

## Speed Dial am Floating Action Button

Der FAB verankert das Kreismenü (`anchor: "fab"`). Der Fächer wird zur Bildschirmmitte hin
beschnitten.

```jsx
<FloatingActionButton icon="plus" />
<RadialMenu
  anchor="fab"
  variant="facher"
  trigger="tap"
  items={quickAccess}
/>
```

## Tastatursteuerung

```jsx
<RadialMenu keyboardNavigation items={items} />
// Pfeiltasten: im Ring bewegen · Enter: eine Ebene tiefer · Esc: zurück oder schließen
```

## Beispiele

### Beispiel 1: Eckmenü, drei Zustände

```
geschlossen        Hover                Unterpunkt aktiv
    ●          ╲      ◆             ╲    ◆ ○
 (Punkt in      ╲    (wächst,      ╲   (Ring 2 fächert
  der Ecke)     ╲    rückt raus)   ╲   aus ◆ heraus)
```

### Beispiel 2: Launcher mit zwei Ringen

```
        ○  ○  ○
      ○  ◆  ●  ◆  ○        ● Anker · ◆ Ring 1 · ○ Ring 2 (Unterpunkte
        ○  ◆  ○              des aktiven ◆, sichtbar innerhalb von coneAngle)
```

### Beispiel 3: Speed Dial unten rechts

```
                      ┌──────────────┐
                      │        ○   ◆ │   Anker = Ecke unten rechts,
                      │      ○   ◆   │   Ring nach innen beschnitten
                      │    ○   ◆  ●  │   als Halbfächer
                      └──────────────┘
```

## Siehe auch

- [Radial Menu – Beschreibung](./description.md)
- [Attribute](./attributes.md)
- [radial-out](../../../../interactions/animations/entrance/radial-out/) und [radial-in](../../../../interactions/animations/exit/radial-in/)
- [Floating Action Button](../../../primitives/actions/floating-action-button/)
