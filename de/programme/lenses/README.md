# Lenses — Der Informations-Betrachter

[← Zurück zum Index](../../INDEX.md) | [Search](../search/README.md)

---

## Philosophie

Der Mensch braucht Informationen, nicht Programme. Lenses stellen Informationen aus vielen Services zusammen — gefiltert, zusammengefasst, mit Links zu den Originalen.

Von vielen Informationen immer mehr ausfiltern, bis der Mensch genau das bekommt was er braucht. Wenn er tiefer eintauchen will, klickt er auf den Link und kommt zum Service.

## Was eine Lens ist

Eine Lens ist eine persönliche, zusammengesetzte Ansicht. Beispiel:

**Lens "Meine Gruppe Helfa Köln":**
- Aus dem Wiki: Artikel über Helfa Köln (Zusammenfassung + Link)
- Aus der Karte: Standort Köln (Kartenausschnitt + Link)
- Aus dem Chat: Letzte 5 Nachrichten (Preview + Link)
- Aus dem PM: 3 offene Aufgaben (Titel + Link)
- Aus Git: Repository-Status (Link)

Jeder Benutzer kann beliebig viele Lenses erstellen. Eine Lens kann als Icon auf dem Desktop platziert werden.

## Wie Lenses funktionieren

1. Benutzer erstellt eine Lens mit einem Suchbegriff/Thema
2. Lens fragt den [Bus](../../konzepte/bus.md): "Welche Services haben Daten zu diesem Thema?"
3. Bus leitet an Services mit passendem [Rollen](../../konzepte/rollen.md) weiter
4. Jeder Service gibt seine Daten zurück (gefiltert nach [Rechten](../../konzepte/rechte.md))
5. Lens zeigt zusammengefasste Ansicht

## Architektur

| Modul | Zweck |
|---|---|
| `model.rs` | `Lens`, `LensItem`, `LensRole` — Domain-Modell |
| `query.rs` | `LensQueryEngine` — Bus-Anfrage + Demo-Fallback |
| `app.rs` | `LensesApp` — Dioxus Root-Komponente |

`LensRole` beschreibt den Service-Typ (`Wiki`, `Chat`, `Git`, `Map`, `Tasks`, `Iam`, `Other`).
`LensQueryEngine` sendet `lens.query` Events auf den Bus. Wenn der Bus nicht erreichbar ist, werden Demo-Daten angezeigt.

## Unterschied zu Tasks

| Lenses | Tasks |
|---|---|
| Zeigt Informationen AN | Macht etwas AUTOMATISCH |
| Persönlich (für den Benutzer) | Organisatorisch (für das System) |
| Lesen | Schreiben/Ausführen |
| Manuell auslösen | Event-/zeitgesteuert |

## Repo

`git@github.com:FreeSynergy/fs-lenses.git`

---

Weiter: [Search](../search/README.md) | [Tasks](../../konzepte/tasks.md)
