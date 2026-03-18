# Desktop — Die Mensch-Maschine-Schnittstelle

[← Zurück zum Index](../../INDEX.md)

---

## Was Desktop macht

Desktop ist die UI für den Menschen. Es zeigt was Node und Conductor tun, bietet den Store-Browser, den Bot Manager, das Task-System, Widgets, Lenses und einen eingebetteten [Browser](../browser/README.md).

Desktop ist auch UI für die Services selbst — Web-Interfaces werden im eingebetteten Browser geöffnet.

## Sidebar-Tabs

| Tab | Funktion |
|---|---|
| 🏠 Home | Persönliches Dashboard, Widgets, Quick-Launch |
| 📋 Tasks | Automatisierungs-Pipelines |
| 🎛️ Conductor | Service-Konfiguration |
| 🤖 Bots | Bots BENUTZEN |
| 🔍 Lenses | Informations-Betrachter |
| 🌐 Browser | Eingebetteter Web-Browser für Service-UIs |
| 📦 Store | Pakete installieren |
| 🔎 Search | Suche über alle Services |
| 🔨 Builder | Resource Builder (Pakete bauen) |
| ⚙️ Settings | Themes, Shortcuts, Profil, Layout |
| ❓ Help | Dokumentation |

## Rendering-Modi

| Modus | Technologie |
|---|---|
| Desktop (WGUI) | Dioxus WebView |
| Web | Dioxus WASM |
| Mobile | Dioxus (Android/iOS — reiner Client) |

## UI-Objekt-System

Alle sichtbaren Elemente basieren auf dem [FsnObject-System](../../technik/ui-objekte.md).

## Eigenständigkeit

Desktop läuft auch offline. Für Live-Daten braucht es eine Verbindung zu einem Node.

## Plattformen

| OS | Status |
|---|---|
| Linux | ✅ (webkit2gtk) |
| macOS | ✅ (WKWebView) |
| Windows | ✅ (WebView2) |
| Android/iOS | ✅ Reiner Client (per Invite verbinden) |

## Repo

https://github.com/FreeSynergy/Desktop

## Bibliotheken

| Crate | Zweck |
|---|---|
| `dioxus` 0.7.x | UI-Framework (inkl. WebView für Browser) |
| `fsn-ui` | Komponenten-Bibliothek |
| `fsn-theme` | Theme-System |
| `fsn-i18n` | Sprach-Snippets |
| `fsn-db` | SQLite (fsn-desktop.db) |
| `fsn-store` | Store-Client |
| `reqwest` | Node-API aufrufen |

---

Weiter: [Browser](../browser/README.md) | [Lenses](../lenses/README.md) | [UI-Objekte](../../technik/ui-objekte.md)
