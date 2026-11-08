# 0059 – Verbinden ohne Server: jeder Client ist ein Knoten, iroh als Kandidat

Status: Richtung akzeptiert (Nutzer, 2026-11-07), nichts gebaut · ergänzt ADR 0019, 0028 · Probelauf nach dem Sprint

## Entscheidung (Nutzer)
iroh kommt in jeden Client, also in `fs-hub`, damit wir uns auch ohne Server unterhalten können.
Beispiel: Bei einem Treffen in einem Saal vernetzen sich die Leute gegenseitig und stimmen ab, der Moderator sieht, wie abgestimmt wurde. Oder er malt am Whiteboard, und alle sehen es auf dem eigenen Smartphone. „Die Daten hat sofort jeder und kann sie mit nach Hause nehmen.“ Der Moderator ist der Server. Fällt er weg, bleiben die anderen vernetzt und finden bei einer neuen IP schnell wieder zueinander, auch ohne WLAN.

## Es muss immer Alternativen geben (Nutzer, 2026-11-07)
„Was ist, wenn FreeSynergy abgestellt wird? Oder Nordkorea, China keine Leitung zu uns zulässt? Dann brauchen wir andere Wege.“ Auch Menschen, die politisch gejagt werden, ohne kriminell zu sein, müssen sich erreichen können. Deshalb: kein Weg darf von uns als Betreiber abhängen, und **Bluetooth wird irgendwann umgesetzt**. Gibt es dafür nichts Freies, programmieren wir es selbst und stellen es kostenlos zur Verfügung.

Weitere Vorgaben (Nutzer, 2026-11-07):
- **Offene Sitzung mit Freigabe beim Eintritt:** Wer eintritt, stimmt zu, dass alle Daten des Ereignisses mit allen geteilt werden, auch mit dem Moderator; wer nicht zustimmt, bleibt draußen. Eine Gruppe wird angelegt, die neuen Daten werden verteilt. Anonyme Abstimmungen sind ein eigener Modus.
- Mesh soll ebenso funktionieren: Wer am Eingang den QR-Code scannt, kennt die anderen, und jeder Knoten kann einen ausgefallenen wieder hereinholen.
- Lokaler Test und Bluetooth-Bibliothek: nach dem Sprint; die AGPL-Bibliothek `iroh-ble-transport` nutzen wir nicht.

## Geprüft (2026-11-07, Doku und Code gelesen, nichts ausgeführt)
- **Mesh:** `iroh-gossip` (0.102, HyParView und PlumTree: 5 aktive Nachbarn, 30 Reserve, Beitritt über jeden bekannten Knoten). Nachrichten nur 30 s vorgehalten; Behalten und Nachholen muss `fs-store` leisten. Zugehörigkeit schützt gossip nicht selbst: signieren wir.
- **Mobile Daten:** Beide treffen sich zuerst an einem Relais, danach direkt (laut iroh etwa 9 von 10 Netzen), sonst über das Relais. Ohne erreichbares Relais finden sich Handys im Mobilfunk nach einem IP-Wechsel nicht wieder.
- **Gegen Abschalten:** Relais kann jeder betreiben; Suche auch über die Mainline-DHT mit verblindeten Schlüsseln (`iroh-mainline-address-lookup-blinded`), Transporte über Tor (`iroh-tor-transport`) und Nym (`iroh-nym-transport`) existieren, alle experimentell.
- **Lokal:** mDNS im WLAN und über Hotspot. Bluetooth nur als AGPL-Bibliothek eines Einzelnen, 3–5 Verbindungen, etwa 100 kbit/s.

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
