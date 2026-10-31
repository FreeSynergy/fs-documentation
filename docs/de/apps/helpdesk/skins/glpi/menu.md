# GLPI - Menüpunkte

## Hauptnavigation (quer, oben)

| Menü | Inhalt |
|------|--------|
| Assistance | Tickets (selbst erstellt/zugewiesen/alles), SLA, Verträge-Tickets |
| Assets | Computer, Bildschirme, Drucker, Netzwerke, Geräte, Software, Verbrauchsmaterial, Kabel, Racks |
| Administrative Verwaltung | Benutzer, Gruppen, Standorte, Banken, Verträge, Lizenzen, Dokumente |
| Werkzeuge (Tools) | Projekte, Aufgaben, Reminders, Knowledge Base (Wissen), Statistik-Reports |
| Konfiguration | allgemeinen Einstellungen, Benachrichtigungen, SLA-Verträge, Regeln (Business Rules), Templates |
| Admin (Admin-Leiste unten) | Cron, Plugins, API, Datenbanken, Sicherheitsprotokolle |

## Assistance-Bereich

- **Tickets**: CRUD + Suche + „Mass Actions“
- pro Ticket Reiter: Eigenschaften, Verknüpfungen (Assets! SLA, Probleme, Änderungen), Aufgaben, Follow-ups, Pläne, Statistiken
- Aktionen: nehmen/behandeln/lösen/schließen, Eskalation, Zuweisen an Gruppen

## Self-Service-Portal

- „Ein Helpdesk-Ticket erstellen“ mit Kategorien-Baum, Watchlist, Knowledge-Base-Suche vor dem Absenden
- eigene Tickets + Benachrichtigungen

## Menüs nach Rolle

| Rolle | Rechte/Menüs |
|-------|--------------|
| Super-Admin | alles inkl. Plugins/Cron |
| Admin | Konfiguration ohne Plugin-Installation (delegierbar) |
| Technician | zugewiesene Tickets, Assets der eigenen Bereiche |
| Requester | Portal + eigene Tickets |
