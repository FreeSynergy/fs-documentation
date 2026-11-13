# 0075 – fs-marketplace als Programm, der Store als Facette

Status: **akzeptiert** (Gründer, 2026-11-13); Code nach dem Meilenstein „Wir benutzen es selbst“; die laufenden Store-Releases bleiben unverändert · baut auf ADR 0020 (AS2-Aktivitäten), 0045 (Themen-Schnittstellen), 0068 (Fähigkeiten, Signatur-Stufen), 0071 (Versionen/Git), 0073 (Kollaboration), 0074 (Schichten)

Grundlage: `.scratch/marketplace/BRAINSTORMING.md` (2026-11-13) und die Antworten des Gründers.

## Einordnung nach unseren Arten (Prüffrage: wessen Daten?)

| Teil | Art | Besitzt | Nutzt über Schnittstellen |
|---|---|---|---|
| **fs-marketplace** | Programm | Angebote, Gesuche, Kataloge (Läden), Zusagen, Übergaben, Moderations-Entscheidungen | Groups und People (Anbieter), Files (Dateien, Installieren, Herkunft), Messages (Rückfragen), Maps, Calendar |
| **Store** | Facette von fs-marketplace | nichts; zeigt einen Marktplatz als „Laden“ für Software, Themes, Icons, Frontends, Server | Files: Installieren |
| weitere Facetten | Facette | nichts | später, z. B. Verschenken/Tauschen, Mitfahrbörse, Räume, Nachbarschaftshilfe, Jobs |

Die gesamte Logik (Angebot, Gesuch, Moderation, Vertrauen, Bestand) liegt in **fs-marketplace**. Der Store hat nur die Facette.

## Entscheidung

### 1. Geld: anzeigen ja, abwickeln nie
Angebote dürfen einen Preis tragen. **FreeSynergy wickelt grundsätzlich nichts ab**, keine Zahlungen, keine Treuhand, keine Gebühren. Wie Menschen bezahlen, klären sie selbst. Unsere eigene Software bleibt immer frei.

### 2. Jeder Datensatz entscheidet selbst, wohin er geht
Ein Angebot wandert nur so weit, wie sein Anbieter es freigibt: lokal, privat geteilt oder öffentlich (Reichweiten-Achse). Föderation (ActivityPub) nur bei Freigabe.

### 3. Anbieter, Betreiber, Moderation
- **Anbieter** sind Gruppen (fs-groups) oder Personen (fs-people).
- Ein **Marktplatz (Laden) liegt in einem Git-Repository**. **Besitzer ist der Inhaber des Repositorys**, eine Gruppe oder eine Person. Der Besitzer muss sich ausweisen können und signiert (ADR 0068, Web of Trust). Jeder darf den Marktplatz lesen und spiegeln.
- Der Besitzer ernennt **Moderatoren**. Sie können Angebote **nicht ändern**, sondern nur Angebote, die gegen die Regeln des Marktplatzes verstoßen, **aus dem Marktplatz nehmen**, mit Grund. Jede Entscheidung ist eine AS2-Aktivität und sichtbar. Das Angebot selbst bleibt beim Anbieter, es ist seine Datenquelle.

### 4. Wo ein Marktplatz liegt
- Ein Marktplatz ist nie nur lokal. Er liegt auf einem eigenen Server (auch zu Hause) oder extern (z. B. Codeberg, GitHub, eigener Forgejo).
- **Git ist die Datenquelle für das, was sich selten ändert**: Angebote, Beschreibungen, Bilder, Bedingungen, Signaturen. Das ist mit fs-catalog schon heute so.
- **Was sich oft ändert, gehört nicht in Git**: Bestand, Verkaufs- und Downloadzahlen, Reservierungen, Kontingente. Dafür meldet ein Laden einen **Laden-Dienst** über die Schnittstelle von fs-marketplace (Thema `marketplace`, Teil `stock`/`stats`). Ohne Laden-Dienst zeigt der Store diese Werte ehrlich als „unbekannt“.
- **Externe Konten dürfen Datenquelle sein.** Liefert ein externer Dienst Zahlen, etwa die Downloadzahlen von GitHub-Releases, darf ein Adapter sie einlesen. Die Herkunft der Zahl wird angezeigt.
- **Grenzen ehrlich benennen:** Ein Downloadlimit, z. B. so viele pro Stunde, lässt sich nur durchsetzen, wenn die Dateien über einen Server des Betreibers ausgeliefert werden. Aus einem öffentlichen, spiegelbaren Git lässt sich nichts begrenzen.

### 5. Herkunft in Files
Jede Datei, die über einen Marktplatz kommt, bekommt in ihrer AS2-Aktivität (ADR 0020, Herkunft je Datei) den **Anbieter** (Gruppe oder Person) und den **Marktplatz** (Repository, Signatur) mit.

### 6. Standards
- **ValueFlows** (Angebot/Gesuch → Zusage → Übergabe, Bestand als Ressource) *[Lizenz und Stand vor Code prüfen]*;
- **schema.org** `Offer`, `Demand`, `Product`, `Service`, `SoftwareApplication`;
- **ActivityStreams 2.0** `Offer`, `Accept`, `Reject`, `Remove`, `Flag`;
- **AppStream** für Software-Angebote (fs-catalog Format 2).

## Folgen
- fs-catalog wird das Katalog-Format von fs-marketplace (Software zuerst).
- fs-store wird nach dem Meilenstein zur Store-Facette auf fs-marketplace. Die Frontends B (Craft) und C (kompakt) bleiben.
- Neues Repository `fs-marketplace` erst mit Beginn des Codes.

## Offen
- Schema des Themas `marketplace` (Angebot, Gesuch, Moderation, `stock`/`stats`).
- Wie ein Laden-Dienst sich ausweist und ob Zahlen signiert werden.
