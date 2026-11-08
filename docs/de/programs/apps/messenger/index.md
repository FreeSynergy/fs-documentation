# Messenger und Instant Messaging

## Kurz gesagt

FreeSynergy Messenger ist ein Ort für E-Mail, Chat und KI-Agenten. Es behandelt eine Nachricht als Nachricht, egal, welches Netz sie gebracht hat. Du liest, antwortest, suchst und sortierst an einem Ort, und Konnektoren übernehmen die Kommunikation mit der Außenwelt. Eine Nachricht wird nur gesendet, wenn sie verschlüsselt gesendet werden kann.

**Befehl:** `fs-messenger`, ein Befehl je Programm mit Unterbefehlen ([ADR 0063](../../../decisions/0063-ein-programm-ein-befehl.md); Programme werden umgestellt, wenn sie ohnehin angefasst werden, deshalb ist noch nicht jedes so weit).

## Was hier anders ist

- Nur verschlüsselt: Gibt es keinen Weg, eine Nachricht an alle Empfänger zu verschlüsseln, wird sie nicht gesendet, und es gibt kein Überschreiben.
- Eingehende Nachrichten sind mit dem gekennzeichnet, was der Konnektor wirklich weiß. Was nicht Ende-zu-Ende nachgewiesen ist, wird nie als sicher angezeigt.
- Das Original jeder E-Mail wird Byte für Byte aufbewahrt.
- KI-Agenten sind Teilnehmer, keine versteckten Mithörer. Jeder ist gekennzeichnet, keiner handelt ohne deine Freigabe, und ein Not-Stopp hat immer Vorrang.
- Messenger besitzt seine eigene offene Schnittstelle; E-Mail, Chat und Agenten sind Konnektoren unter einem Programm.

## Wo es heute steht

Neueste Version: `v0.0.1`. Heute ist es der Kern, ohne Fenster. Es hat ein Nachrichtenmodell für E-Mail, Chat und Agenten, mit Unterhaltungen, einer Seitenaufteilung, die beim Eintreffen neuer Mails nicht springt, ungelesen-Markierungen, Entwürfen, Suche, Anheften, Verschieben, Markieren und Weiterleiten. Das Senden nur verschlüsselt verweigert klar und nennt die Empfänger, die nicht erreichbar sind. Nachrichten werden mit ihrem Original gespeichert. Ein E-Mail-Konnektor holt über IMAP oder JMAP ab und sendet über SMTP oder JMAP, mit OpenPGP und Autocrypt; getestet wird nur gegen einen lokalen Stalwart-Testserver. Eine KI-Wache gibt jeder KI eine Einladung, eine Freigabe je Art von Aktion, Rückfragen bei riskanten Schritten, hält Geheimnisse von KIs fern und hat einen Not-Stopp.

Noch nicht da (geplant): ein Fenster, ein Server, Chat-Konnektoren (Matrix und andere) und Telegram. Nachrichten bleiben bewusst auf dem Gerät, auf dem sie angekommen sind, bis der Schlüsseltresor existiert, und Konto-Passwörter können noch nicht gespeichert werden. Nachrichten bearbeiten und darauf reagieren, geplantes Senden, E-Mail-Regeln, HTML-Inhalte, Schlüsselsuche, STARTTLS und S/MIME antworten mit „nicht möglich“. Die Regel, dass alle Mitglieder zustimmen müssen, bevor eine KI einer Unterhaltung beitritt, ist nicht gebaut, und die Regeln der Wache sind vorläufig. Die Schnittstelle ist ein Entwurf ohne Anbindung.

## Geplante Facetten

Facetten sind Teile eines Programms, die wie eigene Apps wirken ([ADR 0061](../../../decisions/0061-facetten.md)). Jede bekommt einen eigenen Befehl, eine Verbindung zu `fs-messenger` ([ADR 0063](../../../decisions/0063-ein-programm-ein-befehl.md)).

Facetten sind Teile eines Programms, die wie eigene Apps wirken (siehe [Programme](../../index.md)). Vorgeschlagen für `fs-messenger`:

- E-Mail (vorgeschlagen)
- Chat (vorgeschlagen)
- Forum, möglicherweise (vorgeschlagen)

## Überblick

Dieser Bereich enthält Dokumentation zu verschiedenen Messengern und Kommunikationsplattformen.

## Verfügbare Systeme

- **outlook** - E-Mail und Zusammenarbeit von Microsoft
- **kontact** - Persönlicher Informationsmanager von KDE
- **thunderbird** - E-Mail-Programm von Mozilla
- **element** - Sicherer Messenger auf Matrix-Basis
- **discord** - Sprach-, Video- und Textchat
- **mastodon** - Dezentrales soziales Netzwerk
- **telegram** - Cloud-Messenger mit Bots
- **signal** - Privater Nachrichtendienst mit Ende-zu-Ende-Verschlüsselung
- **whatsapp-web** - Web-Oberfläche von WhatsApp
- **jabber/xmpp** - Offenes Protokoll für Sofortnachrichten
- **skype** - Kommunikationsplattform von Microsoft
- **rocketchat** - Quelloffener Team-Chat
- **mattermost** - Quelloffene Alternative zu Slack

## Was ist ein Messenger?

Ein Messenger (Sofortnachrichten-Dienst) ist Software für Kommunikation in Echtzeit über das Internet. Messenger ermöglichen:

- Austausch von Textnachrichten
- Sprach- und Videoanrufe
- Dateiübertragungen
- Gruppenchats und Kanäle
- Bot-Anbindungen
- Ende-zu-Ende-Verschlüsselung

## Anwendungsbereiche

- **Teamkommunikation**: Tägliche Kommunikation im Team
- **Kundensupport**: Kundenbetreuung per Messenger
- **Community**: Diskussionen und Foren in der Gemeinschaft
- **Soziale Netzwerke**: Microblogging und soziale Netzwerke
- **Zusammenarbeit**: Zusammenarbeit mit Dateiaustausch

## Sicherheit und Datenschutz

Achte bei Messengern auf folgende Sicherheitsaspekte:

- **Verschlüsselung**: Ende-zu-Ende-Verschlüsselung für sichere Kommunikation
- **Serverstandort**: Welches Recht gilt?
- **Datenschutz**: Wie werden Daten gespeichert und verarbeitet?
- **Open Source**: Ist der Quellcode überprüfbar?
- **Dezentralisierung**: Ist das System dezentral?

## Auswahlkriterien

Bei der Wahl eines Messengers solltest du folgende Kriterien berücksichtigen:

- **Funktionen**: Welche Funktionen werden gebraucht?
- **Sicherheit**: Verschlüsselung und Datenschutz
- **Plattformen**: Auf welchen Betriebssystemen läuft das System?
- **Skalierbarkeit**: Wie viele Nutzer und Gruppen?
- **Integration**: Wie gut passt das System in die bestehende Infrastruktur?
- **Kosten**: Kostenlos oder kostenpflichtig?

## Verwandte Kategorien

- [Wiki](../wiki/) - Wissensmanagement und Dokumentation
- [Helpdesk](../helpdesk/) - Support- und Ticketsysteme
- [Desktop](../../platform/desktop/) - Desktop-Anwendungen für Kommunikation

## Schnellstart

1. **Messenger auswählen**: Wähle einen Messenger anhand der Anforderungen
2. **Installation**: App herunterladen und installieren
3. **Konto anlegen**: Ein Benutzerkonto erstellen
4. **Kontakte hinzufügen**: Teammitglieder und Kontakte einladen
5. **Gruppen anlegen**: Chats und Kanäle für Teams einrichten

## Weitere Informationen

Weitere Informationen findest du in der Dokumentation der einzelnen Messenger-Systeme.

## Frontends

<!-- gen:frontends (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
Analysierte Programme (9), nach Funktion, nichts kopiert (ADR 0012/0013):

- [Apple Mail](frontends/apple-mail/index.md) — Apple Mail ist das E-Mail-Programm, das auf jedem iPhone, iPad und Mac installiert ist.
- [Discord](frontends/discord/index.md) — Discord ist eine proprietäre Kommunikationsplattform für Gaming-Communities, mit Sprach-/Video-Chat und einer Serverstruktur.
- [Element](frontends/element/index.md) — Element ist der quelloffene Messenger für das Matrix-Protokoll, mit dezentraler Architektur und Ende-zu-Ende-Verschlüsselung.
- [FreeSynergy Simple](frontends/freesynergy-simple/index.md) — Unser eigenes, bewusst schlankes Messenger-Frontend.
- [Kontact](frontends/kontact/index.md) — Kontact ist die integrierte PIM-Anwendung für KDE, die E-Mail, Kalender, Kontakte, Aufgaben und Notizen in einer Anwendung vereint.
- [Mastodon](frontends/mastodon/index.md) — Mastodon ist ein quelloffenes Microblogging-Netzwerk auf Basis des ActivityPub-Protokolls und dezentral organisiert.
- [Outlook](frontends/outlook/index.md) — Outlook ist der beliebteste E-Mail-Client von Microsoft und Teil von Microsoft 365.
- [Telegram](frontends/telegram/index.md) — Telegram ist ein Cloud-Messenger, der auf Geschwindigkeit, große Gruppen/Kanäle und Verschlüsselung setzt.
- [Thunderbird](frontends/thunderbird/index.md) — Thunderbird ist der quelloffene E-Mail-Client von Mozilla, plattformübergreifend und auf E-Mail ausgerichtet.

Übersicht: [frontends](frontends/index.md)
<!-- /gen:frontends -->
