# Streaming — Requirements

What `FreeSynergy.Streaming` (`fs-streaming`) must and can do, derived from the
[frontends](frontends/index.md) (ADR 0006, 0013). Each capability names its data standard
(ADR 0014) and our status. The program receives, relays, packages, records and controls
live media streams. Calls are their own program, built on streaming (ADR 0037, point 6): this
page only names what a call program would reuse (WHIP/WHEP ingest and playback) and does not specify calls.

**Owners (ADR 0050).** `fs-streaming` owns the topic "live media" (WHIP, WHEP, enhanced RTMP; see the
[interface catalogue](../../../interfaces/index.md)). Recordings and videos are kept by [`fs-files`](../files/design.md);
events by `fs-calendar`; people and sign-in by `fs-people` and the [identity wrapper](../../platform/identity.md);
chats by `fs-messenger`. Those are reached through their interfaces and are not specified here.

Status: `implemented` · `planned` · `proposed`

**Stage marker** after the status — decided by what the capability does to the video:
`stage 1` = forwards media **without decoding** (ingest, relay, remux, recording to file, access control);
`stage 2` = needs **decoding or encoding** (transcoding, bitrate ladders, overlays, mixing). We are 100 % Rust
and have no mature pure-Rust H.264 encoder. Codecs are outsourced: each is a provider behind one codec interface, open
ones first (ADR 0048, [design](design.md#encoding)). Stage 2 waits for such a provider.

**Seen in** — analysed frontends: [Am](frontends/ant-media-server/index.md) Ant Media Server ·
[Ff](frontends/ffmpeg/index.md) FFmpeg · [Gs](frontends/gstreamer/index.md) GStreamer ·
[Mt](frontends/mediamtx/index.md) MediaMTX · [Ms](frontends/mistserver/index.md) MistServer ·
[Nr](frontends/nginx-rtmp-module/index.md) nginx-rtmp-module · [Ob](frontends/obs-studio/index.md) OBS Studio ·
[Rt](frontends/restream/index.md) Restream · [Rr](frontends/restreamer/index.md) Restreamer ·
[Wz](frontends/wowza/index.md) Wowza.
*arch.* = required by our architecture or principles, not by counting.
⚠️ = to verify: not (or not clearly) in the feature file, or no evidence in `data/`.

**Rule:** a capability is *Required* when at least five of the ten frontends show it, or when
our architecture needs it. The capability id in backticks (`<object>.<action>`) is a proposal —
a capability is an action on the object, never a menu item or a gesture. Function analysis only,
own wording (ADR 0013).

**Standards:** `docs/en/data/` has no streaming domain yet. Verified: **WHIP = RFC 9725**, JSCalendar RFC 8984
([events](../../../data/events/standards.md)), the [data API](../../../data/api.md) (REST/JSON, bearer or OAuth2).
Every other protocol below (RTMP, SRT, RTSP, HLS, DASH, WHEP, MoQ, TLS variants, CMAF) is named
only as in the feature files: ⚠️ standard and number to verify before they go into a spec.

## Required (common to the analysed programs)

| Capability | Seen in | Data / standard | Status |
|------------|---------|-----------------|--------|
| Accept a published stream over RTMP (`stream.publish`) | Am, Mt, Ms, Nr, Rr, Rt, Wz (Ff, Gs, Ob as senders) | RTMP ⚠️ | proposed · stage 1 |
| Accept a published stream over SRT (`stream.publish`) | Am, Mt, Ms, Rt, Wz; Rr (⚠️ "new versions"); Ff, Gs, Ob as senders | SRT ⚠️ | proposed · stage 1 |
| Accept a stream from an IP camera over RTSP (`stream.publish`) | Am, Mt, Ms, Rr, Wz; Ff, Gs as clients | RTSP ⚠️ | proposed · stage 1 |
| Accept a browser/WebRTC publisher over WHIP (`stream.publish`) | Am, Mt, Ms; Gs (WHIP-like by hand); *arch.* (calls reuse it, ADR 0037) | WHIP RFC 9725 ✅ | proposed · stage 1 |
| Play a stream in the browser over HLS (`stream.play`) | Am, Ff, Gs, Mt, Ms, Nr, Rr, Wz | HLS ⚠️ | proposed · stage 1 |
| Play a stream over MPEG-DASH (`stream.play`) | Am, Ff, Gs, Ms, Nr, Wz | DASH ⚠️ | proposed · stage 1 |
| Play a stream with low delay over WebRTC/WHEP (`stream.play`) | Am, Mt, Ms, Gs; Rr (optional), Wz (⚠️ by version); *arch.* (calls) | WHEP ⚠️ (number not verified) | proposed · stage 1 |
| Convert between protocols and containers without re-encoding (`stream.remux`) | Mt, Ms, Nr, Ff (`-c copy`), Am; *arch.* (core of stage 1) | RTMP/RTSP/SRT in → HLS/DASH/WebRTC out ⚠️ | proposed · stage 1 |
| Pull a stream from an external source and serve it (`source.pull`) | Am, Mt, Ms, Nr, Wz, Ff, Gs | RTSP/RTMP/HLS pull ⚠️; on-demand start of sources | proposed · stage 1 |
| Forward one stream to several external targets (`restream.add`) | Am, Rt, Rr, Wz, Ms, Ob (via plugin) | RTMP(S) targets ⚠️; target = URL + key | proposed · stage 1 |
| Authorise publishers: stream key, password, IP list, hook decision (`publisher.authorize`) | Am, Mt, Ms, Nr, Rr, Wz | key/token per stream; checked through the [identity wrapper](../../platform/identity.md) ([identity data](../../../data/identity/index.md)) | proposed · stage 1 |
| Authorise viewers: time-limited token or login, per stream (`viewer.authorize`) | Am, Mt, Nr, Wz; *arch.* (private streams, FS identity) | signed token (JWT ⚠️); bearer/OAuth2 as in [api](../../../data/api.md) | proposed · stage 1 |
| Encrypt transport on every endpoint (`endpoint.secure`) | Am, Mt, Ob, Rr, Wz; *arch.* (privacy) | TLS for RTMPS / RTSPS / HTTPS ⚠️ | proposed · stage 1 |
| Record a stream to a file (`recording.start`) | Am, Ff, Mt, Ms, Nr, Ob, Rr, Rt, Wz | MP4 / fMP4 / MKV / MPEG-TS ⚠️; segment length configurable | proposed · stage 1 |
| List and play recordings on demand (`recording.list`, `recording.play`) | Am, Mt, Nr, Rr, Rt | the recording lands in `fs-files` and is listed through its interface; a live stream is not a file and stays here | proposed · stage 1 |
| Call a hook on stream events: publish, unpublish, play, record done (`hook.send`) | Am, Mt, Nr, Rr, Wz | HTTP webhook; payload as AS2-style activity = own proposal ⚠️ | proposed · stage 1 |
| Control streams through an API: list, create, kick, read config (`stream.list`, `stream.create`, `stream.delete`) | Am, Mt, Ms, Rr, Rt, Ob (WebSocket), Wz | REST/JSON per [data API](../../../data/api.md); every UI path uses it | proposed · stage 1 |
| Read statistics: viewers, bitrate, health; export metrics (`stats.read`) | Am, Mt, Ms, Nr, Rr, Rt | JSON via API; metrics format (Prometheus ⚠️); logs as JSON lines | proposed · stage 1 |
| Transcode a stream to another codec, size or bitrate (`stream.transcode`) | Ff, Gs, Am, Wz, Rr, Nr (via ffmpeg `exec`) | H.264/AAC/Opus/AV1 ⚠️; hardware encoders optional | proposed · stage 2 |

## Optional (notable ideas)

| Capability | Seen in | Data / standard | Status |
|------------|---------|-----------------|--------|
| Build an adaptive-bitrate ladder with a master playlist (`rendition.create`) | Am (enterprise), Wz; not in Mt, Ms, Nr, Rr, Gs | HLS/DASH master ⚠️ | proposed · stage 2 |
| Watermark or overlay text/images on a stream (`stream.overlay`) | Wz, Ff, Gs; Ob, Rt (scenes) | none; per-stream overlay profile = own | proposed · stage 2 |
| Compose scenes from several sources, switch live (`scene.compose`) | Ob, Rt (Studio), Gs, Ff (filter graph) | scene = own object; kept in `fs-store` | proposed · stage 2 |
| Mix audio tracks, normalise loudness (`audio.mix`) | Ob, Ff, Gs, Rt | EBU R128 named by Ff ⚠️ | proposed · stage 2 |
| Pick a hardware or software encoder (`encoder.select`) | Ff, Gs, Am, Ob | a codec provider behind the codec interface (ADR 0048); NVENC / QSV / VAAPI ⚠️ | proposed · stage 2 |
| Grab a preview picture of a live stream (`stream.preview`) | Am, Rr | decodes one frame; image `mediaType` | proposed · stage 2 |
| Keep a rolling buffer for time shift / jump back (`stream.timeshift`) | Ms (DVR), Wz (nDVR), Ob (replay buffer) | buffer length per stream | proposed · stage 1 |
| Play a list of files or streams in sequence (`playlist.create`) | Am, Rt | AS2 `OrderedCollection`; ⚠️ codecs must match, else stage 2 | proposed · stage 1 |
| Plan a broadcast with a start time and a public page (`broadcast.schedule`) | Rt | the event is made through the `fs-calendar` interface, which owns `Event` (JSCalendar RFC 8984 ✅, [events](../../../data/events/standards.md)) | proposed · stage 1 |
| Link instances as origin and edge (`relay.link`) | Am, Mt, Nr, Wz | publish/pull between nodes; node sync via `fs-hub` (ADR 0019) | proposed · stage 1 |
| Low-latency HLS / chunked CMAF delivery (`stream.play`) | Mt, Wz | LL-HLS, CMAF ⚠️ | proposed · stage 1 |
| Deliver over MoQ (`stream.play`) | Mt | Media over QUIC ⚠️ (young, check status) | proposed · stage 1 |
| Play a plain file over HTTP (`stream.play`) | Ms, Wz | HTTP progressive MP4/WebM ⚠️ | proposed · stage 1 |
| Import a video file as on-demand content (`media.import`) | Am, Rt, Wz | video management belongs to `fs-files`; streaming only takes a file from its interface (AS2 `Document`/`Video`) | proposed · stage 1 |
| Analyse a media file or stream: codecs, tracks, duration (`media.probe`) | Ff (ffprobe), Gs (discoverer) | JSON output | proposed · stage 1 |
| Delete recordings after an age (`recording.expire`) | Mt | retention in days | proposed · stage 1 |
| Disconnect or block a single publisher at runtime (`publisher.disconnect`) | Mt, Nr, Wz | part of the control API | proposed · stage 1 |
| Connect a platform account and publish there (`target.connect`) | Rt (30+ platforms); Wz and Ob explicitly lack it | a publishing-target provider behind its own interface; platform OAuth ⚠️; fallback is URL + key | proposed · stage 1 |
| Show platform chats in one view (`chat.aggregate`) | Rt | owned by `fs-messenger`; streaming only links to its interface | proposed · stage 1 |
| Embed a player on other pages (`player.embed`) | Rr, Rt, Am (test player) | HLS/WebRTC player as a reusable component (ADR 0037) | proposed · stage 1 |

## From the design (not from the frontends)

| Capability | Basis | Data / standard | Status |
|------------|-------|-----------------|--------|
| Check before going live that connection, keys and formats of all targets will work (`target.check`) | [design](design.md#simple-means-automatic) | none | proposed |
| Publish a video not live, through each platform's interface (`video.publish`) | [design](design.md#three-parts); the video comes from `fs-files` | publishing-target provider | proposed |

## Not planned (deliberately)

| Feature | Seen in | Why not |
|---------|---------|---------|
| DRM (Widevine, FairPlay, PlayReady) | Wz (add-on) | licence-bound, closed; tokens and encryption on the transport are enough |
| Smooth Streaming output | Wz | vendor format, no gain over HLS/DASH |
| Video editing, timeline, post-production | Ff (cuts by flags), Gs (GES), Ob (no) | other programs; streaming only records |
| Capturing screen or camera, virtual camera | Ob, Ff, Gs | the publisher's job (OBS or a browser via WHIP), not the server's. ⚠️ Contradicts ADR 0049 (point 9: recording simpler than OBS) and [design](design.md) stage 3 (screen and camera); left as is, to be settled |
| Server-side ad insertion | Am (no) | ADR 0016: no ads |
| Plans that limit targets or streaming time | Rt | free forever, no limits by payment (ADR 0016) |
| Own CDN, billing, multi-tenant resale | Wz (no CDN), Rt | not a hosting product; edges via `relay.link` |
| Java/XML plug-in modules for custom logic | Wz | extension through hooks and capabilities instead |
| Multi-party calls and guest panels | Rt (guests via link) | their own program, built on streaming (ADR 0037, point 6) |

## Notes on the sources

- ⚠️ Restreamer file: lists SRT/RTSP input "in new versions" while naming nginx-rtmp-module as its receiver, which has no SRT; treat SRT there as unverified.
- ⚠️ Wowza file marks WebRTC itself as uncertain; GStreamer's "WHIP-like" means no ready WHIP element.
- ⚠️ Restream is a SaaS reference only; its features cannot be checked against a self-hosted setup.
- ⚠️ Ant Media: ABR, JWT, DASH, playlists and restreaming are enterprise-only; counted as seen.
- MediaMTX says "no token URLs for HLS" but supports JWT auth; counted for `viewer.authorize` as auth, not as URL tokens.
- Stage 2 is only a classification today; no encoder decision is made here.
