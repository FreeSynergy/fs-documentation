# Icon - Verwendung

## Einfaches Icon

```jsx
// React-Beispiel
import { Icon } from '@freesynergy/ui';

<Icon name="mdi:home" size="medium" color="primary" />
```

```html
<!-- HTML mit SVG -->
<svg class="icon icon-medium icon-primary" aria-label="Startseite">
  <use href="#icon-home"></use>
</svg>
```

## Interaktives Icon

```jsx
<Icon 
  name="mdi:pencil" 
  size="medium" 
  interactive={true}
  onClick={() => console.log('Bearbeiten')}
  hoverEffect="zoom"
/>
```

## Icon mit Hover-Text (Tooltip)

```jsx
<Tooltip content="Startseite">
  <Icon name="mdi:home" size="medium" interactive={true} />
</Tooltip>
```

## Loading-Icon (Spin)

```jsx
<Icon 
  name="mdi:loading" 
  size="medium" 
  spin={true} 
  animationDuration={1000}
/>
```

## Responsive Icon

```jsx
<Icon 
  name="mdi:search" 
  size="medium" 
  responsiveSize={true}
  hideOnMobile={true}
/>
```

## Icon mit Badge

```jsx
<div style={{ position: 'relative' }}>
  <Icon name="mdi:email" size="medium" />
  <Badge value="3" position="top-right" />
</div>
```

## Icon in Button

```jsx
<Button variant="primary">
  <Icon name="mdi:plus" size="small" />
  <span>Neu</span>
</Button>
```

## Icon in Navigation

```jsx
<MenuItem 
  icon="mdi:home" 
  label="Startseite" 
  onClick={() => navigate('/')}
/>
```

## Icon in List-Item

```jsx
<ListItem>
  <Icon name="mdi:file-pdf" size="small" shape="rectangular" color="error" />
  <span>Dokument.pdf</span>
</ListItem>
```
