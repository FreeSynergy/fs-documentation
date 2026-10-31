# Axelor - Beschreibung

## Was das Programm macht

Axelor ist „ERP aus einem Guss + Prozess-Werkstatt“: Die Module sind fertig, aber fast alles darüber (Felder, Masken, Freigabe-Workflows) entsteht im App Builder/BPM-Designer. Wer Prozesse modellieren will, ohne zu programmieren, findet hier ein durchgängiges Java-System.

## Vorteile

- **BPM erstklassig integriert** (Freigaben, Aufgabenlisten, SLA-Bearbeitung)
- AGPL, ein Stack (Backend/Frontend/Builder)
- REST automatisch — Integrations-Arbeit klein

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Odoo** | Store-Ökosystem + Website; Axelor Prozess-Builder |
| **ERPNext** | Frappe-Python; Axelor Java/jBPM |
| **Bonitas/BPM-Suiten** | reine Prozess-Engine; Axelor bringt das ERP gleich mit |

## Technische Details

- **Stack**: Java (Spring-Boot-Basis), jAvancé-Framework, PostgreSQL
- **Auth**: Nutzer+Pass, LDAP/SSO (Version prüfen); API: Basic/JWT-Token (`JSESSION`-lose REST-Clients)
- **Deploy**: Docker, Tomcat-War, Axelor Cloud
- **Lizenz**: AGPL (Open Suite), Store-Module teils kommerziell

## Für wen geeignet

- Mittelständler mit starkem Prozess-/Freigabebedarf
- FreeSynergy-Skins: BPM-Knoten + REST-Modell als Prozess-Skin-Vorbild
