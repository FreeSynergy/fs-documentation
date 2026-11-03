# Icon - Usage

## A simple icon

```jsx
// React example
import { Icon } from '@freesynergy/ui';

<Icon name="mdi:home" size="medium" color="primary" />
```

```html
<!-- HTML with SVG -->
<svg class="icon icon-medium icon-primary" aria-label="Home">
  <use href="#icon-home"></use>
</svg>
```

## An interactive icon

```jsx
<Icon
  name="mdi:pencil"
  size="medium"
  interactive={true}
  onClick={() => console.log('Edit')}
  hoverEffect="zoom"
/>
```

## An icon with hover text (tooltip)

```jsx
<Tooltip content="Home">
  <Icon name="mdi:home" size="medium" interactive={true} />
</Tooltip>
```

## Loading icon (spin)

```jsx
<Icon
  name="mdi:loading"
  size="medium"
  spin={true}
  animationDuration={1000}
/>
```

## A responsive icon

```jsx
<Icon
  name="mdi:search"
  size="medium"
  responsiveSize={true}
  hideOnMobile={true}
/>
```

## An icon with a badge

```jsx
<div style={{ position: 'relative' }}>
  <Icon name="mdi:email" size="medium" />
  <Badge value="3" position="top-right" />
</div>
```

## An icon in a button

```jsx
<Button variant="primary">
  <Icon name="mdi:plus" size="small" />
  <span>New</span>
</Button>
```

## An icon in the navigation

```jsx
<MenuItem
  icon="mdi:home"
  label="Home"
  onClick={() => navigate('/')}
/>
```

## An icon in a list item

```jsx
<ListItem>
  <Icon name="mdi:file-pdf" size="small" shape="rectangular" color="error" />
  <span>document.pdf</span>
</ListItem>
```

## Examples

## Example 1: navigation icons

```
┌──────────────────────────┐
│ 🏠 Home                  │
│ 📩 Messages              │
│ 📅 Calendar              │
│ 👥 Contacts              │
├──────────────────────────┤
│ 📊 Dashboard             │
│ 💰 Finance               │
│ 📈 Statistics            │
└──────────────────────────┘
```

## Example 2: toolbar icons

```
┌────────────────────────────────────────────┐
│ [📄] [✏️] [✂️] [✔️] [❌] [🔍] [⚙️]         │
└────────────────────────────────────────────┘
```

## Example 3: action icons

```
┌──────────────────────────┐
│ 📥 Download              │
│ 📤 Upload                │
│ 🖨️ Print                 │
│ 📧 Email                 │
│ 🔗 Share                 │
└──────────────────────────┘
```

## Example 4: status icons

```
Online:   ● (green)
Offline:  ● (grey)
Away:     ● (orange)
Busy:     ● (red)
```

## Example 5: form icons

```
┌──────────────────────────┐
│ 🏷️ Tag                   │
│ 📎 Attachment            │
│ 📅 Date                  │
│ ⏰ Time                  │
└──────────────────────────┘
```

## Example 6: file type icons

```
📄 PDF document
🖼️ Image
🎵 Audio
🎬 Video
📁 Folder
📝 Text document
.xlsx Spreadsheet
```

## Example 7: social media icons

```
📘 Facebook
📷 Instagram
🐦 Twitter/X
📘 LinkedIn
▶️ YouTube
🐙 GitHub
```

## Example 8: settings icons

```
⚙️ General
🔒 Security
👥 Users
🌐 Language
📱 Mobile
 bell Notifications
```
