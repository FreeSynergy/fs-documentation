# Button-Gruppe – Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt ist, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Zwei Aktionen als eine Einheit

```jsx
<ButtonGroup items={[saveButton, publishButton]} variant="verbund" />
```

## Ansicht umschalten (segmentierte Auswahl)

```jsx
<ButtonGroup
  variant="segment"
  value={viewMode}
  onSelect={setViewMode}
  items={[
    { value: "list", label: "List" },
    { value: "grid", label: "Grid" },
    { value: "timeline", label: "Timeline" }
  ]}
/>
```

## Ausrichtung in einem Editor (Mehrfachauswahl)

```jsx
<ButtonGroup
  variant="segment"
  selectionMode="multiple"
  value={activeAlignments}
  onSelect={setActiveAlignments}
  items={alignmentOptions}
/>
```

## Hauptaktion mit Auswahlliste (Split-Button)

```jsx
<ButtonGroup
  variant="split"
  items={[
    { label: "Save", onClick: save },
    { icon: "chevron-down", menu: saveAsMenu }
  ]}
/>
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Werkzeuge im Editor (fett, kursiv, unterstrichen) | `segment`, `selectionMode="multiple"` |
| Dialog: Speichern / Speichern unter | `split` |
| Zwei gleichrangige Aktionen in einem Formular | getrennte Buttons, keine Gruppe |
| Viele Optionen (> 5) | `select` statt einer Segmentgruppe |
