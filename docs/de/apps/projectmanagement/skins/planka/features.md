# Planka - Funktionen

## Übersicht

Planka konzentriert sich auf den Kanban-Kern: Karten ziehen, zuweisen, kommentieren, abhaken. Trotzdem stecken echte Team-Funktionen drin - Echtzeit-Sync, Checklisten, benutzerdefinierte Felder (Community), Webhooks und Benachrichtigungsdienste. Die Pro-Edition ergänzt Ansichtstypen und Verwaltungskomfort.

## Funktionsbereiche

### 1. Projekte, Boards und Listen

- **Hierarchie**: Projekt -> Board -> Liste (Spalte) -> Karte
- **Listen-Aktionen**: hinzufügen, umbenennen, verschieben, Karten archivieren, Liste leeren
- **Board-Hintergründe**: projekteigene Hintergrundbilder, pro Board wählbar
- **Archiv**: Boards und Karten archivieren statt löschen, wiederherstellbar

### 2. Karten

- **Beschreibung in Markdown**: Überschriften, Listen, Code, Links; Editor mit Vorschau (Markdown-Editor integraler Bestandteil)
- **Fälligkeiten** mit Datums-/Zeitangabe und Überschreigungs-Markierung
- **Stopwatch je Karte** (Community-Edition)
- **Labels**: farbige Beschriftungen je Board, Karten mehrfarbig markierbar
- **Zugewiesene** Personen je Karte, Benachrichtigung bei Zuweisung
- **Checklisten (Tasks)**: Teilaufgaben mit Fortschrittsbalken
- **Benutzerdefinierte Felder** (Community): eigene Feldtypen je Projekt/Board (versionsabhängig im Umfang)
- **Anhänge**: Drag & Drop, Bild-Vorschau, Dateiverwaltung je Karte
- **Kommentare** mit Markdown; Aktivitätenprotokoll je Karte

### 3. Echtzeit und Benachrichtigungen

- **Socket.IO-Sync**: Kartenbewegungen, Änderungen und neue Kommentare erscheinen sofort
- **Beobachten/Abonnieren**: Karten und Boards beobachten, Benachrichtigungsstrom in der App
- **E-Mail-Benachrichtigungen** über SMTP
- **Benachrichtigungsdienste**: Anbindung an über 100 Anbieter (Chat-/Push-Dienste über das Notification-Service-Menü; Anbieterauswahl versionsabhängig)

### 4. Zusammenarbeit und Rechte

- **Projekt-Manager** je Projekt ernennbar (verwalten Boards/Mitglieder)
- **Board-Mitgliedschaften**: Mitglieder je Board, Wer-was-darf grob über Projekt-/Boardzugehörigkeit
- **Gastrollen** mit eingeschränkten Rechten: nur Pro-Edition
- **Benutzerverwaltung**: Admins legen Konten an, setzen Rollen, vergeben API-Schlüssel

### 5. Webhooks und Automatisierung

- **Webhooks** (Community): definierte Ereignisse an externe HTTPS-Endpunkte (über Admin-API/Webhook-Verwaltung)
- **REST-API** mit Token-Auth für eigene Skripte (siehe [api.md](api.md))
- **Beispiele**: CI-Trigger bei Kartenverschiebung, Benachrichtigungs-Bots, Reporting-Abrufe

### 6. Ansichten und Komfort (Pro-Edition)

- **Persönliches Dashboard** über alle Projekte
- **Kalender-, Timeline-, Karten-/Medien-Ansichten**
- **Wiederkehrende Karten** und **Vorlagen** (Karten-/Board-Templates)
- **Eine Karte in mehreren Boards**
- **PDF-/HTML-Export**, **fünf Themes** mit Akzentfarbe, **optimierte Telefon-/Tablett-Ansicht**

## Module und Integrationen

- **Kein Plugin-System**: Integration läuft über REST-API, Webhooks und Benachrichtigungsdienste
- **Notes-App** (Testphase) als eigenes Begleitprogramm für Notizen
- **Import**: Kartenimporte aus anderen Systemen (Trello-Import existierte in älteren Versionen; Status versionsabhängig)

## Konfiguration

- **`.env`-Umgebungsvariablen**: `DATABASE_URL`, `APP_URL`, `SECRET_KEY`/`SESSION_SECRET`, Initiale-Admin (`ADMIN_EMAIL`, `ADMIN_PASSWORD` bei Erstanlage, versionsabhängig), SMTP, OIDC (Pro)
- **Docker Compose** liefert Standard-Stack (App + PostgreSQL)
- **Benutzerebene**: Sprache, appearance (heller/dunkler Modus, Community: Umschalten vorhanden; weitere Themes = Pro), Passwort, E-Mail, 2FA-Einrichtung

## Was Planka NICHT kann

- **Kein Gantt, keine Roadmap** in der Community-Edition (Timeline nur Pro)
- **Keine Zeiterfassungs-Auswertung** (Stopwatch ohne Reports/Abrechnung)
- **Keine Scrum-Artefakte**: keine Sprints, Burndowns oder Backlog-Planung
- **Keine feingrananten Workflow-Berechtigungen** (kein Statusrecht je Rolle)
- **Keine native Community-App**: Telefon-/Tablett-Optimierung ist Pro; Community bleibt Web-Browser
- **Kein Darkroom für anonyme Öffnung**: Gast-/Leserollen nur mit Pro-Lizenz
- **Kein Offline-Modus** und kein lokaler Zwischenspeicher für Flüge

## Erweiterungen und Plugins

- **API-first**: Swagger-Referenz als Grundlage für eigene Tools und Codegenerierung
- **Community-Clients**: Inoffizielle Clients für Skripte; offizielle SDKs fehlen
- **Self-hosted Erweiterbar**: Quellcode sichtbar (fair-code), eigene Funktionen möglich - Distribution dann aber lizenzpflichtig, wenn Pro-Merkmale berührt werden (License-Guide beachten)
