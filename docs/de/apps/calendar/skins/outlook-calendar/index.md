# Outlook Kalender Dokumentation

## Übersicht

Outlook Kalender ist der Kalender-Dienst von Microsoft: Termine, Besprechungen, Aufgaben und Ressourcen liegen im Postfach von Exchange Online (Microsoft 365) und werden in Outlook im Web, Outlook für Windows und Mac, Outlook Mobile sowie im klassischen Outlook-Desktop angezeigt. Verwaltet wird über die Weboberfläche und die desktopüblichen Kalendermasken, programmatisiert über Microsoft Graph; der Austausch mit Fremdsystemen läuft über das iCalendar-Format (ICS) sowie die Clientprotokolle Exchange ActiveSync und MAPI.

## Dateistruktur

- [menu.md](menu.md) - Startleiste, Befehlsleiste, Kalenderliste, Kontextmenüs, Rollen
- [features.md](features.md) - Termine, Planungsassistent, Freigaben, ICS-Veröffentlichung, Grenzen
- [description.md](description.md) - Beschreibung und Abgrenzung zu Google Kalender, Nextcloud Kalender und DAViCal
- [structure.md](structure.md) - Ansichten, Dialoge, Drag & Drop, Responsive Design, Accessibility
- [shortcuts.md](shortcuts.md) - dokumentierte Tasten und klar als fehlend markierte Shortcuts
- [api.md](api.md) - Microsoft Graph, Exchange Web Services, Change Notifications, ICS

## Systemesteckbrief

| Feld | Wert |
|------|------|
| Kategorie | Kalender-Systeme |
| Hersteller | Microsoft |
| Lizenz | kommerziell (Microsoft 365), privat über Outlook.com |
| Backend | Exchange Online (Postfachdienste) |
| API | Microsoft Graph (`/v1.0`, `/beta`), Exchange Web Services (veraltet) |
| Austauschformate | iCalendar (ICS), Exchange ActiveSync, MAPI over HTTP |
| CalDAV / CardDAV | ❌ Nicht vorgesehen |
| Self-Hosting | ❌ Nicht möglich (Exchange Server lokal nur als On-Premises-Hybrid) |
| Authentifizierung | OAuth 2.0 / OpenID Connect über Microsoft Entra ID |
