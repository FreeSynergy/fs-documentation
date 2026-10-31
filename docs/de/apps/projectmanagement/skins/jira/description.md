# Jira - Beschreibung

## Was das Programm macht

Jira verwaltet Arbeit als Issues mit definiertem Lebenszyklus: Wer erstellt es, welche Statusfolge durchläuft es, wer arbeitet woran in welchem Sprint. Der Reiz (und Preis) ist die Formbarkeit: Workflows, Felder und Berechtigungen werden projektspezifisch gebaut.

## Vorteile

- **De-facto-Standard** im Software-Engineering (KEY-Referenzen in Commits)
- **Workflow-Maschine** mit Validatoren/Automation
- **API + Webhooks** ausgereift

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Trello** | Brett ohne Workflow-Engine; Jira = Prozess |
| **OpenProject/Redmine** | offene Alternativen, schlankere Administration |
| **Asana** | Aufgaben-Portfolio statt Issue-Workflow-Fokus |

## Technische Details

- **Modell**: Jira Cloud (SaaS, Atlassian-Konto) oder Data Center (self-hosted, lizenziert)
- **Projektmodelle**: Team-managed (einfach) vs. Company-managed (Schemes)
- **Authentifizierung**: Atlassian-Konto/SSO; API: API-Token (E-Mail+Token Basic), PAT (Data Center), OAuth2 (Apps)
- **Preise**: Free (<10 Nutzer), Standard/Premium/Enterprise

## Für wen geeignet

- Engineering-/Support-Organisationen mit Regelbedarf
- FreeSynergy-Skins: Issue-Lebenszyklus + Statusübergänge als Workflow-Vorbild ([modelle.md](../../../../data/modelle.md))
