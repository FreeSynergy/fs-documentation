# 0018 – Messenger umfasst E-Mail und Chats; nur verschlüsselte Nachrichten

Status: akzeptiert (2026-11-05) · Backend entschieden 2026-11-05 (Recherche `temp/research/messaging-crates.md`)

## Kontext
E-Mail, Chat (Telegram, Discord) und Messenger (Element, Signal) sind für Menschen dasselbe:
Ich habe eine Nachricht. Die Trennung kommt aus der Technik, nicht aus dem Bedarf.

## Entscheidung
- **Eine Kategorie, ein Programm:** `FreeSynergy.Messenger` (`fs-messenger`) deckt E-Mail, Chats
  und Messenger ab. Frontends aller bekannten Vertreter liegen unter
  `programs/apps/messenger/frontends/` (Outlook, Thunderbird, Element, Telegram, Discord, …).
  „E-Mail“ / „Chat“ ist ein Merkmal im `index.md` des Frontends, kein eigener Ordner.
- **Nur verschlüsselte Nachrichten.** Unverschlüsseltes wird nicht verschickt. Das Programm
  fragt aktiv nach einem verschlüsselten Weg bzw. sucht ihn (Schlüssel, Gegenstelle) — die
  Menschen sollen Verschlüsselung dabei lernen. Wie mit eingehender unverschlüsselter Post
  umgegangen wird, ist offen.

## Backend (entschieden 2026-11-05)
- **Eigenes Datenmodell** (AS2-Nachricht in `fs-store`) + **Konnektoren**. Matrix ist Transport,
  nicht Datenmodell. Frontends sprechen nur mit `fs-messenger` (Cap'n Proto, ADR 0021).
- **Stufenplan:**
  1. Konnektoren: Matrix (`matrix-sdk`, E2EE), IMAP/JMAP-Client (`async-imap`/`imap-next`,
     `jmap-client`), SMTP (`lettre`), `mail-parser`/`mail-builder`/`mail-auth`, OpenPGP über
     **rPGP** (`pgp`; nicht sequoia — LGPL), Autocrypt selbst, CalDAV/CardDAV (`libdav`).
     Homeserver: **tuwunel**.
  2. **Eigener Mailserver: SMTP rein/raus + JMAP-Server.** Wichtig als **Rückfallweg**: wenn
     etwas nicht funktioniert, muss Kommunikation per Mail gehen — Mail hat sich durchgesetzt,
     Matrix ist öffentlich kaum verbreitet. Unsere Systeme sollen auch untereinander per Mail
     schreiben können.
  3. IMAP-Server nur für fremde Programme (`imap-codec` + `imap-next`).
  Bis Stufe 2: Stalwart als **Empfehlung** für Betreiber (getrennt betrieben, nicht Teil des Stacks).
- **MLS** (RFC 9420, `openmls`) als Kandidat für Gruppenverschlüsselung, unabhängig vom Transport.
- Brücken (Telegram, Discord …) nur optional, selbst betrieben, sichtbar als „nicht Ende-zu-Ende“.
- Kein Delta Chat core: Autocrypt und Chat-über-Mail aus modernen Crates selbst bauen.
- Risiko: Stalwart-Crates wechseln zu AGPL → Versionen der MIT/Apache-Crates festschreiben,
  notfalls selbst weiterpflegen.

- **Inhaltsformat Chat: MIMI** (`draft-ietf-mimi-content-10`, festgeschrieben bis zum RFC; wir
  ziehen Änderungen nach — vom Nutzer bestätigt 2026-11-05). E-Mail: Original-MIME + JMAP-Felder.
- **Eingehende unverschlüsselte Nachrichten werden gekennzeichnet** (keine Quarantäne), mit
  Verweis auf eine Anleitung „So verschlüsselst du deine Mails“ in der Bibliothek (ADR 0031).

## Folgen
- Protokolle (Matrix, IMAP, SMTP, JMAP, XMPP) werden in `data/messages/standards.md` beschrieben,
  nicht als Frontend.
