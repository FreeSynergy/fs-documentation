# Identitäts-Wrapper

Anmelden und Zugang zu Systemen. Wir legen fest, wie es sich verhält; Kanidm führt es aus, wo es kann.

**Status: geplant, noch kein Code (2026-11-06).** Zurück zum [Gesamtplan](../apps/roadmap.md). Der Name ist noch offen. Details: [Kanidm-Recherche](https://github.com/FreeSynergy/fs-documentation/blob/main/temp/research/kanidm-control.md), Quelltext gelesen bei Kanidm 1.13.0-dev (neueste Veröffentlichung 1.12.0), nicht gegen einen Live-Server ausgeführt.

## Idee

Kanidm wird aus der Ferne hinter unserer eigenen [Schnittstelle](../../interfaces/index.md) gesteuert. Wir übernehmen, was es nicht kann, und geben die Steuerung zurück, sobald es das kann (ADR 0047). Ist es nicht da, funktionieren Programme trotzdem allein (ADR 0024).

## Wie wir es steuern

| Weg | Nutzung |
|-----|---------|
| **REST API v1** mit einem Dienstkonto-Token, über unseren kleinen eigenen Rust-Client | Standard: Es ist die Oberfläche, die Kanidms Doku als stabil bezeichnet, mit einer OpenAPI-Beschreibung |
| Crate `kanidm_client`, an die Serverversion gebunden | Nur für verwickelte Abläufe wie Anmeldung und Passkey-Registrierung; nicht von der Stabilitätszusage abgedeckt |
| SCIM | **Noch nicht**: als instabil angegeben, und die generische Erstellung von Einträgen wirkt im Quelltext defekt |

Das engt ADR 0024 ein, das vorsah, Kanidms SCIM hinter unserer Abstraktion zu nutzen.

## Möglichkeiten, keine Pflichten

| Was | Stand |
|-----|-------|
| OAuth2, OIDC, Passkeys | Ja |
| Anmeldung an Rechnern über PAM und NSS (`kanidm-unixd`) | Nur Linux und FreeBSD |
| RADIUS | Vorhanden; für uns nicht näher geprüft |
| Anmeldung unter Windows und macOS | Nicht verfügbar oder nicht etabliert |

## Grenzen, die wir übernehmen

Einladungen, feinkörnige Delegation, Föderation (OpenID Federation ist nicht in Kanidm; ADR 0035). Passkeys können nicht auf Seiten des Servers registriert werden; nur Registrierungslinks lassen sich ausstellen. Siehe [Gruppen](groups.md).

## Offen

- Ob Kanidms Lizenz, MPL-2.0, eine Frage aufwirft: Wir rufen es über das Netzwerk auf und binden es nicht ein, das ist aber nicht geprüft.
- Zusammenarbeit mit dem Kanidm-Team, dessen Tempo langsam ist und dessen Doku hinterherhinkt.
