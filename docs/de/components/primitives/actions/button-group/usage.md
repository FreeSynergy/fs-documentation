# Button Group (Schaltflächengruppe) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Zwei Aktionen als Einheit

```jsx
<ButtonGroup items={[saveButton, publishButton]} variant="verbund" />
```

## Ansicht wechseln (Segmented Control)

```jsx
<ButtonGroup
  variant="segment"
  value={viewMode}
  onSelect={setViewMode}
  items={[
    { value: "list", label: "Liste" },
    { value: "grid", label: "Raster" },
    { value: "timeline", label: "Zeitleiste" }
  ]}
/>
```

## Ausrichtung im Editor (Mehrfachauswahl)

```jsx
<ButtonGroup
  variant="segment"
  selectionMode="multiple"
  value={activeAlignments}
  onSelect={setActiveAlignments}
  items={alignmentOptions}
/>
```

## Hauptaktion mit Dropdown (Split-Button)

```jsx
<ButtonGroup
  variant="split"
  items={[
    { label: "Speichern", onClick: save },
    { icon: "chevron-down", menu: saveAsMenu }
  ]}
/>
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Editor-Werkzeuge (fett, kursiv, unterstrichen) | `segment`, `selectionMode="multiple"` |
| Dialog: Speichern / Speichern unter | `split` |
| Zwei gleichrangige Aktionen im Formular | getrennte Buttons, keine Gruppe |
| Viele Optionen (> 5) | `select` statt Segmentgruppe |
