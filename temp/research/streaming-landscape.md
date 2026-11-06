# Streaming landscape: record once, distribute everywhere

Research note for `FreeSynergy.Streaming` (`fs-streaming`). Retrieval date of every source: **2026-11-06**.
Builds on [the existing streaming analysis](../../docs/en/programs/apps/streaming/index.md) (requirements, design, 10 frontends)
and does not repeat it. Function analysis only, own wording (ADR 0013). Codec and encoder standards are researched
separately: this note only records which codecs each platform accepts.

Conventions: ⚠️ = unverified or only from secondary / conflicting sources. "Fetch summary" means the page was read
through a summarising fetch tool, not word for word. Numbers from vendor blogs and review sites are always ⚠️.

What this is FOR, in one sentence: a person who made a video wants everyone, on every platform they care about, to see
it, without handing the stream to a company, without learning what a keyframe is.

---

## 1. Open source projects that already do this

### 1.1 Comparison table

Activity and licence are from the GitHub API on 2026-11-06 (field `pushed_at`, latest release tag). "Active" means
a push in the last few weeks unless noted.

| Project | Purpose (for people) | Self-hosted? | Licence | Language | Active? |
|---|---|---|---|---|---|
| **OBS Studio** | Capture screen, camera and sound, mix them and send or record. The tool most streamers start from | No server; desktop app on your own machine | GPL-2.0 | C / C++ | Yes. Release 33.0.1 on 2026-10-29 |
| **obs-multi-rtmp** (plugin by sorayuki) | Make one OBS send to several RTMP targets at once | Plugin, runs inside OBS | GPL-2.0 | C++ | Yes. 0.7.4.5 on 2026-10-25 |
| **datarhei Restreamer** | A ready-made box: receive a stream, show it on your own web page, forward it to platforms, record | Yes (Docker) | Apache-2.0 | Go backend + React UI | Repo pushed 2026-05-22; ⚠️ the engine repo `datarhei/core` has pushes in 2026-10 but its latest *release* is v16.16.0 from 2024-06 |
| **MediaMTX** | Protocol router: whatever comes in (RTMP, SRT, WebRTC, RTSP) can go out in another form; can forward to other servers | Yes, single binary | MIT | Go | Very. v1.21.3 on 2026-10-25 |
| **Owncast** | Your own small "Twitch": one streamer, a web page, a chat | Yes | MIT | Go + React | Yes. v0.3.0 on 2026-09-03 |
| **PeerTube** | Your own "YouTube": videos, live, federation between servers | Yes | AGPL-3.0 | TypeScript | Very. v8.3.2 on 2026-10-26 |
| **SRS** | High-performance live media server | Yes | MIT | C++ | Yes. v6.0-r3 on 2026-10-31 |
| **Oryx** (formerly SRS Stack) | SRS plus a web UI: authentication, "stream to multiple platforms", recording, transcoding, "virtual live" (play a file as if live) | Yes (one Docker container) | MIT | Go + React (+ SRS, FFmpeg) | Yes. v7.15.26 on 2026-09-14 |
| **LiveKit** | Real-time rooms (calls, interactive streams) with an SDK. *Egress* sends a room or track to RTMP targets or to files | Yes (egress is a separate service) | Apache-2.0 | Go | Very. v1.13.11 on 2026-10-25 |
| **nginx-rtmp-module** | RTMP intake inside nginx; can push on to other RTMP servers | Yes | BSD-2-Clause | C | ⚠️ Low. Last push 2024-12-24 |
| **OvenMediaEngine** | Sub-second live streaming server with transcoding | Yes | AGPL-3.0 | C++ | Yes. v0.21.0 on 2026-08-13 |
| **MistServer** | Lightweight media server | Yes | Unlicense | C / C++ | Yes. 3.13 on 2026-11-03 |
| **Broadcast Box** | Very simple WebRTC (WHIP in, WHEP out) broadcast to friends | Yes | MIT | Go + React | Yes. Push 2026-11-03 |
| **Jibri** (Jitsi) | Records or streams a Jitsi Meet call to RTMP | Yes | Apache-2.0 | Kotlin | Yes. Push 2026-10-27 |
| **Streamlink** | Opposite direction: *watch/pull* live streams from platforms into a player | Local tool | BSD-2-Clause | Python | Yes |
| **MoQ (moq-dev/moq)** | Media over QUIC: next-generation low-delay delivery, Rust | Library/relay | Apache-2.0 (⚠️ the repo shows one licence; sub-crates not checked) | Rust | Very. Push 2026-11-06 |

Not verified by API this session (rate limit hit), so licence/activity are ⚠️: VDO.Ninja (peer-to-peer browser
production, ⚠️ AGPL), Ant Media Server (community edition; the API reports "NOASSERTION" licence, features such as
ABR and restreaming are enterprise-only per the existing analysis), the small hobby multistreamers below.

### 1.2 Per project: what is simple, what is hard

**OBS Studio.** *Simple:* it is free, runs everywhere, any platform accepts its output, a huge community. *Hard:*
see section 3. It has no concept of "send to several platforms"; that needs the plugin below or an outside relay.

**obs-multi-rtmp.** *Simple:* one extra dock, add targets, press start. It can reuse OBS's main encoder (cheap in CPU)
or start separate encoders per target with their own bitrate. *Hard:* it is a third-party plugin, not part of
OBS, so every OBS update is a risk. Forum and AUR comments report breakage with specific OBS versions (30.1.2, 30.2.2),
and the minimum OBS version has changed. Still, the upload bandwidth multiplies by the number of targets because the
copies leave your machine. Source: OBS resource page, AUR listing (see source list).

**Restreamer.** *Simple:* Docker, a web UI, a built-in player, publishing to YouTube and others with a few forms; the
README promises a "free alternative" to paid restreaming. *Hard:* needs your own server with enough bandwidth;
each target is an FFmpeg job underneath; the engine's release cadence looks slow (⚠️ see table). The existing analysis
already covers its menus.

**MediaMTX.** *Simple:* one binary, one YAML file. Its `forward` block pushes an incoming stream to RTMP(S), SRT, RTSP,
WHIP and MoQ destinations, and an RTMP destination looks like `rtmps://host/path#streamKey`. *Hard:* it is a
config file, not an app: no accounts, no scheduling, no platform knowledge. It documents one platform trap
itself: YouTube silently rejects streams without an audio track. For anything that changes the picture it hands you
to FFmpeg (`runOnAvailable`).

**Owncast.** *Simple:* the whole README sells "a single service that works out of the box": a streamer plus viewers
plus chat. Works with OBS, Streamlabs, Restream. *Hard:* by design a single-user service, and it is a destination, not a
distributor. ⚠️ I could not verify whether it has a built-in multi-target push (the FAQ URL returned 404).

**PeerTube.** *Simple:* upload or go live from the web UI; nice choice of privacy (public, internal, unlisted, private,
password, scheduled); live in "normal" mode (replay replaces the live) or "permanent" mode (each replay becomes its
own video); import from URL. *Hard:* administrator must enable live; live transcoding runs one FFmpeg per live and "uses
significant CPU and RAM" (docs). It is a platform, not a distributor to other platforms.

**SRS / Oryx.** *Simple (Oryx):* one `docker run`, then a browser UI; the README lists streaming to multiple
platforms, recording, "virtual live events" and automatic HTTPS. *Hard:* SRS alone is a configuration-file server for
people who know media; Oryx's UI is in the same engineering mind-set. ⚠️ Whether Oryx's multi-platform feature re-encodes
or only forwards was not verified.

**LiveKit.** *Simple:* if you already use it for calls, egress to YouTube/Twitch/Facebook is one API request; it can
export a single track without transcoding (`PASSTHROUGH` preset for video tracks). *Hard:* room composite needs a
headless Chrome and GStreamer, i.e. heavy; self-hosting means deploying egress separately; no concept of a "broadcast
manager".

**nginx-rtmp-module.** Well-known recipe (accept, `push` to several RTMP URLs, optionally `exec` FFmpeg). *Simple* when it
works; *hard* because everything is hand-written config and the module itself is barely maintained.

**OvenMediaEngine / MistServer.** Media servers with strong low-latency delivery; both are server-room tools. Not aimed at
the "one person with a webcam" case. ⚠️ Feature list not re-verified this session beyond licence/activity.

**Broadcast Box.** The simplest thing in the list conceptually (WHIP in, WHEP out, optional reserved stream keys,
webhooks, admin portal), but only a watching page: no fan-out to other platforms. Setting up WebRTC networking (UDP
ports, NAT, STUN) is its own hurdle (fetch summary of the README).

**Hobby multistreamers (all ⚠️).** Search turned up several small projects: neustream (live as neustream.app; stack
reportedly MediaMTX + FFmpeg with one FFmpeg process per target; no public repo confirmed), xplex (self-hosted,
open source multistream server), MorrowShore Prism (GPL-3.0 per an index listing), a Rust/GStreamer studio with
browser switcher (Show HN listing, no repo link found). They show that people keep re-inventing "Restream at home",
which is itself a finding for section 6. None was verified by reading code.

### 1.3 SaaS tools for comparison

| Tool | What it is | Notable limits | Confidence |
|---|---|---|---|
| **Restream** | Cloud relay + browser studio + chat aggregation | Free: ⚠️ 2 destinations, ⚠️ 720p, ⚠️ branding; Odysee custom RTMP needs a paid plan (Odysee's own help page says so). ⚠️ One review says that when you send from your own encoder, resolution is kept up to 4K | Prices/limits ⚠️ (review sites) |
| **StreamYard** | Browser studio (guests, overlays) + multistream | ⚠️ paid plans cap destinations (3 / 8 / 10 depending on tier); ⚠️ free plan cannot multistream; Odysee via StreamYard needs the paid version (Odysee help) | ⚠️ |
| **Prism Live Studio** (Naver) | Free desktop and mobile app with multistream and built-in chat | Official FAQ: up to 6 simultaneous channels; ⚠️ whether free tier gets all 6 is disputed | Partly official |

All three are SaaS: your stream passes through their servers and their account system. That is exactly what the owner wants
to avoid. They are the benchmark for *ease*: sign in with each platform, pick a title, press one button.

---

## 2. Platforms

Legend: "Ingest" = live input. "Upload API" = non-live. For platform codec acceptance only the facts below were
recorded; encoding standards themselves are researched elsewhere.

### 2.1 Summary table

| Platform | Live ingest and accepted codecs | Non-live upload API | Simulcast terms |
|---|---|---|---|
| **YouTube** | RTMP/RTMPS (H.264, H.265, AV1; AAC or MP3), also HLS (H.264 or HEVC, MPEG-TS, AAC, single audio track, closed GOP) and DASH. CBR; keyframe recommended 2 s, max 4 s; up to 60 fps | Yes: Data API `videos.insert`, resumable, 256 GB max, **100 uploads/day** default, scope `youtube.upload` | No restriction found in the encoder docs; ⚠️ YouTube Terms not read |
| **Twitch** | RTMP(S). H.264 CBR, keyframe 2 s. Enhanced Broadcasting (multi-track, multiple encodes) in the Twitch/OBS/NVIDIA programme; HEVC for higher resolution ⚠️; AV1 status unclear | ⚠️ Not a "post a video" platform; VODs come from past broadcasts. Helix API is for metadata, clips, ⚠️ not verified for uploads | Simulcast allowed, with conditions (see 2.2) |
| **Odysee** | RTMP, custom server + stream key per livestream from the "RTMP Setup" tab; replay is recorded; thumbnails 1280x720, up to 5 tags. ⚠️ Exact codec/bitrate values not found (help page points to "settings suggested by Odysee" without numbers) | ⚠️ No official upload API found. Web upload up to 4 GB (LBRY FAQ). Community uses LBRY SDK (`lbrynet`) with a wallet | ⚠️ Not researched |
| **PeerTube** | RTMP (port 1935) / RTMPS (1936) to the instance; per-live key; optional live transcoding (one FFmpeg per live). ⚠️ no stated codec requirement | Yes: REST API of each instance (OpenAPI); web upload, URL import, torrent import | Per instance. ⚠️ Instance rules differ |
| **Rumble** | RTMP, H.264 4.1 (30 fps) / 4.2 (60 fps), CBR, max 8,000 kbps, keyframe 2 s, 720p or 1080p, AAC 44.1 kHz 128 kbps. ⚠️ Third-party guides: access only for verified/paid accounts or more than 5 followers | ⚠️ No public upload API found. A "live stream API key" exists for reading live data | ⚠️ Not researched |
| **Kick** | ⚠️ Mostly third-party: RTMPS with personal URL + key, H.264, keyframe 2 s, cap about 8,000 kbps (guides disagree) | Public API at `api.kick.com/public/v1`: ⚠️ channel update (title, category, tags up to 10, scope `channel:write`) known only from a Rust client crate. ⚠️ No video upload | ⚠️ Not researched |
| **Facebook** | RTMPS, H.264 level 4.1 (1080p30) / 4.2 (1080p60), AAC-LC 44.1 or 48 kHz stereo (128 kbps preferred, max 256), 1080p30 at 3,000-6,000 kbps, 1080p60 at 4,500-9,000 kbps; keyframe 2 s (⚠️ third-party) | Live Video API (create live, schedule). Needs App Review, permissions `publish_video` / `pages_manage_posts` + `pages_read_engagement`; account at least 60 days old, page/profile at least 100 followers (since 2024-06-10); max 8 h; no settings change mid-stream | ⚠️ Not researched |
| **LinkedIn** | RTMP/RTMPS, H.264 + AAC 128 kbps 48 kHz, 720p recommended / 1080p max, 30 fps, keyframe 2 s, 3.5 Mbps recommended / 6 Mbps max. Baseline profile if processing fails (B-frames cause timestamp trouble). ⚠️ Third-party blogs: access gated to "eligible" broadcasters / preferred partner tools; scheduling required from 2026-06-22 | ⚠️ Not researched (Video API exists for partners ⚠️) | ⚠️ Not researched |
| **Vimeo** | RTMPS from external encoder. Plan limits: Professional 2 simultaneous streams / 5,000 kbps / 30 fps / 12 h; Studio 3 / 5,000 / 30; Enterprise 3+ / 9,000 kbps / 60 fps. Below 2,000 kbps may look pixelated | ⚠️ Vimeo API upload exists, documentation page would not load; quota not verified | Vimeo's own live can simulcast out; destinations may convert if they lack 30/60 fps |
| **X (Twitter)** | RTMP/RTMPS via Live Studio (successor to Media Studio Producer). Producer pages: H.264, AAC-LC 128 kbps, ⚠️ recommended 9 Mbps, keyframe 72/90/180 frames at 24/30/60 fps. ⚠️ Premium requirement not verified | ⚠️ Not researched | ⚠️ |
| **TikTok** | RTMP stream key from LIVE Producer. ⚠️ Vendor blogs: 18+, about 1,000 followers, TikTok publishes no official criteria | ⚠️ Not researched | ⚠️ |
| **Instagram** | ⚠️ Not researched (no RTMP source found) | ⚠️ | ⚠️ |
| **Dailymotion, Bilibili, others** | ⚠️ Not researched | ⚠️ | ⚠️ |

### 2.2 Notes per platform

**YouTube.** The encoder page says Live Control Room auto-detects resolution, frame rate and bitrate when you start,
so the user need not tell YouTube anything: it reads the stream. Bitrate table (H.264 minimum / recommended in Mbps):
1080p30 5 / 14, 1080p60 6 / 17, 720p30 3 / 8; AV1 and H.265 need less (1080p30: 4 / 10). RTMPS is recommended. HDR
requires H.265 and 10-bit. Quota (docs): a project gets 10,000 units/day for most endpoints, with `search.list` and
`videos.insert` in their own buckets of 100 calls/day; `liveBroadcasts.insert`, `bind`, `transition` cost 1 unit,
`thumbnails.set` costs 50. Notable current detail: the `videos.insert` reference says videos from unverified API
projects are **not** restricted to private (the older "unverified projects are locked private" rule is no longer in
this page). More quota requires an audit form. Live API: create a `liveBroadcast` and a `liveStream`, `bind` them,
`transition` through `testing` to `live`; the calls must come from the Google account that owns the channel.

**Twitch.** Broadcasting guidelines (via search snippet): presets 1080p60 6,000 kbps, 1080p30 4,500, 720p60 4,500,
720p30 3,000; keyframe 2 s; CBR; stay below 80 % of your upload speed. Enhanced Broadcasting (blog, 2024-01-08):
the OBS build creates several renditions on the user's GPU and configures OBS from the PC's power and bandwidth;
it uses the Enhanced RTMP multitrack extension. *Simulcast rules* (Terms of Service section 11, via search summaries
and a compliance tracker; the live ToS text could not be fetched, so ⚠️): you may stream elsewhere at the same time
unless you have an exclusivity agreement; your Twitch viewers must get an experience at least as good (including chat
engagement); you may not send your community to leave for the other service; you may not use third-party tools that merge
other platforms' activity (for example combined chat) into the Twitch stream. Enforcement of the combined-activity clause
is disputed in guides (⚠️ one says suspended, one says text still in force as of September 2026). Consequence for
FreeSynergy: a unified-chat *overlay burned into the video* would be risky; a separate chat view only for the streamer
is described as allowed for personal use (⚠️).

**Odysee.** Wants a custom RTMP server/key pair, per livestream, from the creator's page; supports reusing the key.
Restream and StreamYard integration is available only on their paid tiers (Odysee help). Programmatic upload is the weak
point: no official API found; the underlying protocol (LBRY) has an SDK, but a headless setup runs into wallet linking
(community post, ⚠️).

**PeerTube.** Each instance exposes the same REST API, so one adapter fits all instances, and the user supplies the
instance URL. Scheduled live dates exist from PeerTube 7.3. Replacing a video file exists from 6.0, if the admin enables it.

**Rumble, Kick.** Plain RTMP(S) and H.264, so they behave like Twitch. Rumble documents an 8,000 kbps ceiling.

**Facebook.** The most formal: App Review, permission scopes, age/followers thresholds. Meta also publishes an
"Automatic Encoder Configuration API" (page title found in search; ⚠️ content not read), which suggests the platform
can tell the sender what settings to use, a good pattern.

**LinkedIn.** The documented encoder settings are the *tightest* in this list (30 fps, 1080p max, 6 Mbps max), so they
decide the shared stream in section 4.

**Vimeo.** Plan-dependent limits (5,000 kbps / 30 fps) are the second tight constraint. Pay-to-play.

---

## 3. Why OBS feels hard, and what "simple" would mean

OBS is a production tool for people who want control. The pain points below are the places where control is demanded
although the user has no opinion.

| # | Pain point | Evidence | Could be automatic? |
|---|---|---|---|
| 1 | **Two output modes; hidden values.** Simple mode hides settings such as the keyframe interval. A user asking what Simple mode actually uses got no definitive answer on the OBS forum | OBS forum thread "What default settings are used for simple output mode?" | Yes: show the profile in plain words ("1080p, 30 images/s, 5 Mbit/s") |
| 2 | **Keyframe interval:** in Advanced it is seconds (0 = auto); in Simple you must enable custom x264 parameters and type `keyint` in *frames* | OBS forum "Keyframe frequency?"; Eklipse guide | Yes: derive from target platform list (2 s everywhere in section 2) |
| 3 | **Bitrate / resolution guesswork.** Each platform publishes a different table; user must read them | YouTube, Twitch, Facebook, LinkedIn pages (section 2) | Yes: compute one profile that every selected target accepts, check it against measured upload speed |
| 4 | **Audio sources.** Desktop audio, mic/aux, per-device capture and per-application capture are separate source types; adding the same device both globally and as a source gives an echo (OBS knowledge base) | OBS KB "Audio sources"; obs-versions.com Wayland guide (per-app audio is a separate PipeWire source) | Mostly: a "my voice / the computer's sound / both" choice, a loudness meter, auto-ducking; ⚠️ per-app capture depends on OS |
| 5 | **Scenes and sources mental model.** Everything is a source in a scene; to show "me + slides" the user composes layers | Existing analysis of OBS; ⚠️ no single citation, widely reported | Partly: preset layouts ("talk", "screen + face", "just camera"), switch with one click |
| 6 | **Linux / Wayland capture** often shows a black screen or crashes at the share dialogue | Manjaro forum, Arch BBS, OBS forum (PipeWire crash), NVIDIA forum | Not solvable in an app alone; a native portal-based capture helps |
| 7 | **No multi-destination.** Needs a third-party plugin that breaks across OBS versions | OBS resource page; AUR comments | Yes: built-in |
| 8 | **Platform login and metadata outside OBS.** User still opens each platform's dashboard to create the event, copy server and key, set title, category, thumbnail | Odysee, YouTube help pages (copy URL/key by hand) | Yes: with accounts connected via OAuth, create the event, fetch key, set metadata, press go live |
| 9 | **Encoder choice.** x264 vs NVENC vs QSV vs AMF vs VAAPI; wrong choice drops frames | OBS KB search result; Twitch/NVIDIA material | Yes: test-encode on start, pick hardware if present, fall back automatically |
| 10 | **No pre-flight.** Problems (no audio track on YouTube; wrong key; low upload) show only after going live | MediaMTX docs (YouTube silently rejects video-only) | Yes: a dry run |

Existing partial fixes worth reusing as ideas: OBS's own auto-configuration wizard (⚠️ exists, page not fetched);
YouTube's auto-detect of settings; Twitch Enhanced Broadcasting auto-configuring OBS from PC power and bandwidth;
Meta's Automatic Encoder Configuration API.

### What "simple" could mean (proposal, not fact)

1. **Intent presets instead of settings.** "I talk to a camera", "I show my screen and explain", "I play a game", "I replay a recorded video as a premiere". Each preset picks layout, frame rate, audio chain, bitrate.
2. **Targets, not encoders.** User ticks platforms; the program computes the encoder profile (section 4) and tells them in a sentence what it chose.
3. **Connection test before live.** Upload speed and stability test; lowers the profile if needed; warns when headroom is under about 20 % (Twitch recommends staying at or below 80 % of upload).
4. **Audio by default sane:** one meter, "voice louder than music" ducking, loudness normalisation (⚠️ target level to be decided, not researched).
5. **Safety net:** if one target fails, the others continue; auto-reconnect; a local recording always runs.
6. **Same on any device:** browser or app via WHIP so a phone or laptop without OBS can be a source.
7. **A "go live" page** showing every target's state (waiting, live, error) with the reason in plain words.

---

## 4. Simultaneous distribution without re-encoding

### 4.1 When one encoded stream serves all targets

From the figures in section 2, the intersection (everything accepts it) is:

| Parameter | Common ground | Source of limit |
|---|---|---|
| Protocol | RTMP/RTMPS over TCP | all except PeerTube-style WebRTC / HLS special cases |
| Video codec | **H.264** (everyone accepts it; only YouTube clearly takes HEVC/AV1 over RTMP, Twitch only in its enhanced programme) | YouTube, Twitch, Rumble, Facebook, LinkedIn pages |
| Audio | **AAC-LC**, stereo, 48 kHz (44.1 also accepted), 128 kbps | Facebook, LinkedIn, Rumble, YouTube |
| Rate control | CBR | YouTube, Twitch, Rumble |
| Keyframe | **2 s** with closed GOP | all that publish a value (YouTube allows up to 4 s) |
| Frame rate | **30 fps** | LinkedIn (30 fps), Vimeo (30 fps on Pro/Studio) |
| Resolution | **1080p** at most (LinkedIn max), Rumble allows only 720p or 1080p | LinkedIn, Rumble |
| Bitrate | Narrow window around **5-6 Mbps** for 1080p30: YouTube minimum 5, Vimeo cap 5 (Pro/Studio), LinkedIn cap 6, Facebook range 3-6; **3-4 Mbps** at 720p30 satisfies all | see section 2 |
| Profile | If LinkedIn trouble: **no B-frames / Baseline** | LinkedIn help |
| Audio track | Must exist | MediaMTX docs for YouTube |

So a single **1080p30, H.264, about 5 Mbps CBR, 2 s keyframes, AAC 128 kbps** stream satisfies the strictest
documented limits: this is the "lowest common denominator" profile. It is not optimal for any platform
(YouTube recommends 14 Mbps; HEVC/AV1 are unused), but it needs no per-target encoding.

### 4.2 When it does not work

- **Higher quality wanted on one platform.** 60 fps or more than 6 Mbps breaks LinkedIn (30 fps, 6 Mbps max) and Vimeo Pro/Studio (30 fps, 5 Mbps). The sender would then need a second encode for those targets or accept lower quality for all.
- **Newer codecs.** HEVC/AV1 only help YouTube (and Twitch's programme); every other platform gets H.264 anyway.
- **Vertical video (TikTok, Twitch dual format, Instagram/Shorts-style).** A different frame shape requires a different picture: needs a second composition, thus decoding/encoding (stage 2 in the existing design). ⚠️ Twitch dual-format details not read.
- **Per-platform differences that need transformation:** e.g. different resolution caps (Rumble 720/1080 only), a platform that requires an extra audio track, overlays that must differ per platform (Twitch's rule against merged chat overlays).
- **Protocol-level quirks:** YouTube drops video-only; X needs keyframe interval expressed per fps; Odysee/Kick values ⚠️.
- **Unexpected bandwidth.** Fan-out from the sender's machine multiplies upload by the number of targets (5 targets x 5 Mbps = 25 Mbps), so the fan-out must happen on a relay that has the bandwidth, with the sender uploading once.

### 4.3 How existing tools handle it

| Tool | Approach |
|---|---|
| obs-multi-rtmp | Per target, either *shares the main encoder* (one encode, copies fanned out from the client) or uses its own encoder with its own bitrate (more CPU, per-target quality) |
| Restreamer, nginx-rtmp-module | Relay on a server that re-publishes the stream to each target; per-target FFmpeg jobs. Copy mode is possible, re-encode optional (existing analysis) |
| MediaMTX | `forward` block copies the stream as is; for changes it calls FFmpeg through hooks |
| LiveKit Egress | Composes and encodes for a room; individual tracks can pass through without transcoding for video (`PASSTHROUGH`) |
| Twitch Enhanced Broadcasting | Opposite idea: the sender encodes *several* renditions on its GPU so the platform need not transcode |
| PeerTube | Optional server-side live transcoding: one FFmpeg per live (CPU heavy) |
| SaaS (Restream etc.) | ⚠️ Marketing says they take one stream and fan out; whether they transcode per destination was not found |

Practical design hint: **relay-first**. The user's device sends one stream to their own relay (WHIP, RTMP or SRT), and the
relay copies (stage 1, no decoding) to targets whose limits fit; for targets that do not fit, either lower the shared
profile or run a transcode branch only for those (stage 2). That mirrors the existing design's stage 1 / stage 2 split.

---

## 5. Video management

### 5.1 What these tools do

| Aspect | Findings |
|---|---|
| **Titles / descriptions per platform** | Each platform has its own fields. YouTube `videos.insert` sets title, description, tags, category, privacy, `publishAt`; Kick (via API, ⚠️) title/category/tags; Odysee max 5 tags, PeerTube max 5 tags. Limits differ, so one title does not fit everywhere |
| **Thumbnails** | PeerTube: PNG/JPG/JPEG/WebP, 8 MB max, 1280x720 recommended. Odysee: 1280x720. YouTube `thumbnails.set` costs 50 quota units. ⚠️ YouTube also requires a verified account for custom thumbnails (not checked) |
| **Chapters** | ⚠️ YouTube chapters are timestamps in the description (widely documented, not re-verified here). No chapter API found on other platforms. ⚠️ PeerTube chapters exist (feature knowledge, not verified this session) |
| **Scheduling** | YouTube: live API scheduling and `publishAt` for uploads. PeerTube: scheduled privacy and scheduled live date (7.3+). Facebook Live API supports scheduling (⚠️ details not read). LinkedIn: scheduling reportedly required (⚠️). Twitch: ⚠️ schedule API not researched |
| **Privacy states** | PeerTube: public, internal, unlisted, private, password, scheduled. YouTube: public, unlisted, private |
| **Replays / recordings** | PeerTube saves replays per live; Odysee records lives and lets you upload the replay; YouTube turns a `liveBroadcast` into a normal video with the same ID |
| **Import** | PeerTube imports from URL (youtube-dl-compatible sites), direct MP4 and torrent; Oryx has "virtual live" (play a file as a live stream) |
| **Cross-posting generically** | Social schedulers such as Postiz (AGPL-3.0, TypeScript, 41k stars, active) manage posts to many networks; ⚠️ not examined for video details |
| **Archiving** | yt-dlp (Unlicense, Python, very active) is the standard open tool to fetch videos from platforms; ⚠️ its use is bound by each platform's terms |

### 5.2 Where does the line go? (proposal)

| Belongs in the **files program** (`fs-files`) | Belongs in **streaming** (`fs-streaming`) |
|---|---|
| The video file itself, versions, original and exports | Live session: ingest, relay, fan-out, health |
| Thumbnails, subtitles, chapter list as files / sidecar data attached to the video | Per-target connection (account, key, status) |
| Titles, descriptions, tags **as the master copy** | Per-target *overrides* needed at the moment of publishing (title length, category, privacy) |
| Recording from a live session (arrives as a normal file object) | Start recording; hand the result to files |
| Catalog, search, retention | Scheduling a broadcast (JSCalendar event, as the design says) |
| Edits (cut, trim) via other programs | Nothing about editing |

Open question: **non-live publishing** (take a finished file, post it to YouTube/PeerTube/Odysee with metadata) shares
almost all of its logic with live fan-out: platform accounts, per-target metadata, scheduling, status. A neutral
home for it ("publish" or "distribution") that both files and streaming call may be cleaner than putting it in either.
This needs a decision; this note does not make it.

---

## 6. Gaps in open source, and ideas nobody has

### Gaps (supported by sections 1 to 5)

1. **No open tool combines "simple to use" with "multi-platform" with "my own server".** Simple ones (Owncast, Broadcast Box) are destinations only. Distribution ones (Restreamer, MediaMTX, nginx-rtmp, Oryx) are server-room tools. OBS plus a plugin is the usual hack. Hobby projects (neustream, xplex, Prism) keep appearing, none verified as mature.
2. **No platform-aware logic.** Nobody turns "tick YouTube, Odysee, Rumble" into a correct encoder profile, because the facts live in help pages that change.
3. **Platform accounts and events are manual** in all open relays: copy URL and key from each dashboard. (SaaS tools connect accounts; Restreamer's feature list names YouTube Live and others, ⚠️ depth unverified.)
4. **Live and non-live are separate worlds.** Live relays do not publish files; uploaders do not stream; PeerTube does both but only to itself.
5. **Odysee has no usable official upload API**; Rumble and Vimeo upload APIs unverified. Open tooling for these is thin.
6. **No open pre-flight check** (audio present, key valid, upload sufficient, profile accepted).
7. **No open consolidated view of per-target errors** in plain language.

### Ideas (speculation, not evidence)

- **A capability table as data** (`platform -> protocol, codecs, max bitrate, fps, keyframe, access rules, last verified date`), maintained in the open and used by the profile calculator. Staleness is visible by "last verified" dates; a CI check could ping when pages change.
- **"Compatibility sentence"** shown to the user: "Your video will be 1080p at 30 images/s on all four sites. LinkedIn is the reason it is not 60."
- **Premiere mode:** a finished file played as if live to all targets (Oryx has "virtual live"; nobody combines it with multi-platform and scheduling).
- **Rolling local recording with go-back:** record always, clip the last N minutes after the fact, publish as non-live.
- **Safe-guest links:** a guest joins from a browser (WHIP) with no install; the host mixes them. Calls stay a separate program (ADR 0037) but reuse ingest.
- **Per-platform rule check before going live** (for example: "this stream shows combined chat in the video; Twitch's terms may not allow it", subject to the ⚠️ in 2.2).
- **Account-less targets:** custom RTMP always works as the fallback when OAuth is not possible (Odysee, Rumble, Kick).
- **One status history** per broadcast across all platforms: viewers, errors, dropped frames, timeline; exported as data, not hidden in dashboards.
- **Rust fit:** the existing design places stage 1 (copy) in reach of pure Rust (`str0m`, `moq-*`); the profile calculator and platform table are pure logic and are stage-1-compatible. The hard parts remain H.264 encoding (ADR 0015 tension) and capture on Linux/Wayland.

---

## Sources (all retrieved 2026-11-06)

Official or first-party:
- YouTube encoder settings: https://support.google.com/youtube/answer/2853702
- YouTube Data API quota costs: https://developers.google.com/youtube/v3/determine_quota_cost
- YouTube `videos.insert` reference: https://developers.google.com/youtube/v3/docs/videos/insert
- YouTube upload guide: https://developers.google.com/youtube/v3/guides/uploading_a_video
- YouTube Live Streaming API getting started: https://developers.google.com/youtube/v3/live/getting-started
- YouTube ingestion protocol comparison / HLS ingestion: https://developers.google.com/youtube/v3/live/guides/ingestion-protocol-comparison , https://developers.google.com/youtube/v3/live/guides/hls-ingestion (via search summary only)
- YouTube API audit/quota page: https://developers.google.com/youtube/v3/guides/quota_and_compliance_audits
- Twitch broadcasting guidelines: https://help.twitch.tv/s/article/broadcasting-guidelines (via search summary; page itself did not load)
- Twitch Enhanced Broadcasting blog: https://blog.twitch.tv/en/2024/01/08/introducing-the-enhanced-broadcasting-beta/
- Twitch Terms of Service: https://legal.twitch.com/en/legal/terms-of-service (could not be fetched; section 11 content only via search summaries ⚠️)
- Odysee help, stream destination: https://help.odysee.tv/category-livestreaming/streamingdestination
- Odysee help hub: https://help.odysee.tv/category-livestreaming/
- LBRY publish FAQ: https://shop.lbry.io/faq/how-to-publish ⚠️ (via search summary)
- Rumble livestream settings: https://rumble.support/help/livestream-settings
- Facebook Live Video API: https://developers.facebook.com/docs/live-video-api/ ; reference: https://developers.facebook.com/docs/live-video-api/reference (search summary) ; automatic encoder configuration: https://developers.facebook.com/docs/live-video-api/guides/automatic-encoder-configuration-api (title only)
- LinkedIn Live encoder settings: https://www.linkedin.com/help/learning/answer/128955
- Vimeo Live FAQs: https://help.vimeo.com/hc/en-us/articles/12426923921681-Live-FAQs
- X Live Studio / Producer help: https://help.x.com/en/using-x/live-studio , https://help.x.com/en/using-x/how-to-use-live-producer (search summary)
- PeerTube create/upload: https://docs.joinpeertube.org/use/create-upload-video ; admin configuration: https://docs.joinpeertube.org/admin/configuration
- MediaMTX README and forward docs: https://github.com/bluenviron/mediamtx , https://mediamtx.org/docs/features/forward
- Oryx README: https://github.com/ossrs/oryx
- Owncast README: https://github.com/owncast/owncast
- Broadcast Box README: https://github.com/glimesh/broadcast-box
- Restreamer README: https://github.com/datarhei/restreamer
- LiveKit egress overview: https://docs.livekit.io/home/egress/overview/
- OBS knowledge base audio sources: https://obsproject.com/kb/audio-sources
- GitHub API (licence, language, push date, latest release) for: obsproject/obs-studio, sorayuki/obs-multi-rtmp, datarhei/restreamer, datarhei/core, bluenviron/mediamtx, owncast/owncast, Chocobozzz/PeerTube, ossrs/srs, ossrs/oryx, livekit/livekit, arut/nginx-rtmp-module, AirenSoft/OvenMediaEngine, DDVTECH/mistserver, glimesh/broadcast-box, jitsi/jibri, gitroomhq/postiz-app, moq-dev/moq, streamlink/streamlink, yt-dlp/yt-dlp: https://api.github.com/repos/<owner>/<repo>
- Prism Live Studio FAQ: https://prismlive.com/en_us/faq/faq.html (search summary)

Secondary (⚠️ treat as leads):
- obs-multi-rtmp OBS resource: https://obsproject.com/forum/resources/obs-multi-rtmp.964 ; AUR: https://aur.archlinux.org/packages/obs-multi-rtmp
- OBS forum, simple output defaults: https://obsproject.com/forum/threads/what-default-settings-are-used-for-simple-output-mode.70864/
- OBS forum, keyframe frequency: https://obsproject.com/forum/threads/keyframe-frequency.36026/
- Eklipse keyframe guide: https://blog.eklipse.gg/tools/keyframe-interval-obs.html
- Wayland/PipeWire issues: https://forum.manjaro.org/t/obs-studio-window-capture-black-screen-wayland-pipewire/130133 , https://obsproject.com/forum/threads/obs-crashes-on-pipewire-screen-capture.184387/ , https://forums.developer.nvidia.com/t/screen-capture-does-not-work-in-obs-studio-on-wayland/224353 , https://obs-versions.com/blog/obs-studio-wayland-linux-guide
- Twitch simulcast rules (secondary): https://upstream.so/blog/twitch-allows-unified-chat-simulcasting-rules/ , https://conductatlas.com/platform/twitch/twitch-terms-of-service/simulcasting-restrictions/ , https://tubefilter.com/2023/10/23/twitchs-simulcasting-ban-is-officially-over/
- Streaming Media on Enhanced Broadcasting codecs: https://www.streamingmedia.com/Articles/News/Online-Video-News/Twitchs-Dual-Layout-Streaming-Technical-Innovation-or-Industry-Revolution-170053.aspx
- Kick API wrappers: https://docs.rs/kick-api/0.1.8/kick_api/struct.UpdateChannelRequest.html ; Kick settings guide: https://streamersize.pages.dev/platforms/kick/
- TikTok: https://restream.io/learn/platforms/how-many-followers-do-you-need-to-go-live-on-tiktok/
- LinkedIn access/scheduling claims: https://heystream.com/blog/linkedin-live-rtmp-setup , https://epiphan.com/forum/t/linkedin-live-support-via-pearl2/1917
- Restream / StreamYard pricing and limits: https://upstream.so/blog/restream-pricing/ , https://costbench.com/software/video-conferencing/restream/free-plan/ , https://upstream.so/blog/best-multistreaming-software/ , https://streamyard.com/blog/what-is-multistreaming-complete-guide-2026
- Hobby multistreamers: https://contra.com/p/PoRZRWY3-development-of-neustream-multistreaming-platform , https://github.com/xplexHQ , https://www.hnshowcase.com/post/47793158/self-hosted-fan-out-restreaming
- Rumble API (Pipedream): https://pipedream.com/apps/rumble
- PeerTube live transcoding forum thread: https://framacolibri.org/t/peertube-setup-help-live-transcoding-questions/20034
- Odysee headless upload question: https://software.codidact.com/posts/296348

## Not verified (summary)

Twitch ToS section 11 wording and current enforcement; Twitch AV1/HEVC ingest status; Kick, Odysee, Facebook keyframe
and bitrate figures from first-party pages; Odysee and Rumble upload APIs; Vimeo upload API quota; LinkedIn access
gating and scheduling rule; X Premium requirement; TikTok/Instagram/Dailymotion/Bilibili; whether SaaS relays
transcode per target; Oryx forward vs re-encode; Owncast multi-target push; licences of VDO.Ninja and Ant Media
Community; YouTube chapters and custom-thumbnail rules; all SaaS prices.
