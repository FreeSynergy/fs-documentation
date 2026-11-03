# Restream - Menüpunkte

## Übersicht

Restream wird über das Web-Dashboard (`restream.io` → Login) bedient. Die Navigation ist seitlich angeordnet; Reichweite und Details hängen vom Abo-Plan ab.

## Hauptmenüpunkte

### 1. Live / Dashboard

- **Funktion**: zentrale Streaming-Ansicht
- **Details**:
  - „Go Live" / Stream-Status
  - Ingest-Daten (RTMP-URL und Stream-Key für OBS/ffmpeg)
  - aktive Zielplattformen mit Status

### 2. Studio

- **Funktion**: Browser-Produktion ohne lokale Encoder
- **Details**:
  - Szenen und Quellen (Kamera, Bildschirmfreigabe, Medien, Browser-Quelle)
  - Overlays, Backdrops, Text, Layouts
  - Gäste per Link einladen (Interview-Modus)

### 3. Channels / Destinations

- **Funktion**: Zielplattformen verbinden
- **Details**:
  - Plattformen per Login koppeln (YouTube, Twitch, Facebook, LinkedIn, …)
  - Custom-RTMP-Ziele mit Ziel-URL und Key
  - Anzahl verfügbarer Ziele je nach Plan

### 4. Events

- **Funktion**: geplante Streams verwalten
- **Details**: Zeitplan, Pre-Roll/Countdown, Aufzeichnung nach Stream, Erinnerungsteilen

### 5. Chat

- **Funktion**: einheitlicher Chat über alle verbundenen Plattformen
- **Details**: Moderation, gefilterte Wörter, Antworten aus einer Ansicht

### 6. Analytics

- **Funktion**: Zuschauer- und Interaktionszahlen
- **Details**: Viewer über Zeit, Watch-Time, pro Plattform, Export/Reports (Plan-abhängig)

### 7. Video / Bibliothek

- Upload und Verwaltung von VOD-Material, Einbettlinks, Wiedergabelisten

### 8. Settings / Account

| Bereich | Inhalt |
|---------|--------|
| Account | E-Mail, Passwort, 2FA |
| Branding | Logo, Wasserzeichen, Player-Design |
| Sicherheit | Stream-Key zurücksetzen |
| Billing / Pläne | Tarif, Rechnungen |
| API | API-Zugang/Token (Plan-abhängig) |

## Kontext-Menüs

| Objekt | Aktionen |
|--------|----------|
| Kanal/Ziel | verbinden, trennen, umbenennen, Chat dieses Kanals öffnen |
| Szene/Quelle | duplizieren, sperren, anordnen, entfernen |
| Event | bearbeiten, duplizieren, löschen, teilen |

## Menüs nach Benutzerrolle

| Rolle | Zugriff |
|-------|---------|
| Kontoinhaber | alles inkl. Billing und API |
| Team-/Redaktionsmitglied (Team-Pläne) | Studio, Chat, Events je nach Berechtigung |
| Zuschauer | nur eingebetteter Player, kein Dashboard |
