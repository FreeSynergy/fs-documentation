# GStreamer - Struktur & UI/UX

## Übersicht

GStreamer hat kein Fenster. „Struktur" meint den Aufbau einer Pipeline und die Stellen, an denen ein Programm (oder ein Skin) eingreift: Elementkette, Pads, Bus und Zustandsmaschine.

## Modell einer Pipeline

### Hauptbereiche

```
Quelle            Filter / Konvertierung        Kodierung          Senke
┌───────────┐     ┌──────────────────────┐      ┌───────────┐   ┌────────────┐
│ v4l2src   │ --> │ videoconvert → scale │ -->  │ x264enc   │-> │ rtspclientsink │
└───────────┘     └──────────────────────┘      └───────────┘   └────────────┘
      │            Pads verhandeln Caps          Eigenschaften      │
      └── Bus: EOS / Fehler / Tags / Latenz ─────────────────────────┘
```

### Elemente

- **Source**: liefert Puffer (`filesrc`, `v4l2src`, `appsrc`, `udpsrc`)
- **Filter**: verändern Daten (`scale`, `videoconvert`, `audioconvert`)
- **Codec**: `x264enc`, `avdec_h264`, `opusenc` — meist aus base/good/bad/ugly
- **Sink**: verbraucht Puffer (`fakesink`, `autovideosink`, `filesink`, `appsink`)
- **Muxer/Demuxer**: `matroskamux`, `qtdemux`, `hlssink`
- **Bins**: `decodebin3` (automatisch), `tee` + `queue` (Verzweigung)

### Zustandsmaschine

```
NULL → READY → PAUSED → PLAYING
```

Beim `PAUSED`-Start werden Puffer bis zum Syncpunkt gefüllt; `PLAYING` gibt sie frei.

## UI-Struktur eigener Apps (Referenz)

```
┌───────────────────────────────────────────────┐
│ Titelleiste / Transport (Play, Pause, Stop)   │
├───────────────────────────────────────────────┤
│ Video-/Sink-Bereich (autovideosink, gtksink)  │
├───────────────────────────────────────────────┤
│ Status: Position, Codec, Bitrate, Latency     │
└───────────────────────────────────────────────┘
```

## UI/UX

### Design-Prinzipien

- **Explizit statt magisch**: Pads und Caps werden sichtbar verhandelt — Fehlermeldungen nennen Element und Pad
- **Fehler laufen über den Bus**: Anwendungen reagieren auf `ERROR`/`WARNING`/`EOS`, nicht auf Exit-Codes
- **Keine globalen Defaults**: jede Pipeline trägt ihre Eigenschaften selbst

### Interaktionen

- `sync=false` für Vorschaurezweige (schneller, aber unregelmäßig)
- **Seek/Snapshot**: über `GstStream-Events` oder `gst_element_send_event`, nicht über Tasten
- **Dynamische Umbauten**: Pads zur Laufzeit an-/abhängen (Hotplug, Spurwechsel)

## Zugänglichkeit

- Keine eigene Oberfläche → Accessibility hängt am Toolkit der App (GTK/Qt)
- Text- und Untertitelelemente (`subtitleoverlay`) liefern die Basis für Untertitel
- Debug-Ausgaben sind maschinenlesbar und gut filterbar (`GST_DEBUG_CATEGORY`)

## Performance

- Buffer-Pools vermeiden Kopien zwischen Elementen
- Queues mit `max-size-buffers` begrenzen Latenz und RAM
- Hardware-Elemente (`vaapipostproc`, `nvv4l2decoder`) halten Frames auf dem GPU-Speicher
- `GST_TRACERS` (z. B. `latency`, `schedtime`) für Messungen im laufenden Betrieb
