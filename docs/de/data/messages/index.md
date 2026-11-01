# Nachrichten

Chat-, Kommentar- und Mail-artige Mitteilungen. Kanonisches Payload: **AS2-Objekte** (`Note`, `Article`) im ActivityPub-Envelope (Beschluss 1+2).

## Standards in dieser Domäne

| Standard | Beleg | Rolle bei FreeSynergy |
|----------|-------|-----------------------|
| **ActivityStreams 2 Vocabulary, W3C** | ✅ | `Note`, `Article`, `contentMap`/`nameMap` (Mehrsprachigkeit) |
| **JMAP, RFC 8620/8621** | ✅ | Referenz für sauberes Adressieren/Patchen/Synchronisieren von JSON-Ressourcen |
| **Mail-Adressformat, RFC 5322 §3.4.1** | ✅ | Format von Absender-/Empfängeradressen |
| **XMPP (RFC 6120/6121)** | ⚠️ ungeprüft | Interop mit Chat-Alt-Systemen, vor Verwendung belegen |

## Offene Punkte

- threading/Verlauf (Eltern-Kind-Beziehungen) in AS2 nicht vollständig definiert → Regel nötig
- Mail-Interop (SMTP-Versand) ist ein eigenes Transport-Thema, kein Datenmodell-Thema

## Siehe auch

- [standards.md → Aktivitäten](../standards.md)
- [kommentare (vorgeschlagene Domäne)](../index.md) — für Textteil-Tags/Kommentare ist das **W3C Web Annotation Model** (✅) der richtige Standard
