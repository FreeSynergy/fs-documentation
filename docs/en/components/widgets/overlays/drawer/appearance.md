# Drawer - Appearance

## Base layout
A drawer is a side overlay window (collapsible).

```
┌─────────────────────────────────────────┐
│  ┌───────────────────────────────────┐  │
│  │ [✕] Menu                        │  │
│  ├───────────────────────────────────┤  │
│  │                                   │  │
│  │   Content                         │  │
│  │   ...                             │  │
│  │                                   │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Position | Description |
|---------------|----------|-------------|
| **Left Drawer** | left | left |
| **Right Drawer** | right | right |
| **Bottom Drawer** | bottom | bottom |
| **Full Drawer** | full | full screen |

## Sizes

| Size | Width/height | Use |
| ------- | ------------- | ------------ |
| Small | 200px | Wenige Elemente |
| Medium | 300px | Standard |
| Large | 400px | Viele Elemente |
| Full | 100% | Volle Breite/Höhe |

## Colours and states

| State | Colour | Description |
| -------- | ------- | -------------- |
| **Background** | Hell | Hintergrund |
| **Header** | Hell | Titelzeile |
| **Overlay** | Dunkel | Hintergrund abdunkeln |

## Hover and focus effects

| Effect | Description |
| -------- | -------------- |
| `shadow` | stronger shadow |
| `border` | the border lights up |

## Responsive

The drawer slides in from the edge (`slide-in`) and covers the content with a shadow; on a
wide surface it can stay open permanently and then divides the space like
[split-view](../../containers/split-view/). On a narrow surface the left drawer becomes an
overlay with dimming, the bottom drawer fills at most 80 % of the height.

```css
.drawer { position: fixed; top: 0; bottom: 0; left: 0; width: 300px;
          transform: translateX(-100%); transition: transform 200ms; }
.drawer--open { transform: translateX(0); }
.scrim        { background: rgba(0,0,0,.4); }

@media (min-width: 1024px) {
  .drawer--permanent { position: static; transform: none; }   /* fixed, without overlay */
  .scrim { display: none; }
}
@media (max-width: 600px) {
  .drawer--bottom { max-height: 80vh; }                        /* bottom drawer */
}
```

## Overlay

```
┌─────────────────────────────────────────┐
│  ┌───────────────────────────────────┐  │
│  │ [✕] Menu                        │  │
│  │                                   │  │
│  │   Content                         │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```
