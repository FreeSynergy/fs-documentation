# 0048 – Codecs ausgelagert, offene Codecs zuerst

Status: akzeptiert (2026-11-06), die Abschnitte „Kontext“ und „Vorschlag“ sind Verlauf · berührt ADR 0015

## Vorgabe des Nutzers (2026-11-06)
**Wir brauchen offene Formate, soweit es geht.** H.264 wird höchstens gelesen, sonst nichts.

Das ändert den Vorschlag unten: Eigene Ausgabe ist **AV1 und Opus**. Weiterleiten ohne Dekodieren braucht keinen Codec, auch
bei H.264. Offen: Auch Dekodieren kann unter Patente fallen (ungeprüft), und Sisvel bestreitet, dass AV1 vollständig
lizenzfrei ist; gerichtlich ist das nach unseren Quellen nicht entschieden. Folge: Laut Recherche nimmt nur YouTube sicher AV1.

## Entscheidung des Nutzers (2026-11-06)
- **Codecs werden ausgelagert, ähnlich wie bei GStreamer.** Jeder Codec ist ein Anbieter hinter einer Schnittstelle (ADR 0045).
- **Zuerst die offenen Codecs.** Wenn das fertig ist, sehen wir nach, ob andere dazukommen.
- **Wir geben nur Freies heraus.** Macht jemand anderes H.264, ist das seine Sache. Lesen wollen wir es selbst können.
- Unsere eigene Aufnahme erreicht zunächst vor allem YouTube; andere Plattformen über weitergeleitete Streams.
- Ziel: Wenn wir groß werden, schaffen wir Standards. Wenn nicht, auch gut.

RTMP ist kein Codec, sondern Transport (Enhanced RTMP: offene Spezifikation, Apache-2.0). Es trägt AV1 und andere, ersetzt sie aber nicht.

## Kontext
Einfaches Aufnehmen (Streaming) heißt Kodieren. Reines Rust gibt es dafür nur teilweise. Der Nutzer möchte offene Standards
nutzen, auch weil ein Rust-Encoder allen hilft. Die Plattformen brauchen für einen gemeinsamen Stream H.264.

## Vorschlag
1. Schnittstelle `VideoEncoder`, ein festes Ziel für alle Backends (ADR 0045).
2. **Vulkan Video** (offener Khronos-Standard) als erstes Backend: H.264, H.265, AV1 über die Hardware. Der Treiber ist
   nicht in Rust, aber das gilt für jede Grafikausgabe.
3. `rav1e` für Software-AV1; Beiträge dorthin statt Neubau, wenn das Projekt aktiv genug ist (zu prüfen).
4. Eigener Encoder (AV1, später AV2) als langfristiges Ziel, keine Voraussetzung.

## Offen
- **Rechner ohne passende Hardware:** `rav1e` allein reicht nicht, weil die Plattformen H.264 brauchen. OpenH264 wäre eine
  Ausnahme von „100 % Rust“.
- **H.264-Patente:** Rechtsrat nötig, auch für die Nutzung über die Hardware.
- macOS hat kein natives Vulkan; proprietäre Treiber sind ungeprüft.
