# Context Toolbar - Verwendung

## Einfache Context Toolbar

```jsx
<ContextToolbar 
  buttons={[
    { id: 'bold', icon: 'bold', label: 'Fett' },
    { id: 'italic', icon: 'italic', label: 'Kursiv' },
    { id: 'underline', icon: 'underline', label: 'Unterstrichen' }
  ]}
  visible={selectionActive}
/>
```

## In Text-Editor

```jsx
<TextEditor 
  onSelectionChange={(selection) => {
    setSelection(selection);
    setShowToolbar(!!selection);
  }}
>
  <ContextToolbar 
    buttons={textFormatButtons}
    visible={showToolbar}
    target={selection?.target}
  />
</TextEditor>
```

## Mit Event-Handlern

```jsx
<ContextToolbar 
  buttons={buttons}
  onButtonClick={(id) => console.log('Clicked:', id)}
/>
```

## Mit Animation

```jsx
<ContextToolbar 
  buttons={buttons}
  animation="slide-up"
  duration={200}
/>
```
