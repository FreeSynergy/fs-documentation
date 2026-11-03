# GLPI - Struktur und UI/UX

## Seitenstruktur

```
┌─────────────────────────────────────────────────────────────────┐
│ Assistance | Assets | Verwaltung | Werkzeuge | Konfiguration    │
├───────────────┬─────────────────────────────────────────────────┤
│ Kontextbaum   │ Objektmaske: Ticket #9981 „VPN fällt aus“       │
│ Kategorien    │ ┌ Reiter ─────────────────────────────────────┐ │
│ ▸ Netzwerk    │ │ Eigenschaften | Verknüpfungen | Aufgaben    │ │
│ ▸ Server      │ │ Follow-ups | Pläne | Statistiken            │ │
│               │ ├─────────────────────────────────────────────┤ │
│               │ │ Status: angenommen  SLA: 6h (fällig 14:00) │ │
│               │ │ Asset: srv-03 · Vertrag: Wartung 2026       │ │
│               │ │ [Nachverfolgung hinzufügen] [Mass actions]  │ │
└───────────────┴─────────────────────────────────────────────────┘
```

- Links je Bereich Hierarchie-/Filterbäume, rechts Reitermasken mit Tabellen
- „Mass actions“-Leiste unter Tabellen (Zuweisen, Löschen, Ändern)

## UI/UX

- gedrungene Tabellendichte, viele Felder pro Maske; Grundthema + Dark-Mode (neuere Versionen)
- Masken folgen dem Muster: Obereiste Kopfdaten → Reiter → Aktionsleiste

## Interaktionen

- **Kein Drag & Drop**; Formulare, Popover-Picker für Benutzer/Assets
- **Live**: ❌ (Seiten-Reload); Planung/Cron-immanent
- Knowledge-Base-Artikel mit Markdown-Editor

## Responsive Design

| Bereich | Verhalten |
|---------|-----------|
| Self-Service-Portal | responsive (Haupt-Use-Case mobil) |
| Agenten-/Adminmasken | Desktop-optimiert, auf Mobil scrollbar |

## Accessibility

- HTML-Tabellen mit Beschriftungen; viele Felder hintereinander — Screenreader-Langstrecken
- Tastaturtabellen ok; Farbcodes (SLA-Fälligkeit rot) zusätzlich als Text

## Performance

- große Inventare (100k+ Assets) verlangen saubere Indizes/PHP-Timeouts; Reports per Cron-Vorlage generieren
