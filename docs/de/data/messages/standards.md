# Nachrichten – Standards

> Belege: [standards.md](../standards.md) und `temp/research/messages-standards.md` (2026-11-05) —
> was mit ✅ markiert ist, nicht aus dem Web nachladen. Ein Programm deckt E-Mail, Chat und Messenger
> ab, nur verschlüsselt (ADR 0018); immer der jüngste gangbare Standard (ADR 0026).

## Envelope und Protokoll (alle Nachrichtenarten)

| Standard | Beleg | Rolle |
|----------|-------|-------|
| **ActivityStreams 2.0 (W3C Recommendation 2017)** | ✅ | Envelope (ADR 0020): `id`, `type`, `attributedTo`, `to`/`cc`/`bto`/`bcc`, `published`, `updated`, **`context`** (= Unterhaltung), **`inReplyTo`**, **`attachment`**, `mediaType` |
| AS2-Aktivitäten | ✅ | Protokoll: `Create`, `Update` (Bearbeiten), `Delete`, `Like` + `Undo` (Reaktion), **`Read`** (Lesequittung) |
| FEP-c0e0 `EmojiReact` | ✅ Entwurf | Emoji-Reaktionen über `Like` hinaus |
| FEP-7888 / FEP-171b (context, Unterhaltungs-Container) | ✅ Entwürfe, konkurrierend | beeinflussen unser Thread-Profil (Lücke unten) |
| "MLS in ActivityPub" (W3C Social Web CG Task Force) | ✅ inoffizieller Bericht | verschlüsselter Payload als `message/mls`; inneres begrenztes AS2-Profil (`urn:uuid`-IDs, `Create/Update/Delete/Like/Undo/Read`) — das Modell für unseren Envelope um verschlüsselten Inhalt |
| W3C Social Web WG | ✅ Chartung Jan 2026 | beobachten: nächste AS2/ActivityPub-Überarbeitung |

## Inhalt je Nachrichtenart

| Art | Inhaltsstandard | Beleg | Regel |
|-----|-----------------|-------|-------|
| **Chat / Messenger** | **MIMI-Inhaltsformat** `draft-ietf-mimi-content-10` (CBOR, in MLS) + `draft-mahy-mimi-message-status-02` (zugestellt/gelesen) | ✅ Entwürfe, 2026-11-02; Rust: `phnx-im/mimi-content` | festgelegt auf -10 bis zur RFC; deckt Antwort, Thema/Thread, Reaktionen, Edits, Löschen, Ablauf, verschlüsselte externe Anhänge ab |
| **E-Mail** | **Original-MIME-Nachricht** (RFC 5322) unverändert behalten + **JMAP-`Email`-Felder** (RFC 8621) für Index/Anzeige herausgezogen | ✅ | das Original bleibt Quelle der Wahrheit, damit Signaturen verifizierbar bleiben |
| Matrix (Konnektor) | Matrix-Spec **v1.19** (2026-07-08): `m.room.message`, Relationen `m.in_reply_to`, `m.thread`, `m.replace`, `m.annotation`, `m.receipt` | ✅ | Original-Event behalten, auf den Envelope abgebildet |
| Kommentar an einer Ressource | AS2 `Note` mit `inReplyTo`/`context` → die Ressource | ✅ | |
| Kommentar an einem Textfragment | W3C Web Annotation Model | ✅ | |

## Verschlüsselung

| Standard | Beleg | Rolle |
|----------|-------|-------|
| **MLS, RFC 9420** (OpenMLS 0.8) | ✅ | Gruppen und Chats; MIMI-Transport ist HTTPS + MLS (`draft-ietf-mimi-protocol-07`) |
| **OpenPGP, RFC 9580** (v6-Schlüssel, AEAD/SEIPDv2, Ed25519/X25519) | ✅ (Feature-Liste ⚠️ aus Spec-Wissen) | E-Mail, über rPGP |
| **Post-Quanten-OpenPGP, RFC 9980** (Juni 2026) | ✅ | folgen, sobald rPGP es unterstützt (ADR 0026) |
| **Header Protection, RFC 9788** (Aug 2025) | ✅ | schützt Betreff usw. in verschlüsselter Mail |
| **Autocrypt** v1; v2 = `draft-autocrypt-openpgp-v2-cert-03` (Juli 2026, PQ-Hybrid-Schlüssel) | ✅ v2-Entwurf / ⚠️ v1.1 nicht neu abgerufen | Schlüsselaustausch in Mail-Headern |

## Transport und Interoperabilität

| Standard | Beleg | Rolle |
|----------|-------|-------|
| **JMAP RFC 8620/8621** (+ RFC 9007 Mail-Lesequittungen, 9404 Blobs, 9425 Quotas, 9661 Sieve) | ✅ | Mail-Zugriff; eigener Mail-Server Stufe 2 (ADR 0018) |
| SMTP / RFC 5322 §3.4.1 Adressen | ✅ | Mail zwischen Servern |
| MIMI-Protokoll `-07`, Architektur `-03`, Raumrichtlinie `-04` | ✅ Entwürfe | Messenger-Interoperabilität (DMA) |
| XMPP (RFC 6120/6121) | ⚠️ ungeprüft | nicht geplant |

## Lücken → Kandidaten für eigene Spezifikationen (ADR 0014)

- „zugestellt“-Zustand und gebündeltes „gelesen bis X“ in AS2 (MIMI message-status deckt es nur innerhalb MIMIs ab)
- Ablauf (verschwindende Nachrichten) als AS2-Eigenschaft
- Beschreiber für verschlüsselte Anhänge in AS2
- Identität über Edits hinweg: MIMI/Matrix zeigen auf die **erste** Fassung, AS2-`Update` ändert an Ort und Stelle
- ein Profil für Thread vs. `context` vs. Thema (FEPs konkurrieren)
- Alias-Tabelle für Nachrichten-IDs protokollübergreifend (Message-ID, Matrix `event_id`, MIMI-ID, unser UUIDv7)
- Reaktionen und Edits für E-Mail
