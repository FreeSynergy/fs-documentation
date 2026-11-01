# OBS Studio - API Dokumentation

## Übersicht

Der Zugangsweg ist **obs-websocket 5.x**: ein eingebauter WebSocket-Server (Standard-Port 4455) mit JSON-Nachrichten. Zusätzlich existiert das Kommandozeilenwerkzeug **OBS-Command** und die C-API **libobs** für Plugins.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| obs-websocket 5 (JSON/WebSocket) | Szenen, Quellen, Aufnahme, Streaming, Audio | offiziell |
| obs-cli / OBS-Command | Scripting von außen | offiziell/Community |
| libobs (C-Plugin-API) | eigene Quellen/Filter | offiziell |
| obs-scripting (Python/Lua) | Automatisierung in OBS | offiziell |
| REST/HTTP | — | ❌ (nur über Wrapper) |

## Authentifizierung

- Server in *Einstellungen → Erweiterungen → WebSocket-Server* aktivieren (Port, Passwort)
- Client-Handshake: `Hello` → `HelloResponse` mit `authentication`-Anforderung, Antwort mit `password`/`authentication` (SHA256 aus `password+secret`, Base64)
- Berechtigungsstufen pro Verbindung (Konfiguration, Szenen, Studio-Modus, Aufnahmen …)

## Kernoperationen (Auswahl)

| Operation | Beschreibung |
|-----------|--------------|
| `GetVersion` | OBS- und obs-websocket-Version |
| `GetSceneList` / `SetCurrentProgramScene` | Szenen lesen und umschalten |
| `CreateScene` / `CleanUpSceneItem` | Szenen anlegen/entfernen |
| `GetSceneItemList` / `CreateSceneItem` | Quellen in Szenen |
| `SetSceneItemEnabled` / `SetSceneItemTransform` | Sichtbarkeit und Transformation |
| `StartStream` / `StopStream` | Streaming steuern |
| `StartRecord` / `StopRecord` / `GetRecordStatus` | Aufnahme steuern |
| `StartVirtualCamera` / `StopVirtualCamera` | virtuelle Kamera |
| `SetInputMute` / `SetInputVolume` / `GetInputAudioTracks` | Audio |
| `SetCurrentTransition` / `TriggerStudioModeTransition` | Übergänge |
| `GetMediaState` / `SetMediaCursor` | Medienquellen steuern |
| `SaveProjector` … `BroadcastCustomMessage` | eigene Nachrichten zwischen Clients |

## Beispiel

Request (JSON über WebSocket):

```json
{
  "op": 6,
  "d": {
    "requestType": "StartRecord",
    "requestId": "rec-1",
    "requestData": { "recordFileName": "talk-2026-10.mkv" }
  }
}
```

Response:

```json
{
  "op": 7,
  "d": {
    "requestType": "StartRecord",
    "requestId": "rec-1",
    "responseType": "RequestResponse",
    "responseData": { "success": true, "outputPath": "/videos/talk-2026-10.mkv" }
  }
}
```

## Ereignisse (Input/Output)

`InputStartedRecording`, `InputStopRecording`, `SceneCurrentSceneStarted`, `Exit`, `MediaEnded` … — als `EventSubscription` abonnierbar.

## Rate Limits

Keine Kontingente; praktisch begrenzt durch Encode-Last. Empfehlung: Ereignis-Abos statt Polling, `Get*`-Aufrufe drosseln.

## SDKs und Client-Bibliotheken

- **offiziell**: obs-websocket-Protokollspezifikation, Python-Beispiele in der Doku
- **Community**: `obsws` (Python), `obs-websocket-js` (Node/Browser), `obs-rs` (Rust), OBS-Command (CLI)
- **Plugins**: obs-multi-encoder, obs-browser, move-to (Szenenwechsel-Historie)

## Skin-Hinweis

Szene/Quelle/Ausgangsziel entsprechen dem Standardmodell ([modelle.md](../../../../data/modelle.md)); Hotkey-Felder folgen [felder.md](../../../../data/felder.md).
