# Entscheidungen (ADR)

Die Entscheidungen hinter FreeSynergy, in der Reihenfolge, in der sie fielen. Status und Titel stammen aus dem jeweiligen Eintrag.

| Nr. | Titel | Status |
|---|---|---|
| 0001 | [Sechs Ebenen und Namen](0001-ebenen-und-namen.md) |  |
| 0002 | [Sprache: Identifikatoren englisch, Prosa deutsch](0002-sprache.md) | Teil „Prosa deutsch / Deutsch = Quelle“ **ersetzt durch 0011** (2026-11-05), Rest gilt |
| 0003 | [Repo-Schale und Skript-Schattenbaum](0003-repo-schale-und-skripte.md) |  |
| 0004 | [Komponenten-Einteilung primitives / widgets / workbenches](0004-komponenten-einteilung.md) |  |
| 0005 | [App und Widget: derselbe Kern, unterschiedliche Ebene](0005-widget-und-app-gleicher-kern.md) |  |
| 0006 | [Haken, Abbruchkriterium und Pflichtmenge pro Kategorie](0006-haaken-abbruchkriterium-und-pflichtmenge.md) | Punkt 2 und 3.4 **ersetzt durch 0013** (2026-11-05), Rest gilt |
| 0007 | [`skins/` wird `masks/`](0007-skins-zu-masks.md) | **superseded by 0012** (2026-11-05) |
| 0008 | [Englisch zuerst, Deutsch zweite Sprache](0008-englisch-zuerst.md) | **superseded by 0011** (2026-11-05) |
| 0009 | [GUI: Blinc ist gesetzt](0009-gui-blinc.md) |  |
| 0010 | [Ein Prüfer für die Übersetzung: `scripts/doc_sync.py`](0010-ein-uebersetzungspruefer.md) |  |
| 0011 | [Nur Englisch wird gepflegt, Deutsch wird übersetzt](0011-nur-englisch.md) | akzeptiert (2026-11-05) |
| 0012 | [`masks/` wird `frontends/`, mit Versionsordner](0012-frontends-mit-versionen.md) | akzeptiert (2026-11-05) |
| 0013 | [Funktionen analysieren, nichts kopieren; Programme nach Ideen auswählen](0013-funktionen-analysieren-nichts-kopieren.md) | akzeptiert (2026-11-05) |
| 0014 | [Standards zuerst, ActivityStreams 2.0 als gemeinsame Basis](0014-standards-zuerst-as2.md) | akzeptiert (2026-11-05) |
| 0015 | [Fremdprojekte, die wir nutzen und unterstützen; Crate-Regel](0015-fremdprojekte-und-crates.md) | akzeptiert (2026-11-05) |
| 0016 | [Lizenz: MIT OR Apache-2.0, für immer kostenlos](0016-lizenz-mit-oder-apache.md) | akzeptiert (2026-11-05) |
| 0017 | [Programme heißen nach Kategorie, ein Repo pro Programm](0017-programme-und-repos.md) | akzeptiert (2026-11-05) |
| 0018 | [Messenger umfasst E-Mail und Chats; nur verschlüsselte Nachrichten](0018-messenger-mit-mail-nur-verschluesselt.md) | akzeptiert (2026-11-05) |
| 0019 | [Datenhaltung: `fs-store` in jedem Programm, `fs-hub` pro Gerät](0019-fs-store-und-fs-hub.md) | akzeptiert (2026-11-05) |
| 0020 | [Speicherformat: AS2-Hülle + Fachstandard + Aktivitätsprotokoll; Leihen = Live-Verweis](0020-speicherformat-as2-huelle.md) | akzeptiert (2026-11-05) |
| 0021 | [Schnittstelle: ein Vertrag, viele Zugänge](0021-schnittstellenvertrag.md) | akzeptiert (2026-11-05) |
| 0022 | [Jedes Programm hat zwei Referenz-Frontends](0022-zwei-referenz-frontends.md) | **superseded by 0038** (2026-11-05) |
| 0023 | [Darstellungs-Register; zwei Editor-Workbenches](0023-darstellungs-register-und-editoren.md) | Punkt 4 **ersetzt durch 0039** (drei Editoren), Rest gilt |
| 0024 | [Programm ohne Hub: lokale Daten, Verschlüsselung, Schlüsseltresor, SCIM](0024-programm-ohne-hub-und-schluesseltresor.md) | akzeptiert (2026-11-05) |
| 0025 | [Abschauen nur im äußersten Notfall, nie bei Closed Source](0025-abschauen-nur-im-notfall.md) | akzeptiert (2026-11-05) |
| 0026 | [Immer die neueste Technik](0026-neueste-technik.md) | akzeptiert (2026-11-05) |
| 0027 | [IDs: UUIDv7 (RFC 9562)](0027-ids-uuidv7.md) | akzeptiert (2026-11-05) |
| 0028 | [Namen, Domains und Erreichbarkeit über den Hub](0028-namen-domains-und-hub.md) | akzeptiert (2026-11-05) |
| 0029 | [Schutzbedürftige Daten müssen gekennzeichnet werden](0029-schutzbeduerftige-daten.md) | akzeptiert (2026-11-05) |
| 0030 | [Original + Hülle: Empfangenes wird unverändert aufbewahrt](0030-original-plus-huelle.md) | akzeptiert (2026-11-05) |
| 0031 | [Jeder Text ist ein Wiki-Eintrag; die Bibliothek; Hilfe dort, wo man ist](0031-texte-wiki-bibliothek.md) | akzeptiert (2026-11-05) |
| 0032 | [name-Regel; Beschlossenes bleibt](0032-name-regel-und-bestand.md) | akzeptiert (2026-11-05) |
| 0033 | [Markieren: ein Mechanismus für alles (Punkt = einsetzen, Bereich = ersetzen/benennen)](0033-markieren-ein-mechanismus.md) | akzeptiert (2026-11-05) |
| 0034 | [Textstruktur technisch denken: Absatz, Seite, Kollektion, Regal](0034-textstruktur-technisch.md) | akzeptiert (2026-11-05) |
| 0035 | [Föderation zwischen Instanzen: OpenID Federation 1.0](0035-foederation-openid-federation.md) | akzeptiert (2026-11-05) |
| 0036 | [Git als dezentrale Verteilung: Pakete, Themes, Programme, Medien](0036-git-als-verteilung.md) | akzeptiert (2026-11-05) |
| 0037 | [Jedes Programm ist mindestens eine Workbench; Programme zeigen sich gegenseitig an](0037-programme-als-workbenches.md) | akzeptiert (2026-11-05) |
| 0038 | [Referenz-Frontends: vier Arten, am besten ganze Suiten](0038-referenz-frontends.md) | akzeptiert (2026-11-05) |
| 0039 | [Drei Text-Editoren](0039-drei-text-editoren.md) | akzeptiert (2026-11-05) |
| 0040 | [Cap'n-Proto-Schema-Compiler in reinem Rust; Anerkennung ohne Drama](0040-capnp-compiler-in-rust.md) | akzeptiert (2026-11-05) |
| 0041 | [Rust-Hygiene: Build-Ausgabe klein halten, nie in Git, regelmäßig aufräumen](0041-rust-hygiene.md) | akzeptiert (2026-11-05) |
| 0042 | [Text + Ebenen; die Datenbank ist die Wahrheit, Dateien sind Exporte](0042-text-ebenen-datenbank-wahrheit.md) | akzeptiert (2026-11-05) |
| 0043 | [Entwurfsmuster, Schnittstellen zuerst, kleine Dateien, Refactoring und Doku](0043-design-patterns-schnittstellen-kleine-dateien.md) | akzeptiert (2026-11-06) |
| 0044 | [Weitere Programme: Files, Kanban, Surveys, Gallery, Whiteboard, Streaming](0044-weitere-programme-und-reihenfolge.md) | **überholt durch ADR 0049** (2026-11-06) |
| 0045 | [Jedes Thema eine Schnittstelle; Schnittstellen sind Ziele; Hot-Plugins](0045-themen-schnittstellen-als-ziele.md) | akzeptiert (2026-11-06) |
| 0046 | [Speichern ist nicht Exportieren](0046-speichern-ist-nicht-exportieren.md) | akzeptiert (2026-11-06) |
| 0047 | [Kanidm hinter eigenem Wrapper](0047-kanidm-hinter-wrapper.md) | akzeptiert (2026-11-06) |
| 0048 | [Codecs ausgelagert, offene Codecs zuerst](0048-video-encoder.md) | akzeptiert (2026-11-06), die Abschnitte „Kontext“ und „Vorschlag“ sind Verlauf |
| 0049 | [Gesamtplan: Programme nach Zweck, Workbench und Suite](0049-gesamtplan-programme-nach-zweck.md) | akzeptiert (2026-11-06) |
| 0050 | [Ein Standard, ein Programm, eine Schnittstelle; `fs-contacts` heißt `fs-people`](0050-ein-standard-ein-programm.md) | akzeptiert (2026-11-06) |
| 0051 | [Releases: `fs-release`, nur kostenlose Wege, offene Signatur](0051-releases-nur-freie-wege.md) | akzeptiert (2026-11-06) |
| 0052 | [Eine Person mit Rollen; Rollen sind standardisiert oder selbst definiert; Vertrauen sichtbar machen](0052-personen-rollen-und-vertrauen.md) | akzeptiert (2026-11-06) |
| 0053 | [LLM-Chat als Component und Programm; Übersetzung vorerst nicht; Projektadresse](0053-llm-chat-und-uebersetzung.md) | akzeptiert (2026-11-06), Punkt 1 präzisiert durch ADR 0054 |
| 0054 | [KIs sind markierte Teilnehmer; der Assistent ist ein Messenger-Frontend](0054-kis-als-markierte-teilnehmer.md) | akzeptiert (2026-11-06) |
| 0055 | [Sprechende Namen statt IDs; `fs-groups` ist die Quelle der Wahrheit für Gruppen](0055-sprechende-namen-und-quellen-der-wahrheit.md) | akzeptiert (2026-11-06) |
| 0056 | [Oberster Admin; Agenten werden nie Admin; Workbench gibt Kontext; Kanidm flach](0056-admins-agenten-workbench-kanidm.md) | akzeptiert (2026-11-06) |
| 0057 | [Was ein Mensch liest, ist übersetzbar; die Bibliothek kommt später](0057-texte-uebersetzbar.md) | akzeptiert (2026-11-07) |
| 0058 | [Kontakte sind Profile](0058-user-und-kontakte-trennen.md) | Idee vom Nutzer (2026-11-07), Ausgestaltung Vorschlag bis zur Bestätigung |
| 0059 | [Verbinden ohne Server: jeder Client ist ein Knoten, iroh als Kandidat](0059-p2p-mit-iroh.md) | Richtung akzeptiert (Nutzer, 2026-11-07), nichts gebaut |
| 0060 | [Die Datenablage heißt `fs-objects`; `fs-store` wird der Laden](0060-fs-store-wird-fs-objects.md) | akzeptiert (Nutzer, 2026-11-07), Umbau nach dem Sprint |
| 0061 | [Facetten: ein Programm, mehrere Apps; jedes mit Admin-Frontend](0061-facetten.md) | akzeptiert (Nutzer, 2026-11-08) |
| 0062 | [Pakete liegen in Git: Katalog-Repo, ein Tag je Version, TUF, Spiegel überall](0062-paket-repos-in-git.md) | akzeptiert (Nutzer, 2026-11-08) |
| 0063 | [Ein Programm, ein Befehl: `fs-<programm>` mit Unterbefehlen](0063-ein-programm-ein-befehl.md) | akzeptiert (Nutzer, 2026-11-08) |
