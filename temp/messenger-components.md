# Messenger-Frontend → Bausteine (Zerlegung)

Stand 2026-11-05 · Grundlage: `docs/en/programs/apps/messenger/frontends/*/latest/{features,layout,menus,shortcuts}.md`
(7 Frontends), `docs/en/programs/apps/messenger/requirements.md`, CONVENTIONS §2/§3, ADR 0005/0018/0022/0023,
`docs/en/components/blinc-cn-components.md`, `temp/research/blinc-issues.md`.

Zweck: Brücke von der Frontend-Seite — welche Bausteine braucht ein Messenger-Frontend, welche
haben wir (84 Komponenten), welche fehlen, was gehört nach Blinc. Nichts kopiert (ADR 0013); die
Elemente sind nach Funktion benannt.

**Achtung Eingangsdaten:** Die Frontend-Dateien sind dünn und teils schablonenhaft (gleiche
Menü- und Kürzellisten bei Discord/Element/Telegram, Fehler wie „Address Book via Lightning“,
„KNode“, „200,000 instead of 200,000“). `Notable ideas` ist in allen 7 `index.md` leer.
Reaktionen, Threads, Schedule-Send, Snooze, Swipe-Aktionen stehen dort **nicht** — sie sind
unten mit ⚠️ als „bekannt, nicht belegt“ geführt.

Legende Spalten:
- **Wo gesehen:** Di Discord · El Element · Ko Kontact · Ma Mastodon · Ou Outlook · Te Telegram · Th Thunderbird; ⚠️ = nicht in unseren Dateien
- **Pfad:** relativ zu `docs/en/components/`; **NEW** = fehlt in den 84
- **Band** nach Testfragen §2: primitive = nicht zerlegbar · widget = kennt seine Inhalte beim Bauen (bindet ein `data/`-Modell), endliche Kinder, eigener Zustand · workbench = Inhalt erst zur Laufzeit, offen. App = Hülle (Menü, Fenster, Einstellungen, ADR 0005), kein Baustein.
- **Datentyp (ADR 0023):** was das Element im Darstellungs-Register bindet
- **Blinc cn:** yes = `cn::`/`blinc_layout`-Baustein vorhanden · partly = Teil/Workaround · no = „No direct Blinc equivalent“ bzw. nicht in der Referenz · Id = Blinc-Issue

## Tabelle

| UI element | Where seen | Our component (path) or NEW | Band | Data type it binds (ADR 0023) | Blinc cn has it? |
|------------|-----------|------------------------------|------|-------------------------------|------------------|
| **App-Hülle** (Fensteraufteilung 3–4 Spalten, verstellbar) | alle | `widgets/containers/split-view` + App-Hülle | widget (Aufteilung) / App | — (Layout) | yes (`resizable_group`/`resizable_panel`) |
| Aktivitätsleiste / Konto-Umschalter (Icon-Schiene links) | Di (Server), El, Ou, Th (Activity Bar), Te | `widgets/navigation/sidebar` (eingeklappt) + `widgets/data/avatar` + `primitives/feedback/badge` | widget | Account-Liste (Konnektor-Konfiguration) — **kein Standard** ⚠️ | partly (`cn::sidebar(is_collapsed)`, keine Icon-Schiene) |
| Ordner-/Raumliste (Konto → Ordner; Kategorie → Kanal) | Ko, Ou, Th (Ordner), Di (Kategorien), El (Räume, gepinnt), Te | `widgets/data/tree-view` | widget | JMAP `Mailbox` (RFC 8621); Räume = AS2 `context`-Sammlung | yes (`cn::tree_view`; Bug 5bfc932 Expand-Animation friert) |
| Konversationsliste (virtuell, lang) | alle | `widgets/data/list-view` | widget | Liste von Konversationen (AS2 `context` + letzte `Note`) | partly (`virtual_list`; keine Auswahl-/Mehrfachauswahl-Logik) |
| Konversations-Listeneintrag (Avatar, Name, Vorschau, Zeit, Ungelesen, Verschlüsselung) | alle | `widgets/data/list-view` Varianten `With Avatars`+`With Badges`+`With Actions` + Register-Eintrag `Conversation → list-entry` ⚠️ | widget (Zeile der Liste) | Konversation (AS2 `context`, JMAP `Thread`) | partly (Zeile von Hand aus `avatar`/`label`/`badge`) |
| Wisch-Aktionen am Eintrag (archivieren, löschen, gelesen) | ⚠️ (mobile Mail/Chat allgemein); list-view-Doku nennt `swipe` | `widgets/data/list-view` + `interactions/gestures/swipe/swipe` | widget + Geste | Aktion auf Konversation (`Delete`, `Read`, Mailbox-Wechsel) | no (keine Swipe-Geste in der cn-Referenz; Klickverlust 9ab9dc6) |
| Nachrichtenansicht Chat (chronologisch, unten verankert, ältere nachladen, Tagestrenner, Ungelesen-Trenner) | Di, El, Te, Ma | **NEW `message-list`** ⚠️ (Abgrenzung zu `widgets/data/timeline` prüfen) | widget | AS2 `Note`-Folge in einem `context` | partly (`virtual_list`, aber kein umgekehrtes Scrollen/Verankern) |
| Nachrichtenblase / Chat-Nachricht (Absender, Text, Antwort-Bezug, Reaktionen, Status) | Di, El, Te, Ma | **NEW `message-bubble`** | widget | AS2 `Note` + MIMI content / Matrix event | no |
| Mail-Ansicht / Lesebereich (Kopf: Von/An/Cc/Betreff/Datum, Körper, Anhänge) | Ko, Ou, Th (Preview), Ou-Editor | **NEW `mail-view`** (Kopf über `widgets/data/description-list`) | widget | JMAP `Email` + Original-MIME (`message/rfc822`) | no (`description-list` ebenfalls no) |
| HTML-Mailkörper (bereinigt, ohne Fernladen) | Ko, Ou, Th | `workbenches/special/embed` Variante „sanitised html“ ⚠️ — oder NEW `html-view` | workbench (fremder Inhalt) ⚠️ | `text/html`-Teil der MIME-Nachricht | backlog **a782b47** (`html_view()` phased plan); `embed`: no |
| Formatierter Chattext (Markdown anzeigen) | El, Ma | `workbenches/fields/rich-text-editor` im Nur-Lese-Modus ⚠️ (Änderung) | workbench ⚠️ | MIMI-Textteil `text/markdown` ⚠️ | partly (`rich_text_editor`, kein read-only belegt) |
| Thread-Bereich (Seitenspalte für Antwortstrang) | ⚠️ Di, El | `widgets/containers/panel` / `widgets/overlays/drawer` + `message-list` | widget | AS2 `context`/`inReplyTo`; Matrix `m.thread`; MIMI topic | partly (`sheet_right`, `resizable_panel`; `panel`: no) |
| Detailbereich (Mitglieder, Rauminfo, Kontaktkarte) | El (rechte Seitenleiste), Te, Di (Mitglieder), Ou/Ko/Th (Kontakt-Vorschau) | `widgets/containers/panel` + `widgets/data/description-list` + `widgets/data/list-view` + `widgets/data/avatar` | widget | Gruppe (MLS-Mitglieder, MIMI room policy), JSContact | partly |
| Kontaktkarte beim Überfahren | Di, El, Ma, Te (Profil öffnen) | `widgets/overlays/hover-card` + `avatar` (+ Karten-Widget des Kontakte-Programms) | widget | JSContact (geliehen, ADR 0020) | yes (`cn::hover_card`) |
| Composer schlicht (Textfeld + Senden) | alle Chats | `primitives/fields/textarea` (wachsend) + `primitives/actions/button` | primitive | MIMI-Text / `text/plain` | yes (`cn::textarea`, `cn::button`; IME **e864f0c**) |
| Composer reich (Formatleiste, Links, Listen) | El, Ma (Markdown), Ko, Ou, Th (Formatleiste) | `workbenches/fields/rich-text-editor` | workbench | `text/html` (Mail) / `text/markdown` (MIMI) ⚠️ | yes (`rich_text_editor` + `selection_toolbar`) |
| Composer als Ganzes (Feld + Leiste + Anhänge + Emoji + Erwähnung + Verschlüsselung + Senden) | alle | **NEW `composer`** ⚠️ Band offen (siehe Frage 2) | widget ⚠️ (enthält ggf. Workbench) | Entwurf: AS2 `Note` (Entwurf) + Empfänger + `$draft` | no |
| Empfängerfelder An/Cc/Bcc mit Adressbuch-Vorschlag und Schlüsselstatus je Empfänger | Ko, Ou, Th (Mail-Editor) | `primitives/fields/tags-input` + `primitives/fields/combobox` — Variante `recipients` (Änderung) | primitive | RFC 5322-Adressen, JSContact, Schlüssel vorhanden ja/nein | no (`tags-input` no; `combobox` yes, Bug 8115bf5) |
| Betreff | Ko, Ou, Th | `primitives/fields/text-input` | primitive | JMAP `subject` (mit RFC 9788 geschützt) | yes (`cn::input`) |
| Anhänge im Composer (Ablegen, Fortschritt, Entfernen) | Di, El, Te, Ma, Ou | `widgets/fields/file-upload` + `primitives/feedback/progress` | widget | AS2 `attachment`; JMAP Blob (RFC 9404); MIMI verschlüsselter externer Teil | no (`file-upload` nicht in cn); `progress` yes |
| Emoji-Auswahl | Di, El, Ou | `widgets/fields/emoji-picker` (Varianten `inline`, `overlay`, `reaktion`) | widget | Unicode-Emoji; eigene Emoji als `attachment` ⚠️ | no |
| Erwähnungen (@Person) | Di, El, Ma | `primitives/fields/mention-input` — im Rich-Composer als Inline-Entität (Änderung) | primitive | AS2 `tag` Typ `Mention`; JSContact; Matrix-User-ID | no (Workaround `rich_text_editor` + `popover`) |
| Reaktionsleiste (Emoji + Zahl, eigene an/aus) | ⚠️ Di, El, Te | **NEW `reaction-bar`** | widget | `Like`/`EmojiReact` + `Undo` (aggregiert); MIMI reaction; Matrix `m.annotation` | partly (`badge`, `toggle_group`) |
| Zustellt/Gelesen-Anzeige (senden … gesendet … zugestellt … gelesen … Fehler) | Di, El, Te | **NEW `message-status`** (Icon-Zustände + Tooltip) | primitive | MIMI message-status `-02`; `Read`; Matrix `m.receipt`; DSN/MDN | no |
| „Gelesen von“ (kleine Avatare) | El, Te ⚠️ | `widgets/data/avatar` (Gruppe) | widget | `Read`-Aktivitäten je Person | yes (`cn::avatar_group`) |
| Verschlüsselungs-Kennzeichen (unverschlüsselt sichtbar markiert, Klick → Anleitung) | El, Te (Sicherheitshinweise); ADR 0018 | **NEW `encryption-state`** (nicht `badge`: Badge ist nicht bedienbar, dies verlinkt die Anleitung, ADR 0031) | primitive | `freesynergy.net:encryption` (`mls`·`openpgp`·`megolm`·`transport-only`·`none`) | partly (`badge` + `link`) |
| Avatar mit Anwesenheit | Di, El, Te | `widgets/data/avatar` | widget | JSContact-Foto; Präsenz: **kein Standard** (Matrix `m.presence`) ⚠️ | yes (Avatar mit Präsenzpunkt) |
| Ungelesen-Zähler | alle (Listen, Navigation) | `primitives/feedback/badge` (`counter`, `dot`) | primitive | abgeleitet aus `Read`-Log / JMAP `$seen` | yes (`cn::badge`; CSS-Bug 9008028 bei gebundenem Badge) |
| Suche (Feld) | alle | `primitives/fields/search-field` | primitive | Suchanfrage (JMAP-Filtermodell) | partly (`input_type(Search)`) |
| Suchergebnisse (Treffer mit Fundstelle) | El, Ko, Ou, Th, Te | `widgets/data/list-view` + `message-bubble`/`mail-view` kompakt | widget | AS2 `Note` + Treffer-Position (Web Annotation Selector ⚠️) | partly |
| Schnellfilter (ungelesen, markiert, mit Anhang, Erwähnungen) | Ma (Filter), Th (Ansicht), Ou ⚠️ | `primitives/actions/button-group` | primitive | Filter-Parameter von `conversation.list` | yes (`cn::toggle_group`) |
| Regel-Editor (Bedingung → Aktion, an/aus) | Ko, Ou, Th (Filterregeln, Filter-Kontextmenü), Ma (Wortfilter) | **NEW `rule-editor`** (aus `widgets/data/repeater` + `select` + `text-input` + `switch`) | widget | Sieve (RFC 5228, JMAP Sieve RFC 9661) | no (`repeater` no) |
| Hauptmenü (Menüleiste / Backstage) | Ko, Ou, Th; Te, El, Di (Einstellungsmenü) | `widgets/navigation/menu` (Menü-Widget, ADR 0023 Pkt. 3) | widget | Fähigkeitenliste des Programms (Manifest) | yes (`cn::menubar`, `dropdown_menu`) |
| Kontextmenü (Nachricht, Konversation, Mitglied, Datei) | alle | `widgets/overlays/context-menu` | widget | Fähigkeiten am Objekt | yes (`cn::context_menu`; Web-Rechtsklick 436d0ad) |
| Schnellaktionen an der Nachricht (beim Überfahren: antworten, reagieren, mehr) | ⚠️ Di, El | `widgets/navigation/toolbar` (Variante schwebend) | widget | Fähigkeiten an `Note` | no (nur editor-eigene `selection_toolbar`) |
| Werkzeugleiste / Ribbon | Ou (Ribbon ⚠️), Th, Ko | `widgets/navigation/toolbar` (+ `tabs` für Ribbon-Reiter) | widget | Fähigkeiten | no |
| Befehlspalette | ⚠️ (Kürzel „Quick switcher“ in Di/El/Te: Kanal/Raum suchen) | `widgets/navigation/command` | widget | Fähigkeiten + Konversationen | no |
| In-App-Hinweis (gesendet, Fehler, rückgängig) | alle | `primitives/feedback/toast` | primitive | — | yes (`cn::toast`; Web-Exit d58924b) |
| Systembenachrichtigung | Ko, Th, Di, El, Te | Plattform (Shell, Ebene 6), kein Baustein | — | Benachrichtigungsereignis aus `Events` | no (mobile Push fehlt: 883ead2) |
| Anhangsvorschau (Bild groß, Lightbox) | Di, El, Te, Ma | `primitives/media/image` + `widgets/overlays/modal` | widget | `attachment` mit `mediaType` `image/*` | partly (`image`, `cn::dialog`) |
| Dokumentvorschau (PDF u. a.) | Di, El, Te (Dokumente) | `workbenches/special/embed` ⚠️ | workbench | `application/pdf` u. a. | no |
| Medienübersicht der Konversation | Te (Medien), El ⚠️ | `widgets/media/gallery` | widget | alle `attachment` eines `context` | no |
| Link-Vorschau (Titel, Bild, Seite — vom Absender erzeugt) | ⚠️ El, Te | **NEW `link-preview`** (auf `widgets/containers/card`) | widget | AS2 `Link`/`Page` als Anhang ⚠️ | partly (`cn::card`) |
| Sprachnachricht abspielen | ⚠️ Te, El | `widgets/media/audio` | widget | `attachment` `audio/*` | yes (`audio_player` mit Wellenform) |
| Video in Nachricht | Di, El, Te, Ma | `widgets/media/video` | widget | `attachment` `video/*` | yes (`video_player`) |
| Anruf-Steuerung (Mikro, Kamera, Bildschirm teilen, auflegen) + Kachelraster | Di, El, Te | **NEW `call-controls`** + `widgets/data/grid-view` | widget | Anrufsitzung (MatrixRTC ⚠️ / kein FS-Standard) | no (Mediensteuerung nur für Player; `grid-view` no) |
| Mitgliederliste mit Rollen | Di, El, Te | `widgets/data/list-view` + `avatar` + `badge` + `context-menu` | widget | MLS-Gruppe, MIMI room policy, Rollen | partly |
| Konto einrichten (Assistent, Autodiscovery) | Th, Ko, Ou (Konto hinzufügen) | `widgets/containers/wizard` | widget | Konto/Konnektor-Konfiguration ⚠️ | no |
| Schlüssel-/Geräteprüfung (Fingerabdruck, Vergleich, QR) | El, Te (Geräte), Ko, Th (GPG prüfen) | **NEW `key-verification`** | widget | OpenPGP-Fingerprint, MLS-Credential, Web-of-Trust-Bestätigung (`data/identity`) | no |
| „Kein verschlüsselter Weg gefunden“ – Nachfrage | ADR 0018 | `widgets/overlays/alert-dialog` + `primitives/feedback/alert` + `primitives/basics/link` | widget | Empfänger + Schlüsselstatus | yes |
| Tagestrenner / „Neu ab hier“ | Di, El, Te ⚠️ | `primitives/basics/separator` (mit Beschriftung — Änderung) | primitive | `published`-Datum, Lesemarke | yes (`cn::separator`, Beschriftung ⚠️) |
| Tipp-Anzeige („schreibt …“) | ⚠️ Di, El, Te | Teil von `message-list` | — | Matrix `m.typing`; MIMI/AS2: keiner | no |
| Leerer Zustand („alles erledigt“) | alle ⚠️ | `primitives/feedback/empty-state` | primitive | — | no |
| Ladeplatzhalter | El (Lazy loading) | `primitives/feedback/skeleton` | primitive | — | yes |
| Reiter (Ou „Fokus/Andere“ ⚠️, Ma Zeitleisten, Th Tabs) | Ma, Th, Ou ⚠️ | `widgets/navigation/tabs` | widget | gespeicherte Sicht/Filter | yes (`cn::tabs`) |
| Untere Navigation (mobil) | Te, Di, El ⚠️ (Mobil-Apps) | `widgets/navigation/bottom-navigation` | widget | — | partly (`navigation_menu`) |
| Zeit wählen (Senden planen, Snooze) | ⚠️ Ou | `widgets/fields/date-picker` + `widgets/fields/time-picker` | widget | Zeitpunkt (`sendAt`, Snooze-Datum) | partly (`cn::calendar`; time-picker no; backlog **bf7c901** `date_picker`) |
| Kalendereinladung in Mail (annehmen/ablehnen) | Ko, Ou, Th | Widget des Kalender-Programms (`widgets/data/calendar-view` / Termin-Karte), geliehen | widget | JSCalendar / iMIP | partly (`cn::calendar`) |
| Einstellungsseiten | alle (Allgemein, Medien, Sicherheit, Theme, Sprache) | App-Hülle aus `sidebar`/`tabs` + `primitives/fields/field` + `switch` + `select` + `language-switcher` | App (Hülle, ADR 0005) | Programmeinstellungen | partly (`field` = Affordanzen am Input; `language-switcher` no) |
| Nachrichten verschieben per Ziehen auf Ordner | Ou, Th | `tree-view` (Ablageziel) + Geste `drag` | widget + Geste | Mailbox-Wechsel (`mailboxIds`) | partly ⚠️ (Drag nicht als cn-Baustein; 9ab9dc6) |

## (a) NEUE Komponenten

| Name | Band | Zweck (eine Zeile) |
|------|------|-------------------|
| `message-list` ⚠️ | widget (`data`) | Nachrichten einer Konversation, unten verankert, nachladend, mit Tages-/Ungelesen-Trennern; ggf. Variante von `timeline` |
| `message-bubble` | widget (`data`) | eine Chat-Nachricht mit Absender, Inhalt, Antwortbezug, Reaktionen, Status, Verschlüsselung |
| `mail-view` | widget (`data`) | eine Mail mit Kopf, Körper (Text/HTML), Anhängen, Signatur- und Verschlüsselungsstatus |
| `composer` ⚠️ | widget (Band offen) | Nachricht verfassen: Feld, Formatierung, Anhänge, Emoji, Erwähnung, Verschlüsselung, Senden |
| `reaction-bar` | widget (`data`) | Reaktionen gezählt anzeigen und eigene an-/abschalten |
| `message-status` | primitive (`feedback`) | Zustand einer gesendeten Nachricht: wird gesendet / gesendet / zugestellt / gelesen / Fehler |
| `encryption-state` | primitive (`feedback`) | Verschlüsselungsart einer Nachricht/Konversation, unverschlüsselt deutlich markiert, führt zur Anleitung |
| `rule-editor` | widget (`fields` ⚠️) | Regeln „wenn … dann …“ bearbeiten, gespeichert als Sieve |
| `link-preview` | widget (`data`) | Vorschaukarte eines Links, vom Absender erzeugt |
| `key-verification` | widget (`overlays` ⚠️) | Schlüssel/Gerät einer Person prüfen und Vertrauen bestätigen |
| `call-controls` | widget (`media`) | Bedienleiste eines Anrufs (nur falls Anrufe im Messenger bleiben) |
| `html-view` ⚠️ | workbench oder `embed`-Variante | fremdes HTML (Mail) bereinigt, ohne Fernladen, darstellen |

Nicht neu, aber Register-Eintrag (ADR 0023): `Conversation → list-entry` (in `list-view`), `Message → bubble | mail | list-entry | text`, `Encryption → encryption-state | text`.

## (b) Vorhandene Komponenten mit Änderungsbedarf

- `list-view` — Mehrfachauswahl, Wisch-Aktionen je Richtung (Fähigkeit konfigurierbar), Tastatur „nächste ungelesene“, virtuelle Zeilen; Zeilen-Template für Konversation.
- `tags-input` — Variante `recipients`: Adressbuch-Vorschlag (JSContact), Schlüsselstatus je Chip, ungültige Adresse.
- `mention-input` — als Inline-Entität im `rich-text-editor` nutzbar, nicht nur als eigenes Feld.
- `rich-text-editor` — Nur-Lese-Modus für empfangene formatierte Texte; Ausgabe als `text/html` **und** `text/markdown`; Erwähnungen/Emoji als Inline-Knoten. (ADR 0023: Block-Editor-Frage — ist rich-text = Block-Editor?)
- `emoji-picker` — Variante `reaktion` mit „zuletzt benutzt“ und Schnellreihe.
- `toolbar` — Variante schwebend (Nachricht beim Überfahren) und Ribbon (mit `tabs`).
- `separator` — Beschriftung in der Mitte (Datum, „Neu“).
- `avatar` — Präsenz an ein Datenfeld binden (heute nur optischer Punkt), Verschlüsselungs-/Verifiziert-Marke ⚠️.
- `badge` — bleibt nicht bedienbar; Abgrenzung zu `encryption-state` in `badge/description.md` vermerken.
- `file-upload` — verschlüsselter Upload (Blob wird vor dem Senden verschlüsselt), Einfügen aus Zwischenablage.
- `embed` — Variante „bereinigtes HTML ohne Fernladen“ oder Verweis auf `html-view`.
- `timeline` — klären, ob `message-list` eine Variante davon ist.

## (c) Upstream in Blinc vs. unsere Schicht

Leitlinie: **interaktive Grundbausteine ohne Fachwissen → Blinc** (passt zu c422b97, Promotion
`blinc_cn` → `blinc_layout`, CSS-überschreibbar, themenneutral); **alles, was ein Datenmodell bindet
(Nachricht, Konversation, Verschlüsselung, Sieve) → unsere Schicht** (ADR 0023).

| Baustein | Wo | Bezug |
|----------|----|-------|
| Swipe-/Drag-Gesten an Listenzeilen | Blinc | kein Issue; 9ab9dc6 (verlorene Klicks/Drags bei Rebuild) vorher lösen |
| Umgekehrte, verankerte `virtual_list` (Chat-Scrollen, nachladen oben) | Blinc | kein Issue — neu melden |
| `html_view()` (bereinigtes HTML) | Blinc | **a782b47**; Fernladen-Sperre als Option fordern |
| `tags-input` / Chips | Blinc | kein Issue; Teil von **bf7c901** prüfen |
| `date_picker`, `time-picker` | Blinc | **bf7c901** (date_picker geplant) |
| Mention/Inline-Entitäten im `rich_text_editor` | Blinc | kein Issue — neu melden |
| `toolbar` allgemein | Blinc | kein Issue (heute nur `selection_toolbar`) |
| `command`-Palette, `empty-state`, `file-upload` (Dropfläche) | Blinc | kein Issue; generisch, gehört nach cn |
| IME/Vorschreiben (CJK, mobil) im Composer | Blinc | **e864f0c** — für einen Messenger Pflicht |
| Mobile Push, Benachrichtigungen | Blinc/Plattform | **883ead2** |
| Combobox-Hover (Empfänger-Vorschlag) | Blinc | **8115bf5** |
| Barrierefreiheit (AccessKit) | Blinc | **kein Issue** (nur in c422b97/4405aa3 erwähnt) — für uns Pflicht, melden |
| `emoji-picker` | ⚠️ offen | generisch → Blinc; Emoji-Daten/Skin-Tones evtl. unsere Schicht |
| `message-list`, `message-bubble`, `mail-view`, `composer`, `reaction-bar`, `message-status`, `encryption-state`, `rule-editor`, `link-preview`, `key-verification` | unsere Schicht | binden `data/messages`, `data/identity`, Sieve |

## (d) Bau-Reihenfolge

**Stufe 1 — „Mails anzeigen und wegwischen“** (eigenes Referenz-Frontend, ADR 0022; Vertrag nur
`Capabilities`, `Accounts`, `Conversations`, `Messages`):
1. `list-view` (virtuell) + Konversations-Zeile (`avatar`, `label`, `badge`, `encryption-state`)
2. Wischgeste (archivieren/löschen/gelesen) — Blinc-Gesten oder vorerst Schaltflächen in der Zeile
3. `mail-view` mit Klartext-Körper; HTML zunächst als Text-Fallback, bis `html_view` (a782b47) da ist
4. `encryption-state` + Hinweis mit Link zur Anleitung (ADR 0018/0031)
5. `toast` (mit „Rückgängig“), `empty-state`, `skeleton`
Noch **kein** Composer, keine Ordner, keine Suche. Diese Stufe prüft den Vertrag mit minimaler Fläche.

**Stufe 2 — Chat-Grundlage:** `message-list`, `message-bubble`, Composer schlicht (`textarea` +
`button`), `message-status`, `avatar` mit Präsenz, `search-field`.

**Stufe 3 — Outlook-artiges Vorbild-Frontend** (Vorbild-Wahl offen, siehe Frage 1):
`split-view` mit 3–4 Bereichen, `sidebar` als Konto-Schiene, `tree-view` Ordner, `menu` (Menüleiste),
`toolbar`/Ribbon, `context-menu`, `composer` reich (`rich-text-editor`, Empfänger-`tags-input`,
`file-upload`, `emoji-picker`, `mention-input`), `rule-editor`, `command`, Einstellungsseiten,
`wizard` (Konto einrichten), `key-verification`, `date-picker`/`time-picker` (planen, Snooze),
Kalendereinladung über das Kalender-Widget.

**Stufe 4 — Kür:** `reaction-bar`, Thread-Bereich, `link-preview`, `gallery`, `audio`/`video`,
`call-controls`.

## Offene Fragen

1. Welches Vorbild-Frontend (ADR 0022)? Outlook (Mail-lastig) oder Element/Telegram (Chat-lastig)? Der Auftrag nennt Outlook.
2. Band des `composer`: Widget, das eine Workbench (`rich-text-editor`) enthält, verletzt die Testfrage — ist der Composer Workbench, oder bleibt der reiche Editor ein austauschbarer Kind-Baustein?
3. Frontend-Dateien sind dünn/ungeprüft (Reaktionen, Threads, Schedule-Send, Snooze fehlen) — zuerst nachrecherchieren, bevor Required/Optional festgeschrieben wird?
4. Anrufe (Sprache/Video/Bildschirm) im Messenger oder eigenes Programm?
5. Präsenz und „zugestellt“ haben keinen AS2-Standard — eigene Spezifikation (ADR 0014) oder nur Matrix/MIMI-Abbildung?
6. Eigener Status-Baustein vs. `badge`-Variante für `message-status`/`encryption-state` — Regel „Badge ist nicht bedienbar“ beibehalten?
7. Mail-HTML: `embed`-Variante oder neue `html-view`; und wie lange Text-Fallback bis a782b47?
