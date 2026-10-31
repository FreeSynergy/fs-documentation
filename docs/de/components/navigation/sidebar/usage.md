# Sidebar - Verwendung

## Einfache Sidebar

```
┌──────────────────┐
│  🏠 Dashboard    │
│  📩 Nachrichten  │
│  📅 Termine      │
│  ──────────────── │
│  👤 Profil       │
│  ⚙️ Einstellungen │
└──────────────────┘
```

## Sidebar mit Gruppen

```
┌──────────────────┐
│ ⭐ Hauptmenü     │
├──────────────────┤
│  🏠 Dashboard    │
│  📩 Nachrichten  │
├──────────────────┤
│ 📊 Daten         │
├──────────────────┤
│  📅 Kalender     │
│  📋 Aufgaben     │
└──────────────────┘
```

## Sidebar mit Sub-Menüs

```
┌────────────────────┐
│ 📁 Dateien         │
│   ├─ Dokumente     │
│   ├─ Bilder        │
│   └─ Musik         │
├────────────────────┤
│ 🛠️ Einstellungen   │
│   ├─ Allgemein     │
│   └─ Sicherheit    │
└────────────────────┘
```

## Code-Beispiel (Pseudocode)

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
            label: "Nachrichten",
            icon: "email",
            path: "/messages",
            badge: Some("3")
        }
    ],
    groups: vec![
        MenuGroup {
            label: "Daten",
            items: vec![
                MenuItem { /* ... */ }
            ]
        }
    ]
}
```

## Integration in Programme

- **Messenger**: Server-Navigation, Kanäle, Kontakte
- **Desktop**: App-Übersicht, Einstellungen, Profile
- **CRM**: Kunden, Kontakte, Aufgaben
- **ERP**: Buchhaltung, Lager, Lieferanten
