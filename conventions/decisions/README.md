# Beschlüsse (ADRs)

Nummerierte Entscheidungs-Records. Ein Beschluss ist unänderbar; Änderungen bekommen eine
neue Nummer und ersetzen die alte (Status `superseded by NNNN`).

Format: **Kontext → Entscheidung → Folgen**, plus Verweis auf betroffene Doku.

| Nr. | Titel | Status |
|-----|-------|--------|
| 0001 | Sechs Ebenen und Namen | akzeptiert |
| 0002 | Sprache: Identifikatoren englisch, Prosa deutsch | teilweise ersetzt durch 0011 |
| 0003 | Repo-Schale und Skript-Schattenbaum | akzeptiert |
| 0004 | Komponenten-Einteilung primitives/widgets/workbenches | akzeptiert |
| 0005 | App und Widget: derselbe Kern, unterschiedliche Ebene | akzeptiert |
| 0006 | Haken, Abbruchkriterium, Pflichtmenge pro Kategorie | teilweise ersetzt durch 0013 |
| 0007 | `skins/` wird `masks/` | superseded by 0012 |
| 0008 | Englisch zuerst, Deutsch zweite Sprache | superseded by 0011 |
| 0009 | GUI: Blinc ist gesetzt | akzeptiert |
| 0010 | Ein Prüfer für die Übersetzung: `scripts/doc_sync.py` | akzeptiert |
| 0011 | Nur Englisch wird gepflegt, Deutsch wird übersetzt | akzeptiert |
| 0012 | `masks/` wird `frontends/`, mit Versionsordner | akzeptiert |
| 0013 | Funktionen analysieren, nichts kopieren; Programme nach Ideen | akzeptiert |
| 0014 | Standards zuerst, ActivityStreams 2.0 als Basis | akzeptiert |
| 0015 | Fremdprojekte, die wir nutzen und unterstützen; Crate-Regel | akzeptiert |
| 0016 | Lizenz: MIT OR Apache-2.0, für immer kostenlos | akzeptiert |
| 0017 | Programme heißen nach Kategorie, ein Repo pro Programm | akzeptiert |
| 0018 | Messenger umfasst E-Mail und Chats; nur verschlüsselt; Backend-Stufenplan | akzeptiert |
| 0019 | Datenhaltung: `fs-store` je Programm, `fs-hub` je Gerät | akzeptiert |
| 0020 | Speicherformat: AS2-Hülle + Fachstandard + Protokoll; Leihen = Live-Verweis | akzeptiert |
| 0021 | Schnittstelle: ein Vertrag (Cap'n Proto), viele Zugänge | akzeptiert |
| 0022 | Zwei Referenz-Frontends je Programm | superseded by 0038 |
| 0023 | Darstellungs-Register; Code- und Block-Editor | Punkt 4 ersetzt durch 0039 |
| 0024 | Programm ohne Hub, Verschlüsselung, Schlüsseltresor, SCIM | akzeptiert |
| 0025 | Abschauen nur im äußersten Notfall, nie bei Closed Source | akzeptiert |
| 0026 | Immer die neueste Technik | akzeptiert |
| 0027 | IDs: UUIDv7 (RFC 9562) | akzeptiert |
| 0028 | Namen, Domains, Erreichbarkeit über den Hub (`freesynergy.net`) | akzeptiert (Technik: Vorschlag) |
| 0029 | Schutzbedürftige Daten müssen gekennzeichnet werden | akzeptiert (Form: Vorschlag) |
| 0030 | Original + Hülle: Empfangenes unverändert aufbewahren | akzeptiert |
| 0031 | Jeder Text ist ein Wiki-Eintrag; Bibliothek; Hilfe dort, wo man ist | akzeptiert (Standards offen) |
| 0032 | name-Regel; Beschlossenes bleibt | akzeptiert |
| 0033 | Markieren: ein Mechanismus (Punkt = einsetzen, Bereich = ersetzen/benennen) | akzeptiert |
| 0034 | Textstruktur technisch: Absatz, Seite, Kollektion, Regal | akzeptiert |
| 0035 | Föderation zwischen Instanzen: OpenID Federation 1.0 | akzeptiert |
| 0036 | Git als dezentrale Verteilung (gix): Pakete, Themes, Programme, Medien | akzeptiert |
| 0037 | Jedes Programm ist mindestens eine Workbench; Programme zeigen sich gegenseitig an | akzeptiert |
| 0038 | Referenz-Frontends: vier Arten, am besten ganze Suiten | akzeptiert |
| 0039 | Drei Text-Editoren | akzeptiert |
| 0040 | Cap'n-Proto-Schema-Compiler in reinem Rust; Anerkennung ohne Drama | akzeptiert |
| 0041 | Rust-Hygiene: Build-Ausgabe klein, nie in Git, regelmäßig aufräumen | akzeptiert |
| 0042 | Text + Ebenen; Datenbank ist die Wahrheit, Dateien sind Exporte; begrenztes dauerhaftes Rückgängig | akzeptiert |
| 0043 | Entwurfsmuster, Schnittstellen zuerst, kleine Dateien, Refactoring, Doku | akzeptiert |
| 0044 | Weitere Programme: Files, Kanban, Surveys, Gallery, Whiteboard, Streaming | überholt durch 0049 |
| 0045 | Jedes Thema eine Schnittstelle; Schnittstellen sind Ziele; Hot-Plugins | akzeptiert (Form der Plugins: Vorschlag) |
| 0046 | Speichern ist nicht Exportieren | akzeptiert (Details: Vorschlag) |
| 0047 | Kanidm hinter eigenem Wrapper | akzeptiert (ergänzt 0024) |
| 0048 | Codecs ausgelagert, offene Codecs zuerst | akzeptiert |
| 0049 | Gesamtplan: Programme nach Zweck, Workbench und Suite | akzeptiert |
| 0050 | Ein Standard, ein Programm, eine Schnittstelle; `fs-contacts` heißt `fs-people` | akzeptiert (Abgrenzung: Vorschlag) |
| 0051 | Releases: `fs-release`, nur kostenlose Wege, offene Signatur | akzeptiert |
| 0052 | Eine Person mit Rollen; Rollen standardisiert oder selbst definiert; Vertrauen sichtbar machen | akzeptiert |
| 0053 | LLM-Chat als Component und Programm; Übersetzung vorerst nicht; Projektadresse | akzeptiert |
| 0054 | KIs sind markierte Teilnehmer; der Assistent ist ein Messenger-Frontend | akzeptiert (Aussperren: vorerst bestätigt; Identität offen) |
| 0055 | Sprechende Namen statt IDs; `fs-groups` ist die Quelle der Wahrheit für Gruppen | akzeptiert |
| 0056 | Oberster Admin; Agenten werden nie Admin; Workbench gibt Kontext; Kanidm flach | akzeptiert |
| 0057 | Was ein Mensch liest, ist übersetzbar; Bibliothek `mf2` | akzeptiert |
| 0058 | Kontakte sind Profile; Verknüpfen nur nach Rückfrage | akzeptiert |
| 0059 | Verbinden ohne Server: jeder Client ist ein Knoten, iroh als Kandidat | Richtung akzeptiert, nichts gebaut |
| 0060 | Die Datenablage heißt `fs-objects`; `fs-store` wird der Laden | akzeptiert, Umbau nach dem Sprint |
| 0061 | Facetten: ein Programm, mehrere Apps; jedes mit Admin-Frontend | akzeptiert |
| 0062 | Pakete liegen in Git: Katalog-Repo, ein Tag je Version, TUF, Spiegel überall | akzeptiert |
| 0063 | Ein Programm, ein Befehl: `fs-<programm>` mit Unterbefehlen; Facetten als Link `fs-<facette>` | akzeptiert |
| 0064 | Versionsnummern beginnen bei 0.0.1; 0.1.0 erst nach Handtest | akzeptiert |
| 0065 | Ein Standard für jedes Fenster: Menü, Version, Hilfe, Meldungen | akzeptiert im Grundsatz |
| 0066 | Datentypen mit festen Components, vier Frontends je Programm | akzeptiert |
| 0067 | Tresor `fs-vault`; Server hält nur Verschlüsseltes, Gruppenschlüssel (MLS), Suche auf dem Gerät | akzeptiert |
| 0068 | Fähigkeiten statt fester Anforderungen (provides/requires); fremde Pakete gespiegelt samt Quellcode; `catalog.freesynergy.net` | akzeptiert |
| 0069 | Update schließt ein laufendes Programm und startet es am selben Punkt neu (Sitzungsdatei, automatisches Speichern, Klon, `suspend_and_exit()`) | akzeptiert (Strategie); F1 entschieden (Nutzer, ja) |
| 0070 | Thema `storage`: ein Baum für alles, worauf man Zugriff hat (`StorageProvider` neben `BlobBackend`) | akzeptiert (Strategie); Code erst nach 3b grün |
| 0071 | Versionen, Git und Backup in Files (drei Schichten; `versions` aus 0070 erweitert; Ergänzung 2026-11-12: Platz-Profile, Backup-Ziele, Git-Nebenfenster, Backup in jedem Programm) | akzeptiert (Strategie); Code erst nach 3b und Wiki/Groups |
| 0072 | Blöcke als Quelle für Texte: Handbuch im Wiki, Store-Beschreibung und Hilfe daraus; Kopie im Paket | akzeptiert (Strategie); Code nach 3b und Wiki |
| 0073 | Kollaboration überall mit Loro (Awareness, AS2-Änderungsstrom, Rechte vor Import, „wirklich löschen“) | Entwurf |
| 0074 | Stil, Bausteine, Bewegung, Klang und Menüs: getrennte Schichten aus Standards | akzeptiert (Gründer); Code nach dem Meilenstein „Wir benutzen es selbst“ |
| 0075 | fs-marketplace als Programm, der Store als Facette | akzeptiert (Gründer); Code nach dem Meilenstein „Wir benutzen es selbst“ |
| 0076 | Das Grundmodell: Akteure, Ressourcen, Orte, Zeit, Ziele, Abläufe, Ereignisse | akzeptiert (Gründer) |
| 0077 | Katalog-Arten (`kind`) und Store-Gruppen; Server nur mit rpm/deb | akzeptiert (Strategie); Nutzerregel: alle Server in den Katalog, überall installierbar |
| 0078 | Paketquellen apt/dnf: ein Repo `fs-packages`, getrennt vom Katalog | akzeptiert (Strategie) |
| 0079 | `fs-server`: Server einrichten und verwalten, jeder Schritt protokolliert | akzeptiert (Strategie); Nutzerentscheidung 14.11. |
| 0080 | Umzug fs-wiki → fs-text: Repo, Crates, Version, Daten, Katalog | akzeptiert (Strategie); Nutzer-JA zu Umbenennung/Löschen und „Projekt“ |
| 0081 | CI-Ereignisse (CloudEvents) ≠ Programm-Ereignisse (AS2, fs-history); Pull ohne Token, Rot-Issues | akzeptiert (Strategie, 2026-11-14) |
| 0082 | `fs-server` verbindet: Konfiguration von außen (Typbeschreibung), Adapter je Server (Kanidm, Zentinel, später Mail) | akzeptiert (Strategie, 2026-11-14; Nutzerentscheidung Vermittler + People/Groups mit Kanidm) |
| 0084 | Editor-Bausteine: ein Vertrag (`TextEditor`, nur Änderungs-Operationen), Umsetzungen Block/RichText/Markdown, gemeinsame Konformitätssammlung | akzeptiert (Strategie, 2026-11-14; Nutzerentscheidung: mehrere Editor-Bausteine, Daten nur über unser Modell) |
| 0085 | Normalisierung an der Grenze: Zeiten (UTC plus IANA-Zonen-Id, Datum ohne Uhrzeit), Personen (Verweis auf People, eingefrorener Abzug), Importer/Exporter als Grenz-Adapter | Entwurf (Strategie, 2026-11-14; Nutzerregeln) |
