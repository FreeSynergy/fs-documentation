# Wiki-Systeme

## Kurz gesagt

FreeSynergy Wiki macht aus Texten miteinander verbundene Seiten. Seiten verlinken sich gegenseitig, und du siehst, was auf eine Seite verweist. Es beantwortet die Frage: Wo leben die Dinge, die wir schreiben, damit wir sie finden, verlinken und pflegen können?

**Befehl:** `fs-wiki`, ein Befehl je Programm mit Unterbefehlen ([ADR 0063](../../../decisions/0063-ein-programm-ein-befehl.md); Programme werden umgestellt, wenn sie ohnehin angefasst werden, nicht jedes ist es schon).

## Was hier anders ist

- Ein Text wird als Text plus Schichten gespeichert, nicht als eine flache Datei. Die Datenbank ist die Wahrheit, und Dateien sind Exporte.
- Speichern ist nicht Exportieren: Nichts wird in deine Dateien geschrieben, bis du auf Exportieren drückst. Wenn sowohl die Datei als auch die Datenbank geändert wurden, zeigt dir das Programm den Konflikt, statt eines von beiden zu überschreiben.
- Du kannst einen Ordner mit Markdown-Dateien importieren, im Programm bearbeiten und Markdown erneut exportieren, wenn du dich dafür entscheidest.
- Wiki besitzt die offene Textschnittstelle, sodass andere Programme über eine Schnittstelle auf Texte zugreifen können, statt ein eigenes Textmodell zu führen.

## Wo es heute steht

Neueste Version: `v0.4.0`. Du kannst Texte nach Pfad anlegen, bearbeiten, verschieben, löschen und auflisten, mit Links, Rückverweisen und Suche. Beim Verschieben eines Textes oder Ordners werden die Links darauf umgeschrieben. Markdown lässt sich importieren und exportieren. Ein Überschreiben wird abgelehnt, wenn jemand anderes zuerst gespeichert hat, und andere Programme werden benachrichtigt, wenn sich ein Text ändert. Ein kleiner Server bietet all das über einen lokalen Socket an. Es gibt ein erstes Fenster, den Leser: einen Seitenbaum, Lesen mit Formatierung, Folgen von Links, Zurück, Suche, Bearbeiten und Speichern sowie eine Schaltfläche Exportieren. Ungespeicherte Entwürfe werden gesichert und nach einem Absturz wieder angeboten. Der erste Start importiert einen Dokumentationsordner (etwa 30 Sekunden für 1.400 Seiten).

Noch nicht vorhanden (geplant): Das Tippen im echten Fenster ist durch Tests nicht geprüft; keine weiteren Editoren, keine Sammlungen oder Regale, keine Vorlagen im Programm. Die Bearbeitungssperre funktioniert nur innerhalb eines einzelnen Prozesses. Einige Zeichen (bestimmte Emojis) erscheinen als Kästchen, und sehr breite Tabellen können über den Rand hinausragen. Die Schnittstelle ist ein Entwurf ohne bisherigen Verbraucher.

## Übersicht

Dieser Bereich enthält Dokumentation für verschiedene Wiki-Systeme und Wissensplattformen.

## Verfügbare Systeme

- **wikijs** - Modernes, leichtgewichtiges Wiki mit Markdown-Unterstützung
- **xwiki** - Enterprise-Wiki mit Erweiterungen und Makros
- **mediawiki** - Die Wiki-Engine von Wikipedia
- **tango** - Klicks in Schritt-für-Schritt-Anleitungen erfassen (tango.ai, kein Wiki)
- **notion** - All-in-one-Arbeitsbereich mit Wiki-Funktionen
- **confluence** - Teamzusammenarbeit von Atlassian
- **vscodium** - VS Code ohne Telemetrie (für das lokale Hosten eines Wikis)
- **dokuwiki** - Einfaches dateibasiertes Wiki
- **mediagoblin** - Föderierte Plattform für Medien-Hosting

## Was ist ein Wiki?

Ein Wiki ist ein kollaboratives Web-System zum Erstellen, Bearbeiten und Ordnen von Wissensdatenbanken, Dokumentationen oder gemeinschaftlichen Texten. Wiki-Systeme zeichnen sich aus durch:

- Einfaches Bearbeiten über die Weboberfläche
- Versionsverlauf und Revisionen
- Kategorisierung und Verlinkung von Inhalten
- Benutzerrollen und Berechtigungssysteme
- Suchfunktionen und Indexierung

## Anwendungsbereiche

- **Technische Dokumentation**: Projektdokumentation, API-Dokumentation
- **Wissensmanagement**: Firmen-Wikis, Wissensdatenbanken
- **Bildung**: Lehrmaterialien, Kursdokumentation
- **Community-Projekte**: Open-Source-Dokumentation, gemeinschaftliche Wikis

## Auswahlkriterien

Bei der Wahl eines Wiki-Systems solltest du folgende Kriterien berücksichtigen:

- **Funktionen**: Welche Funktionen werden benötigt?
- **Skalierbarkeit**: Wie viele Benutzer und Seiten?
- **Integration**: Wie gut passt das System in die bestehende Infrastruktur?
- **Bedienbarkeit**: Wie benutzerfreundlich ist es?
- **Kosten**: Selbst gehostet oder Cloud-Dienst?
- **Open Source**: Sind die Lizenzbedingungen geeignet?

## Verwandte Kategorien

- [Messenger](../messenger/) - Kommunikation und Chat
- [Helpdesk](../helpdesk/) - Support- und Ticketsysteme
- [Projektmanagement](../../suites/projectmanagement/) - Aufgaben- und Projektverwaltung
- [Desktop](../../platform/desktop/) - Desktop-Anwendungen für die Arbeit mit Wikis

## Schnellstart

1. **Wiki auswählen**: Wähle ein System passend zu deinen Anforderungen
2. **Installation**: Selbst hosten oder einen Cloud-Dienst nutzen
3. **Konfiguration**: Passe das System an und konfiguriere es
4. **Inhalte erstellen**: Lege die ersten Wiki-Seiten an
5. **Benutzer einladen**: Lade Teammitglieder ein und vergib Berechtigungen

## Mehr Informationen

Weitere Informationen findest du in der Dokumentation der einzelnen Wiki-Systeme.

## Frontends

<!-- gen:frontends (scripts/gen_frontend_indexes.py) — Änderungen darin werden überschrieben -->
Analysierte Programme (8), nach Funktion, nichts kopiert (ADR 0012/0013):

- [Confluence](frontends/confluence/index.md) — Confluence ist eine Team-Wiki- und Kollaborationslösung von Atlassian.
- [MediaWiki](frontends/mediawiki/index.md) — MediaWiki ist die Wiki-Engine hinter Wikipedia und den anderen Wikimedia-Projekten.
- [Notion](frontends/notion/index.md) — Notion ist ein gehosteter All-in-one-Arbeitsbereich für Notizen, Dokumente und Datenbanken, aufgebaut aus typisierten Blöcken.
- [Tango](frontends/tango/index.md) — Tango verwandelt aufgezeichnete Klicks in Schritt-für-Schritt-Anleitungen; kein Wiki, dokumentiert wegen seiner Idee von der Erfassung bis zur Anleitung.
- [Tango.io](frontends/tango.io/index.md) — Tango.io ist eine moderne Plattform für Wissensmanagement mit Schwerpunkt auf Zusammenarbeit.
- [VSCodium](frontends/vscodium/index.md) — VSCodium ist eine quelloffene Version von Microsoft Visual Studio Code.
- [Wiki.js](frontends/wikijs/index.md) — Wiki.js ist eine quelloffene, selbst gehostete Wiki-Engine.
- [XWiki](frontends/xwiki/index.md) — XWiki ist eine leistungsstarke Enterprise-Wiki-Plattform mit erweiterten Funktionen für Wissensmanagement.

Übersicht: [frontends](frontends/index.md)
<!-- /gen:frontends -->
