# Key Verification (Schlüsselprüfung)

| Feld | Wert |
|------|------|
| **Kategorie** | `overlays` |
| **Erbt von** | `base` |
| **Varianten** | `fingerprint`, `qr`, `device-list` |
| **Zustände** | `unverified`, `comparing`, `verified`, `mismatch` |
| **Gesten** | keine — Gesten kommen vom Frontend, nicht von der Komponente (ADR 0037) |
| **Animationen** | `fade-in`, `pop-in` |
| **Verwandt** | `modal`, `encryption-state`, `avatar`, `popover` |
| **Status** | Skizze |

## Beschreibung

Eine Schlüsselprüfung lässt eine Person den Schlüssel oder das Gerät eines Gegenübers prüfen und das Vertrauen bestätigen.

## Verwendungszweck

- Einen OpenPGP-Fingerabdruck oder ein MLS-Credential prüfen
- Ein neues Gerät eines Kontakts bestätigen
- Vertrauen festhalten (Bestätigung im Web of Trust)

## Varianten

| Variante | Beschreibung |
|---|---|
| **fingerprint** | Fingerabdruck-Gruppen vergleichen |
| **qr** | QR-Code scannen oder anzeigen |
| **device-list** | Geräteliste mit Zustand |

## Features

- Fingerabdruck in lesbaren Gruppen, zusätzlich ein QR-Code
- Auf beiden Seiten vergleichen, bestätigen oder ablehnen
- Geräteliste mit Zustand
- Das Ergebnis wird bei der Identität gespeichert

## Datenbindung

Bindet OpenPGP-Fingerabdruck, MLS-Credential und die Web-of-Trust-Bestätigung (`data/identity`). Darstellungsregister (ADR 0023): `Key → key-verification | text`. Messenger-Anforderungen `key.verify`, `device.list`.

## Abgrenzung

- **Nicht verwechseln mit** [modal](../modal/): Das Modal ist ein generischer Dialog; diese Komponente ist ein fester Prüfablauf.
- **Nicht verwechseln mit** [encryption-state](../../../primitives/feedback/encryption-state/): Der Status zeigt an; die Prüfung bestätigt.

## Best Practices

- Klar sagen, was Bestätigen bedeutet.
- Nie automatisch bestätigen; eine Abweichung ist ein deutlicher Fehler.
- Einen Vergleich über einen zweiten Kanal anbieten (persönlich, Anruf).

## Hinweis zu Blinc

Kein Blinc-Gegenstück. In unserer Schicht gebaut (bindet Identitätsdaten); den generischen Dialogteil liefert `modal`. Backlog-ID: keine ⚠️.

## Offene Punkte

- ⚠️ QR-Format für den Austausch
- ⚠️ Zuständigkeit für Vertrauensdatensätze (Identität oder Nachrichten)

## Siehe auch

- [overlays – Übersicht](../index.md)
- [Modal](../modal/)
- [Encryption State](../../../primitives/feedback/encryption-state/)
- [Messenger-Anforderungen](../../../../programs/apps/messenger/requirements.md)
- [Basiskomponente](../../../primitives/basics/base.md)
