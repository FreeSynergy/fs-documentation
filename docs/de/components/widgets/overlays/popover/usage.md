# Popover - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung zu Rust und Blinc wechselt,
    werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Aktionen an einem Eintrag

```jsx
<Popover trigger="click" placement="bottom" variant="aktionen" content={entryActions} />
```

## Schneller Dialog: Fälligkeitsdatum setzen

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

## Gesteuertes Öffnen und Schließen

```jsx
<Popover open={menuOpen} onClose={() => setMenuOpen(false)} content={rowMenu} />
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Mehr-Menü an Tabellenzeilen | `aktionen`, `trigger="click"` |
| Datum oder Farbe schnell setzen | `formular`, `closeOnAction` |
| Vorschau eines Linkziels | [hover-card](../hover-card/), sonst `inhalt` mit `trigger="hover"` |
| zentrierter Bestätigungsdialog | [modal](../modal/) oder [alert-dialog](../alert-dialog/) |
