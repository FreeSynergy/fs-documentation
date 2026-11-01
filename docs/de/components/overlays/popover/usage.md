# Popover (Inhaltspopover) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Aktionen an einem Eintrag

```jsx
<Popover trigger="click" placement="bottom" variant="aktionen" content={entryActions} />
```

## Schneller Dialog: Fälligkeit setzen

```jsx
<Popover
  variant="formular"
  trigger="click"
  closeOnAction={true}
  content={<DatePicker value={due} onChange={setDue} />}
/>
```

## Vorschau beim Überfahren

```jsx
<Popover trigger="hover" placement="right" dismiss="click-outside" content={previewCard} />
```

## Gesteuert öffnen und schließen

```jsx
<Popover open={menuOpen} onClose={() => setMenuOpen(false)} content={rowMenu} />
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Mehr-Menü an Tabellenzeilen | `aktionen`, `trigger="click"` |
| Datum/Farbe schnell setzen | `formular`, `closeOnAction` |
| Link-Ziel-Vorschau | hover-card (geplant, Welle 2), sonst `inhalt` mit `trigger="hover"` |
| Zentrierter Bestätigungsdialog | [modal](../modal/) bzw. alert-dialog (geplant) |
