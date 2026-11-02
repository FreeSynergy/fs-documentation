# Radial Menu (Kreismenü) - Verwendung

## Eckenmenü mit Hover (oben rechts)

Der Klassiker: Punkte sitzen in der Ecke, wachsen bei Hover und schieben ihre
Unterpunkte nach innen in die Fläche (`clamp` macht aus dem Vollkreis einen Fächer).

```jsx
<RadialMenu
  anchor="top-right"
  variant="facher"
  trigger="hover"
  items={[
    { id: 'neu', icon: 'plus', label: 'Neu' },
    { id: 'teilen', icon: 'share', label: 'Teilen',
      children: [
        { id: 'link', icon: 'link', label: 'Link kopieren' },
        { id: 'mail', icon: 'mail', label: 'E-Mail' }
      ] },
    { id: 'einstellungen', icon: 'cog', label: 'Einstellungen' }
  ]}
  onSelect={(id) => run(id)}
/>
```

## Freier Anker mitten in der Fläche

Anker auf freie Koordinaten oder auf ein anderes Element setzen — das Menü erscheint
dort, wo der Nutzer arbeitet (Whiteboard, Karte, Editor).

```jsx
<RadialMenu
  variant="launcher"
  anchor={{ x: cursor.x, y: cursor.y }}
  size="large"
  items={palette}
/>

<RadialMenu anchor="#avatar-42" items={personenAktionen} />
```

## Unterpunkte im nächsten Ring

Hover auf einem Punkt öffnet dessen `children` im zweiten Ring; bei drei Ebenen
entspricht `levels={3}` drei Ringen.

```jsx
<RadialMenu
  anchor="center"
  levels={3}
  activeItem={hoveredItem}      // Kinder erscheinen im nächsten Ring
  dimInactive
  items={[
    { id: 'dokument', icon: 'file', children: [
        { id: 'umbenennen', icon: 'pencil' },
        { id: 'versionen', icon: 'history', children: [
            { id: 'v1', label: 'v1' },
            { id: 'v2', label: 'v2' }
        ] }
    ] }
  ]}
/>
```

## Sektoren statt Punkte (Pie-Menu)

Große Trefferflächen, Auswahl rein über die Richtung — gut auf Touch und Controllern.

```jsx
<RadialMenu
  variant="sektoren"
  trigger="long-press"
  items={werkzeugModi}
/>
```

## Kontextmenü am Zeiger

Rechtsklick öffnet dasselbe Menü an der Zeigerposition — die runde Variante des
[context-menu](../../overlays/context-menu/).

```jsx
<RadialMenu variant="kontext" items={kontextAktionen} />
```

## Speed-Dial am Floating Action Button

Der FAB verankert das Kreismenü (`anchor: "fab"`), der Fächer klemmt zur Bildschirmmitte.

```jsx
<FloatingActionButton icon="plus" />
<RadialMenu
  anchor="fab"
  variant="facher"
  trigger="tap"
  items={schnellzugriff}
/>
```

## Tastatursteuerung

```jsx
<RadialMenu keyboardNavigation items={items} />
// Pfeiltasten: im Ring herum · Enter: eine Ebene hinein · Esc: zurück bzw. schließen
```

## Beispiele

### Beispiel 1: Eckmenü, drei Zustände

```
geschlossen        Hover                Unterpunkt aktiv
    ●          ╲      ◆             ╲    ◆ ○
 (Punkt in     ╲    (wächst,      ╲   (Ring 2 fächert
  Ecke)        ╲    wandert aus)   ╲   aus ◆ heraus)
```

### Beispiel 2: Launcher mit zwei Ringen

```
        ○  ○  ○
      ○  ◆  ●  ◆  ○        ● Anker · ◆ Ring 1 · ○ Ring 2 (Kinder
        ○  ◆  ○              des aktiven ◆, im coneAngle sichtbar)
```

### Beispiel 3: Speed-Dial unten rechts

```
                      ┌──────────────┐
                      │        ○   ◆ │   Anker = Ecke unten rechts,
                      │      ○   ◆   │   Ring als Halbfächer nach
                      │    ○   ◆  ●  │   innen geklemmt
                      └──────────────┘
```

## Siehe auch

- [Radial Menu – Beschreibung](./description.md)
- [Attribute](./attributes.md)
- [radial-out](../../../animations/entrance/radial-out/) und [radial-in](../../../animations/exit/radial-in/)
- [Floating Action Button](../../actions/floating-action-button/)
