# Taiga - Funktionen

## Hauptfunktionen

### Agile Projektarbeit
- Scrum-Projekte (Product Backlog, Sprints mit Points/Burndown) und Kanban-Projekte (Tafel, Swimlanes)
- Epics mit Subtasks und epic-progress; klassische Issues parallel
- Story-Status/Point-Werte je Projekt anpassbar

### Projektwissen
- Wiki, Anhang-Verwaltung, Aktivitätsprotokoll (History), Benachrichtigungen
- Timeline mit Meilensteinen; Statistiken (Burn-down/Chart, Cycle)

### Integrationen nativ
- GitHub/GitLab: Commit-Referenzen `#123`, Branch-Verknüpfung, Merge→Statuswechsel
- Slack/Telegram-Chats, Webhooks pro Projekt
- Import aus Jira/Asana/Trello/GitHub-Issues (Assistent)

## Was Taiga NICHT kann

- **keine Portfolio-/Ressourcenplanung** (Workloads à la Asana: ❌)
- **keine Gantt-CPM-Berechnung** (Timeline ist Darstellung)
- **Dashboard-Gadgets begrenzt** (Statistiken starr)
- **keine offizielle Mobile-App** (Web responsive; Drittklienten)
- **Berechtigungsmodell grob** (Rollen je Projekt, keine Feldrechte)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| REST-API + Webhooks | offiziell |
| Taiga-CLI (`taiga`) | Skript-Automatisierung |
| GitHub/GitLab/Slack/Telegram | eingebaute Integrations-Paneele |
