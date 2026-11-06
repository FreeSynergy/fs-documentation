# Messenger — Anforderungen

Was `FreeSynergy.Messenger` muss und kann, abgeleitet aus den [Frontends](frontends/index.md)
(ADR 0006, 0013). Jede Fähigkeit nennt ihren Datenstandard (ADR 0014) und unseren Stand.
Ein Programm deckt E-Mail, Chat und Messenger ab und sendet **nur verschlüsselt** (ADR 0018).

Stand: `implemented` · `planned` · `proposed`

**Gesehen in** — analysierte Frontends: [Di](frontends/discord/index.md) Discord ·
[El](frontends/element/index.md) Element · [Ko](frontends/kontact/index.md) Kontact ·
[Ma](frontends/mastodon/index.md) Mastodon · [Ou](frontends/outlook/index.md) Outlook ·
[Te](frontends/telegram/index.md) Telegram · [Th](frontends/thunderbird/index.md) Thunderbird.
*arch.* = von unserer Architektur oder unseren Grundsätzen gefordert, nicht durch Zählen.
⚠️ = nicht (oder nicht eindeutig) in unseren Frontend-Dateien; aus den Produkten bekannt, dort erst zu prüfen.

**Regel:** Eine Fähigkeit ist *Pflicht*, wenn mindestens vier der sieben Frontends sie zeigen, oder wenn
unsere Architektur sie braucht. Die Fähigkeits-Kennung in Backticks (`<objekt>.<aktion>`) ist ein Vorschlag
für die Fähigkeitsliste (siehe offener Punkt zum Eintragsformat) — eine Fähigkeit ist eine Aktion auf dem
Objekt, nie ein Menüpunkt oder eine Geste.

Daten-Verweise: [messages-Standards](../../../data/messages/standards.md) ·
[messages technisch](../../../data/messages/technical.md) (Protokoll-Abbildung, Verschlüsselungszustand) ·
[contacts](../../../data/people/index.md) · [identity](../../../data/identity/index.md).

## Pflicht (gemeinsam in den analysierten Programmen)

| Fähigkeit | Gesehen in | Daten / Standard | Stand |
|------------|-------------|------------------|-------|
| Mehrere Konten in einem Programm verwalten — Mail, Matrix, MIMI (`account.add`, `account.remove`, `account.edit`) | Ko, Ou, Th, Te; *arch.* (ein Programm, ADR 0018) | Konnektoren: JMAP RFC 8620/8621, IMAP, SMTP, Matrix v1.19, MIMI-Protokoll `-07` | proposed |
| Unterhaltungen über alle Konten hinweg auflisten, neueste zuerst (`conversation.list`) | Di, El, Ko, Ma, Ou, Te, Th | AS2 `context` = Unterhaltung; JMAP `threadId`; Matrix-Raum; MIMI-Raum | proposed |
| Unterhaltungen ordnen: Ordner, Kategorien, angeheftete (`conversation.move`, `mailbox.create`) | Ko, Ou, Th (Ordner, verschieben/kopieren); Di (Kanal-Kategorien); El (angeheftete Räume); Te (Sortierung) | JMAP `Mailbox` + `mailboxIds`; Chat-Ordner: Lücke → eigenes Profil | proposed |
| Eine Unterhaltung öffnen und ihre Nachrichten lesen, flach (Chat) oder als Baum (Mail) (`conversation.open`, `message.open`) | Di, El, Ko, Ma, Ou, Te, Th | AS2 `Note`, `context`, `inReplyTo`; Original behalten (MIME / MIMI CBOR / Matrix-Event) | proposed |
| Eine Nachricht an eine Person oder Gruppe senden (`message.send`) | Di, El, Ko, Ma, Ou, Te, Th | `Create`; MIMI-Inhalt `-10`; MIME RFC 5322 über SMTP/JMAP-Auftrag; Matrix `m.room.message` | proposed |
| Nur verschlüsselt senden; einen verschlüsselten Weg finden (Schlüssel, Gegenstelle) und es erklären, wenn es keinen gibt (`message.send`-Vorbedingung, `key.discover`) | El (E2EE als Standard), Te (geheime Chats), Ko, Ou, Th (OpenPGP/S/MIME); *arch.* ADR 0018 | MLS RFC 9420; OpenPGP RFC 9580 + Header Protection RFC 9788; Autocrypt (v2-Entwurf) | proposed |
| Den Verschlüsselungszustand jeder Nachricht zeigen; unverschlüsselte eingehende markieren, mit Link zum Bibliotheksführer (`message.encryption`) | El, Te (Sicherheitshinweise); *arch.* ADR 0018/0031 | `freesynergy.net:encryption` = `mls` · `openpgp` · `megolm` · `transport-only` · `none` | proposed |
| Signaturen, Schlüssel und Geräte überprüfen; dem Schlüssel eines Kontakts vertrauen (`key.verify`, `device.list`) | Ko, Th (GPG-Signatur prüfen); El, Te (Geräteverwaltung) | OpenPGP RFC 9580; MLS-Credentials; Web of Trust ([identity](../../../data/identity/index.md)) | proposed |
| Auf eine Nachricht antworten — an den Absender oder an alle (`message.reply`) | Di, El, Ko, Ou, Te, Th; Ma (Antwort ⚠️) | `Create` mit `inReplyTo`; `In-Reply-To`-Header; Matrix `m.in_reply_to`; MIMI-Antwort | proposed |
| Eine Nachricht weiterleiten (`message.forward`) | Di, El, Ko, Ou, Te, Th | neues `Create`, Original als `attachment` (E-Mail: `message/rfc822`) ⚠️ kein MIMI-Forward-Typ | proposed |
| Einen Teil einer Nachricht zitieren (`message.quote`) | Di, El, Ma, Te; Ko, Th (als Zitat einfügen) | W3C Web Annotation `TextQuoteSelector` auf der Quelle (ADR 0033); bei Mail zusätzlich zitierter Text | proposed |
| Eine gesendete Nachricht bearbeiten; die ID der ersten Fassung bleibt (`message.edit`) | Di, El, Ma, Te | `Update`; MIMI-Edit; Matrix `m.replace`; E-Mail: Lücke | proposed |
| Eine Nachricht löschen — für mich, oder für alle, wo der Transport es erlaubt (`message.delete`) | Di, El, Ko, Ma, Ou, Te, Th | `Delete` + Tombstone; MIMI leerer Rumpf; Matrix Redaction; JMAP in den Papierkorb / zerstören | proposed |
| Eine Nachricht für später markieren ⚠️ „Markieren“ in den Menüs ist mehrdeutig (Flagieren vs. Auswählen) (`message.flag`) | Di, El, Ko, Ou, Te, Th ⚠️ | JMAP-Schlüsselwort `$flagged`; Chat: Lücke → eigenes Anbieter-Schlüsselwort | proposed |
| Als gelesen/ungelesen markieren; zur nächsten ungelesenen springen (`message.read`, `conversation.markRead`) | Te (Chat als gelesen markieren); El, Ma (nächste ungelesene); Ko, Ou, Th (markieren) | `Read`-Aktivität; JMAP `$seen`; Matrix `m.receipt`; MIMI message-status; gebündelt „gelesen bis X“ ist eine Lücke | proposed |
| Nachrichten suchen — in einer Unterhaltung und über alle Konten, Volltext (`message.search`) | Di, El, Ko, Ou, Te, Th; Ma (Hashtags) | Volltext über die herausgezogenen Felder (technical.md); JMAP-`Email/query`-Filtermodell | proposed |
| Anhänge senden, in Vorschau zeigen und speichern (Drag & Drop ist ein Frontend-Weg) (`attachment.add`, `attachment.save`) | Di, El, Ma, Te; Ko, Th (Anhänge speichern); Ou | AS2 `attachment`; JMAP Blobs RFC 9404; MIMI verschlüsselte externe Teile; Beschreiber für verschlüsselte Anhänge in AS2: Lücke | proposed |
| Medien inline in Vorschau zeigen (Bilder, Video, Dokumente) (`attachment.preview`) | Di, El, Ma, Te | `mediaType` des Anhangs; Miniaturbilder lokal abgeleitet | proposed |
| Text beim Verfassen formatieren (fett, kursiv, Code, Zitat, Listen, Links) (`message.compose` mit Format) | El, Ma (Markdown); Ko, Ou, Th (Formatierungsleiste) | E-Mail: `multipart/alternative` text/plain + text/html; Chat: MIMI-Körperteil `text/markdown` ⚠️ | proposed |
| Entwürfe automatisch behalten und sie wieder aufnehmen (`draft.save`, `draft.list`) | Di, El, Ko, Ma, Ou, Te, Th (Auto-Speicherung) | JMAP-Schlüsselwort `$draft` + Drafts-Postfach; Chat-Entwürfe: nur lokal (Lücke) | proposed |
| Benachrichtigungseinstellungen je Unterhaltung — alle, nur Erwähnungen, stumm (`conversation.notify`) | Di, El, Te (Kanal-/Raum-Benachrichtigungen); Ma (Benachrichtigungsarten); Ko, Th (Systembenachrichtigungen) | Programm-Einstellung; Matrix-Push-Regeln werden darauf abgebildet; kein gemeinsamer Standard ⚠️ | proposed |
| Unterhaltungen gruppieren: anlegen, benennen, beschreiben, einladen, verlassen (`group.create`, `group.invite`, `group.leave`) | Di, El, Te; Ko, Ou, Th (Kontaktgruppen / Verteilerlisten) | MLS-Gruppenmitgliedschaft (Add/Remove); MIMI-Raumrichtlinie `-04`; AS2 `Invite`, `Join`, `Leave`; JSContact `kind: group` | proposed |
| Rollen und Rechte innerhalb einer Gruppe (`group.role`) | Di, El, Te; Ma (Moderatoren) | MIMI-Raumrichtlinie `-04`; Matrix Power Levels | proposed |
| Moderieren: entfernen, verbannen, blockieren, melden (`member.remove`, `actor.block`, `message.report`) | Di, El, Ma, Te | AS2 `Remove`, `Block`, `Flag` | proposed |
| Kontakte nutzen: Empfänger aus dem Adressbuch wählen, die Karte eines Absenders öffnen (`contact.lookup` — geliehen, ADR 0020) | Ko, Ou, Th (Adressbuch); Di, El, Ma, Te (Profil öffnen) | JSContact RFC 9553 ([contacts](../../../data/people/index.md)), lebende Referenz in das Kontaktprogramm | proposed |
| Das eigene Profil bearbeiten: Name, Bild, Kurztext (`profile.edit`) | Di, El, Ma, Te | AS2-Schauspieler; JSContact für die eigene Card; [profile](../../../data/profile/index.md) | proposed |
| Regeln und Filter: automatisch sortieren, beschriften, verschieben, stummschalten (`rule.create`, `rule.run`) | Ko, Ou, Th (Filterregeln); Ma (Wort-/Benutzerfilter); Di (AutoMod) | Sieve über JMAP RFC 9661 für Mail; dasselbe Regelmodell auf Chat angewandt ⚠️ (Lücke) | proposed |
| Offline arbeiten und über Geräte hinweg synchron bleiben (`sync`) | Ko, Th (Offline-Modus); El (Synchronisation); Te (Cloud) | `fs-store` + `fs-hub`, Objekt-Sync (ADR 0019); lokal, im Ruhezustand verschlüsselt (ADR 0024) | proposed |
| Kein Fremdinhalt oder Tracking-Bild, ohne dass der Mensch es will (`message.open`-Standard) | Th (Tracking-Schutz); *arch.* (Privatsphäre) | Regel in unserem Renderer; MIME-`cid`-Teile erlaubt, ferne URLs standardmäßig gesperrt | proposed |

## Kür (bemerkenswerte Ideen)

| Fähigkeit | Gesehen in | Daten / Standard | Stand |
|------------|-------------|------------------|-------|
| Mit einem Emoji auf eine Nachricht reagieren (`message.react`) — nach Verifizierung vermutlich Pflicht | ⚠️ Di, El, Te, Ma (nicht in unseren Dateien) | `Like` / FEP-c0e0 `EmojiReact`, rückgängig über `Undo`; MIMI-Reaktion; Matrix `m.annotation`; E-Mail: Lücke | proposed |
| Threads: in einem Seitenthread antworten, ohne die Hauptunterhaltung zu fluten (`thread.open`) | ⚠️ Di, El (nicht in unseren Dateien); Th (gruppierte Ansicht) | AS2 `context` / `inReplyTo`; Matrix `m.thread`; MIMI-Thema; Thread-Profil ist eine Lücke (FEPs konkurrieren) | proposed |
| Zugestellt-/Gelesen-Status gesendeter Nachrichten zeigen; Senden von Quittungen ist Sache des Menschen (`message.status`) | Di, El, Te (Lesequittungen) | MIMI message-status-Entwurf `-02`; `Read`; Matrix `m.receipt`; Mail DSN / MDN RFC 9007; „zugestellt“ in AS2 ist eine Lücke | proposed |
| Emojis in Text einfügen | Di, El, Ou (Emoji-Picker) | Unicode; eigene Emojis als `attachment` ⚠️ | proposed |
| Eine Person erwähnen und benachrichtigen (`message.mention`) | Di, El (Erwähnung); Ma (Erwähnungs-Benachrichtigungen) | AS2 `tag` vom Typ `Mention`; Matrix-Erwähnungen; MIMI ⚠️ | proposed |
| Präsenz: online, abwesend, beschäftigt, zuletzt gesehen — opt-in (`presence.set`) | Di, El, Te | Matrix `m.presence`; kein AS2/MIMI-Standard → Lücke | proposed |
| Labels / Kategorien mit Farbe (`message.label`) | Ko, Ou, Th (kategorisieren) | JMAP-Schlüsselwörter | proposed |
| Die Liste sortieren und gruppieren (Datum, Absender, Betreff, Unterhaltung) | Th (sortieren, gruppieren); Te (Chat-Sortierung) | Ansichts-Parameter von `conversation.list` | proposed |
| Spam/Junk-Behandlung mit Lernen (`message.junk`) — in Stufe 2 (eigener Mail-Server) nötig | Ou (Clutter), Th (Spam-Filter); Ko, Ou, Th (Junk-Ordner) | JMAP-Schlüsselwörter `$junk` / `$notjunk`; Rolle Junk-Postfach | proposed |
| Senden planen (`message.schedule`) | ⚠️ Ou, Te (nicht in unseren Dateien) | JMAP `EmailSubmission` mit `sendAt` (FUTURERELEASE) ⚠️; Chat: lokal bis zum Zeitpunkt gehalten | proposed |
| Snooze: eine Unterhaltung bis zu einem Zeitpunkt verbergen (`conversation.snooze`) | ⚠️ Ou (nicht in unseren Dateien) | JMAP: kein Standard-Snooze ⚠️ → Anbieter-Schlüsselwort + Datum | proposed |
| Senden innerhalb weniger Sekunden rückgängig machen (`message.send` mit Verzögerung) | ⚠️ (nicht in unseren Dateien) | lokale Verzögerung, bevor das `Create` das Gerät verlässt | proposed |
| Eine unterhaltungsübergreifende Lesezeichnung / Sicherung (`message.bookmark`) | Ma (Lesezeichen); Te (Save-Bot) | eigene Sammlung von Referenzen (AS2 `Collection`) | proposed |
| Verschwindende Nachrichten mit Timer (`message.expire`) | Te (Selbstzerstörung) | MIMI-Ablauf; AS2-Ablauf: Lücke | proposed |
| Signaturen an Mails angehängt | Ko, Ou, Th | Textblock je Konto/Identität; Web-Annotation-Punkt-Anker (ADR 0033) für Variablen ⚠️ | proposed |
| Unterhaltungen oben anheften | El (angeheftete Räume) | Sortier-Präferenz je Konto | proposed |
| Umfragen in einer Unterhaltung (`poll.create`) | El, Te (über Bots) | AS2 `Question` mit `oneOf` / `anyOf` | proposed |
| Broadcast-Kanäle und öffentliche Timelines verfolgen (`channel.follow`) | Te (Kanäle); Ma (Timelines, Hashtags) | ActivityPub `Follow`, AS2 `Collection`; Abgrenzung zu einem sozialen Programm offen ⚠️ | proposed |
| Einen öffentlichen Beitrag teilen / weiterverbreiten (`message.announce`) | Ma | AS2 `Announce` | proposed |
| Inhaltswarnung / sensible Medien (`message.sensitive`) | Ma | AS2 `summary` + `sensitive` ⚠️ (De-facto); unsere sensible Markierung (ADR 0029) | proposed |
| Alt-Text für Bilder (`attachment.describe`) — für Barrierefreiheit empfohlen | Ma | AS2 `name` am Anhang | proposed |
| Den Verlauf einer Unterhaltung leeren (für mich) | Di, El, Te | lokales `Delete` des Bereichs, nicht gesendet | proposed |
| Nachrichten importieren / exportieren (EML, mbox) (`message.export`, `message.import`) | Th (EML); Te (Nachrichten exportieren) | RFC 5322 `.eml`; mbox ⚠️ | proposed |
| Eine Nachricht drucken | Ou, Th | Drucklayout aus den herausgezogenen Feldern | proposed |
| Sprach- und Videoanrufe, Bildschirmfreigabe, Anrufprotokoll (`call.start`) | Di, El, Te | MLS-geschützte Medienschlüssel ⚠️; Matrix-Anrufe (MatrixRTC) ⚠️; Abgrenzung offen (eigenes Programm?) | proposed |
| Sprachnachrichten (aufnehmen, wiedergeben) | ⚠️ Te, El (nicht in unseren Dateien) | `attachment` mit `audio/*` | proposed |
| Von der Gegenseite erzeugte Link-Vorschau, nie vom Leser abgerufen (`message.compose`) | ⚠️ El, Te (nicht in unseren Dateien) | AS2 `Link` / `Page` als Anhang ⚠️ | proposed |
| Bots und Automatisierung über unseren eigenen Vertrag | Di, El, Te (Bots, Webhooks) | Cap'n Proto → JSON / CLI / MCP (ADR 0021) — keine separate Bot-API | proposed |
| Kalendereinladungen vor Ort beantworten (annehmen / ablehnen) | Ko, Ou, Th (Mail + Kalender zusammen) | iMIP / JSCalendar, vom Kalenderprogramm behandelt (ADR 0017), über dessen Widget angezeigt | proposed |
| GIFs, Sticker und Bilder aus **Git-Repositories** suchen und senden (eigene, Community-, kostenlose Angebote) (`media.search`) | Di, El (GIF-Suche als Idee) | Pakete über Git (ADR 0036); keine Tracking-Abfragen | proposed |
| Bridges in andere Netzwerke (Telegram, Discord, WhatsApp, …), auf Nachfrage installierbar (`bridge.install`) | El (Bridges) ⚠️ | Matrix-Bridges, selbst gehostet; mit „not end-to-end" markiert (ADR 0018) | proposed |

## Nicht geplant (bewusst)

| Funktion | Gesehen in | Warum nicht |
|----------|------------|-------------|
| Unverschlüsselt senden (nur-TLS-Chats, Klartext-Mail) | Di, Ma, Te (Standard-Chats), Ko, Ou, Th (optionale Verschlüsselung) | nur verschlüsselt; das Programm fragt nach oder sucht einen verschlüsselten Weg (ADR 0018) |
| Verschlüsselung als eigener, opt-in Chat-Modus | Te (geheime Chats) | Verschlüsselung ist immer an, kein Modus (ADR 0018) |
| Bezahlstufen, die größere Dateien, mehr Konten, mehr Mitglieder freischalten | Di (Nitro), Te (Premium) | dauerhaft frei, keine Armen-Diskriminierung (ADR 0016) |
| Werbung, gesponserte Nachrichten | — | ADR 0016 |
| Tracking-Pixel / Fremdinhalt standardmäßig laden; stille Lesequittungen | (Mail allgemein) | Privatsphäre; Quittungen und Fremdinhalt sind Sache des Menschen |
| Klartext in einer Anbieter-Cloud | Te (Cloud-Speicher) | Inhalt im Ruhezustand verschlüsselt gespeichert (ADR 0024) |
| Gebridgte Chats als Ende-zu-Ende dargestellt | — | Bridges optional, selbst gehostet, sichtbar „nicht Ende-zu-Ende“ (ADR 0018) |
| Abfragen bei Drittanbieter-Diensten während dem Tippen (GIF-/Sticker-Suche) | Di, El (GIF-Dienste) | leakt, was Menschen tippen; nur lokale oder selbst gehostete Pakete ⚠️ |
| Anbietergebundene Büro-/Cloud-Integrationen | Ou (Microsoft 365, Teams, OneDrive, SharePoint, Power Automate) | andere FreeSynergy-Programme teilen stattdessen standardisierte Daten (ADR 0017) |
| Kalender, Kontakte, Aufgaben, Notizen im Messenger eingebaut | Ko, Ou, Th | getrennte Programme; der Messenger leiht sie per lebender Referenz (ADR 0017, 0020) |
| Eigener Login, 2FA, Passwortbehandlung | Di, El, Te | Plattform-Identität (Kanidm), nicht der Messenger |
| Newsgroups (NNTP), RSS/Atom-Lesen | Ko, Th | keine Unterhaltung; gehört in ein Reader-Programm ⚠️ |
| XMPP-, IRC-Konnektoren | — | in `data/messages/standards.md` nicht geplant |

## Fähigkeiten → Vertrag

Kandidaten für Cap'n-Proto-Schnittstellengruppen von `fs-messenger` (ADR 0021) — nur Namen, noch kein Schema.
Zwei Referenz-Frontends (ADR 0022) müssen beide darauf laufen: das Frontend „Mails zeigen und
wegwischen“ nutzt nur die ersten vier; das Outlook-artige Frontend nutzt fast alle.

- `Capabilities` — was dieses Programm anbietet, Vertrags-Versionsbereich (Manifest, ADR 0021)
- `Accounts` — Konten, Konnektoren, Identitäten, Signaturen
- `Conversations` — auflisten, öffnen, ordnen (Ordner/Labels), benachrichtigen, snooze, anheften
- `Messages` — lesen, flaggen, beschriften, als gelesen markieren, reagieren, bearbeiten, löschen, weiterleiten, Status
- `Compose` — Entwürfe, Empfänger, Formatierung, Anhänge, Verschlüsselungs-Vorbedingung, Planung
- `Encryption` — Schlüssel, Geräte, Überprüfung, Vertrauen, Verschlüsselungszustand
- `Attachments` — hochladen, herunterladen, Vorschau, Blobs
- `Search` — Abfragen, gespeicherte Suchen
- `Rules` — Filter (Sieve für Mail, gleiches Modell für Chat)
- `Groups` — Mitglieder, Rollen, Einladungen, Moderation
- `Presence` — eigener Status, Status anderer (opt-in)
- `Events` — Live-Strom der Änderungen für das Frontend (neue Nachricht, gelesen, tippt, Status)
- `Calls` — nur falls Anrufe in diesem Programm bleiben (offen)

Kontakte, Kalendereinladungen und Profil sind **keine** eigenen Gruppen: sie sind von den
Kontakten-, Kalender- und Profilprogrammen geliehen (ADR 0017, 0020).
