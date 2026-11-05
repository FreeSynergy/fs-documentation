# QGIS - Structure and UI/UX

## Window layout

```
┌────────────────────────────────────────────────────────────────┐
│ Menu · toolbars (digit.: ✏ snap identify measure…)             │
├──────────┬──────────────────────────────────┬──────────────────┤
│Layer tree│  Map view (CRS on-the-fly)       │Processing toolbox│
│▸ Points  │   (zoom/pan, overlaid)           │▸ Analysis…       │
│▸ Water   │                                  │▸ Overlay…        │
├────────────────────────────────────────────────────────────────┤
│ Status: coordinates | scale | snap radius | render log         │
└────────────────────────────────────────────────────────────────┘
Attribute table dockable at the bottom; layer properties as a dialog
```

- The layer tree on top = drawing order (bottom = top of the map)
- Processing toolbox on the right with a search field (the "find everything" of the analyses)

## UI/UX

- Desktop classic: dialogs, right-click context menu per layer/tool
- Styles as qml files (exchangeable, versionable within projects)

## Interactions

- Edit mode: drag vertices, snapping (Shift for a temporary breakout)
- Identify tool = attribute popups; scale/selection tabs in the attribute table

## Responsive design

Not applicable (desktop; QField for mobile)

## Accessibility

- Qt standard; menus/shortcuts fully keyboard-driven; colour areas for the colour-blind (pattern styles)

## Performance

- Large layers: generalisation/overviews, indexes in PostGIS; use render parallelism
