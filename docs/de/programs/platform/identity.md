# Identitäts-Wrapper

## Kurz gesagt

Identity soll der eine Ort werden, an dem Anmeldung und Zugriff auf Systeme geregelt werden. Wir beschreiben, wie es sich verhalten soll, und Kanidm, ein offener Identitätsserver, übernimmt die Arbeit, wo es kann. Heute ist es eine kleine Brücke, noch keine Anmeldung.

**Befehl:** `fs-identity`, ein Befehl je Programm mit Unterbefehlen ([ADR 0063](../../decisions/0063-ein-programm-ein-befehl.md); Programme werden umgestellt, wenn sie ohnehin angefasst werden, nicht jedes ist es schon).

## Was hier anders ist

- Kanidm entscheidet nie, wer wozu gehört. [Gruppen](groups.md) entscheidet, und Kanidm spiegelt es.
- Kanidm sitzt hinter unserer eigenen Schnittstelle. Wir übernehmen, was es nicht kann, und geben die Steuerung zurück, sobald es das kann.
- Wenn du Kanidm nicht betreibst, laufen alle Programme trotzdem allein.
- Unser eigener kleiner Client spricht mit der REST-Schnittstelle von Kanidm, geprüft gegen Kanidm 1.12.0.

## Wo es heute steht

Neueste Version: `v0.2.0`. Der Adapter legt Gruppen in Kanidm an, liest, aktualisiert, listet und entfernt sie, sodass sie zu Gruppen passen, und er lässt sich gefahrlos wiederholen. Er lief einmal gegen einen echten Kanidm-1.12.0-Container. Eine Anmeldung gibt es noch nicht: keine Passwörter, OAuth2-Clients, SCIM, PAM oder RADIUS. Er kann in Kanidm keine Einladungen anlegen oder Rechte vergeben. Der Name des Repositorys ist vorläufig.

Anmeldung und Zugang zu Systemen. Wir legen fest, wie es sich verhält; Kanidm führt es aus, wo es kann.

**Status: nur ein Kanidm-Adapter für Gruppen, `v0.0.1`; noch keine Anmeldung.** Zurück zum [Gesamtplan](../apps/roadmap.md). Der Repository-Name `fs-identity` ist vorläufig. Details:
[Kanidm-Recherche](https://github.com/FreeSynergy/fs-documentation/blob/main/temp/research/kanidm-control.md), Quelltext gelesen bei Kanidm 1.13.0-dev (neueste Veröffentlichung 1.12.0), nicht gegen einen Live-Server ausgeführt.

## Idee

Kanidm wird aus der Ferne hinter unserer eigenen [Schnittstelle](../../interfaces/index.md) gesteuert. Wir übernehmen, was es nicht kann, und geben die Steuerung zurück, sobald es das kann (ADR 0047). Ist es nicht vorhanden, funktionieren Programme trotzdem allein (ADR 0024).

## Wie wir es steuern

| Weg | Nutzung |
|-----|---------|
| **REST API v1** mit einem Dienstkonto-Token, über unseren kleinen eigenen Rust-Client | Standard: Es ist die Schnittstelle, die Kanidms Doku als stabil bezeichnet, mit einer OpenAPI-Beschreibung |
| Crate `kanidm_client`, an die Serverversion gebunden | Nur für verwickelte Abläufe wie Anmeldung und Passkey-Registrierung; nicht von der Stabilitätszusage abgedeckt |
| SCIM | **Noch nicht**: als instabil angegeben, und das generische Anlegen von Einträgen wirkt im Quelltext defekt |

Das engt ADR 0024 ein, das vorsah, Kanidms SCIM hinter unserer Abstraktion zu nutzen.

## Möglichkeiten, keine Pflichten

| Was | Stand |
|-----|-------|
| OAuth2, OIDC, Passkeys | Ja |
| Anmeldung an Rechnern über PAM und NSS (`kanidm-unixd`) | Nur Linux und FreeBSD |
| RADIUS | Vorhanden; für uns nicht näher geprüft |
| Anmeldung unter Windows und macOS | Nicht verfügbar oder nicht etabliert |

## Grenzen, die wir übernehmen

Einladungen, feinkörnige Delegation, Föderation (OpenID Federation ist nicht in Kanidm; ADR 0035). Passkeys können nicht auf der Seite des Servers registriert werden; es lassen sich nur Registrierungslinks ausstellen. Siehe [Gruppen](groups.md).

## Offen

- Ob Kanidms Lizenz, MPL-2.0, eine Frage aufwirft: Wir rufen es über das Netzwerk auf und binden es nicht ein, das ist aber nicht geprüft.
- Zusammenarbeit mit dem Kanidm-Team, dessen Tempo langsam ist und dessen Doku hinterherhinkt.
