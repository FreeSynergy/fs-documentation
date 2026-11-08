# Icon - Verwendung

## Ein einfaches Icon

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

## Ein interaktives Icon

```jsx
<Icon
  name="mdi:pencil"
  size="medium"
  interactive={true}
  onClick={() => console.log('Bearbeiten')}
  hoverEffect="zoom"
/>
```

## Ein Icon mit Hinweistext (Tooltip)

```jsx
<Tooltip content="Startseite">
  <Icon name="mdi:home" size="medium" interactive={true} />
</Tooltip>
```

## Ladeicon (drehend)

```jsx
<Icon
  name="mdi:loading"
  size="medium"
  spin={true}
  animationDuration={1000}
/>
```

## Ein responsives Icon

```jsx
<Icon
  name="mdi:search"
  size="medium"
  responsiveSize={true}
  hideOnMobile={true}
/>
```

## Ein Icon mit Badge

```jsx
<div style={{ position: 'relative' }}>
  <Icon name="mdi:email" size="medium" />
  <Badge value="3" position="top-right" />
</div>
```

## Ein Icon im Button

```jsx
<Button variant="primary">
  <Icon name="mdi:plus" size="small" />
  <span>Neu</span>
</Button>
```

## Ein Icon in der Navigation

```jsx
<MenuItem
  icon="mdi:home"
  label="Startseite"
  onClick={() => navigate('/')}
/>
```

## Ein Icon in einem Listenelement

```jsx
<ListItem>
  <Icon name="mdi:file-pdf" size="small" shape="rectangular" color="error" />
  <span>dokument.pdf</span>
</ListItem>
```

## Beispiele

## Beispiel 1: Navigationsicons

```
┌──────────────────────────┐
│ 🏠 Startseite            │
│ 📩 Nachrichten           │
│ 📅 Kalender              │
│ 👥 Kontakte              │
├──────────────────────────┤
│ 📊 Dashboard             │
│ 💰 Finanzen              │
│ 📈 Statistiken           │
└──────────────────────────┘
```

## Beispiel 2: Werkzeugleisten-Icons

```
┌────────────────────────────────────────────┐
│ [📄] [✏️] [✂️] [✔️] [❌] [🔍] [⚙️]         │
└────────────────────────────────────────────┘
```

## Beispiel 3: Aktions-Icons

```
┌──────────────────────────┐
│ 📥 Herunterladen         │
│ 📤 Hochladen             │
│ 🖨️ Drucken               │
│ 📧 E-Mail                │
│ 🔗 Teilen                │
└──────────────────────────┘
```

## Beispiel 4: Status-Icons

```
Online:   ● (grün)
Offline:  ● (grau)
Abwesend: ● (orange)
Beschäftigt: ● (rot)
```

## Beispiel 5: Formular-Icons

```
┌──────────────────────────┐
│ 🏷️ Tag                   │
│ 📎 Anhang                │
│ 📅 Datum                 │
│ ⏰ Uhrzeit               │
└──────────────────────────┘
```

## Beispiel 6: Dateityp-Icons

```
📄 PDF-Dokument
🖼️ Bild
🎵 Audio
🎬 Video
📁 Ordner
📝 Textdokument
.xlsx Tabelle
```

## Beispiel 7: Social-Media-Icons

```
📘 Facebook
📷 Instagram
🐦 Twitter/X
📘 LinkedIn
▶️ YouTube
🐙 GitHub
```

## Beispiel 8: Einstellungs-Icons

```
⚙️ Allgemein
🔒 Sicherheit
👥 Benutzer
🌐 Sprache
📱 Mobil
 bell Benachrichtigungen
```
