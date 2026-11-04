# Sidebar - Usage

## Simple sidebar

```
┌──────────────────┐
│  🏠 Dashboard    │
│  📩 Messages     │
│  📅 Appointments │
│  ────────────────│
│  👤 Profile      │
│  ⚙️ Settings     │
└──────────────────┘
```

## Sidebar with groups

```
┌──────────────────┐
│ ⭐ Main menu     │
├──────────────────┤
│  🏠 Dashboard    │
│  📩 Messages     │
├──────────────────┤
│ 📊 Data          │
├──────────────────┤
│  📅 Calendar     │
│  📋 Tasks        │
└──────────────────┘
```

## Sidebar with sub-menus

```
┌────────────────────┐
│ 📁 Files           │
│   ├─ Documents     │
│   ├─ Images        │
│   └─ Music         │
├────────────────────┤
│ 🛠️ Settings        │
│   ├─ General       │
│   └─ Security      │
└────────────────────┘
```

## Code example (pseudocode)

```rust
Sidebar {
    position: SidebarPosition::Left,
    width: 240,
    items: vec![
        MenuItem {
            id: "dashboard",
            label: "Dashboard",
            icon: "house",
            path: "/dashboard"
        },
        MenuItem {
            id: "messages",
            label: "Messages",
            icon: "email",
            path: "/messages",
            badge: Some("3")
        }
    ],
    groups: vec![
        MenuGroup {
            label: "Data",
            items: vec![
                MenuItem { /* ... */ }
            ]
        }
    ]
}
```

## Integration in programs

- **Messenger**: server navigation, channels, contacts
- **Desktop**: app overview, settings, profiles
- **CRM**: customers, contacts, tasks
- **ERP**: accounting, warehouse, suppliers

## Examples

## Example 1: messenger sidebar (similar to Element/Discord)

```
┌──────────────────────────┐
│  🔵 FreeSynergy          │
├──────────────────────────┤
│  📩 All messages         │
│  💬 Private chat         │
│  📊 Team channel         │
│  🎮 Gaming channel       │
├──────────────────────────┤
│  👥 Contacts             │
│  📅 Appointments         │
├──────────────────────────┤
│  ──────────────────────  │
│  🏠 Workspace            │
│  ⚙️ Settings             │
│  ❓ Help                 │
└──────────────────────────┘
```

## Example 2: desktop shell

```
┌──────────────────────────┐
│     🖥️ FreeSynergy       │
├──────────────────────────┤
│  🏠 Start page           │
│  📁 Files                │
│  📷 Photos               │
│  🎵 Music                │
│  🎥 Videos               │
├──────────────────────────┤
│  📧 E-mail               │
│  📅 Calendar             │
│  👥 Contacts             │
├──────────────────────────┤
│  🛠️ System               │
│  🔧 Settings             │
│  ❓ Support              │
└──────────────────────────┘
```

## Example 3: CRM with sub-menus

```
┌──────────────────────────┐
│ 📊 Overview              │
├──────────────────────────┤
│ 👥 Customers             │
│   ├─ Active customers    │
│   ├─ Inactive customers  │
│   └─ Suppliers           │
├──────────────────────────┤
│ 📋 Tasks                 │
│   ├─ Open tasks          │
│   ├─ Done tasks          │
│   └─ Appointments        │
├──────────────────────────┤
│ 💰 Finance               │
│   ├─ Invoices            │
│   └─ Expenses            │
└──────────────────────────┘
```

## Interactive examples

Two examples are planned as demos and not yet created: a sidebar with dropdown groups
and a sidebar whose groups can be collapsed and expanded.
