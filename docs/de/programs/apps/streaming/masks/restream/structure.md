# Restream - Struktur & UI/UX

## Übersicht

Restream ist ein Web-Dashboard mit Studio-Ansicht. Diese Datei beschreibt das Layout, die Planstufen und die Einbettung — ohne Preise zu nennen (die ändern sich häufig).

## Fenster-Struktur

### Hauptbereiche

```
┌────────────────────────────── Restream Dashboard ───────────────────────────┐
│ Logo │ Konto/Plan │ Benachrichtigungen                                     │
├───────────────┬─────────────────────────────────────────────────────────────┤
│ Navigation    │ Content                                                    │
│               │                                                            │
│ Live          │ Status, Ingest-Daten (RTMP-URL + Key), Ziel-Status         │
│ Studio        │ Vorschaufenster, Szenenliste, Quellenliste, Steuerung      │
│ Channels      │ Kacheln je Plattform (verbunden/nicht), Custom-RTMP       │
│ Events        │ Kalender, Event-Detail (Pre-Roll, Aufnahme)                │
│ Chat          │ Eine Spalte je Plattform, Eingabezeile                     │
│ Analytics     │ Diagramme (Viewer, Watch-Time), Filter nach Event/Plattform│
│ Video         │ Bibliothek, Upload, Einbettlinks                          │
│ Settings      │ Account, Branding, Sicherheit, Billing, API                │
└───────────────┴─────────────────────────────────────────────────────────────┘
```

### Studio-Ansicht

- oben: Vorschaufenster mit Szenen/Layout-Auswahl
- links: Szenen- und Quellenlisten, Hinzufügen-Dialoge
- rechts: Chat-Overlay, Chat-Eingabe, Steuerung (Mikrofon, Kamera, Bildschirmfreigabe)
- unten: „Go Live", Aufnahme, Proben (Preview ohne Senden)

## UI/UX

### Design-Prinzipien

- **Aufgabenorientiert**: „Go Live" und Verbundene Ziele dominieren die Startseite
- **Wenig Konfiguration**: Plattformen werden per Login gekoppelt, nicht per Port/Protokoll
- **Alles im Browser**: Produktion, Moderation und Auswertung ohne lokale Tools

### Farbschema

- hell, blaue Akzente; Status grün (live/verbunden), grau (getrennt), rot (Fehler)
- Studio dunkel (Video-Vorschau)

### Interaktionen

- Drag & Drop für Quellen in Szenen
- Verbinden/Trennen von Zielen über Kachel-Buttons
- Chat-Tabs je Plattform, einheitliches Eingabefeld

### Planstufen (qualitativ)

| Stufe | typischer Umfang |
|-------|------------------|
| Free | Multistreaming mit wenigen Zielen, Branding des Anbieters |
| Premium | mehr Ziele, eigene Marke, längere Streaming-Zeit |
| Business/Team | Team-Zugänge, Analytik-Ausbau, weitere Kanäle |
| Enterprise | API-/Integrationsumfang nach Vereinbarung |

## Zugänglichkeit

- Standard-Web-Bedienung (Tab-Reihenfolge, Formularlabels), aber nicht als barrierefrei zertifiziert dokumentiert
- Studio lebt von Kamera/Mikrofon — Tastaturalternativen sind begrenzt
- Untertitel: nicht als Kernfunktion dokumentiert

## Performance

- Latenz hängt vom Anbieter und den Zielplattformen ab (WebRTC-/HLS-Varianter nicht frei wählbar)
- Studio-Bedarf: stabile Upstream-Bandbreite und ein aktueller Browser
- Analytics-Diagramme bei langen Events träge — Zeiträume filtern
