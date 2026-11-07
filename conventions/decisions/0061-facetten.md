# 0061 – Facetten: ein Programm, mehrere Apps; jedes mit Admin-Frontend

Status: akzeptiert (Nutzer, 2026-11-08) · ergänzt ADR 0021 (Motor und Frontend), 0036 (Laden), 0049 (Ordnung nach Zweck) · öffentlich: `docs/en/programs/kinds.md`

## Anlass (Nutzer)
`fs-people` bleibt das Programm. Menschen suchen aber „Kontakte“, nicht „People“; wer E-Mail will, versteht nicht, dass `fs-messenger` auch Mail kann. Ein Frontend, das wie ein Mail-Programm aussieht, reicht nicht: Es muss für die Menschen wie ein eigenes Programm wirken.

## Entscheidung
1. **Facette** (englisch *facet*): Das Programm legt vorab fest, welche Facetten es hat. Eine Facette hat Namen, Logo, einen festen Filter auf die Daten des Programms und einen eigenen Menüeintrag. Sie hat keine eigenen Daten. Beispiele: `fs-people` → Contacts, Users, AIs, Partners; `fs-messenger` → Mail, Chat.
2. **Frontends** gibt es für das Programm und für jede Facette. Ein Frontend für Contacts zeigt nur Kontakte.
3. **Nach außen heißt alles „App“.** Das Wort „Facette“ ist intern und in der Doku. Wer Contacts installiert, bekommt `fs-people` mit, ohne es wissen zu müssen.
4. **Jedes Programm und jede Facette hat Pflicht-Einträge: Frontend und Admin-Frontend.** Das Admin-Frontend bietet *alle* Einstellungen. So kann man mit einer einfachen Oberfläche etwas verstellen und es mit dem Admin-Frontend, notfalls mit Hilfe eines Profis, wieder richten. Das Admin-Frontend einer Facette ist das des Programms, auf die Facette gefiltert.
5. **Menü:** Admin-Frontends stehen gesammelt unter „Einstellungen“ (freedesktop-Kategorie `Settings`), nicht neben jeder App (Strategie; Nutzer schlug „Ansichten“ vor und überließ es uns).
6. **Facette ist das Gegenteil einer Suite:** Eine Suite fasst mehrere Programme zusammen, eine Facette zeigt einen Ausschnitt eines Programms.
7. **Laden:** Der Katalog (AppStream) führt jede Facette als eigene App mit eigenem Logo; installiert wird das Programm (AppStream erlaubt mehrere Komponenten je Paket).

## Folgen
- Ersetzt die offene Frage „eigenständige Ansichten“ (Galerie, Kanban): Galerie ist eine Facette von `fs-files`, Kanban bleibt ein Frontend von `fs-tasks`.
- Die Liste der Facetten je Programm steht in dessen Manifest; Format mit dem Laden (Thread S) festlegen.
- Weitere mögliche Facetten (Vorschlag): `fs-people` Team, Members; `fs-messenger` Forum; `fs-files` Gallery, Music, Videos, Documents; `fs-tasks` To-dos, Tickets; `fs-calendar` Booking (mit `fs-resources`).
