# Empfehlung: fs-wiki-Frontend (Opus-Auswertung von BEFUND.md)

Stand: 2026-11-11. Grundlage ist `BEFUND.md` im selben Ordner. Punkte, die dort **[nicht belegt]** sind, bleiben unbelegt. Ich habe nichts aus dem Gedächtnis ergänzt.

## 1. Stichproben der Quellen (WebFetch, 2026-11-11)

| Quelle | Aussage im Befund | Ergebnis |
|---|---|---|
| Outline Revision History | Verlauf in der Seitenleiste, Diff, Wiederherstellen als neue Version, Version mindestens alle 5 Min., Löschen nur in Cloud/Lizenzedition | **bestätigt**, alle fünf Punkte |
| Obsidian Backlinks | Verknüpfte und unverlinkte Erwähnungen, Filter, Anzeige im Dokument, eigener Tab | **bestätigt** |
| Confluence Page History | Grün/Rot/Blau (Hinzugefügt/Gelöscht/Formatierung), Wiederherstellen als Kopie, endgültiges Löschen, Entwurf geht verloren | **bestätigt** |
| BookStack v26.05 | Eigene Rechte für Revisionen | **bestätigt**. Korrektur: "gebrochen" ist überzogen. Laut Upgrade-Hinweis haben manche Nutzer nach dem Upgrade *standardmäßig* keinen Zugriff mehr auf Revisionen. |
| Outline GitHub | BSL 1.1 | **bestätigt** |

Zwei Anmerkungen zum Befund:
- Fazit 4 widerspricht sich selbst ("nützlich, passt aber gut"). Gemeint ist offenbar: Include-Blöcke passen gut zu Blöcken.
- Docmost: Lizenz und Seitenrechte bleiben ungeprüft. Docmost ist deshalb nur Vorbild für das Layout (Details-Panel), nicht für Rechte.

## 2. Antworten auf die 10 Fragen

1. **Editor:** Der Block-Editor ist Standard. Markdown gibt es als Import/Export und zusätzlich als Quelltext-Ansicht desselben Dokuments, nicht als zweiten Editor. Grund: Save ≠ Export. Gespeichert wird im fs-store, Markdown ist nur Export. Zwei gleichwertige Editoren wie bei BookStack bedeuten doppelte Pflege.
2. **Verlauf:** Beides, in zwei Stufen. Die Seitenleiste zeigt die Versionsliste wie bei Outline. Ein Klick öffnet den Vergleich zweier frei wählbarer Versionen wie bei Confluence, mit Farben plus Symbol (+/−/~), damit der Vergleich nicht nur über Farbe lesbar ist. Wiederherstellen erzeugt immer eine neue Version und löscht nie.
3. **Unverlinkte Erwähnungen:** Ja, aber getrennt und eingeklappt unter den echten Rückverweisen, mit der Aktion "zu Link machen". Das ist günstig, weil die Suche ohnehin indexiert.
4. **Rechte-Ebenen:** Drei Ebenen: Wiki (Workspace), Bereich (Space/Sammlung) und Seite. Die Seite erbt standardmäßig, Ausnahmen sind möglich. Revisionen bekommen von Anfang an ein eigenes Recht, damit kein späteres Upgrade-Problem wie bei BookStack entsteht. Identität und Gruppen kommen über den Kanidm-Wrapper bzw. fs-groups. Die Vision legt die Ebenen nicht fest, das muss der Owner bestätigen.
5. **Rechte Spalte:** Tabs für Gliederung (Standard), Rückverweise, Verlauf und Kommentare. Kommentare stehen zusätzlich inline am Block.
6. **Kopf/Suche:** Vector 2022 dient als Gerüst (Navigation links, Suche oben, Werkzeuge rechts, Sticky-Header). Ein Aktionsmenü ersetzt die Tabs. Das ist eine Vorgabe für Variante A, nicht für alle Varianten.
7. **Include-Blöcke:** In v1 kommt nur "Seite/Block verlinken mit Vorschau" (Live-Referenz). Echtes Einbinden kommt in v1.1. Es braucht Regeln zu Rechten (Was sieht ein Leser ohne Recht auf die Quelle?) und Schutz vor Zyklen.
8. **Echtzeit:** Die Vision sagt "Live-Zusammenarbeit wie in Spielen", also ist Echtzeit das Ziel. Für v1 empfehle ich Präsenz (wer ist auf der Seite, wer bearbeitet welchen Block), Sperren pro Block und automatische Versionen. Volle gleichzeitige Bearbeitung (CRDT) kommt als eigener Sprung in v2. Das muss der Owner entscheiden.
9. **Lizenzen:** BSL (Outline) und AGPL (Wiki.js, AppFlowy) sind nur Gestaltungsvorbild: Muster beschreiben, keinen Code, keine Assets und keine CSS übernehmen. Das gilt laut Vision auch für MIT (BookStack). Proprietäre Produkte (Notion, Confluence, Obsidian) sind ebenso nur Vorbild für Funktionen.
10. **Zweiter Durchgang:** Ja, aber gezielt mit echten Demos/Instanzen: Notion, das Layout von Wiki.js 2.x, AppFlowy und zusätzlich die Lizenz von Docmost. Screenshots werden nur verlinkt. Das hat niedrige Priorität, weil die drei Varianten unten nicht davon abhängen.

## 3. Drei Frontend-Varianten (eine Engine, drei Frontends)

Alle drei Varianten nutzen dieselbe fs-wiki-Engine. **Pflicht in allen drei:**
- Verlauf mit Diff zweier Versionen. Wiederherstellen erzeugt eine neue Version.
- Rückverweise.
- Volltextsuche.
- Warnung vor Datenverlust, wenn beim Wiederherstellen ein Entwurf offen ist. Besser: der Entwurf wird automatisch als eigene Version gesichert.

### A: Klassisch / Vector-artig (Referenz-Wiki, öffentliches Wissen)

```
+----------------------------------------------------------------+
| Logo | [ Suche ............................ ] | Konto | Aktionen▾ |  <- Sticky-Header
+-----------+--------------------------------------+-------------+
| Navigation| Titel                     [Bearb.] ⋯ | Werkzeuge ▸ |
| - Bereiche| ------------------------------------ | Gliederung  |
| - Zuletzt | Inhalt (Block-Editor im Lesemodus)   | Rückverw.   |
| Inhalts-  |                                      | Verlauf     |
| verz. ▾   |                                      | Seiten-Info |
+-----------+--------------------------------------+-------------+
```
- Inhaltsverzeichnis links, einklappbar. Werkzeuge rechts, einklappbar. Der Verlauf öffnet sich als Vollseite: Versionsliste plus Vergleich zweier Versionen.
- Rückverweise im Werkzeug-Panel ("Links auf diese Seite").
- **Aufwand: mittel** (ca. 3–4 Wochen). Wenig Interaktion, viel Layout. Gut als erstes Referenz-Frontend.

### B: Vernetzt / Obsidian-artig (persönliches und Team-Wissen)

```
+----------+-------------------------------------+---------------+
| Baum     | [Tab Seite A][Tab Seite B][+]       | Rückverweise  |
| Bereiche | ----------------------------------- |  verlinkt (5) |
| Favoriten| Block-Editor, immer bearbeitbar     |  unverl. (3)▸ |
| -------- | /-Befehle, [[Link]]-Vervollst.      | Gliederung    |
| Suche ⌘K | ----------------------------------- | Lokaler Graph |
|          | Rückverweise (unten im Dokument)    | Verlauf       |
+----------+-------------------------------------+---------------+
```
- Mehrere Seiten in Tabs, Befehlspalette mit Suche (⌘K), `[[`-Verlinkung mit Vorschlägen.
- Rückverweise mit unverlinkten Erwähnungen und Filter. Der Verlauf liegt im rechten Panel (Liste), der Diff erscheint als Überlagerung im Editor.
- Der lokale Graph ist optional (v1.1).
- **Aufwand: hoch** (ca. 6–8 Wochen). Tabs, Vervollständigung, Erwähnungs-Index und Präsenz/Block-Sperren liegen hier.

### C: Einfach / Lesemodus (Einsteiger, Mobil, Kiosk)

```
+----------------------------------------+
| ☰  Titel der Seite          🔍   ✎     |
+----------------------------------------+
| Inhalt, eine Spalte, große Schrift     |
| ...                                    |
| ---------------------------------------|
| Verweise hierher: Seite X, Seite Y     |
| Zuletzt geändert: vor 2 Std. · Verlauf |
+----------------------------------------+
```
- Eine Spalte. Die Navigation sitzt im Schubladen-Menü, die Suche im Vollbild.
- Bearbeiten (✎) öffnet einen reduzierten Block-Editor.
- Der Verlauf zeigt eine einfache Liste. Der Diff kommt standardmäßig gegen die Vorversion, mit wählbarer Version.
- Rückverweise stehen am Seitenende.
- **Aufwand: niedrig** (ca. 2 Wochen). Dient auch als Gegenprobe: Lässt sich das Frontend tauschen, ohne die Engine zu ändern?

### Reihenfolge

Zuerst C, damit die Engine-Schnittstelle früh steht. Dann A als Referenz-Wiki, dann B. Alle Varianten in Blinc (Rust), Code komplett eigen.

## Offen für den Owner
- Frage 4 (Rechte-Ebenen) und Frage 8 (Echtzeit in v1 oder v2) sind echte Entscheidungen. Die Empfehlung oben ist nur ein Vorschlag.

---
# Befund (Haiku-Recherche)

# Befund: Vorbilder für das Wiki-Frontend (fs-wiki)

Stand: 2026-11-11. Quelle sind öffentliche Doku-Seiten, GitHub-READMEs und Suchtreffer. Nichts wurde installiert, keine Desktop-Sitzung benutzt, keine Bilder gespeichert. Punkte mit **[nicht belegt]** konnte ich nicht quellenseitig prüfen. Sie sind bewusst nicht aus dem Gedächtnis ergänzt.

## Vergleichstabelle

| Produkt | Layout | Bearbeiten | Verlauf / Diff | Suche | Verlinkung / Rückverweise | Rechte | Gut | Schlecht | Lizenz (belegt) |
|---|---|---|---|---|---|---|---|---|---|
| **Wiki.js 2.x** | Seitenbaum/Navigation laut Doku ("Navigation"-Guide); Layout-Details [nicht belegt] | Markdown, AsciiDoc, Visual Editor (Sekundärquelle, Doku-Seite "Editors" nicht lesbar) | Seiten-Historie mit Vergleich und Wiederherstellen (Doku-Index "Page History"); Diff-Details [nicht belegt] | Eingebaute DB-Suche, optional Elasticsearch/Algolia u. a. (Sekundärquelle) | Rückverweise [nicht belegt] | Admin > Permissions, Gruppen, Approvals für Vorschläge von Lesern (Doku-Index); "Page Rules" laut Sekundärquelle | Viele Editor-Optionen, Such-Backends wählbar | Schwer verifizierbar: Doku-Seiten meist nicht abrufbar; Version 3 ist Entwicklungsstand, kein Drop-in-Upgrade | AGPL-3.0 (GitHub) |
| **BookStack** | Hierarchie Regal > Buch > Kapitel > Seite; Sortieren über Verschieben [Layout-Details nicht belegt] | WYSIWYG als Standard, Markdown-Editor (CommonMark + Tabellen/Tasklisten) wählbar, Admin kann Standard setzen | Revisionen: ansehen, vergleichen, wiederherstellen; seit v26.05 eigene Rechte für Revisionen | Suche über Inhalte (Doku verweist nur auf Seite "Searching Content") | Include-Tags binden ganze Seiten oder Blöcke ein; Rückverweise laut Doku nicht auf der Seite | Rollen mit kombinierbaren Rechten; Anhänge folgen View-Recht der Seite | Klare Hierarchie; zwei Editoren; Wiederverwendung über Include | WYSIWYG-Standard; Revisions-Rechte nach Upgrade gebrochen (Release-Notes) | MIT (GitHub) |
| **Outline** | Sidebar mit Sammlungen (Collections), mehrstufig verschachtelbar | Markdown-Kürzel, Blockbearbeitung [Details nicht belegt] | Verlauf in Seitenleiste; Diff-Ansicht; Wiederherstellen erzeugt neue Version; Version mindestens alle 5 Min.; Export als Markdown/HTML; Löschen einzelner Versionen nur Cloud/Lizenz | Suche (Doku nicht im Detail gelesen) | Rückverweise ("References") automatisch unter Dokument | Rechte je Sammlung und Dokument (view/edit/admin), private Sammlungen, öffentliche Links mit Passwort | Verlauf mit Diff gut gelöst; Wiederherstellen non-destruktiv | Versionslöschung und Teile nur in Cloud/Lizenzedition | BSL 1.1 (GitHub) |
| **Notion** | Sidebar-Baum, Seiten in Seiten [nicht belegt, Quelle nicht abrufbar] | Block-Editor [nicht belegt] | [nicht belegt, Hilfeseite nicht abrufbar] | [nicht belegt] | [nicht belegt] | [nicht belegt] | Referenzprodukt für Block-UX | Proprietär, Cloud | proprietär |
| **Confluence** (Cloud/DC 11) | Seitenbaum, Seiten-Tools [nicht belegt] | Editor mit ungespeicherten Änderungen ("View changes" vor Veröffentlichung) | Seitenverlauf; Vergleichsansicht mit Farben (grün/rot/blau); Wiederherstellen erzeugt Kopie als neue Version; Versionen löschen endgültig | [nicht belegt] | [nicht belegt] | Seitenbeschränkungen (Verweis auf separaten Artikel) | Vergleichsansicht vorbildlich | Unveröffentlichte Entwürfe gehen bei Wiederherstellen verloren (Warnung) | proprietär |
| **Obsidian** | Rechte Seitenleiste mit Backlinks, Gliederung, Graph (nur Backlinks belegt) | Lokale Markdown-Notizen | Kein eingebauter Verlauf auf der Backlinks-Seite belegt | Suche [nicht belegt] | Backlinks mit Verknüpfungen **und** unverlinkten Erwähnungen; Panel filterbar; Pin-Tab je Notiz; Anzeige unten im Dokument | Keine Rechte-Ebene (lokale Dateien) [nicht belegt] | Backlinks mit unverlinkten Erwähnungen ist ein starkes Muster | Kein Mehrbenutzer-Modell in dieser Quelle | proprietär [nicht geprüft] |
| **MediaWiki Vector 2022** | Links Navigation + Inhaltsverzeichnis (einklappbar), Kopf mit Suche, rechts Seitenwerkzeuge (einklappbar), Sticky-Header | Tab "Bearbeiten" (Wikitext/VisualEditor) | Tab "Versionen" | Suche im Kopf | Werkzeugkasten: "Links auf diese Seite" | Rechte über Gruppen/Schutz [nicht vertieft] | Klare Trennung Navigation / Inhalt / Werkzeuge; bewährt | Tabs statt Aktionsmenü; Vector-2022-Editor-Layout nicht belegt | GPL (MediaWiki) [nicht vertieft] |
| **Docmost** | Spaces mit Seitenbaum; Details-Panel mit Rückverweisen | Block-Editor, Slash-Befehle/Markdown-Kürzel, Echtzeit-Mitbearbeitung | Versionsverlauf mit Wiederherstellen | Suche (Doku-Index "Search") | Rückverweise im Details-Panel | Spaces mit eigenen Rechten, Gruppen; **Seitenrechte laut Quellen Bezahlfunktion, Quellen widersprechen sich** | Echtzeit + Verlauf + Rückverweise, schlanker Aufbau | Seitenrechte evtl. Bezahl-Edition | [nicht geprüft] |
| **AppFlowy** | Workspace/Sidebar [nicht belegt] | Block-Editor (Doku nennt "Block" nur über Screenshot-Text) | [nicht belegt] | [nicht belegt] | [nicht belegt] | [nicht belegt] | Offline-fähig, Flutter/Rust, Datenbanken/Kanban | Doku-Seite lieferte kaum Funktionen | AGPLv3 (GitHub) |

## Fazit (10 Zeilen)

1. Verlauf mit Diff ist Pflicht: Outline (Versionen mit Diff, Wiederherstellen als neue Version) und Confluence (Vergleich farbig, Wiederherstellen als Kopie) sind die klarsten Vorbilder.
2. Zwei Editoren sind die übliche Lösung: BookStack bietet WYSIWYG und Markdown. Für fs-wiki wäre ein Block-Editor mit Markdown-Export die modernere Linie, muss aber gesondert entschieden werden.
3. Rückverweise sind Standard: Outline (References unter dem Dokument), Docmost (Details-Panel) und Obsidian (Panel mit unverlinkten Erwähnungen, das stärkste Muster).
4. Verlinkung über Include-Blöcke (BookStack) ist eine nützliche Idee für Wiederverwendung, passt aber gut zu fs-wikis Blöcken.
5. Navigation: Vector 2022 trennt Navigation links, Suche oben, Werkzeuge rechts, Inhaltsverzeichnis einklappbar. Das ist ein gutes Gerüst für die Vierteilung Seitenleiste/Kopf/Editor/rechte Spalte.
6. Rechte: Outline und BookStack arbeiten mit Rollen/Ebenen je Sammlung oder Seite. Docmost ist bei Seitenrechten uneinheitlich dokumentiert, deshalb hier nicht als Vorbild nehmen.
7. Vorsicht bei Lizenzen: Outline (BSL 1.1) ist kein freies Vorbild für Code-Übernahme. Wiki.js und AppFlowy (AGPL) sowie BookStack (MIT) sind lizenztechnisch leichter einzuordnen. Die FreeSynergy-Regel "kein Kopieren" gilt ohnehin, Muster sind frei nutzbar.
8. Die Doku mehrerer Vorbilder war nicht abrufbar (Notion, Wiki.js 2.x, BookStack-Layout). Vor Designentscheidungen sollten die Oberflächen in echten Instanzen oder Demos geprüft werden, nicht nur in Doku.
9. Bekannte Fehlerquellen: Entwürfe gehen verloren (Confluence-Warnung), Revisions-Rechte können nach Upgrade wegfallen (BookStack). Beides sollte fs-wiki von Anfang an richtig behandeln.
10. Noch offen ist eine Prüfung echter Oberflächen (Screenshots nur verlinken, nicht speichern), besonders Notion, Wiki.js 2.x und AppFlowy.

## Fragen für Opus

1. Soll fs-wiki einen Block-Editor als Standard haben, mit Markdown nur als Import/Export und Option, oder beides gleichwertig wie BookStack?
2. Soll die Verlaufsansicht Outline-artig (Sidebar) oder Confluence-artig (Vergleich zweier Versionen) sein?
3. Sollen Rückverweise auch unverlinkte Erwähnungen zeigen (Obsidian-Muster)?
4. Welche Rechte-Ebenen braucht fs-wiki: Workspace, Sammlung/Space, Seite? Gibt es Vorgaben aus dem Projektvision-Dokument?
5. Soll die rechte Spalte Rückverweise, Gliederung oder Kommentare enthalten?
6. Gibt es einen festen Vorgabe-Stil für Kopfzeile und Suche (Vector 2022 als Vorbild, ja oder nein)?
7. Sollen Include-Blöcke (Seite oder Block einbinden) in v1 sein?
8. Ist Zusammenarbeit in Echtzeit ein Muss für v1, oder reicht Sperren/Versionen?
9. Wie wird mit Lizenzen umgegangen, wenn ein Vorbild nur BSL hat (Outline)? Nur Muster, kein Code.
10. Sollen die nicht belegten Punkte (Notion, Wiki.js 2.x Layout, AppFlowy) in einem zweiten Durchgang mit echten Oberflächen geprüft werden?

## Quellen

- Outline Revision History: https://docs.getoutline.com/s/guide/doc/revision-history-AiL6p22Ssq
- Outline Diff-View (Changelog): https://www.getoutline.com/changelog/diff-view
- Outline GitHub (Lizenz BSL 1.1): https://github.com/outline/outline
- BookStack User-Doku: https://www.bookstackapp.com/docs/user/
- BookStack Release v26.05: https://www.bookstackapp.com/blog/bookstack-release-v26-05/
- BookStack GitHub (MIT): https://github.com/BookStackApp/BookStack
- Wiki.js Doku (Index): https://docs.js.wiki/
- Wiki.js GitHub (AGPL-3.0): https://github.com/requarks/wiki
- Docmost Doku: https://docmost.com/docs/
- Obsidian Backlinks: https://obsidian.md/help/Plugins/Backlinks
- Confluence Seitenverlauf und Vergleich: https://confluence.atlassian.com/doc/page-history-and-page-comparison-views-139379.html
- MediaWiki Vector 2022: https://www.mediawiki.org/wiki/Skin:Vector/2022
- MediaWiki Vector (Sidebar, Tabs): https://www.mediawiki.org/wiki/Help:Navigation
- AppFlowy GitHub (AGPLv3): https://github.com/AppFlowy-IO/AppFlowy
- Notion Seitenverlauf: nicht abrufbar (404), daher nicht belegt
- Sekundärquellen (nur Hinweise, nicht als Beleg): Wiki.js-Editoren und Suche über Verzeichnisseiten wie wikimatrix.org und g2.com; Docmost-Rechte über Drittseiten
