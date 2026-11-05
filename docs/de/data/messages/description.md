# Nachrichten – Beschreibung

**Was diese Domäne ist:** E-Mail, Chat, Messenger und Kommentare als eine Domäne (ADR 0018), nur verschlüsselt. Gespeichert als Original + AS2-Envelope + Aktivitätsprotokoll (ADR 0020); Inhaltsstandards je Art in [standards.md](standards.md).

**Was sie abdeckt:**

- 1:1- und Gruppen-Nachrichten (Messenger-App)
- Kommentare an Ressourcen (Wiki-Seite, Task, Bild) — als `Note` mit Referenz auf das kommentierte Objekt
- E-Mail als erstklassige Nachrichtenart (Original MIME behalten, JMAP-`Email`-Felder indiziert)
- Mehrsprachigkeit über `contentMap`/`nameMap` (AS2, ✅)
- Offenlegungssteuerung über `to`/`cc`/`bto`/`bcc` (Offenlegung, **keine** Zugriffskontrolle — Beschluss 2)

**Abgrenzung zu anderen Domänen:**

| Thema | Wo es liegt | Warum |
|-------|-------------|-------|
| Wiki-Seiten, Beiträge mit Blöcken | [../apps/wiki/](../../programs/apps/wiki/index.md) oder die geplante Domäne `documents/` | Dokumente sind redigierbare Werke, Nachrichten sind vergängliche Äußerungen |
| Tag/Kommentar **auf einem Textteil** | W3C Web Annotation Model (✅) — Selektor `TextQuoteSelector` | Der Text wird nicht umgeschrieben |
| iTIP-Einladung und -Antwort | [events/](../events/index.md) | Protokollnachrichten, kein Chat |
| Benachrichtigungen (Notification) | eigene Domäne noch offen ([index.md → vorgeschlagen](../index.md)) | eine Notification zeigt auf eine Nachricht, ist aber nicht sie |

**Noch nicht ausgeführt (offene Frage 6.2 aus dem Gespräch):** was genau „Nachrichten“ umfasst, wird aus der App-Inventur abgeleitet (Messenger, Helpdesk-Tickets, Democracy-Kommentare, Whiteboard-Kommentare). Gemeinsamer Nenner ist überall `Note` + Referenz + Publikum.
