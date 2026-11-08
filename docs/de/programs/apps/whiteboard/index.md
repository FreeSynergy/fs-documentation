# Whiteboards

## Kurz gesagt

Whiteboard ist eine endlose Fläche für Ideen. Du legst Seiten, Formen, Texte, Verbindungen und Zeichnungen ab, und mehrere Personen können dieselbe Fläche gleichzeitig ändern. Es beantwortet die Frage: Wie denken wir gemeinsam an einem Bild, ohne uns gegenseitig im Weg zu stehen?

**Befehl:** `fs-whiteboard`, ein Befehl je Programm mit Unterbefehlen ([ADR 0063](../../../decisions/0063-ein-programm-ein-befehl.md); Programme werden umgestellt, wenn sie ohnehin angefasst werden, nicht jedes ist es schon).

## Was hier anders ist

- Wenn zwei Personen dieselbe Fläche ändern, werden die Änderungen Eigenschaft für Eigenschaft zusammengeführt. Verschiebst du eine Form, während jemand anderes sie umfärbt, bleiben beide Änderungen erhalten.
- Das Zusammenführen hängt nicht von der Reihenfolge ab, in der Änderungen eintreffen. Eigenschaftstests prüfen das.
- Dein Rückgängig macht nur deine eigenen Schritte. Es überspringt eine Eigenschaft, die seitdem jemand anderes geändert hat.
- Eine Fläche lässt sich als SVG exportieren.
- Whiteboard besitzt seine eigene Schnittstelle, `whiteboard.capnp` in `fs-interfaces`. Sie ist ein Entwurf und als vorläufig markiert.

## Wo es heute steht

Neueste Version: `v0.2.0` (Stufe 1 des Entwurfs). Es gibt **noch kein Fenster und noch keinen Server.**

Heute funktioniert der Kern: Flächen, Seiten und jede Art von Element aus dem Vertrag; das Zusammenführen von Änderungen aus zwei Richtungen; Rückgängig für jede Bearbeitung; Gruppen, Kopieren, Ausrichten, Sperren und Umordnen; ein schnelles Finden dessen, was im Sichtbereich liegt; und der Export nach SVG. PNG- und PDF-Export antworten „nicht möglich“. Es gibt 104 Tests mit echten Speichern, und ein unabhängiger Prüfer hat es in mehreren Runden kontrolliert.

Noch nicht vorhanden: Nichts überträgt Änderungen zwischen Geräten, daher wird das Zusammenführen nirgends genutzt. Live-Anwesenheit, Freigabe, Bibliotheken, Vorlagen und Kommentare sind geplant, aber noch nicht gebaut.

**Status: erster Kern `v0.2.0` in [`fs-whiteboard`](https://github.com/FreeSynergy/fs-whiteboard), noch kein Fenster (Stufe 1).** Siehe das [Design](design.md), die [Anforderungen](requirements.md) und die [Roadmap](../roadmap.md).

## Übersicht

Dieser Bereich enthält Dokumentation für verschiedene Whiteboard- und Kollaborationswerkzeuge.

## Verfügbare Systeme

- **mural** - Visuelle Kollaborationsplattform
- **miro** - Online-Whiteboard für Teamzusammenarbeit
- **excalidraw** - Kollaboratives Whiteboard
- **figma** - Werkzeug für Oberflächendesign mit Whiteboard-Funktionen
- **jamboard** - Googles digitales Whiteboard
- **leantime** - Open-Source-Projektmanagement mit Whiteboard
- **stormboard** - Kollaboratives Brainstorming-Werkzeug
- **whimsical** - Visuelle Zusammenarbeit für Teams
- **gitmind** - Mind-Mapping-Werkzeug
- **mindmeister** - Online-Mind-Mapping

## Was ist ein Whiteboard?

Ein Whiteboard ist ein digitales Werkzeug für visuelle Zusammenarbeit und Brainstorming. Whiteboards ermöglichen:

- Visuelles Brainstorming und Ideensammlung
- Zusammenarbeit in Echtzeit
- Mind-Mapping und Konzeptentwicklung
- Erstellen von Diagrammen und Flussdiagrammen
- Nutzen von Vorlagen und fertigen Layouts
- Unterstützung für Remote-Arbeit

## Anwendungsbereiche

- **Brainstorming**: Ideen sammeln und entwickeln
- **Produktplanung**: Produktfunktionen planen
- **Projektmanagement**: Aufgaben und Prozesse sichtbar machen
- **Workshops**: Workshops und Retrospektiven
- **Teambesprechungen**: Visuelle Zusammenarbeit im Team
- **Bildung**: Bildung und Lehre

## Vorteile von Whiteboards

- **Visuelle Klarheit**: Komplexe Konzepte sichtbar machen
- **Zusammenarbeit**: Zusammenarbeit in Echtzeit
- **Flexibilität**: Unbegrenzte Anpassung und Bearbeitung
- **Remote-Arbeit**: Ideal für verteilte Teams
- **Vorlagen**: Vorgefertigte Vorlagen
- **Integration**: Verbindung mit anderen Werkzeugen

## Auswahlkriterien

Bei der Wahl eines Whiteboard-Werkzeugs solltest du folgende Kriterien berücksichtigen:

- **Funktionen**: Welche Funktionen werden benötigt?
- **Bedienbarkeit**: Wie benutzerfreundlich ist es?
- **Zusammenarbeit**: Wie gut funktioniert die Zusammenarbeit in Echtzeit?
- **Integration**: Wie gut passt das System in die bestehende Infrastruktur?
- **Preis**: Kostenlos oder kostenpflichtig?
- **Sicherheit**: Datenschutz und Sicherheit

## Verwandte Kategorien

- [Projektmanagement](../../suites/projectmanagement/) - Werkzeuge für Projektmanagement
- [Helpdesk](../helpdesk/) - Support- und Ticketsysteme
- [Messenger](../messenger/) - Kommunikation und Chat

## Schnellstart

1. **Whiteboard auswählen**: Wähle ein Whiteboard passend zu deinen Anforderungen
2. **Installation/Konto**: Werkzeug installieren oder Konto anlegen
3. **Vorlagen nutzen**: Greife auf vorgefertigte Vorlagen zurück
4. **Team einladen**: Lade deine Teammitglieder ein
5. **Brainstorming starten**: Starte die erste Sitzung

## Mehr Informationen

Weitere Informationen findest du in der Dokumentation der einzelnen Whiteboard-Werkzeuge.

## Frontends

<!-- gen:frontends (scripts/gen_frontend_indexes.py) — Änderungen darin werden überschrieben -->
Analysierte Programme (6), nach Funktion, nichts kopiert (ADR 0012/0013):

- [draw.io](frontends/drawio/index.md) — draw.io (diagrams.net) ist ein freies Diagrammwerkzeug für Flussdiagramme, Netzwerkpläne, UML und BPMN.
- [Excalidraw](frontends/excalidraw/index.md) — Excalidraw ist ein freies, quelloffenes kollaboratives Whiteboard im handgezeichneten Stil.
- [Miro](frontends/miro/index.md) — Miro ist das kommerzielle Online-Whiteboard (SaaS) für visuelle Zusammenarbeit: unendliche Fläche, Formen und Haftnotizen, Frames, Vorlagenbibliothek (Retros, Workshops, Customer Journeys), Abstimmung/Timer und boa…
- [Mural](frontends/mural/index.md) — Mural ist die Workshop-Whiteboard-Suite (SaaS) mit starker Moderationsunterstützung: Fläche mit Formen und Notizen, „Facilitation Sequence“ (Moderationsabläufe), Teilnahmesteuerung und Vorlagen.
- [OpenBoard](frontends/openboard/index.md) — OpenBoard ist ein freies interaktives Whiteboard-Werkzeug (C++, Qt) für Unterricht und Präsentationen: mehrseitige „Boards“, Stifte, Text und Bilder, integrierter Browser, Dokument- und Notizwerkzeuge, offline-first mit einem lo…
- [tldraw](frontends/tldraw/index.md) — tldraw ist eine quelloffene Bibliothek und App für Whiteboards mit unendlicher Fläche in TypeScript: einsatzbereit auf tldraw.com und als React-SDK (`tldraw`) für eigene Canvas-Anwendungen.

Übersicht: [frontends](frontends/index.md)
<!-- /gen:frontends -->
