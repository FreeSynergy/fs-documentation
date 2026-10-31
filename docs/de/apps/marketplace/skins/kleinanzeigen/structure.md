# Kleinanzeigen - Struktur und UI/UX

## App/Web-Layout

```
┌──────────────────────────────────────────────────────────────┐
│ 🔍 Suche…            [+ Anzeige]            [Chat][Meins]    │
├──────────────────────────────────────────────────────────────┘
│ Kategorien-Kacheln · Umkreis-Slider (Umkreis-Karte)          │
│ Anzeigenliste: Bild · Titel · Preis · Ort+Entfernung · Datum │
│ Detail: Galerie, Beschreibung, „Nachricht schreiben“,        │
│         Standort-Cluster auf Karte, Anbieterprofil, Sicherheit│
│ Chat: Blasen mit Systemhinweisen (Sicher bezahlen / Betrug)  │
└──────────────────────────────────────────────────────────────┘
```

## UI/UX

- App-Prägung (Mobile-first), Große Buttons für Anzeige/Chat
- Sicherheits-Banner im Chat (Enkeltrick-Betrugsschutz-Kampagnen)

## Interaktionen

- Anzeigen-Erstellung als mehrstufiger Assistent (Kategorie→Foto→Text→Preis/Ort)
- Such-Alarme als Erlaubnis-Dialog (Push)

## Responsive Design

- Web responsiv; App Hauptzugang

## Accessibility

- Standard-App-Komponenten; Alternativtext bei Fotos optional (Empfehlung)

## Performance

- Listen virtualisiert; Karten-Kacheln clustern
