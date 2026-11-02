# Multi-Finger Swipe

## Description

A multi-finger swipe is a swipe with **two or more fingers** at the same time
(classically three). It belongs to the system and accessibility gestures: on
macOS it controls Mission Control navigation, in iOS VoiceOver it switches
apps, and Android uses multi-finger swipes in its accessibility features
(three-finger swiping for back/home/recents in older navigation sets).

Whether two, three, or four fingers do the swiping is a setting
(`pointerCount`) – the gesture stays the same.

## Usage

- Switching apps / tasks (iOS VoiceOver, Android accessibility)
- Switching desktop/workspace (macOS Mission Control, Linux workspaces)
- Back/forward in documents (e-readers, reader apps)
- Fullscreen control in video apps (multi-finger swipe = mini player)

## Direction

| Direction | Typical action |
|-----------|----------------|
| Left/Right | Switch workspace/page |
| Up | Open the task overview |
| Down | Close the task overview / home |

## Duration

- Swipe duration: 150–500ms
- All fingers must be down together within ~150ms

## Detection

| Method | Description |
|--------|-------------|
| **Pointer Count** | Exactly `pointerCount` active pointers (default 3) |
| **Sync Window** | Tolerate a common down moment |
| **Direction Vector** | Horizontal/vertical main vector as with Swipe |

## Difference from Swipe

- **Swipe**: one finger, app-internal navigation
- **Multi-Finger Swipe**: two or more fingers, usually the system/app-switching level

## Difference from Pinch

- **Pinch**: pointers move towards each other, transforming content
- **Multi-Finger Swipe**: all pointers in the same direction, changing context
