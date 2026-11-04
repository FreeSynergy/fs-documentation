# Toolbar - Usage

## Einfache Toolbar

```jsx
<Toolbar 
  buttons={[
    { id: 'new', icon: 'plus', label: 'New', onClick: ... },
    { id: 'save', icon: 'save', label: 'Save', onClick: ... },
    { id: 'delete', icon: 'trash', label: 'Delete', onClick: ... }
  ]}
/>
```

## With separators

```jsx
<Toolbar 
  buttons={[
    { id: 'new', icon: 'plus', label: 'New' },
    { id: 'open', icon: 'folder', label: 'Open' },
    { separator: true },
    { id: 'copy', icon: 'copy', label: 'Copy' },
    { id: 'paste', icon: 'paste', label: 'Paste' }
  ]}
/>
```

## Floating Toolbar

```jsx
<FloatingToolbar 
  buttons={actionButtons}
  position="bottom-right"
/>
```

## In an app

```jsx
<AppShell>
  <Header />
  <Toolbar 
    buttons={toolbarButtons}
    position="top"
  />
  <Content />
</AppShell>
```

## With event handlers

```jsx
<Toolbar 
  buttons={buttons}
  onButtonClick={(id) => console.log('Clicked:', id)}
/>
```

## Examples

## Example 1: Text-Editor

```
┌─────────────────────────────────────────────────────┐
│ [📄] [✏️] [✂️] [✔️] [❌] [🔍] [⚙️] [Drucken]       │
└─────────────────────────────────────────────────────┘
```

## Example 2: Bildbearbeitung

```
┌─────────────────────────────────────────────────────┐
│ [Neu] [Öffnen] [Speichern] [Exportieren]           │
│ [Back] [Fwd] [Zoom-] [Zoom+] [100%]               │
└─────────────────────────────────────────────────────┘
```

## Example 3: Chat-Tools

```
┌─────────────────────────────────────────────────────┐
│ [🖼️] [ sticker] [🎤] [📹] [📁] [😀]                │
└─────────────────────────────────────────────────────┘
```

## Example 4: IDE-Toolbar

```
┌─────────────────────────────────────────────────────┐
│ [▶] [⏸] [⏹] [🪲] [⚙️] [🔍] [🧪] [💾]               │
└─────────────────────────────────────────────────────┘
```

## Example 5: Dashboard

```
┌─────────────────────────────────────────────────────┐
│ [📊] [📋] [👥] [⚙️] [🔔] [👤] [❓]                  │
└─────────────────────────────────────────────────────┘
```
