# 0072 – Blöcke als Quelle für Texte: Handbuch im Wiki, Store-Beschreibung und Hilfe daraus

Status: Entwurf (Strategie, 2026-11-11; Nutzerwunsch „Blöcke mit Metadaten“); Code erst nach 3b und Wiki · präzisiert ADR 0031, 0033 und 0034 (Absatz) · baut auf ADR 0057 (Übersetzbarkeit), 0062 und 0068 (Katalog, Paket), 0065 (Hilfe im Fenster), 0045 (Schnittstellen), 0046 (Speichern ≠ Export)

## Kontext
Ein Text steht heute oft mehrfach: die Beschreibung eines Programms im Store, ein Absatz im Handbuch, die Hilfe im Fenster. Drei Kopien laufen auseinander. ADR 0034 hat den **Absatz** als benannten, wiederverwendbaren Teil beschlossen; ADR 0031 sagt, dass jede Hilfe ein Wiki-Eintrag ist. Offen ist, **wie Programme einen bestimmten Absatz finden**, ohne Seiten zu zerlegen, und wie das **ohne Internet** funktioniert (lokal zuerst).

## Entscheidung (Entwurf)

### 1. Ein Absatz ist ein Block mit stabiler Id und Metadaten
- **Id:** UUIDv7 (ADR 0027), ändert sich nie, auch wenn der Text, die Seite oder die Reihenfolge sich ändern. Ein Block gehört zu einer Seite, kann aber über seine Id an anderer Stelle **eingesetzt** werden (ADR 0033).
- **Metadaten je Block** (Vorschlag, anhängbar):

| Feld | Bedeutung | Beispiel |
|---|---|---|
| `lang` | Sprache (BCP 47) | `en`, `de` |
| `program` | Programm, zu dem der Block gehört (Paketname, ADR 0017) | `fs-files` |
| `purpose` | Zweck, ein **sprechender Schlüssel** (ADR 0055) | `store.summary`, `store.description`, `help.versions`, `manual.intro` |
| `translationOf` | Id des Ursprungsblocks (ADR 0057/0011: Englisch wird gepflegt, Übersetzung folgt) | Id des englischen Blocks |
| `rev` | Fassung (monoton), plus Zeit und Urheber aus der Seitenhistorie | |

- **Zweck-Schlüssel** sind ein offenes, dokumentiertes Vokabular: `store.*` für den Laden, `help.<thema>` für die Hilfe im Fenster (ADR 0065), `manual.*` für das Handbuch. Programme dürfen eigene Zwecke unter ihrem Namensraum anlegen (`<programm>.<zweck>`); die Standards bleiben bei uns, wir schreiben keine feste Menge vor.
- AS2/Annotation (ADR 0020, 0031): ein Block ist eine benannte Marke im `Article` der Seite (ADR 0034); die Metadaten stehen als Felder des Blocks, nicht im Fließtext. Das genaue Blockformat bleibt Teil der Spezifikation der Domäne `documents` (`temp/research/documents-standards.md`).

### 2. Programme fragen Blöcke über die Wiki-Schnittstelle ab
Thema `wiki` (ADR 0045): ein Programm fragt **nicht nach Seiten, sondern nach Blöcken**: „gib mir `purpose = store.summary` für `program = fs-files` in `lang = de`, sonst `en`“. Die Antwort enthält Id, Text, Sprache, `rev`; Rückfall auf die Ausgangssprache wird **als solcher gekennzeichnet** (ADR 0057), nie als deutsche Übersetzung ausgegeben.
```capnp
# Vorschlag; Ordinale nur anhängen, Standardantwort Unsupported (ADR 0045)
struct BlockQuery { program @0 :Text; purpose @1 :Text; lang @2 :List(Text); }  # lang = Wunschliste mit Rückfall
struct Block { id @0 :Text; lang @1 :Text; program @2 :Text; purpose @3 :Text; rev @4 :UInt32; text @5 :Text; fallbackFrom @6 :Text; }
# interface WikiProvider (anhängen):  blocks (query :BlockQuery, cursor :Cursor) -> (page :BlockPage);
#                                      block  (id :Text, lang :Text) -> (block :Block);
```
Ein Programm **liest** nur; Schreiben geschieht im Wiki (Editor, ADR 0039). Die Hilfe im Fenster (ADR 0065) und die Beschreibung im Laden sind dadurch **dieselbe Quelle** wie das Handbuch.

### 3. Jedes Programm bekommt ein Handbuch im Wiki; Teile werden zur Store-Beschreibung
- Jedes Programm hat im Wiki eine **Kollektion „Handbuch“** (ADR 0034) mit Blöcken nach Zweck. Das ist Teil des Programm-Standards (Doku-Transparenz: die Doku ist immer aktuell, weil das Programm daraus liest).
- **Store-Beschreibung** (`store.summary` kurz, `store.description` lang) sind **Blöcke des Handbuchs**, keine eigenen Texte. Beim Paketbau wird daraus das Feld im Katalog (AppStream, ADR 0062) befüllt; nichts wird doppelt gepflegt.
- **Fehlt der Block** (neues Programm, keine Übersetzung), meldet der Paketbau eine **Warnung**, keinen Absturz; der Laden zeigt den Ausgangstext in der Ausgangssprache.

### 4. Lokal zuerst: Kopie der Blöcke im Paket und im Katalog
Kein Online-Zwang. Beim **Paketbau** legt das Werkzeug eine **Kopie der Blöcke** dieses Programms (alle Sprachen, mit Id, Metadaten, `rev`) als Datei **ins Paket** (`blocks/<lang>.json`, Format bei Umsetzung) und die für den Laden nötigen (`store.*`) **in den Katalog** (ADR 0062, signiert wie dieser). Ein Programm liest Blöcke in dieser Reihenfolge:
1. **eigene Wiki-Instanz/Regal** des Menschen (neueste Fassung, auch eigene Erklärungen, ADR 0031 Punkt 5),
2. **Kopie im installierten Paket** (immer da, offline),
3. **Katalog** (für noch nicht installierte Programme im Laden, aus dem lokal gehaltenen Katalogstand),
4. **online** nur als Aktualisierung, nie als Voraussetzung.

Gleiche Block-Id und höheres `rev` gewinnt. Die Kopie ist ein **Export** im Sinn von ADR 0046; die Wahrheit liegt im Wiki (ADR 0042: Datenbank ist die Wahrheit). Ein Update des Pakets aktualisiert die Kopie; **eigene Erklärungen des Menschen werden nie überschrieben**, sie stehen daneben (ADR 0031 Punkt 5).

### 5. Entwurfsmuster (ADR 0043)
**Repository/Query** (Abfrage statt Seitenzugriff), **Fallback-Kette** (Chain of Responsibility: Wiki, Paket, Katalog, online), **Snapshot** (Kopie beim Paketbau). Schnittstelle zuerst: `WikiProvider.blocks` wird vor dem ersten Verbraucher festgelegt.

## Risiken und offene Punkte
1. **Block-Id über Übersetzungen:** eine Id je Sprache (mit `translationOf`) oder dieselbe Id mit Sprach-Varianten? Vorschlag: eine Id je Sprache, `translationOf` verbindet; so bleibt jede Fassung ein eigener Absatz mit eigener Historie.
2. **Größe der Kopie im Paket:** nur Blöcke des eigenen Programms, Text komprimiert; Sprachen wählbar (Paket kann Sprachen weglassen, Rückfall englisch).
3. **Veraltete Kopie:** `rev` und Zeitstempel werden angezeigt; Aktualisierung beim Paket-Update oder, wenn online, aus dem Wiki.
4. **Sicherheit:** Blöcke sind Text, kein ausführbarer Inhalt; beim Anzeigen gilt die gleiche Bereinigung wie für Wiki-Seiten. Pakettext ist signiert (TUF, ADR 0062).
5. **Blockformat:** ist Teil der `documents`-Spezifikation (ADR 0034 Folgen); dieser ADR legt nur die **Metadaten und die Abfrage** fest.
6. **Zweck-Vokabular:** wer pflegt es? Vorschlag: eine Liste in `fs-interfaces`, Erweiterung je Programm im eigenen Namensraum.

## Folgen
- `fs-interfaces`: Thema `wiki` um `blocks`/`block` erweitern (nach Annahme und 3b); `fs-wiki`: Metadaten am Block, Abfrage; Paketbau (`fs-release`/Paket-Werkzeug): Kopie ins Paket und `store.*` in den Katalog; `fs-store` (der Laden, ADR 0060): liest `store.*` aus dem Katalog; alle Programme: Hilfe über `help.<thema>`.
- Dokumentation: Programm-Standard ergänzen („Handbuch im Wiki, Pflichtzwecke `store.summary`, `store.description`“); Verweis aus ADR 0031/0034 nach Annahme.
- Code erst nach Runde 3b grün und nach dem Wiki.

## English summary
**Decision (draft):** a paragraph is a block with a stable id (UUIDv7) and metadata (language, program, purpose such as `store.summary` or `help.<topic>`, `translationOf`, `rev`). Programs query blocks, not pages, through the wiki interface (`blocks`/`block`, language wish list with a marked fallback). Every program gets a manual in the wiki; parts of it are the store description, so nothing is maintained twice. Local first, no online requirement: the package build puts a copy of the program's blocks into the package and the `store.*` blocks into the signed catalog; programs read in the order own wiki, installed package, catalog, online (only as an update). The copy is an export, the wiki stays the truth; the human's own explanations are never overwritten. **Status: draft; code only after round 3b and the wiki.**
