# Call Controls (Anrufsteuerung)

| Feld | Wert |
|------|------|
| **Kategorie** | `media` |
| **Erbt von** | `base` |
| **Varianten** | `bar`, `compact` |
| **Zustände** | `idle`, `ringing`, `connected`, `muted`, `sharing` |
| **Gesten** | keine — Gesten kommen vom Frontend, nicht von der Komponente (ADR 0037) |
| **Animationen** | `pop-in` |
| **Verwandt** | `button-group`, `media-player`, `grid-view`, `toolbar` |
| **Status** | Skizze |

## Beschreibung

Anrufsteuerungen sind die Bedienleiste eines Anrufs: Mikrofon, Kamera, Bildschirmfreigabe und Auflegen. Sie gehören zum **eigenen Anruf-Programm**, nicht zum Messenger (ADR 0037).

## Verwendungszweck

- Bedienleiste des Anruf-Programms
- Mini-Leiste in anderen Programmen während eines laufenden Anrufs
- Wiederverwendbar für Streaming, SIP und normale Telefonanrufe

## Varianten

| Variante | Beschreibung |
|---|---|
| **bar** | vollständige Bedienleiste |
| **compact** | nur Mikrofon und Auflegen |

## Features

- Umschalt-Schaltflächen mit Zustand
- Auflegen als eigene Aktion ohne Bestätigungsabfrage
- Optionale Geräteauswahl
- Kombinierbar mit [grid-view](../../data/grid-view/) für das Kachelraster

## Datenbindung

Bindet eine Anrufsitzung (MatrixRTC ⚠️ / noch kein FreeSynergy-Standard). Darstellungsregister (ADR 0023): `CallSession → call-controls`. ADR 0037, Punkt 6: Anrufe sind immer ein eigenes Programm; sichtbar davon sind wiederverwendbare Komponenten.

## Abgrenzung

- **Nicht verwechseln mit** [media-player](../media-player/): Der Player steuert die Wiedergabe; Anrufsteuerungen steuern eine laufende Sitzung.
- **Nicht verwechseln mit** [button-group](../../../primitives/actions/button-group/): Die Gruppe ist generisch; diese Komponente bindet die Sitzung.

## Best Practices

- Stumm- und Kamera-aus-Zustand müssen ohne Farbe sichtbar sein.
- Auflegen ist von den übrigen Bedienelementen getrennt.
- Die Leiste bleibt während einer Bildschirmfreigabe erreichbar.

## Hinweis zu Blinc

Kein direktes Blinc-Gegenstück (Medienbedienelemente gibt es nur für den Player). In unserer Schicht gebaut; generische Umschalt-Schaltflächen kommen aus Blinc. Backlog-ID: keine ⚠️.

## Offene Punkte

- ⚠️ Anruf-Protokoll oder Standard (MatrixRTC, SIP, WebRTC)
- ⚠️ Name des Anruf-Programms

## Siehe auch

- [media – Übersicht](../index.md)
- [Media Player](../media-player/)
- [Button Group](../../../primitives/actions/button-group/)
- [Messenger-Anforderungen](../../../../programs/apps/messenger/requirements.md)
- [Basiskomponente](../../../primitives/basics/base.md)
