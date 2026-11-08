# Messenger — Anforderungen

Was `FreeSynergy.Messenger` muss und kann, abgeleitet aus den [Frontends](frontends/index.md)
(ADR 0006, 0013). Jede Fähigkeit nennt ihren Datenstandard (ADR 0014) und unseren Stand.
Ein Programm deckt E-Mail, Chat und Messenger ab und sendet **nur verschlüsselt** (ADR 0018).

Stand: `implemented` (umgesetzt) · `planned` (geplant) · `proposed` (vorgeschlagen)

**Gesehen in** — analysierte Frontends: [Di](frontends/discord/index.md) Discord ·
[El](frontends/element/index.md) Element · [Ko](frontends/kontact/index.md) Kontact ·
[Ma](frontends/mastodon/index.md) Mastodon · [Ou](frontends/outlook/index.md) Outlook ·
[Te](frontends/telegram/index.md) Telegram · [Th](frontends/thunderbird/index.md) Thunderbird ·
[Ap](frontends/apple-mail/index.md) Apple Mail (iOS 26). Outlook (Ou) auch aus Screenshots, Version `m365-2026-11`.
*arch.* = durch unsere Architektur oder Grundsätze gefordert, nicht durch Zählen.
⚠️ = nicht (oder nicht eindeutig) in unseren Frontend-Dateien; aus den Produkten bekannt, dort zuerst zu prüfen.

**Regel:** Eine Fähigkeit ist *Pflicht*, wenn mindestens vier der sieben Frontends sie zeigen oder
unsere Architektur sie braucht. Die Fähigkeits-ID in Backticks (`<Objekt>.<Aktion>`) ist ein Vorschlag
für die Liste der Fähigkeiten (siehe offener Punkt zum Eintragsformat) — eine Fähigkeit ist eine Aktion am
Objekt, nie ein Menüpunkt oder eine Geste.

Datenverweise: [Nachrichten-Standards](../../../data/messages/standards.md) ·
[Nachrichten-Technik](../../../data/messages/technical.md) (Log-Zuordnung, Verschlüsselungsstatus) ·
[Kontakte](../../../data/people/index.md) · [Identität](../../../data/identity/index.md).

## Pflicht (allen analysierten Programmen gemeinsam)

| Fähigkeit | Gesehen in | Daten / Standard | Stand |
|------------|---------|-----------------|--------|
| Mehrere Konten in einem Programm verwalten — Mail, Matrix, MIMI (`account.add`, `account.remove`, `account.edit`) | Ko, Ou, Th, Te; *arch.* (ein Programm, ADR 0018) | Konnektoren: JMAP RFC 8620/8621, IMAP, SMTP, Matrix v1.19, MIMI-Protokoll `-07` | proposed |
| Unterhaltungen aller Konten auflisten, neueste zuerst (`conversation.list`) | Di, El, Ko, Ma, Ou, Te, Th | AS2 `context` = Unterhaltung; JMAP `threadId`; Matrix-Raum; MIMI-Raum | proposed |
| Unterhaltungen ordnen: Ordner, Kategorien, angeheftet (`conversation.move`, `mailbox.create`) | Ko, Ou, Th (Ordner, Verschieben/Kopieren); Di (Kanal-Kategorien); El (angeheftete Räume); Te (Sortierung) | JMAP `Mailbox` + `mailboxIds`; Chat-Ordner: Lücke → eigenes Profil | proposed |
| Eine Unterhaltung öffnen und ihre Nachrichten lesen, flach (Chat) oder als Baum (Mail) (`conversation.open`, `message.open`) | Di, El, Ko, Ma, Ou, Te, Th | AS2 `Note`, `context`, `inReplyTo`; Original bleibt erhalten (MIME / MIMI-CBOR / Matrix-Ereignis) | proposed |
| Eine Nachricht an eine Person oder eine Gruppe senden (`message.send`) | Di, El, Ko, Ma, Ou, Te, Th | `Create`; MIMI-Inhalt `-10`; MIME RFC 5322 über SMTP/JMAP-Einreichung; Matrix `m.room.message` | proposed |
| Nur verschlüsselt senden; einen verschlüsselten Weg finden (Schlüssel, Gegenstelle) und erklären, wenn keiner existiert (`message.send`-Voraussetzung, `key.discover`) | El (Standard-E2EE), Te (geheime Chats), Ko, Ou, Th (OpenPGP/S/MIME); *arch.* ADR 0018 | MLS RFC 9420; OpenPGP RFC 9580 + Header Protection RFC 9788; Autocrypt (v2-Entwurf) | proposed |
| Den Verschlüsselungsstatus jeder Nachricht zeigen; unverschlüsselte eingehende kennzeichnen, mit Link zum Bibliotheks-Leitfaden (`message.encryption`) | El, Te (Sicherheitshinweise); *arch.* ADR 0018/0031 | `freesynergy.net:encryption` = `mls` · `openpgp` · `megolm` · `transport-only` · `none` | proposed |
| Eine KI nur in eine Unterhaltung lassen, wenn alle vorher zustimmen; wer später beitritt, akzeptiert sie ebenfalls oder bleibt fern; zieht jemand zurück, geht sie; keine Ausnahme, auch nicht für eine lokale KI; keine Historie von vor ihrem Eintritt (`participant.consent`) | *arch.* ADR 0054 | Markierter Teilnehmer (JSContact `kind` `application`); MLS Add; Matrix: keine `shared_history`-Schlüssel für eine KI | proposed |
| Signaturen, Schlüssel und Geräte prüfen; dem Schlüssel eines Kontakts vertrauen (`key.verify`, `device.list`) | Ko, Th (GPG-Signatur prüfen); El, Te (Geräteverwaltung) | OpenPGP RFC 9580; MLS-Credentials; Web of Trust ([Identität](../../../data/identity/index.md)) | proposed |
| Auf eine Nachricht antworten — an den Absender oder an alle (`message.reply`) | Di, El, Ko, Ou, Te, Th; Ma (Antwort ⚠️) | `Create` mit `inReplyTo`; Kopfzeile `In-Reply-To`; Matrix `m.in_reply_to`; MIMI-Antwort | proposed |
| Eine Nachricht weiterleiten (`message.forward`) | Di, El, Ko, Ou, Te, Th | neues `Create`, Original als `attachment` (E-Mail: `message/rfc822`) ⚠️ kein MIMI-Weiterleitungstyp | proposed |
| Einen Teil einer Nachricht zitieren (`message.quote`) | Di, El, Ma, Te; Ko, Th (als Zitat einfügen) | W3C Web Annotation `TextQuoteSelector` auf der Quelle (ADR 0033); bei Mail zusätzlich zitierter Text | proposed |
| Eine gesendete Nachricht bearbeiten; die ID der ersten Version bleibt (`message.edit`) | Di, El, Ma, Te | `Update`; MIMI-Bearbeitung; Matrix `m.replace`; E-Mail: Lücke | proposed |
| Eine Nachricht löschen — für mich oder für alle, wo der Weg es erlaubt (`message.delete`) | Di, El, Ko, Ma, Ou, Te, Th | `Delete` + Grabstein; MIMI leerer Inhalt; Matrix-Schwärzung; JMAP in den Papierkorb verschieben / löschen | proposed |
| Eine Nachricht für später markieren ⚠️ „Markieren“ in den Menüs ist mehrdeutig (Markierung vs. Auswahl) (`message.flag`) | Di, El, Ko, Ou, Te, Th ⚠️ | JMAP-Schlüsselwort `$flagged`; Chat: Lücke → eigenes Herstellerschlüsselwort | proposed |
| Als gelesen / ungelesen markieren; zur nächsten ungelesenen springen (`message.read`, `conversation.markRead`) | Te (Chat als gelesen markieren); El, Ma (nächste ungelesene); Ko, Ou, Th (markieren) | `Read`-Aktivität; JMAP `$seen`; Matrix `m.receipt`; MIMI-Nachrichtenstatus; gesammeltes „gelesen bis X“ ist eine Lücke | proposed |
| Nachrichten durchsuchen — in einer Unterhaltung und über alle Konten, Volltext (`message.search`) | Di, El, Ko, Ou, Te, Th; Ma (Hashtags) | Volltext über extrahierte Felder (technical.md); JMAP-Filtermodell `Email/query` | proposed |
| Anhänge senden, vorschauen und speichern (Drag & Drop ist ein Weg im Frontend) (`attachment.add`, `attachment.save`) | Di, El, Ma, Te; Ko, Th (Anhänge speichern); Ou | AS2 `attachment`; JMAP-Blobs RFC 9404; MIMI verschlüsselte externe Teile; Beschreibung verschlüsselter Anhänge in AS2: Lücke | proposed |
| Medien direkt anzeigen (Bilder, Video, Dokumente) (`attachment.preview`) | Di, El, Ma, Te | `mediaType` des Anhangs; Vorschaubilder lokal erzeugt | proposed |
| Text beim Verfassen formatieren (fett, kursiv, Code, Zitat, Listen, Links) (`message.compose` mit Format) | El, Ma (Markdown); Ko, Ou, Th (Formatleiste) | E-Mail: `multipart/alternative` text/plain + text/html; Chat: MIMI-Teil `text/markdown` ⚠️ | proposed |
| Entwürfe automatisch sichern und wieder aufnehmen (`draft.save`, `draft.list`) | Di, El, Ko, Ma, Ou, Te, Th (automatisches Speichern) | JMAP-Schlüsselwort `$draft` + Entwürfe-Ordner; Chat-Entwürfe: nur lokal (Lücke) | proposed |
| Benachrichtigungen je Unterhaltung — alle, nur Erwähnungen, stumm (`conversation.notify`) | Di, El, Te (Kanal-/Raum-Benachrichtigungen); Ma (Benachrichtigungsarten); Ko, Th (Systembenachrichtigungen) | Programmeinstellung; Matrix-Push-Regeln werden darauf abgebildet; kein gemeinsamer Standard ⚠️ | proposed |
| Gruppen-Unterhaltungen: anlegen, benennen, beschreiben, einladen, verlassen (`group.create`, `group.invite`, `group.leave`) | Di, El, Te; Ko, Ou, Th (Kontaktgruppen / Verteilerlisten) | MLS-Gruppenmitgliedschaft (Add/Remove); MIMI-Raumrichtlinie `-04`; AS2 `Invite`, `Join`, `Leave`; JSContact `kind: group` | proposed |
| Rollen und Rechte innerhalb einer Gruppe (`group.role`) | Di, El, Te; Ma (Moderatoren) | MIMI-Raumrichtlinie `-04`; Matrix-Berechtigungsstufen | proposed |
| Moderieren: entfernen, sperren, blockieren, melden (`member.remove`, `actor.block`, `message.report`) | Di, El, Ma, Te | AS2 `Remove`, `Block`, `Flag` | proposed |
| Kontakte nutzen: Empfänger aus dem Adressbuch wählen, die Karte eines Absenders öffnen (`contact.lookup` — geliehen, ADR 0020) | Ko, Ou, Th (Adressbuch); Di, El, Ma, Te (Profil öffnen) | JSContact RFC 9553 ([Kontakte](../../../data/people/index.md)), Live-Verweis in das Kontakte-Programm | proposed |
| Das eigene Profil bearbeiten: Name, Bild, Kurztext (`profile.edit`) | Di, El, Ma, Te | AS2-Akteur; JSContact für die eigene Karte; [Profil](../../../data/profile/index.md) | proposed |
| Regeln und Filter: automatisch sortieren, kennzeichnen, verschieben, stummschalten (`rule.create`, `rule.run`) | Ko, Ou, Th (Filterregeln); Ma (Wort-/Nutzerfilter); Di (AutoMod) | Sieve über JMAP RFC 9661 für Mail; dasselbe Regelmodell für Chat ⚠️ (Lücke) | proposed |
| Offline arbeiten und über Geräte hinweg synchron bleiben (`sync`) | Ko, Th (Offline-Modus); El (Synchronisierung); Te (Cloud) | `fs-store` + `fs-hub`, Synchronisierung auf Objektebene (ADR 0019); lokal, im Ruhezustand verschlüsselt (ADR 0024) | proposed |
| Entfernte Inhalte und Tracking-Bilder nicht laden, außer die Person bittet darum (Standard von `message.open`) | Th (Tracking-Schutz); *arch.* (Datenschutz) | Regel in unserem Renderer; MIME-`cid:`-Teile erlaubt, entfernte URLs standardmäßig blockiert | proposed |

## Optional (bemerkenswerte Ideen)

| Fähigkeit | Gesehen in | Daten / Standard | Stand |
|------------|---------|-----------------|--------|
| Mit einem Emoji auf eine Nachricht reagieren (`message.react`) — wahrscheinlich Pflicht, sobald geprüft | ⚠️ Di, El, Te, Ma (nicht in unseren Dateien) | `Like` / FEP-c0e0 `EmojiReact`, Rücknahme über `Undo`; MIMI-Reaktion; Matrix `m.annotation`; E-Mail: Lücke | proposed |
| Threads: im Nebenstrang antworten, ohne die Hauptunterhaltung zu fluten (`thread.open`) | ⚠️ Di, El (nicht in unseren Dateien); Th (gruppierte Ansicht) | AS2 `context` / `inReplyTo`; Matrix `m.thread`; MIMI-Thema; Thread-Profil ist eine Lücke (FEPs konkurrieren) | proposed |
| Zugestellt- und Gelesen-Status gesendeter Nachrichten zeigen; Lesebestätigungen senden ist die Wahl der Person (`message.status`) | Di, El, Te (Lesebestätigungen) | MIMI-Nachrichtenstatus-Entwurf `-02`; `Read`; Matrix `m.receipt`; E-Mail DSN / MDN RFC 9007; „zugestellt“ in AS2 ist eine Lücke | proposed |
| Emoji in den Text einfügen | Di, El, Ou (Emoji-Auswahl) | Unicode; eigene Emojis als `attachment` ⚠️ | proposed |
| Eine Person erwähnen und benachrichtigen (`message.mention`) | Di, El (Erwähnung); Ma (Erwähnungsbenachrichtigungen) | AS2 `tag` vom Typ `Mention`; Matrix-Erwähnungen; MIMI ⚠️ | proposed |
| Anwesenheit: online, abwesend, beschäftigt, zuletzt gesehen — nur auf Wunsch (`presence.set`) | Di, El, Te | Matrix `m.presence`; kein AS2-/MIMI-Standard → Lücke | proposed |
| Markierungen / Kategorien mit Farbe (`message.label`) | Ko, Ou, Th (kategorisieren) | JMAP-Schlüsselwörter | proposed |
| Die Liste sortieren und gruppieren (Datum, Absender, Betreff, Unterhaltung) | Th (sortieren, gruppieren); Te (Chat-Sortierung) | Ansichtsparameter von `conversation.list` | proposed |
| Spam- und Junk-Behandlung mit Lernen (`message.junk`) — bei Stufe 2 Pflicht (eigener Mailserver) | Ou (Clutter), Th (Spamfilter); Ko, Ou, Th (Junk-Ordner) | JMAP-Schlüsselwörter `$junk` / `$notjunk`; Junk-Ordnerrolle | proposed |
| Senden planen (`message.schedule`) | ⚠️ Ou, Te (nicht in unseren Dateien) | JMAP `EmailSubmission` mit `sendAt` (FUTURERELEASE) ⚠️; Chat: lokal bis zur Fälligkeit zurückgehalten | proposed |
| Schlummern: eine Unterhaltung bis zu einer Zeit ausblenden (`conversation.snooze`) | ⚠️ Ou (nicht in unseren Dateien) | JMAP: kein Standard für Schlummern ⚠️ → Herstellerschlüsselwort + Datum | proposed |
| Senden innerhalb weniger Sekunden rückgängig machen (`message.send` mit Verzögerung) | ⚠️ (nicht in unseren Dateien) | lokale Verzögerung, bevor `Create` das Gerät verlässt | proposed |
| Nachricht über Unterhaltungen hinweg merken / speichern (`message.bookmark`) | Ma (Lesezeichen); Te (Speicher-Bot) | eigene Sammlung von Verweisen (AS2 `Collection`) | proposed |
| Verschwindende Nachrichten mit Timer (`message.expire`) | Te (Selbstzerstörung) | MIMI-Ablauf; AS2-Ablauf: Lücke | proposed |
| Signaturen an Mails anhängen | Ko, Ou, Th | Textblock je Konto/Identität; Web-Annotation-Punktanker (ADR 0033) für Variablen ⚠️ | proposed |
| Unterhaltungen oben anheften | El (angeheftete Räume) | Sortierung je Konto als Einstellung | proposed |
| Umfragen in einer Unterhaltung (`poll.create`) | El, Te (über Bots) | AS2 `Question` mit `oneOf` / `anyOf` | proposed |
| Broadcast-Kanäle und öffentliche Zeitleisten folgen (`channel.follow`) | Te (Kanäle); Ma (Zeitleisten, Hashtags) | ActivityPub `Follow`, AS2 `Collection`; Umfang mit einem offenen Social-Programm ⚠️ | proposed |
| Einen öffentlichen Beitrag teilen / weiterverbreiten (`message.announce`) | Ma | AS2 `Announce` | proposed |
| Inhaltswarnung / sensible Medien (`message.sensitive`) | Ma | AS2 `summary` + `sensitive` ⚠️ (de facto); unsere Kennzeichnung sensibler Inhalte (ADR 0029) | proposed |
| Alternativtext für Bilder (`attachment.describe`) — für Barrierefreiheit empfohlen | Ma | AS2 `name` am Anhang | proposed |
| Den Verlauf einer Unterhaltung leeren (für mich) | Di, El, Te | lokales `Delete` des Bereichs, nicht gesendet | proposed |
| Nachrichten importieren / exportieren (EML, mbox) (`message.export`, `message.import`) | Th (EML); Te (Nachrichten exportieren) | RFC 5322 `.eml`; mbox ⚠️ | proposed |
| Eine Nachricht drucken | Ou, Th | Drucklayout aus den extrahierten Feldern | proposed |
| Sprach- und Videoanrufe, Bildschirmfreigabe, Anrufverlauf (`call.start`) | Di, El, Te | MLS-geschützte Medienschlüssel ⚠️; Matrix-Anrufe (MatrixRTC) ⚠️; Umfang offen (eigenes Programm?) | proposed |
| Sprachnachrichten (aufnehmen, abspielen) | ⚠️ Te, El (nicht in unseren Dateien) | `attachment` mit `audio/*` | proposed |
| Linkvorschau vom Absender erzeugt, nie vom Leser abgerufen (`message.compose`) | ⚠️ El, Te (nicht in unseren Dateien) | AS2 `Link` / `Page` als Anhang ⚠️ | proposed |
| Bots und Automatisierung über unseren eigenen Vertrag | Di, El, Te (Bots, Webhooks) | Cap'n Proto → JSON / CLI / MCP (ADR 0021) — keine eigene Bot-API | proposed |
| Kalendereinladungen direkt beantworten (annehmen / ablehnen) | Ko, Ou, Th (Mail und Kalender zusammen) | iMIP / JSCalendar, vom Kalenderprogramm verarbeitet (ADR 0017) und über dessen Widget gezeigt | proposed |
| GIFs, Sticker, Bilder aus **Git-Repositories** suchen und senden (eigene, Community-, freie Angebote) (`media.search`) | Di, El (GIF-Suche als Idee) | Pakete über Git (ADR 0036); keine Tracking-Abfragen | proposed |
| Brücken zu anderen Netzen (Telegram, Discord, WhatsApp, …), bei Bedarf installierbar (`bridge.install`) | El (Brücken) ⚠️ | Matrix-Brücken, selbst gehostet; als „nicht Ende-zu-Ende“ gekennzeichnet (ADR 0018) | proposed |
| Gespeicherte Ansichten / intelligente Postfächer: eine gespeicherte Suche, die wie ein Ordner erscheint (`view.save`) | Ou (Suchordner), Ap (intelligente Postfächer) | gespeicherte Abfrage über die Briefumschlag-Felder; JMAP-Filter `Email/query` als Vorbild | proposed |
| Automatische Kategorien / fokussierter Posteingang mit Erklärung (`message.classify`) | Ou (Fokussiert/Andere), Ap (Kategorien) | nur lokale Klassifizierung (keine Cloud), Ergebnis als JMAP-Schlüsselwort / Herstellereigenschaft | proposed |
| Wiedervorlage-Erinnerung zu einer Nachricht (`message.followup`) | Ou, Ap | JSCalendar `Task`, verknüpft über `relatedTo` | proposed |
| Eine Unterhaltung anheften (`conversation.pin`) | Ou | JMAP-Schlüsselwort | proposed |
| Eine gesendete Nachricht zurückholen (`message.recall`) | Ou | nur wo beide Seiten unsere sind / MIMI-Löschung; Mail: nach bestem Bemühen ⚠️ | proposed |
| VIP-Absender (`contact.vip`) | Ap | Kontakte: JSContact-Herstellereigenschaft `freesynergy.net:vip` | proposed |
| Privatsphäre beim Öffnen von Mails schützen: entfernte Inhalte über Proxy, IP verbergen (`privacy.proxy`) | Ap (Mail-Aktivität schützen) | passt zu ADR 0018/0029; Hub als Proxy | proposed |
| Vor Empfängern außerhalb einer vertrauten Gruppe warnen (`recipient.warn`) | Ap (Adressen markieren) | Kontakte + Vertrauen (Web of Trust) | proposed |
| Mit einem Klick von Mailinglisten abmelden (`list.unsubscribe`) | Ap | RFC 2369 `List-Unsubscribe`, RFC 8058 Ein-Klick ⚠️ prüfen | proposed |
| Automatische Antworten / Abwesenheitsnotiz (`autoreply.set`) | Ou | Sieve-Urlaubsnotiz (RFC 5230) ⚠️ prüfen | proposed |
| Eine Unterhaltung stummschalten / ignorieren (`conversation.ignore`) | Ou (ignorieren), Ap (stummschalten) | JMAP-Schlüsselwort | proposed |
| Nachrichtenpriorität / Wichtigkeit (`message.priority`) | Ou | MIME-Kopfzeile `Importance`; Chat: Herstellereigenschaft | proposed |
| Absendealiasse je Konto (`account.alias`) | Ap | JMAP `Identity` | proposed |
| Offline: wählen, welche Ordner und wie viele Tage bleiben (`sync.scope`) | Ou | Synchronisierungsregel von `fs-store` (ADR 0019) | proposed |
| Eine lange Nachricht zusammenfassen (`message.summarize`) | Ou | **nur lokales Modell** (keine Cloud, ADR 0029) ⚠️ | proposed |

## Angenommene Ideen (Projektinhaber, 2026-11-08), Schritt für Schritt umzusetzen

Alle diese Ideen sind gewollt und werden eingebaut; noch keine ist terminiert. Die Reihenfolge wird in der Planung nach dem Sprint festgelegt.

| # | Idee | Baut auf | Stand |
|---|------|-----------|--------|
| 1 | Abkühlphase: Bevor eine hitzige Nachricht gesendet wird, anbieten „jetzt senden oder in 10 Minuten“; zurückholen, solange sie ungelesen ist | Kern | accepted |
| 2 | Senden, wenn die andere Person wach ist (ihre Zeitzone und Ruhezeiten) | Personen, Kalender | accepted |
| 3 | Ruhige Benachrichtigungen: Zusammenfassungen, nur von Menschen, die ich kenne, Ruhezeiten | Hub `subscribe` | accepted |
| 4 | Lesebestätigungen nur auf Gegenseitigkeit: Wer sie sehen will, muss sie selbst zeigen | Kern | accepted |
| 5 | Eine Nachricht mit einer Aktion zu einer Aufgabe, einem Termin oder einer Wiki-Seite machen | Aufgaben, Kalender, Texte (`jobRef` existiert) | accepted |
| 6 | Umfragen innerhalb einer Unterhaltung | Umfragen | accepted |
| 7 | Eine Unterhaltung, mehrere Kanäle: Ein Strang kann von Mail zu Matrix wechseln und bleibt ein Strang | Kern, Anbieter | accepted |
| 8 | Ohne Netz: Bluetooth und lokales WLAN, für Treffen und Notfälle | ADR 0059 | accepted |
| 9 | Verschlüsselung erklären: sagen, warum eine Nachricht nicht verschlüsselt ist und wie sich das ändern lässt | Kern, Manifest | accepted |
| 10 | Alles mitnehmen: jede Unterhaltung in einem offenen Format exportieren | Kern (ADR 0046) | accepted |
| 11 | Gruppenmoderation: Langsam-Modus, Moderation durch Abstimmung, ein offenes Moderationsprotokoll | Gruppen, Umfragen, Verlauf | accepted |
| 12 | Ankündigungskanal, eins zu viele (Kandidat für den Transport: Nostr) | Anbieter | accepted |
| 13 | Sprachnachrichten mit Transkript, auf dem Gerät erstellt | Dateien | accepted |
| 14 | Übersetzung auf dem Gerät, ohne dass ein externer Dienst mitliest | ADR 0057 | accepted |
| 15 | Eine lange Unterhaltung mit einer KI zusammenfassen, nur wenn alle zugestimmt haben (ADR 0054) | KI-Teilnehmer | accepted |

Weitere zu prüfende Anbieter: Nostr (öffentliche Beiträge, Ausweichweg für Direktnachrichten), I2P als Anonymitätstransport (ADR 0059). I2P-Bote ist nicht geplant.

## KIs als Teilnehmer (vorläufig, ADR 0054)

Aus dem Vertragsentwurf 0.2, der noch in Prüfung ist. Siehe den [Assistenten](../assistant/index.md).

| Fähigkeit | Was sie tut |
|------------|--------------|
| `toolcall.show` | Zeigt, was eine KI tun will oder getan hat |
| `toolcall.decide` | Eine Person erlaubt oder verweigert einen Tool-Aufruf, nur auf ihrem eigenen Gerät |
| `turn.stop` | Stoppt, was eine KI gerade tut |
| `conversation.usage` | Zeigt, was eine Unterhaltung verbraucht und gekostet hat |
| `text.stream` | Zeigt eine Antwort, während sie geschrieben wird |

**`toolcall.decide` wird einer KI nie angeboten.** Es wird nie als MCP-Werkzeug erzeugt, weil eine KI sonst ihre eigenen Aktionen freigeben könnte.

## Nicht geplant (bewusst)

| Funktion | Gesehen in | Warum nicht |
|---------|---------|-----------------|
| Unverschlüsselt senden (nur TLS-Chats, Klartext-Mail) | Di, Ma, Te (Standardchats), Ko, Ou, Th (optionale Verschlüsselung) | nur verschlüsselt; das Programm verlangt einen verschlüsselten Weg oder sucht ihn (ADR 0018) |
| Verschlüsselung als eigener, optionaler Chat-Modus | Te (geheime Chats) | Verschlüsselung ist immer an, kein Modus (ADR 0018) |
| Bezahlstufen, die größere Dateien, mehr Konten, mehr Mitglieder freischalten | Di (Nitro), Te (Premium) | dauerhaft kostenlos, keine Benachteiligung armer Menschen (ADR 0016) |
| Werbung, gesponserte Nachrichten | — | ADR 0016 |
| Tracking-Pixel / entfernte Inhalte standardmäßig laden; stille Lesebestätigungen | (Mail allgemein) | Datenschutz; Bestätigungen und entfernte Inhalte sind die Wahl der Person |
| Klartext in einer Cloud des Anbieters | Te (Cloud-Speicher) | Inhalt im Ruhezustand verschlüsselt gespeichert (ADR 0024) |
| Brücken-Chats, die als Ende-zu-Ende dargestellt werden | — | Brücken sind optional, selbst gehostet und sichtbar „nicht Ende-zu-Ende“ (ADR 0018) |
| Abfragen bei **Tracking**-Diensten Dritter während des Tippens | Di, El (GIF-Dienste) | verrät, was Menschen tippen → stattdessen GIF-/Sticker-Suche über Git-Repositories (siehe Optional, ADR 0036) |
| An einen Anbieter gebundene Büro- oder Cloud-Anbindungen | Ou (Microsoft 365, Teams, OneDrive, SharePoint, Power Automate) | andere FreeSynergy-Programme teilen stattdessen Standarddaten (ADR 0017) |
| Kalender, Kontakte, Aufgaben, Notizen im Messenger eingebaut | Ko, Ou, Th | eigene Programme; der Messenger leiht sie sich per Live-Verweis (ADR 0017, 0020) |
| Eigene Anmeldung, 2FA, Passwortverwaltung | Di, El, Te | Plattform-Identität (Kanidm), nicht der Messenger |
| Newsgroups (NNTP), RSS/Atom-Lesen | Ko, Th | keine Unterhaltung; gehört zu einem Leseprogramm ⚠️ |
| XMPP-, IRC-Konnektoren | — | nicht geplant in `data/messages/standards.md` |

## Fähigkeiten → Vertrag

Mögliche Cap'n-Proto-Schnittstellengruppen für `fs-messenger` (ADR 0021) — nur Namen, noch kein Schema.
Zwei Referenz-Frontends (ADR 0022) müssen beide darauf laufen: Das Frontend „Mails zeigen und wegwischen“
nutzt nur die ersten vier; das Outlook-artige Frontend fast alle.

- `Capabilities` — was dieses Programm anbietet, Vertragsversionsbereich (Manifest, ADR 0021)
- `Accounts` — Konten, Konnektoren, Identitäten, Signaturen
- `Conversations` — auflisten, öffnen, ordnen (Ordner/Labels), benachrichtigen, schlummern, anheften
- `Messages` — lesen, markieren, kennzeichnen, als gelesen markieren, reagieren, bearbeiten, löschen, weiterleiten, Status
- `Compose` — Entwürfe, Empfänger, Formatierung, Anhänge, Verschlüsselungsvoraussetzung, Planung
- `Encryption` — Schlüssel, Geräte, Prüfung, Vertrauen, Verschlüsselungsstatus
- `Attachments` — hochladen, herunterladen, Vorschau, Blobs
- `Search` — Abfragen, gespeicherte Suchen
- `Rules` — Filter (Sieve für Mail, gleiches Modell für Chat)
- `Groups` — Mitglieder, Rollen, Einladungen, Moderation
- `Presence` — eigener Status, Status anderer (nur auf Wunsch)
- `Events` — Live-Strom der Änderungen für das Frontend (neue Nachricht, gelesen, Tippen, Status)
- `Calls` — nur, wenn Anrufe in diesem Programm bleiben (offen)

Kontakte, Kalendereinladungen und Profil sind **keine** eigenen Gruppen: Sie werden aus den Programmen
Kontakte, Kalender und Profil geliehen (ADR 0017, 0020).
