# Streaming — Design

**Status: Vorschlag (2026-11-06).** Zurück zum [Gesamtplan](../roadmap.md) · [Anforderungen](requirements.md) ·
[Recherche](https://github.com/FreeSynergy/fs-documentation/blob/main/temp/research/streaming-landscape.md).

## Wofür es da ist

**Einmal aufnehmen und überall zeigen:** YouTube, Odysee und andere Plattformen gleichzeitig, live und nicht live, ohne dass ein SaaS-Anbieter dazwischen steht. Und das Aufnehmen muss weit einfacher sein als bei OBS.

Kein offenes Werkzeug, das wir gefunden haben, ist zugleich einfach, plattformübergreifend und selbst gehostet. Restreamer und MediaMTX sind für Serverräume gedacht, und OBS mit einem Multi-Output-Plugin ist der übliche Ausweg, wobei das Plugin über OBS-Versionen hinweg bricht.

Anrufe sind ein eigenes Programm, das dieselben Teile nutzt (ADR 0037).

## Drei Teile

| Teil | Aufwand | Hinweise |
|------|---------|----------|
| **Live verteilen** | Machbar | Ein kodierter Strom wird an viele Ziele weitergeleitet, ohne erneutes Kodieren |
| **Nicht live veröffentlichen** | Machbar | Upload über die Schnittstelle jeder Plattform; teilt eine Ebene „Veröffentlichen“ mit dem Live-Teil |
| **Einfache Aufnahme** | Schwer | Bedeutet Kodierung, siehe unten |

Videoverwaltung, Versionen und Sync gehören zu [`fs-files`](../files/design.md), und Aufnahmen landen dort. Ein Live-Stream ist keine Datei, daher bleibt dieser Teil hier.

## Einfach heißt automatisch

Die Person wählt ihre Ziele. Das Programm ermittelt die Einstellungen und prüft vor dem Start, ob alles funktioniert: Verbindung, Schlüssel und ob die gewählten Ziele das Format annehmen. Szenen, Bitraten und Keyframes bleiben verborgen, solange niemand sie möchte. Ein umfangreiches Frontend für Fortgeschrittene kann sie alle auf derselben Engine zeigen.

## Ein Strom für alle

Aus der Recherche: H.264, AAC-LC, konstante Bitrate, 2-Sekunden-Keyframes, 1080p bei 30 fps und etwa 5 Mbps passen zu allen untersuchten Plattformen, wobei LinkedIn und Vimeo die Grenzen setzen. AV1 und HEVC helfen nur bei YouTube. Vertikales Video braucht eine zweite Kodierung.

## Plattformen

| Plattform | Live | Nicht live |
|-----------|------|------------|
| YouTube | Enhanced RTMP: H.264, HEVC, AV1 | API, dokumentiert mit 100 Uploads pro Tag |
| Twitch | RTMP; Codec über H.264 hinaus unklar ⚠️ | Nicht zutreffend |
| Odysee | Eigenes RTMP | Keine offizielle API gefunden |
| Rumble | ⚠️ nicht verifiziert | Keine API gefunden |

Twitch erlaubt Simulcasting ohne Exklusivitätsvereinbarung, beschränkt aber das Zusammenführen von Aktivitäten anderer Plattformen mit dem Stream, laut Sekundärquellen ⚠️. Die Veröffentlichungsziele brauchen eine Prüfung vor der Nutzung, weil sich Bedingungen ändern.

## Kodierung

**Entschieden (2026-11-06): Codecs werden ausgelagert, ähnlich wie bei GStreamer. Jeder ist ein Anbieter hinter einer [Schnittstelle](../../../interfaces/index.md). Wir beginnen mit den offenen.** Danach schauen wir uns andere an. Wir veröffentlichen nur, was frei ist; wer H.264 will, kann es selbst bereitstellen. Wir wollen es lesen können.

| Codec-Anbieter | Hinweise |
|----------------|----------|
| **AV1** mit `rav1e` (Rust) | Offen, lizenzgebührenfrei nach den Bedingungen seiner Allianz. Sisvel bestreitet das; laut unseren Quellen hat kein Gericht entschieden |
| **AV1 per Hardware** über Vulkan Video (offener Khronos-Standard) | Live-Geschwindigkeit. Offene Mesa-Treiber implementieren es |
| **Opus** mit `mousiki` (Rust) | Für Ton. Jung, muss getestet werden |
| AV2 | Spezifikation 1.0 seit Mai 2026; kein Rust-Encoder gefunden. Eine Chance, als Erste dabei zu sein, aber für Plattformen zu früh |
| VP8, VP9 | Veröffentlicht. VP9 hat außerdem einen Sisvel-Pool. Nur Bindings zu `libvpx` gefunden |

**Transport ist eine eigene Sache.** RTMP ist kein Codec: Es transportiert einen. [Enhanced RTMP](https://github.com/veovera/enhanced-rtmp) ist eine offene Spezifikation (Apache-2.0), die unter anderem AV1 ergänzt. Sie bringt also offene Codecs zu Plattformen, aber nur zu denen, die sie annehmen. Das Weiterleiten eines Streams aus einem anderen Werkzeug braucht keinen Codec von uns, daher geht H.264 von anderswo unverändert durch.

**Die Folge, akzeptiert:** Laut Recherche nimmt nur YouTube AV1 zuverlässig. Unsere eigenen Aufnahmen erreichen also zuerst YouTube und andere Plattformen über weitergeleitete Streams. Offen: welche Formate PeerTube und Odysee annehmen, und ob das Lesen von H.264 selbst durch Patente gedeckt ist.

## Muster

| Muster | Verwendung |
|--------|------------|
| Strategy | Encoder, Eingangs- und Ausgangsprotokolle, Veröffentlichungsziele |
| Pipeline | Erfassen → Kodieren → Leiten → Ziele |
| Observer | Status für die Schnittstelle |
| State | `idle`, `checking`, `live`, `ended`, `error` |
| Adapter | Jede fremde Crate hinter unserem eigenen Trait |

## Kandidaten

`str0m` 0.25 (WebRTC), `moq-rtc` 0.3 (WHIP- und WHEP-Gateway), `xcap` (Bildschirmaufnahme), `nokhwa` (Kamera), `ash` und `gpu-video` (Vulkan, nicht geprüft), `rav1e` 0.8, `mousiki` (Opus in Rust). Keiner ist bisher auf C-Abhängigkeiten geprüft.

## Stufen

1. Weiterleiten: einen Strom empfangen, an viele senden, Aufnahme in `fs-files`.
2. Nicht live veröffentlichen, mit Titeln je Plattform und Planung.
3. Einfache Aufnahme mit Bildschirm und Kamera, automatische Einstellungen und eine Prüfung vor dem Start.
4. Zweite Kodierung für vertikales Video, Overlays.

## Offene Fragen

1. Wie erreichen wir Plattformen, die H.264 brauchen? Siehe oben. 2. Welche Plattformen zuerst?
