# Restream - Tastatur-Shortcuts

## Übersicht

Restream dokumentiert **keine offiziellen Shortcuts**. Das Dashboard und das Studio folgen den üblichen Web-Konventionen.

## Web-UI (Dashboard und Studio)

| Taste | Funktion |
|-------|----------|
| `Tab` / `Shift+Tab` | Formularfelder und Kacheln wechseln |
| `Enter` | Dialoge bestätigen, Verbinden/Trennen auslösen |
| `Esc` | Modals schließen (Kanal-Dialog, Event-Dialog) |
| `Strg+Enter` | Chat senden (Chat-Eingabefeld fokussiert) |
| `Strg+R` | Seite neu laden |

## Studio (nicht garantiert, verhaltensähnlich zu anderen Production-Tools)

| Taste | Beobachtetes Verhalten |
|-------|------------------------|
| `Space` | Mikrofon stummschalten, wenn das Studio den Fokus hat |
| `M` | Kamera/Mikrofon-Schnellsteuerung in manchen Studio-Versionen |

Diese beiden Zeilen sind **Beobachtungen, keine dokumentierten Zusagen** — vor einer Skin-Umsetzung im aktuellen Studio prüfen.

## Mac-Varianten

| Windows/Linux | Mac |
|---------------|-----|
| `Strg+Enter` | `Cmd+Enter` |
| `Strg+R` | `Cmd+R` |
| `Esc` | `Esc` |

## Zusammenfassung

- Kurz: **keine dokumentierten Shortcuts**; nur Standard-Web-Bedienung
- Für eine FreeSynergy-Skin-Umsetzung sind Tasten selbst zu definieren (z. B. „Go Live", „Stumm", „Szene wechseln") und dann hier zu dokumentieren
- Automatisierung läuft über die API (siehe `api.md`), nicht über Tasten
