# Notion — Beschreibung (2026-11-07)

## Was es ist

Notion ist ein Web- und Desktop-Arbeitsbereich, in dem Menschen Seiten schreiben, sie in Datenbanken ordnen und teilen [S22, S12]. Notion nennt sein Produkt einen KI-Arbeitsbereich für Teams und deren Agenten [S22]. Das Kernmodell ist ein Baum aus Seiten. Jede Seite enthält Blöcke. Datenbanken sind Seiten mit einer Sammlung von Zeilen und Ansichten [S13, S9].

## Warum es für ein Wiki-Frontend wichtig ist

- Inhalte sind blockbasiert. Ein Frontend muss einen Baum aus typisierten Blöcken darstellen und bearbeiten [S9].
- Die Struktur entsteht aus Seiten und Unterseiten in einem Baum der Seitenleiste [S12].
- Datenbanken sind eine zweite Art von Inhalt, mit Schema, Zeilen und Ansichten [S7, S13].
- Das Produkt hat eine öffentliche API mit OAuth und Webhooks [S3, S4].

## Bemerkenswerte Ideen

1. **Der Block als Einheit.** Jeder Absatz, Listeneintrag, jede Tabelle, jedes Bild und jede Einbettung ist ein Block mit ID und Typ. Blöcke können Kinder haben [S9, S18].
2. **Markdown-Eingabe beim Schreiben.** Beim Tippen von `# `, `- `, `[] ` und ähnlichen Präfixen entsteht der passende Block [S11].
3. **Datenbankansichten auf einem Datenbestand.** Tabelle, Liste, Board, Kalender, Galerie und Diagramm sind Ansichten derselben Daten [S13].
4. **Schema pro Datenquelle.** Seit API-Version `2025-09-03` kann eine Datenbank mehrere Datenquellen enthalten, jede mit eigenen Eigenschaften [S7].
5. **Papierkorb mit Wiederherstellung.** Gelöschte Seiten bleiben 30 Tage erhalten und können wiederhergestellt werden [S14].

## Für wen es geeignet ist (aus der Produktseite, kein Urteil)

Notion richtet sich an Teams und Einzelpersonen, die Notizen, Wikis und kleine Datenbanken in einem Werkzeug wollen [S22, S13]. Notion veröffentlicht auf den gelesenen Seiten keine Liste von Marktsegmenten.

## Unterschiede, die zu beachten sind

Notion ist ein gehosteter Dienst. Auf den gelesenen offiziellen Seiten wurde keine selbst gehostete Ausgabe gefunden [ungeprüft]. Das Datenmodell von Notion ist proprietär. Ein Export ist möglich (siehe [features.md](features.md)).

## Quellen

[S22], [S12], [S13], [S9], [S7], [S3], [S4], [S14]. Die früheren Vergleiche mit anderen Produkten (Tango.io, Confluence, XWiki) sind nicht geprüft und hier entfernt.
