# OpenBoard - Structure and UI/UX

## Page structure

```
┌──────────────────────────────────────────────────────────────────┐
│ Tool strip left │   Full-screen board page (page 3/8)            │
│ ✏️🖍 🧽 ▢◯  T 🌐 📄 │                                            │
│ 📏📐 ⏱ 🎥 🗂       │     handwritten elements, images,          │
│ (expandable)       │     text fields, embedded PDFs             │
│                    │                                            │
│ Library (bottom, collapsible: media/stacks/documents)            │
│ Page tabs: ‹ 1 2 3 4 ›  + new page                               │
└──────────────────────────────────────────────────────────────────┘
```

- Full screen without a menu bar; the tool strips fold out sideways (touch logic)

## UI/UX

- Large controls usable with gloves and pen; dark page background option (beamer contrast)
- Page changes feel like turning pages, the presentation mode hides the UI

## Interactions

- Pen/touch/multitouch (zooming with fingers, palm eraser depending on the device driver)
- Move/scale elements with a selection frame; groups ("stacks")

## Responsive design

not applicable (desktop/whiteboard application; several page formats)

## Accessibility

- Keyboard control is elementary (shortcuts below); primarily pen/touch operation — screen readers are not a core goal

## Performance

- Heavy media load (video) stutters on old whiteboard hardware; keep embedded PDFs lean
