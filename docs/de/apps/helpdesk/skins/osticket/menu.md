# osTicket - Menüpunkte

## Agenten-Navigation (oben)

| Menü | Inhalt |
|------|--------|
| Dashboard | Ticket-Kacheln nach Status/Alter/SLA |
| Tickets | gefilterte Listen (meine, offene, überfällige, alle) |
| Kunden | Kunden-/Organisationssuche und -profile |
| Wissen (Knowledge Base) | FAQ-Artikel, Themen |
| Dateien | Upload-Bibliothek |

## Ticketansicht (Tabs und Aktionen)

- Tabs: **Allgemein**, **Verlauf (Log)**, **Notizen**, **Anhänge**
- Aktionenmenü (⋮): Beantworten, Weiterleiten, Notiz, Zusammenführen, Teilen, Sperren, Löschen, Status setzen (new/open/pending/closed), Zuweisen, Priorität, Help Topic, SLA-Manuell

## Admin-Menüs (Admin-Tab)

| Menü | Inhalt |
|------|--------|
| Tickets | Einstellungen, Prioritäten, SLA-Pläne, Help Topics, Ticket-Status |
| E-Mail | Mail-Fetching, Auto-Respond, Filterregeln (Eingang + ausgehend) |
| Kunden | Felder (Formulare), Organisationen, Kundenportale, Passwörter |
| Team/Roles/Staff | Teams, Rollen, Mitarbeiter, Gruppen |
| Wissen | Artikelkategorien, Vorlagen (E-Mail-Templates) |
| Dateien | Upload-Limits, Virenscan-Optionen |

## Kundenportal

- Tickets auflisten/neu anlegen, Antworten, Artikel lesen, Passwort-Reset
- keine Menüs je Rolle über „Kunde“ hinaus (nur loginbasiert)

## Menüs nach Rolle

| Rolle | Menü |
|-------|------|
| Administrator | Admin-Tab voll |
| Agent | zugewiesene Gruppen-Tickets, keine Admin-Menüs |
| Kunde | Portal nur eigene Tickets |
