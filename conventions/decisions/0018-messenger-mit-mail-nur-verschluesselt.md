# 0018 – Messenger umfasst E-Mail und Chats; nur verschlüsselte Nachrichten

Status: akzeptiert (2026-11-05) · Backend-Wahl offen

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

## Offen (eigenes Gespräch)
- Backend: Matrix mit **tuwunel** (Nutzer empfiehlt), eigener Stack aus SMTP/JMAP-Crates, oder
  beides als Brücken. Kriterien: Verschlüsselung Ende-zu-Ende, Rust, AS2-Abbildung (ADR 0014),
  Föderation.
- Umgang mit eingehenden unverschlüsselten Nachrichten.

## Folgen
- Protokolle (Matrix, IMAP, SMTP, JMAP, XMPP) werden in `data/messages/standards.md` beschrieben,
  nicht als Frontend.
