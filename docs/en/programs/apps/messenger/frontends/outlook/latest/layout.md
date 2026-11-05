# Outlook - Structure & UI/UX

## Overview

Outlook has a classic, feature-rich UI with an activity bar, a navigation area, a content area and a status bar.

## Window Structure

### Main Areas

```
┌───────┬──────────────────┬──────────────────┬───────────────────┐
│  Title bar (menu, title, window controls)                       │
├───────┬──────────────────┬──────────────────┬───────────────────┤
│       │                  │                  │                   │
│  Act. │   Navigation     │   Content        │   Preview         │
│  Bar  │   (left)         │   (middle)       │   (right)         │
│ (ext.)│  - Mailboxes     │  - Messages      │  - Messages       │
│       │  - Calendar      │  - Appointments  │  - Preview        │
│       │  - Contacts      │  - Contacts      │  - Details        │
│       │  - Tasks         │  - Tasks         │                   │
│       │  - Notes         │  - Notes         │                   │
│       │                  │                  │                   │
└───────┴──────────────────┴──────────────────┴───────────────────┘
```

### Activity Bar (Left)

The activity bar holds the main navigation:

| Element | Function |
|---------|----------|
| Mailboxes | Email view |
| Calendar | Appointment overview |
| Contacts | Address management |
| Tasks | Task list |
| Notes | Note management |

### Navigation (Left)

Next to the activity bar:

| Element | Function |
|---------|----------|
| Inbox | Email folders |
| Sent items | Sent messages |
| Drafts | Drafts |
| Deleted items | Deleted items |
| Junk email | Spam folder |
| Calendar | Calendar overview |
| Contacts | Contact folders |

### Content Area (Center)

The content area takes up most of the screen:

- **Mailbox list**: the selected mailbox
- **Folder list**: subfolders
- **Item list**: messages/appointments/contacts

### Preview Area (Right)

Optionally on the right:

- **Message preview**: the content of the selected message
- **Appointment preview**: details of the selected appointment
- **Contact preview**: details of the selected contact

## UI/UX

### Design Principles

- **Classic**: a traditional office application
- **Functional**: function over form
- **Consistency**: a uniform design across all areas
- **Customisable**: a wide range of layout options

### Interactions

- **Hover effects**: visual feedback on hover
- **Click feedback**: direct feedback on clicks
- **Drag & drop**: for moving emails
- **Auto-save**: drafts save automatically

### Responsive Design

- **Desktop**: full features with a sidebar
- **Tablet**: limited (the desktop app)
- **Mobile**: a separate app (Outlook Mobile)

## Editor Structure

### Email Editor

```
┌─────────────────────────────────────────────────────────────────┐
│  Subject                                                        │
├─────────────────────────────────────────────────────────────────┤
│  To: [recipient]                                                │
│  Cc: [copy]                                                     │
│  Bcc: [blind copy]                                              │
├─────────────────────────────────────────────────────────────────┤
│  Formatting bar (menu)                                          │
├─────────────────────────────────────────────────────────────────┤
│  Content area (full width)                                      │
│                                                                 │
│  [email text]                                                   │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  Attachments                                                    │
└─────────────────────────────────────────────────────────────────┘
```

### Calendar Editor

```
┌─────────────────────────────────────────────────────────────────┐
│  Subject                                                        │
├─────────────────────────────────────────────────────────────────┤
│  From: [date]     To: [date]                                    │
│  Location: [place]                                              │
│  Attendees: [attendees]                                         │
├─────────────────────────────────────────────────────────────────┤
│  Description                                                    │
│                                                                 │
│  [appointment description]                                      │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  Options (duration, reminder, colour, etc.)                     │
└─────────────────────────────────────────────────────────────────┘
```

## Accessibility

- **Keyboard navigation**: full control via the keyboard
- **Screen reader support**: ARIA attributes
- **Contrast**: high contrast for better readability
- **Zoom**: scalable UI (100–400 %)

## Performance

- **Fast loading**: messages open quickly
- **Caching**: client-side caching (OST files)
- **Pagination**: for large lists
- **Debounce**: for the search functions

## Themes

Colours, typography and theme details: see [themes](themes/index.md).
