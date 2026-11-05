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
| 0022 | Zwei Referenz-Frontends je Programm | akzeptiert |
| 0023 | Darstellungs-Register; Code- und Block-Editor | akzeptiert |
| 0024 | Programm ohne Hub, Verschlüsselung, Schlüsseltresor, SCIM | akzeptiert |
| 0025 | Abschauen nur im äußersten Notfall, nie bei Closed Source | akzeptiert |
| 0026 | Immer die neueste Technik | akzeptiert |
| 0027 | IDs: UUIDv7 (RFC 9562) | akzeptiert |
| 0028 | Namen, Domains, Erreichbarkeit über den Hub (`freesynergy.net`) | akzeptiert (Technik: Vorschlag) |
| 0029 | Schutzbedürftige Daten müssen gekennzeichnet werden | akzeptiert (Form: Vorschlag) |
| 0030 | Original + Hülle: Empfangenes unverändert aufbewahren | akzeptiert |
| 0031 | Jeder Text ist ein Wiki-Eintrag; Bibliothek; Hilfe dort, wo man ist | akzeptiert (Standards offen) |
