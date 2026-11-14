# 0082 – `fs-server` verbindet: Konfiguration von außen, Anbindungen an Server

Status: **Entwurf** (Strategie, 2026-11-14; Nutzerentscheidung 14.11.) · baut auf ADR 0021 (Motor und Frontend), 0066 (Typbeschreibung), 0067 (Tresor), 0068 (Fähigkeiten), 0076 (Grundmodell), 0079 (`fs-server`) · berührt 0019 (`fs-hub`), 0047 (Kanidm-Wrapper), 0056 (Admins)

## Kontext
ADR 0079 macht `fs-server` zum Programm, das Server einrichtet und jeden Schritt protokolliert. Der Nutzer erweitert die Rolle (14.11.): `fs-server` **verbindet** die Programme. Er liest und setzt deren Einstellungen **von außen**, stellt sie online und bindet sie an Server an (Kanidm, Zentinel, später Mail wie Stalwart); ein Programm kümmert sich nur um sich. Bestand (gelesen, 2026-11-14): Die Programme `fs-wiki`, `fs-tasks`, `fs-people`, `fs-files`, `fs-calendar` haben **keine** OIDC-Anbindung; `fs-identity` spiegelt nur Kanidm-Gruppen („No sign-in, no passwords, no OAuth2 clients“). Ein Gesamttest Zentinel → Kanidm → OIDC → Tuwunel läuft lokal (`fs-kanidm/scripts/test/podman-stack.sh`), ist aber ein Testskript, kein Weg. In `fs-types` gibt es eine Typbeschreibung für Datentypen (Modul `describe`, `TypeRegistry`); ein Typ „Einstellungen“ mit Befehlen zum Lesen und Setzen ist **[nicht belegt]**.

## Einschlägige ADRs (Zitate)
- 0066: „Das Backend meldet je Datentyp eine Typbeschreibung: Felder … und die **Befehle**“; „Admin: alle Felder, alle Einstellungen, alle Befehle. **Aus der Typbeschreibung erzeugt**“; „Das Programm liefert nur Daten und die Schnittstelle“.
- 0068 §1: „Fremde Programme (Kanidm, Zentinel, Stalwart …) bekommen ihre Fähigkeiten von uns im Katalog eingetragen“; „Zur Laufzeit meldet die Schnittstelle selbst, was wirklich geht (Typbeschreibung, `supported`)“.
- 0047: „Wir legen fest, was geschieht, und gleichen Kanidm an. Kanidm ist per REST-API oder Client ferngesteuert“; Service-Account-Token, SCIM vorerst nicht.
- 0045: „Viele Schnittstellen sind nur Konfiguration, die geprüft und atomar getauscht wird“ (Hot-Plugins nach Vorbild Zentinel); „Schnittstellen sind Ziele“.
- 0019: „Programme suchen einander nicht – nur der Hub kennt alle“; der Hub ist „einmal pro Gerät“. 0079: „`fs-hub` verbindet Programme auf einem Gerät und bleibt unberührt“.
- 0079: „Gate `human`“, „Trockenlauf“, „Idempotenz“, „Mensch führt aus, keine KI auf dem Ziel“, „Anbieter austauschbar (Ports and Adapters)“. 0067/0071: „Zugang über Tresor-Verweis … nie in Dateien, auf der Kommandozeile oder in der URL“.
- 0056: „Ein Agent darf niemals Admin werden“. 0021: Risikomarken „gesetzt von der Engine und nie vom Aufrufer“.

## Einordnung („wessen Daten?“)
| Gegenstand | Besitzer | Begründung |
|---|---|---|
| Einstellungen eines Programms | das **Programm** | Es führt sie aus und bleibt Quelle der Wahrheit; `fs-server` hält keine Kopie als Wahrheit, nur den **gewünschten Sollwert** je Server-Satz |
| Verbindung „Programm X ↔ Kanidm-Client“, „Programm X ↔ Route/Domain“ | **`fs-server`** | Sie gehört zu keinem der beiden Enden, sondern zum Server, auf dem beide laufen (Server-Inventar, ADR 0079) |
| Sollwerte der Server (Kanidm-Clients, Zentinel-Routen) | der **Server** (Kanidm, Zentinel) | `fs-server` legt sie nur über den Adapter an und prüft sie |
| Personen und Gruppen samt Mitgliedschaften | **`fs-people`/`fs-groups`** (Wahrheit, ADR 0047); Kanidm ist Spiegel | „FreeSynergy legt fest, Kanidm gleicht an“ |
| Zugangsdaten (Client-Secret, Token, Zertifikatsschlüssel) | **`fs-vault`** | `fs-server` speichert nur den **Verweis** (0067) |
| Protokolle der Anbindungen | **`fs-server`** (voll, nur anhängend); Zusammenfassung als AS2 an `fs-history` | 0079, Entscheidung 4 |
| Programme installieren | **`fs-store`** | `fs-server` verbindet, was installiert ist |
| Programme auf **einem Gerät** untereinander | **`fs-hub`** | Gerät/lokal; `fs-server` ist Server/Verbindungen und ersetzt ihn nicht |
| Oberfläche zum Bedienen | **Admin-Workbench** (0066) | Frontend ohne eigene Daten |

## Entscheidung
1. **Mediator.** `fs-server` ist der Vermittler zwischen Programmen und Servern. Ein Programm kennt weder Kanidm noch Zentinel; es meldet nur, was es **anbietet und braucht** (provides/requires, 0068), z. B. `identity.oidc` (braucht), eine Web-Adresse (bietet). `fs-server` löst auf und verbindet.
2. **Konfiguration nur über die Typbeschreibung/Admin-Schnittstelle des Programms (0066), nie über Dateien hinter dem Rücken.** Lesen und Setzen geschehen über dieselben Befehle, aus denen das Admin-Frontend erzeugt wird; das Programm prüft und übernimmt (Hot, atomar, 0045). Meldet ein Programm den Befehl nicht oder `supported = false`, ist die Anbindung **nicht möglich** mit Hinweis; sie wird nicht über die Konfigurationsdatei erzwungen.
3. **Ein Adapter je Server** (Ports and Adapters, 0043/0079): Kanidm (REST, 0047), Zentinel (Konfiguration, geprüft und atomar getauscht), später Stalwart und weitere. Ein Adapter **bietet** (z. B. `identity.oidc`, `proxy.route`) und **braucht** nichts von Programmen; fremde Server tragen ihre Fähigkeiten im Katalog (0068).
4. **Adapter-Vertrag** (Schnittstelle in `fs-interfaces`, Ziel nach 0045): Operationen **anbinden**, **prüfen**, **lösen**, **Zustand**.
   - **idempotent:** Anbinden mit gleichem Sollwert ändert nichts; Wiederholen ist ungefährlich.
   - **Trockenlauf:** Jede Operation liefert vorab den Plan (was geändert würde, ohne Werte von Geheimnissen); ausgeführt wird nur nach Bestätigung.
   - **Protokoll:** je Operation Vorher/Nachher-Zustand (ohne Geheimnisse), Lauf-ID, Ergebnis; Format und Ablage wie ADR 0079 Entscheidung 4.
   - **Zustand** meldet nur Lesbares: angebunden, abweichend, fehlt, nicht erreichbar.
5. **Sicherheitsregeln.** Zugangsdaten nur als **Tresor-Verweis** (0067, 0071), nie im Klartext, nie in Protokoll, Befehlszeile oder URL; erzeugte Geheimnisse (z. B. OIDC-Client-Secret) gehen vom Adapter **direkt** in den Tresor und von dort an das Programm. Gate `human` vor Schritten, die Zugang öffnen oder löschen (Client anlegen/entfernen, Route veröffentlichen, Domain umhängen). **Der Mensch führt `fs-server` auf dem Server aus; kein Agent, keine KI auf dem Ziel** (0079, 0056). Agenten schreiben und testen nur lokal (VM, Container).
6. **Personen und Gruppen mit Kanidm** (Nutzer, 14.11.): `fs-people` ↔ Kanidm `person`, `fs-groups` ↔ Kanidm `group` samt Mitgliedschaft. Richtung nach 0047: FreeSynergy legt fest, Kanidm gleicht an (anlegen, ändern, sperren, Mitgliedschaft), zurücklesen zum Abgleich; **Abweichungen werden gemeldet, nie still überschrieben** (Überschreiben nur nach Bestätigung). Weg: REST `/v1/person`, `/v1/group`; SCIM nicht (0047, `identity.scim` unstable). **Wiederverwenden, nicht neu bauen:** der Gruppen-Adapter `fs-identity-kanidm` (Repo `fs-identity`, v0.0.1) bleibt Besitzer des Kanidm-Wortschatzes für Personen und Gruppen; der Kanidm-Adapter von `fs-server` baut darauf auf und ergänzt nur die **Anbindungen** (OIDC-Clients, später Reset-Links). Vorschlag, vom Nutzer zu bestätigen. **Kein Agent erzeugt Passwörter oder Schlüssel** (0054, „Agenten erzeugen keine Geheimnisse“): Erstanmeldung über einen **Kanidm-Reset-Link** (`_credential/_update_intent`) oder Passkey, den der **Mensch** auslöst.
7. **Abgrenzung.** `fs-server` installiert keine Programme (`fs-store`), spiegelt keine Objekte zwischen Programmen (`fs-hub`), hält keine Schlüssel (`fs-vault`), besitzt keine Programmeinstellungen und ist kein Frontend.

## Folgen
- **`fs-interfaces`:** Zu klären und zu bauen: (a) eine **Konfigurations-Schnittstelle** der Programme: Typ „Einstellungen“ mit Lesen/Setzen/Prüfen über die Typbeschreibung (heute **[nicht belegt]**); (b) die Adapter-Schnittstelle; (c) ein Thema je Server-Fähigkeit (`identity.oidc`, `proxy.route`), jeweils zuerst als Entwurf (0045).
- **`fs-server`:** Adapter-Crates `-adapter-kanidm`, `-adapter-zentinel` (später `-adapter-stalwart`), ein Verbindungs-Modell (Inventar um Anbindungen erweitert) und Unterbefehle `connect`, `check`, `disconnect`, `status`.
- **Katalog (0068):** provides/requires in `fs-catalog` müssen die Fähigkeiten der drei Server tragen; ob `gen_catalog.py` sie heute schreibt, ist **[nicht belegt]**. Die Art `server` fehlt im Katalog und im Store-Parser (Bestand, ADR 0077).
- **`fs-identity`:** Der Adapter spricht REST v1 (`POST/GET/DELETE /v1/group`, `PUT/POST/DELETE …/_attr/{attr}`), Gruppe = `fsg-<uuid>`, Personen nur über eine vom Aufrufer gelieferte Zuordnung (`PersonMap`, SPN). Es **fehlen**: Person anlegen/ändern/sperren, Abgleich-Bericht (heute stellt `apply` Handänderungen **zurück** und entfernt unzugeordnete Mitglieder; das widerspricht „melden statt überschreiben“), Rollen, Reset-Link, OIDC-Clients. Kanidm bietet laut Upstream-Quellcode `/v1/person`, `/v1/person/{id}/_attr/{attr}`, `…/_credential/_update_intent`, `/v1/oauth2*`; ob Sperren über `account_expire` per `_attr` geht, ist **[nicht belegt]**.
- **Programme:** brauchen für Anmeldung selbst OIDC-Unterstützung (fehlt heute) und die Einstellungs-Schnittstelle; ohne sie bleibt die Anbindung „nicht möglich“.

## Alternativen
| Option | Bewertung |
|---|---|
| Programme konfigurieren sich selbst (jedes spricht Kanidm/Zentinel direkt) | Verworfen: jedes Programm kennt jeden Server, die Logik wächst mit der Zahl der Programme quadratisch (0019: „Programme suchen einander nicht“); widerspricht „ein Programm kümmert sich nur um sich“. |
| Konfigurationsdateien der Programme von außen schreiben | Verworfen (Nutzer): Dateien hinter dem Rücken umgehen Prüfung und Hot-Übernahme (0045) und die Typbeschreibung (0066). |
| Zentrale Konfigurationsverwaltung wie Ansible/Puppet | Verworfen: sie setzen Dateien und Pakete, kennen keine Typbeschreibung und keinen Tresor-Verweis, besitzen weder Verbindungs-Daten noch unser Protokoll (Gründe wie 0079); als Ausführer ersetzbar, nicht als Kern. |
| `fs-hub` übernimmt es | Verworfen: der Hub ist pro Gerät und lokal (0019, 0079); Server-Verbindungen betreffen Dienste auf Servern. |

## Offen
- Konfigurations-Schnittstelle (Typ „Einstellungen“): Form und Besitzer in `fs-interfaces` **[nicht belegt]**.
- Ob Zentinel Konfigurationsänderungen zur Laufzeit über eine Schnittstelle zulässt oder nur Datei plus `kill -HUP` **[nicht belegt]**; wäre Letzteres der Weg, ist es die einzige Stelle, an der `fs-server` eine Datei des **Servers** (nicht eines Programms) schreibt, und sie gehört dem Adapter.
- Umgang mit Servern ohne jede Verwaltungs-Schnittstelle **[nicht entschieden]**.
- Verhältnis zu `fs-groups`/`fs-identity` (Kanidm-Gruppen, ADR 0047) bei der Client-Anlage **[nicht belegt]**.
