# 0059 – Verbinden ohne Server: jeder Client ist ein Knoten, iroh als Kandidat

Status: Richtung akzeptiert (Nutzer, 2026-11-07), nichts gebaut · ergänzt ADR 0019, 0028 · Probelauf nach dem Sprint

## Entscheidung (Nutzer)
iroh kommt in jeden Client, also in `fs-hub`, damit wir uns auch ohne Server unterhalten können.
Beispiel: Bei einem Treffen in einem Saal vernetzen sich die Leute gegenseitig und stimmen ab, der Moderator sieht, wie abgestimmt wurde. Oder er malt am Whiteboard, und alle sehen es auf dem eigenen Smartphone. „Die Daten hat sofort jeder und kann sie mit nach Hause nehmen.“ Der Moderator ist der Server. Fällt er weg, bleiben die anderen vernetzt und finden bei einer neuen IP schnell wieder zueinander, auch ohne WLAN.

## Regeln (Vorschlag der Strategie, vom Nutzer bejaht)
- Hinter einem eigenen Transport-Trait, austauschbar. Stand geprüft: v1.4.1, MIT oder Apache-2.0.
- Nur eigenes Relais; kein öffentlicher Dienst von n0 (`dns.iroh.link`, öffentliche Relais) als Voreinstellung.
- Finden über Einladung und QR-Code, im selben Netz über mDNS (ADR 0028).
- Ein Modus, der nie direkt verbindet, weil die Gegenseite sonst die IP-Adresse sieht.

## Offen, nach dem Sprint
- **Ohne jedes Netz:** Geräte brauchen eine Verbindung, etwa Hotspot, Wi-Fi Direct/Aware oder Bluetooth. Was iroh davon trägt, ist nicht geprüft.
- **Handy:** Issue #4651 (Keepalive je Weg nicht über 5 s setzbar) ist offen; nur im Vordergrund verbinden.
- **Abstimmen ohne Server:** Hat jeder alle Daten, sieht jeder alle Stimmen, das widerspricht der Anonymität (`fs-surveys`). Doppelte Stimmen brauchen eine Teilnehmerliste, die der Moderator unterschreibt.
- **Moderator fällt weg:** Wer zählt, und wer darf das Whiteboard ändern? Zusammenführen wie geplant (logische Uhr, CRDT für Text).
- **Offline:** Ist die Gegenseite weg, kommt nichts an; Nachrichten brauchen einen Aufbewahrungsort.
