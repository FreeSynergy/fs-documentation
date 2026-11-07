# MediaWiki 1.46 — Abhängigkeiten von unseren Komponenten

Zweck: auflisten, welche UI-Komponenten und welche Operationen unseres Textvertrags (`/srv/FreeSynergy/fs-interfaces/schema/texts.capnp`, DRAFT 0.1, 2026-11-06) ein Frontend im MediaWiki-Stil benötigt.

## Vertrag wie er steht (texts.capnp, Schnittstelle `Texts`)

Vorhandene Operationen: `supportReport`, `create`, `edit`, `move`, `delete`, `get`, `getByPath`, `list` (prefix + cursor), `find` (term + cursor), `links`, `backlinks`, `importText`, `exportText`, `subscribe`, `moveFolder`, `editIf` (Compare-and-set auf `revision`).

Eintragsform: `TextEntry` mit `envelope` (AS2), `path`, `document` (JSON), `revision`. Links: `LinkRow` mit `source`, `target` (Pfad), `at`.

## Benötigte UI-Komponenten (MediaWiki-Stil) und was sie vom Vertrag brauchen

| UI-Komponente (MediaWiki-Entsprechung) | Benötigt | Von texts.capnp bereitgestellt | Lücke |
|----------------------------------------|----------|--------------------------------|-------|
| Seitenansicht (Lesen) | Abruf nach ID oder Pfad, gerenderter Inhalt | `get`, `getByPath`, `exportText` (für Markdown oder HTML) | Rendern nach HTML ist nicht im Vertrag; `exportText` nimmt einen Medientyp, daher muss der Anbieter `text/html` unterstützen |
| Seiteneditor (Quelltext) | Abruf, Bearbeiten mit Compare-and-set | `get`, `editIf` | keine für einfaches Bearbeiten |
| Behandlung von Bearbeitungskonflikten | Revisionsnummer, Konfliktgrund | `editIf` (Präfix `conflict:`) | Der Grund ist ein Text; kein maschinenlesbares Konfliktfeld. Akzeptabel, wenn das Präfix ein stabiler Vertragsbestandteil ist. |
| Seite erstellen | Erstellen mit Pfad und Markdown | `create` | Erstellen nimmt Markdown; die Dokumentform wird nicht akzeptiert. Mit dem Eigentümer abstimmen. |
| Seite verschieben / umbenennen | Verschieben mit Linkfolge | `move`, `moveFolder` | keine |
| Seite löschen | Löschen nach ID | `delete` | Löschen ist im Vertrag endgültig; keine Papierkorb- oder Wiederherstellungsoperation (MediaWiki hat delete und undelete) |
| Seitenverlauf (Liste der Versionen) | Liste früherer Versionen mit Autor und Zeit | keine | Fehlt. `TextEntry` hat nur die aktuelle Revisionsnummer. |
| Unterschied zwischen zwei Versionen | Version nach Nummer abrufen, vergleichen | keine | Fehlt. |
| Ältere Version wiederherstellen | Alte Version abrufen, als neue schreiben | keine | Fehlt. |
| Liste der letzten Änderungen | Änderungsfeed mit Filtern | `subscribe` (ChangeListener) | Der Vertrag hat keine Abfrage für "letzte Änderungen" mit Zeitfenster und Filter; `subscribe` liefert Ereignisse, keine Liste. |
| Beobachtungsliste | Beobachtungsmenge pro Benutzer, Liste beobachteter Texte, beobachten und nicht mehr beobachten | keine | Fehlt: beobachten, nicht mehr beobachten, Liste und Benutzeridentität im Vertrag. |
| Diskussionsseite zu einem Text | gepaarter Diskussionstext, Namensraummodell | keine | Fehlt. Der Vertrag hat nur Pfade; eine Diskussions-Namensraum- oder Paarungsregel ist nötig. |
| Namensräume | Liste der Namensräume, Namensraum eines Pfads | keine (Präfix in `list`) | Fehlt als explizites Konzept. Präfix-Auflistung kann es nachbilden, nicht aber die Namensraumregeln. |
| Kategorien | Kategorien eines Textes, Mitglieder einer Kategorie | keine | Fehlt. |
| Kategorieseite | Liste der Kategoriemitgliedschaften | keine | Fehlt. |
| Vorlagen (Transklusion) | Liste der von einem Text verwendeten Vorlagen, Transklusionsabhängigkeiten | keine | Fehlt. Der Vertrag hat nur Links, keine Transklusionen. |
| Rückverweise | Seiten, die auf einen Text verlinken | `backlinks` | keine |
| Links auf diese Seite (Spezialseite) | Rückverweise mit Fundstelle | `backlinks` (`LinkRow.at`) | keine |
| Weiterleitungen | Weiterleitungsquelle und -ziel | keine | Fehlt. |
| Suche | Titel und Volltext, seitenweise | `find` | Fehlt: Ausschnitt und Hervorhebung in Suchergebnissen. Seitenweise Abfrage ist vorhanden. |
| Suchvorschläge (Typeahead) | Präfixsuche, schnell | `list` mit Präfix oder `find` | Präfixsuche nach Titel als eigene Operation ist nicht im Vertrag. |
| Spezialseiten (Listen verwaister Seiten, fehlender Links, langer Seiten) | serverseitige Abfragen | keine | Fehlt: es sind Berichte; eine Berichtsoperation wird benötigt, falls wir sie wollen. |
| Datei / Medium hochladen | Binärdaten hochladen, Dateien auflisten, Dateiseite | keine | Fehlt: texts.capnp ist nur für Text. Dateien brauchen einen eigenen Vertrag oder die Dateibibliothek `fs-*`. |
| Seite schützen (Bearbeiten sperren) | Schutzstufe pro Seite setzen | keine | Fehlt. |
| Benutzerrechte und Sperren | Benutzerrollen, Sperrstatus | keine | Außerhalb dieses Vertrags; kommt von der Identitätsseite. |
| Einstellungen (Textgröße, Breite, Thema, Sprache) | Einstellungen pro Benutzer | keine | Außerhalb von texts; gehört zum Frontend oder zu den Benutzereinstellungen. |
| Druckansicht | gerenderte Seite zum Drucken | `exportText` (HTML) | Wie Seitenansicht. |
| Live-Aktualisierungen | Änderungsereignisse | `subscribe` | Felder der Ereignis-Nutzlast sind in `common.capnp` definiert (in diesem Lauf nicht gelesen). |
| Import und Export (Markdown) | Import und Export nach Medientyp | `importText`, `exportText` | keine |
| Version / Support | Anbieterinformationen | `supportReport` | keine |

## Zusammenfassung der Lücken in texts.capnp

Operationen oder Konzepte, die ein Frontend im MediaWiki-Stil braucht und der Vertrag nicht hat:

1. Versionsverlauf: Versionen eines Textes auflisten, eine frühere Version abrufen, zwei vergleichen.
2. Eine frühere Version wiederherstellen.
3. Undelete oder Papierkorb.
4. Beobachtungsliste: beobachten, nicht mehr beobachten, auflisten (mit Benutzeridentität).
5. Diskussions- oder Diskussionsseiten und ihre Paarungsregel.
6. Namensräume als Konzept.
7. Kategorien: Kategorien eines Textes und Mitglieder einer Kategorie.
8. Vorlagen oder Transklusionsabhängigkeiten.
9. Weiterleitungen.
10. Abfrage der letzten Änderungen (Zeitfenster, Filter), nicht nur ein Abonnement.
11. Suchergebnisse mit Ausschnitten und Hervorhebung.
12. Präfix- oder Titelsuche für Vorschläge.
13. Schutzstatus eines Textes.
14. Dateien und Medien (außerhalb von texts; brauchen einen eigenen Vertrag).
15. Spezial- oder Berichtsabfragen (verwaiste Seiten, fehlende Ziele).
16. Gerendertes HTML als erstklassige Ausgabe (derzeit nur über den Medientyp von `exportText`).

Die Punkte 1, 2, 10, 11 sind in der Oberfläche am sichtbarsten und sollten zuerst entschieden werden. Die Punkte 5 und 6 brauchen eine Namensregel, nicht nur eine Operation. Die Punkte 4 und 5 hängen vom Identitätsmodell ab, das außerhalb des texts-Vertrags liegt.

## Hinweise

- Dies ist die Liste dessen, was der MediaWiki-Stil braucht. Andere Frontend-Stile brauchen womöglich weniger. Sie dient als Eingabe für die Entscheidung des Eigentümers, nicht als Liste verpflichtender Änderungen.
- Regeln aus texts.capnp: Die Weiterentwicklung ist nur anhängend, daher können Lücken nur durch neue Operationen geschlossen werden.
