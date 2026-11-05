# OBS Studio - API documentation

## Overview

The access path is **obs-websocket 5.x**: a built-in WebSocket server (standard port 4455)
with JSON messages. Additionally there is the command-line tool **OBS-Command** and the C
API **libobs** for plugins.

**API kinds at a glance**

| Kind | Use | Status |
|------|-----|--------|
| obs-websocket 5 (JSON/WebSocket) | scenes, sources, recording, streaming, audio | official |
| obs-cli / OBS-Command | scripting from outside | official/community |
| libobs (C plugin API) | your own sources/filters | official |
| obs-scripting (Python/Lua) | automation inside OBS | official |
| REST/HTTP | — | ❌ (only via wrappers) |

## Authentication

- Enable the server under *Settings → Extensions → WebSocket server* (port, password)
- Client handshake: `Hello` → `HelloResponse` with an `authentication` requirement, the answer with `password`/`authentication` (SHA256 of `password+secret`, Base64)
- Permission levels per connection (configuration, scenes, studio mode, recordings …)

## Core operations (selection)

| Operation | Description |
|-----------|-------------|
| `GetVersion` | the OBS and obs-websocket versions |
| `GetSceneList` / `SetCurrentProgramScene` | read scenes and switch them |
| `CreateScene` / `CleanUpSceneItem` | create/remove scenes |
| `GetSceneItemList` / `CreateSceneItem` | sources in scenes |
| `SetSceneItemEnabled` / `SetSceneItemTransform` | visibility and transformation |
| `StartStream` / `StopStream` | control streaming |
| `StartRecord` / `StopRecord` / `GetRecordStatus` | control recording |
| `StartVirtualCamera` / `StopVirtualCamera` | virtual camera |
| `SetInputMute` / `SetInputVolume` / `GetInputAudioTracks` | audio |
| `SetCurrentTransition` / `TriggerStudioModeTransition` | transitions |
| `GetMediaState` / `SetMediaCursor` | control media sources |
| `SaveProjector` … `BroadcastCustomMessage` | your own messages between clients |

## Example

Request (JSON over WebSocket):

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

## Events (input/output)

`InputStartedRecording`, `InputStopRecording`, `SceneCurrentSceneStarted`, `Exit`,
`MediaEnded` … — subscribable as an `EventSubscription`.

## Rate limits

No quotas; in practice limited by the encode load. Recommendation: event subscriptions
instead of polling, throttle the `Get*` calls.

## SDKs and client libraries

- **official**: the obs-websocket protocol specification, Python examples in the documentation
- **Community**: `obsws` (Python), `obs-websocket-js` (Node/browser), `obs-rs` (Rust), OBS-Command (CLI)
- **Plugins**: obs-multi-encoder, obs-browser, move-to (scene-switch history)

## Frontend note

Scene/source/output target correspond to the standard model
([models.md](../../../../../../data/models.md)); the hotkey fields follow
[fields.md](../../../../../../data/fields.md).
