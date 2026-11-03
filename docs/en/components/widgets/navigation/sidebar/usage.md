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

## Beispiele

## Beispiel 1: Messenger Sidebar (ähnlich Element/Discord)

```
┌──────────────────────────┐
│  🔵 FreeSynergy          │
├──────────────────────────┤
│  📩 Alle Nachrichten     │
│  💬 Privatchat           │
│  📊 Team-Kanal           │
│  🎮 Gaming-Channel       │
├──────────────────────────┤
│  👥 Kontakte             │
│  📅 Termine              │
├──────────────────────────┤
│  ──────────────────────  │
│  🏠 Workspace             │
│  ⚙️ Einstellungen        │
│  ❓ Hilfe                │
└──────────────────────────┘
```

## Beispiel 2: Desktop Shell

```
┌──────────────────────────┐
│     🖥️ FreeSynergy       │
├──────────────────────────┤
│  🏠 Startseite           │
│  📁 Dateien              │
│  📷 Fotos                │
│  🎵 Musik                │
│  🎥 Videos               │
├──────────────────────────┤
│  📧 E-Mail               │
│  📅 Kalender             │
│  👥 Kontakte             │
├──────────────────────────┤
│  🛠️ System               │
│  🔧 Einstellungen        │
│  ❓ Support              │
└──────────────────────────┘
```

## Beispiel 3: CRM mit Sub-Menüs

```
┌──────────────────────────┐
│ 📊 Übersicht             │
├──────────────────────────┤
│ 👥 Kunden                │
│   ├─ Aktive Kunden       │
│   ├─ Inaktive Kunden     │
│   └─ Lieferanten         │
├──────────────────────────┤
│ 📋 Aufgaben              │
│   ├─ Offene Aufgaben     │
│   ├─ Erledigte Aufgaben  │
│   └─ Termine             │
├──────────────────────────┤
│ 💰 Finanzen              │
│   ├─ Rechnungen          │
│   └─ Ausgaben            │
└──────────────────────────┘
```

## Interaktive Beispiele

Zwei Beispiele sind als Demo vorgesehen und noch nicht angelegt: eine Sidebar mit
Dropdown-Gruppen und eine Sidebar, deren Gruppen sich ein- und ausklappen lassen.
