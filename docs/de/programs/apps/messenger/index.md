# Messenger und Sofortnachrichten

## Kurz gesagt

FreeSynergy Messenger ist ein Ort für Mail, Chat und KI-Agenten. Es behandelt eine Nachricht als Nachricht, egal welches Netz sie gebracht hat. Du liest, antwortest, suchst und ordnest alles an einem Ort ein, und Connectoren übernehmen die Kommunikation mit der Außenwelt. Eine Nachricht wird nur gesendet, wenn sie verschlüsselt gesendet werden kann.

## Was hier anders ist

- Nur verschlüsselt: Gibt es keine Möglichkeit, eine Nachricht an alle ihre Empfänger zu verschlüsseln, wird sie nicht gesendet, und es gibt keine Ausnahme.
- Eingehende Nachrichten sind mit dem markiert, was der Connector wirklich weiß. Alles, was nicht Ende-zu-Ende nachgewiesen ist, wird nie als sicher angezeigt.
- Das Original jeder Mail wird Byte für Byte aufbewahrt.
- KIs sind Teilnehmer, keine versteckten Mithörer. Jede ist markiert, keine handelt ohne deine Freigabe, und ein Not-Halt hat Vorrang vor allem.
- Messenger besitzt seine offene Schnittstelle; Mail, Chat und Agenten sind Connectoren unter einem Programm.

## Wo es heute steht

Neueste Version: `v0.4.0`. Heute ist es der Kern, ohne Fenster. Es hat ein Nachrichtenmodell für Mail, Chat und Agenten, mit Unterhaltungen, Seitenumbruch, der nicht springt, wenn neue Mail eintrifft, ungelesenen Markierungen, Entwürfen, Suche, Anheften, Verschieben, Markieren und Weiterleiten. Nur-verschlüsselt-Senden verweigert klar und nennt die Empfänger, die nicht erreicht werden können. Nachrichten werden mit ihrem Original gespeichert. Ein Mail-Connector ruft über IMAP oder JMAP ab und sendet über SMTP oder JMAP, mit OpenPGP und Autocrypt; getestet nur gegen einen lokalen Stalwart-Testserver. Ein KI-Wächter gibt jeder KI eine Einladung, eine Freigabe pro Aktionsart, stellt Rückfragen bei riskanten Schritten, hält Geheimnisse von KIs fern und hat einen Not-Halt.

Noch nicht da (geplant): ein Fenster, ein Server, Chat-Connectoren (Matrix und andere) und Telegram. Nachrichten bleiben aus Absicht auf dem Gerät, auf dem sie ankamen, bis der Schlüsseltresor existiert, und Konto-Passwörter können noch nicht gespeichert werden. Nachrichten bearbeiten und darauf reagieren, zeitgesteuertes Senden, Mail-Regeln, HTML-Inhalte, Schlüsselsuche, STARTTLS und S/MIME antworten mit „nicht möglich“. Die Regel, dass alle Mitglieder zustimmen müssen, bevor eine KI einer Unterhaltung beitritt, ist nicht gebaut, und die Regeln des Wächters sind vorläufig. Die Schnittstelle ist ein Entwurf ohne Anbindung.

## Geplante Facetten

Facetten sind Teile eines Programms, die wie eigene Apps aussehen (siehe [Programme](../../index.md)). Vorgeschlagen für `fs-messenger`:

- Mail (vorgeschlagen)
- Chat (vorgeschlagen)
- Forum, möglicherweise (vorgeschlagen)

## Übersicht

Dieser Bereich enthält Dokumentation für verschiedene Messenger und Kommunikationsplattformen.

## Verfügbare Systeme

- **outlook** - Microsoft E-Mail und Zusammenarbeit
- **kontact** - Persönlicher Informationsmanager von KDE
- **thunderbird** - E-Mail-Client von Mozilla
- **element** - Sicherer Messenger auf Matrix-Basis
- **discord** - Sprach-, Video- und Text-Chat
- **mastodon** - Dezentrales soziales Netzwerk
- **telegram** - Cloud-Messenger mit Bots
- **signal** - Privater Messenger mit Ende-zu-Ende-Verschlüsselung
- **whatsapp-web** - WhatsApp-Weboberfläche
- **jabber/xmpp** - Offenes Protokoll für Sofortnachrichten
- **skype** - Kommunikationsplattform von Microsoft
- **rocketchat** - Quelloffener Team-Chat
- **mattermost** - Quelloffene Slack-Alternative

## Was ist ein Messenger?

Ein Messenger (Sofortnachrichtendienst) ist eine Software für Echtzeitkommunikation über das Internet. Messenger ermöglichen:

- Austausch von Textnachrichten
- Sprach- und Videoanrufe
- Dateiübertragungen
- Gruppenchats und Kanäle
- Bot-Integrationen
- Ende-zu-Ende-Verschlüsselung

## Anwendungsbereiche

- **Teamkommunikation**: Tägliche Kommunikation im Team
- **Kundensupport**: Kundenservice per Messenger
- **Community**: Gemeinschaftsdiskussionen und Foren
- **Soziale Netzwerke**: Microblogging und soziale Netzwerke
- **Zusammenarbeit**: Zusammenarbeit mit Dateifreigabe

## Sicherheit und Datenschutz

Beim Einsatz von Messengern solltest du folgende Sicherheitsaspekte beachten:

- **Verschlüsselung**: Ende-zu-Ende-Verschlüsselung für sichere Kommunikation
- **Serverstandort**: Welche Rechtsordnung gilt?
- **Datenschutz**: Wie werden Daten gespeichert und verarbeitet?
- **Open Source**: Ist der Quellcode überprüfbar?
- **Dezentralität**: Ist das System dezentral aufgebaut?

## Auswahlkriterien

Bei der Wahl eines Messengers solltest du folgende Kriterien berücksichtigen:

- **Funktionen**: Welche Funktionen sind nötig?
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
3. **Konto anlegen**: Benutzerkonto erstellen
4. **Kontakte hinzufügen**: Teammitglieder und Kontakte einladen
5. **Gruppen anlegen**: Chats und Kanäle für Teams einrichten

## Weitere Informationen

Weitere Informationen findest du in der Dokumentation der einzelnen Messenger-Systeme.

## Frontends

<!-- gen:frontends (Spiegel von docs/en; ADR 0011) — edits inside are overwritten -->
Analysierte Programme (9), nach Funktion, nichts kopiert (ADR 0012/0013):

- [Apple Mail](frontends/apple-mail/index.md) — Apple Mail ist das Mailprogramm, das auf jedem iPhone, iPad und Mac installiert ist.
- [Discord](frontends/discord/index.md) — Discord ist eine proprietäre Kommunikationsplattform für Gaming-Communities, mit Sprach- und Videofunktion und einer Serverstruktur.
- [Element](frontends/element/index.md) — Element ist der quelloffene Messenger für das Matrix-Protokoll, mit dezentraler Architektur und Ende-zu-Ende-Verschlüsselung.
- [FreeSynergy Simple](frontends/freesynergy-simple/index.md) — Unser eigenes, bewusst schlankes Messenger-Frontend.
- [Kontact](frontends/kontact/index.md) — Kontact ist die integrierte PIM-Anwendung für KDE, die E-Mail, Kalender, Kontakte, Aufgaben und Notizen in einer einzigen Anwendung vereint.
- [Mastodon](frontends/mastodon/index.md) — Mastodon ist ein quelloffenes Microblogging-Netzwerk auf Basis des ActivityPub-Protokolls, und es ist dezentral.
- [Outlook](frontends/outlook/index.md) — Outlook ist Microsofts beliebtester E-Mail-Client, Teil von Microsoft 365.
- [Telegram](frontends/telegram/index.md) — Telegram ist ein Cloud-Messenger mit Fokus auf Geschwindigkeit, große Gruppen und Kanäle und Verschlüsselung.
- [Thunderbird](frontends/thunderbird/index.md) — Thunderbird ist Mozillas quelloffener E-Mail-Client, plattformübergreifend und auf E-Mail ausgerichtet.

Übersicht: [frontends](frontends/index.md)
<!-- /gen:frontends -->
