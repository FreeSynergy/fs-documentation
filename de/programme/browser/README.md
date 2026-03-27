# Browser — Der eingebettete Web-Browser

[← Zurück zum Index](../../INDEX.md) | [Desktop](../desktop/README.md) | [Lenses](../lenses/README.md)

---

## Was der Browser macht

Der Browser ist eine eigenständige App die Web-Seiten anzeigt — als Standalone-Fenster oder eingebettet in den Desktop-Shell.

## Warum ein eigener Browser?

1. **Service-UIs anzeigen** — Kanidm, Forgejo, Outline haben Web-Interfaces. Statt den System-Browser zu öffnen, zeigt der FreeSynergy-Browser sie direkt im Desktop an.
2. **Integration** — Links aus Lenses, Search, Widgets öffnen im Browser statt extern.
3. **Downloads** — Dateien aus Service-UIs herunterladen, direkt in den S3-Storage.

## Technisch

- Dioxus WebView (webkit2gtk/WebView2/WKWebView) — keine separate Browser-Engine
- Tabs für mehrere Seiten gleichzeitig
- Lesezeichen (`BookmarkManager`, SQLite)
- Verlauf (`HistoryManager`, SQLite)
- Suchmaschinen-Registry (`SearchEngineRegistry`) — konfigurierbar, Fallback auf Brave

## Module

| Modul | Zweck |
|---|---|
| `app.rs` | Root-Komponente (`BrowserApp`), URL-Leiste, Tabs |
| `model.rs` | `BrowserTab`, `BrowserConfig` — Domain-Modell |
| `bookmarks.rs` | `BookmarkManager` — CRUD, Serialisierung |
| `history.rs` | `HistoryManager` — chronologischer Verlauf |
| `search_engine.rs` | `SearchEngineRegistry` — URL-Builder je Engine |

## Interfaces

| Interface | Funktion |
|---|---|
| URL-Leiste | Direkte URL-Eingabe |
| Tabs | Mehrere Seiten gleichzeitig |
| Service-Links | Klick auf Service im Container Manager → öffnet dessen Web-UI |
| Lens-Links | Klick auf Ergebnis in Lens → öffnet im Browser |

## Einschränkungen

- Kein vollständiger Browser (kein Erweiterungs-System, kein DevTools)
- Gedacht für Service-UIs und interne Seiten
- Für normales Surfen: System-Browser empfohlen

## Repo

`git@github.com:FreeSynergy/fs-browser.git`

---

Weiter: [Desktop](../desktop/README.md) | [Lenses](../lenses/README.md)
