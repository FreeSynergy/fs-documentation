# Kontact - Structure & UI/UX

## Overview

Kontact has a classic, feature-rich UI with Activity Bar, Navigation area, Content area, and Status bar, optimized for the KDE desktop environment.

## Window Structure

### Main Areas

```
┌─────────────────────────────────────────────────────────────────┐
│  Title bar (Menu, Title, Window control)                        │
├───────┬──────────────────┬──────────────────┬───────────────────┤
│       │                  │                  │                   │
│  Act. │   Navigation     │   Content        │   Sidebars        │
│  Bar  │   (Left)         │   (Center)       │   (Right)         │
│ (Ext.)│  - Kontact       │  - Email         │  - Calendar       │
│       │  - Email         │  - Calendar      │  - Contacts       │
│       │  - Calendar      │  - Contacts      │  - Tasks          │
│       │  - Contacts      │  - Tasks         │  - Notes          │
│       │  - Tasks         │  - Notes         │  - Quick search   │
│       │  - Notes         │                  │                   │
│       │                  │                  │                   │
└───────┴──────────────────┴──────────────────┴───────────────────┘
```

### Activity Bar (Left)

The Activity Bar contains the main navigation and is located on the left edge:

| Element | Function |
|---------|----------|
| Kontact | Main view (Overview) |
| Email | Email view (KMail) |
| Calendar | Appointment overview (KOrganizer) |
| Contacts | Address management (KAddressBook) |
| Tasks | Task list (To-do lists) |
| Notes | Note management (KNotes) |
| News | News reader (KNode) |

### Navigation (Left Sidebar)

Next to the Activity Bar (in the current view):

| Element | Function |
|---------|----------|
| Inbox | Email folders |
| Sent Items | Sent messages |
| Drafts | Drafts |
| Trash | Deleted items |
| Junk Email | Spam folder |
| Calendar | Calendar overview |
| Contacts | Contact folders |
| Tasks | Task lists |
| Notes | Notes |

### Content Area (Center)

The Content area takes up the largest part of the screen:

- **Mailbox List**: Selected mailbox
- **Folder List**: Subfolders (for email)
- **Items List**: Messages/Appointments/Contacts/Tasks/Notes
- **Calendar View**: Month/Week view (for calendar)
- **Appointments**: Appointment list with timeline

### Sidebars (Right)

Optional right side: Display of details depending on the selected element

- **Email Preview**: Content of selected message
- **Appointment Preview**: Details of selected appointment
- **Contact Preview**: Details of selected contact
- **Task Preview**: Details of selected task
- **Note Preview**: Content of selected note

## UI/UX

### Design Principles

- **KDE-native**: Follows KDE Human Interface Guidelines
- **Functional**: Function over form
- **Consistent**: Consistent design across all areas
- **Adjustable**: Versatile layout options
- **Plasma Integration**: Seamless integration with KDE Plasma

### Color Scheme

- **Light Theme**: Classic light color scheme (Breeze Light)
- **Dark Theme**: Dark color scheme (Breeze Dark)
- **Customizable**: Customizable colors via system settings
- **Context-sensitive colors**: Colors for calendar, categories

### Typography

- **Headings**: Clear hierarchy (H1, H2, H3)
- **Text**: Readable font sizes (9-12pt)
- **Lists**: Clear bullet points with checkboxes
- **Monospace**: For email headers and code

### Interactions

- **Hover effects**: Visual feedback on hover (Breeze theme)
- **Click feedback**: Direct feedback on clicks
- **Drag & Drop**: For moving emails, appointments, contacts
- **Auto-save**: Automatic saving of drafts, notes
- **Context menus**: Right-click for context actions

### Responsive Design

- **Desktop**: Full functions with sidebar
- **Tablet**: Limited (desktop app)
- **Mobile**: Separate app (KDE Mobile Apps)

## Editor Structure

### Email Editor

```
┌─────────────────────────────────────────────────────────────────┐
│  Subject                                                        │
├─────────────────────────────────────────────────────────────────┤
│  To: [Recipient]                                                │
│  Cc: [Copy]                                                     │
│  Bcc: [Blind copy]                                              │
├─────────────────────────────────────────────────────────────────┤
│  Formatting toolbar (Menu)                                      │
├─────────────────────────────────────────────────────────────────┤
│  Content area (Full screen)                                     │
│                                                                 │
│  [Email text]                                                   │
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
│  From: [Date]     To: [Date]                                    │
│  Location: [Location]                                           │
│  Participants: [Participants]                                   │
├─────────────────────────────────────────────────────────────────┤
│  Description                                                    │
│                                                                 │
│  [Appointment description]                                      │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  Options (Duration, Reminder, Color, etc.)                     │
└─────────────────────────────────────────────────────────────────┘
```

### Contact Editor

```
┌─────────────────────────────────────────────────────────────────┐
│  General                                                        │
├─────────────────────────────────────────────────────────────────┤
│  Name: [First name] [Last name]                                 │
│  Organization: [Organization]                                   │
├─────────────────────────────────────────────────────────────────┤
│  Contact information                                            │
├─────────────────────────────────────────────────────────────────┤
│  Email: [Email]      Phone: [Phone]                             │
│  Web: [Website]      Fax: [Fax]                                 │
├─────────────────────────────────────────────────────────────────┤
│  Address                                                        │
├─────────────────────────────────────────────────────────────────┤
│  Street: [Street]    City: [City]                               │
│  ZIP: [ZIP]          Country: [Country]                         │
├─────────────────────────────────────────────────────────────────┤
│  Custom fields                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Accessibility

- **Keyboard navigation**: Complete control via keyboard
- **Screen reader support**: AT support (AT-SPI)
- **Contrast**: High contrast for better readability
- **Zoom**: Scalable UI (100-400%)
- **Accessibility**: KDE accessibility settings

## Performance

- **Fast loading**: Fast opening of messages
- **Caching**: Client-side caching
- **Pagination**: For large lists
- **Debounce**: For search functions
- **Threading**: Multithreading for fast computational operations
