# OBS Studio - Structure and UI/UX

## Main window (default layout)

```
┌──────────────────────────────────────────────────────────────────────┐
│ File  View  Edit  Settings  Help                                     │
├──────────────┬────────────────────────────────┬──────────────────────┤
│ Scenes       │        Preview (program)       │ Sources              │
│ ▸ Folder     │   ┌──────────────────────┐     │ ▸ Screen             │
│   ▸ Intro    │   │   red border =       │     │ ▸ Camera             │
│ ▸ Talk       │   │   active scene       │     │ ▸ Browser source     │
│--------------│   └──────────────────────┘     │----------------------│
│ Transitions  │  FPS | CPU | dropped (status)  │ Audio mixer          │
├──────────────┴────────────────────────────────┴──────────────────────┤
│ Controls: Start Streaming | Start Recording | Studio Mode | Replays  │
└──────────────────────────────────────────────────────────────────────┘
```

- Red border = active program output, green border = studio preview
- Every area is a dock and freely arrangeable (View menu)

## UI/UX

- Default dark theme, surface scaling configurable for 4K
- Status bar bottom right: FPS, dropped frames, CPU usage, bandwidth
- Context menus instead of buttons for most source actions

## Interactions

- **Drag & drop**: files into the scene list (new scene) or into the source list (new source)
- **Drag the handle points** in the preview to transform, `Alt`+drag to crop
- **Fast switching** via hotkey or scene click
- **Studio mode**: prepare the preview, then "execute transition"

## Responsive design

| Platform | Behaviour |
|----------|-----------|
| Desktop (Win/macOS/Linux) | full dock layout, multi-monitor capable |
| 4K/HiDPI | UI scaling 100–300 % |
| Mobile | ❌ no official client (remote control via obs-websocket apps) |

## Accessibility

- Keyboard control via hotkeys and menu focus; screen readers only limited (Qt docks) (⚠)
- Preview without colour coding as a state: the status bar supplies text values
- Hotkeys fully configurable, a conflict warning for occupied keys is integrated

## Performance

- Encoding load visible in the status bar, a dropped counter for streams
- Recommendation: separate recording/streaming encoders, NVENC/QSV to spread the load
