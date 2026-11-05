# Thunderbird - Structure & UI/UX

## Overview

Thunderbird has a classic, functional UI with activity bar, navigation area, content area, and status bar, optimized for email communication.

## Window Structure

### Main Areas

```
┌─────────────────────────────────────────────────────────────────┐
│  Title bar (Menu, Title, Window controls)                       │
├───────┬──────────────────┬──────────────────┬───────────────────┤
│       │                  │                  │                   │
│  Act. │   Navigation     │   Content        │   Sidebar         │
│  Bar  │   (Left)         │   (Center)       │   (Right)         │
│ (Int.)│  - Accounts      │  - Messages      │  - Preview        │
│       │  - Calendar      │  - Appointments  │  - Contacts       │
│       │  - Contacts      │  - Contacts      │  - Search results │
│       │                  │                  │                   │
└───────┴──────────────────┴──────────────────┴───────────────────┘
```

### Activity Bar (Left)

The activity bar contains the main navigation (integrated into the navigation bar):

| Element | Function |
|---------|----------|
| Accounts | Account management |
| Inbox | Email folders |
| Sent Items | Sent messages |
| Drafts | Drafts |
| Trash | Deleted items |
| Junk Email | Spam folder |
| Calendar | Appointment overview (Lightning) |
| Address Book | Address management (Lightning) |

### Navigation (Left)

Left in the navigation bar:

| Element | Function |
|---------|----------|
| Mailboxes | Email folders |
| Accounts | Account management |
| Calendar | Calendar overview (Lightning) |
| Address Book | Address book (Lightning) |
| Subscription Feeds | RSS/Atom feeds |

### Content Area (Center)

The content area takes up the largest part of the screen:

- **Mailbox list**: Selected mailbox
- **Folder list**: Subfolders
- **Items list**: Messages/appointments/contacts
- **Calendar view**: Month/week view (for calendar)

### Sidebar (Right)

Optionally right: Display of details depending on the selected item

- **Preview window**: Content of selected message
- **Appointment preview**: Details of selected appointment
- **Contact preview**: Details of selected contact
- **Search results**: Live search results

## UI/UX

### Design Principles

- **Functional**: Function over form
- **Consistent**: Consistent design across all areas
- **Customizable**: Versatile layout options
- **Mozilla-style**: Follows Mozilla design guidelines
- **Accessible**: Focus on accessibility

### Color Scheme

- **Light Theme**: Classic light color scheme
- **Dark Theme**: Dark color scheme
- **Custom**: Customizable colors via theme system
- **Context-based colors**: Colors for calendar, categories

### Typography

- **Headings**: Clear hierarchy
- **Text**: Readable font sizes (10-12pt)
- **Lists**: Clear bullet points with checkboxes
- **Monospace**: For email headers

### Interactions

- **Hover effects**: Visual feedback on hover
- **Click feedback**: Direct feedback on clicks
- **Drag & Drop**: For moving emails, appointments
- **Auto-save**: Automatic saving of drafts
- **Context menus**: Right-click for context actions

### Responsive Design

- **Desktop**: Full features with sidebar
- **Tablet**: Limited (desktop app)
- **Mobile**: Separate app (Thunderbird Mobile in development)

## Editor Structure

### Email Editor

```
┌─────────────────────────────────────────────────────────────────┐
│  Subject                                                         │
├─────────────────────────────────────────────────────────────────┤
│  To: [Recipient]                                                │
│  Cc: [Copy]                                                     │
│  Bcc: [ Blind copy]                                             │
├─────────────────────────────────────────────────────────────────┤
│  Formatting bar (menu)                                          │
├─────────────────────────────────────────────────────────────────┤
│  Content area (full screen)                                     │
│                                                                 │
│  [Email text]                                                   │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  Attachments                                                     │
└─────────────────────────────────────────────────────────────────┘
```

### Calendar Editor (Lightning)

```
┌─────────────────────────────────────────────────────────────────┐
│  Subject                                                         │
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

## Accessibility

- **Keyboard navigation**: Complete control via keyboard
- **Screen reader support**: ARIA attributes
- **Contrast**: High contrast for better readability
- **Zoom**: Scalable UI (100-400%)
- **Accessibility**: Mozilla accessibility settings

## Performance

- **Fast loading**: Fast opening of messages
- **Caching**: Client-side caching
- **Pagination**: For large lists
- **Debounce**: For search functions
- **Lazy loading**: For large calendars and address books
