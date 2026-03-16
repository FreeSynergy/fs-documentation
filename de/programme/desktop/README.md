# Desktop — Die Mensch-Maschine-Schnittstelle

[← Zurück zum Index](../../INDEX.md)

---

## Was Desktop macht

Desktop ist die UI für den Menschen. Es zeigt was Node und Conductor tun, bietet den Store-Browser, den Bot Manager, das Task-System, Widgets und Lenses.

Desktop ist auch UI für die Services selbst — Web-Interfaces werden eingebettet oder in Tabs geöffnet. Zukünftig: Gehostete Websites, Dokumenten-Betrachter, und mehr.

## Sidebar-Tabs

| Tab | Funktion |
|---|---|
| 🏠 Home | Persönliches Dashboard, Widgets, Quick-Launch |
| 📋 Tasks | Automatisierungs-Pipelines |
| 🎛️ Conductor | Service-Konfiguration |
| 🤖 Bots | Bots BENUTZEN |
| 🔍 Lenses | Informations-Betrachter |
| 📦 Store | Pakete installieren |
| 🔎 Search | Suche über alle Services |
| ⚙️ Settings | Themes, Shortcuts, Profil, Layout |
| ❓ Help | Dokumentation |

## Rendering-Modi

| Modus | Technologie |
|---|---|
| Desktop (WGUI) | Dioxus Webview |
| Native (GUI) | Dioxus Blitz/WGPU (experimentell) |
| Web | Dioxus WASM |
| TUI | Nicht umgesetzt (Dioxus TUI deprecated) |

## UI-Objekt-System

Alle sichtbaren Elemente basieren auf dem [FsnObject-System](../../technik/ui-objekte.md). Fenster, Widgets, Modals — alles folgt denselben Regeln für Resize, Drag, Minimize, Close.

## Eigenständigkeit

Desktop läuft auch offline. Es zeigt gecachte Daten, Widgets (Uhr, Notizen), und lokale Settings. Für Live-Daten braucht es eine Verbindung zu einem Node.

## Repo

https://github.com/FreeSynergy/Desktop

## Bibliotheken

| Crate | Zweck |
|---|---|
| `dioxus` 0.7.x | UI-Framework |
| `fsn-ui` | Komponenten-Bibliothek |
| `fsn-theme` | Theme-System |
| `fsn-i18n` | Sprach-Snippets |
| `fsn-db` | SQLite (fsn-desktop.db) |
| `fsn-store` | Store-Client |
| `reqwest` | Node-API aufrufen |

---

Weiter: [Lenses](../lenses/README.md) | [UI-Objekte](../../technik/ui-objekte.md)
