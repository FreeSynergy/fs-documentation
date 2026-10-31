# Google Kalender Dokumentation

## Übersicht

Google Kalender (calendar.google.com) ist der Kalender-Dienst von Google: eine Web-Oberfläche und mobile Apps für Android und iOS, in denen Termine, wiederkehrende Ereignisse, Aufgaben und Mehrpersonentermine über mehrere Kalender hinweg verwaltet werden. Organisationskalender, Freigaben mit Berechtigungsstufen, Ressourcenkalender (Räume und Geräte) und Terminpläne stammen aus Google Workspace. Zugriff programmatisch über die **Calendar REST API v3**, dazu CalDAV, ICS-Abonnements und Push-Benachrichtigungskanäle. Der Dienst läuft ausschließlich in der Google-Cloud; ein Self-Hosting ist nicht möglich.

## Dateistruktur

- [menu.md](menu.md) - Kopfzeile, Seitenleiste, Kalender- und Termin-Menüs, Rollen in Workspace
- [features.md](features.md) - Ansichten, Termine, Freigaben, Grenzen ("Was Google Kalender NICHT kann"), Integrationen
- [description.md](description.md) - Beschreibung und Abgrenzung zu Outlook-Kalender, Nextcloud Calendar und CalDAV-Selbstbau
- [structure.md](structure.md) - Seiten-, Raster- und Dialogstruktur, UI/UX, Responsive Design, Barrierefreiheit
- [shortcuts.md](shortcuts.md) - Offizielle Tastatur-Shortcuts der Web-App und klar als fehlend markierte Tasten
- [api.md](api.md) - Calendar API v3, OAuth-2.0-Scopes, CalDAV, Push-Kanäle, Limits, SDKs

## Kurzprofil

| Merkmal | Wert |
|---------|------|
| Kategorie | Kalender-Systeme (Groupware-Kalender) |
| Typ | Cloud-Dienst (SaaS), Web-App + Android/iOS |
| Datenhaltung | Google-Cloud, Export/Import als ICS, Google Takeout |
| API | Calendar REST API v3 (JSON), CalDAV, ICS, Tasks-API |
| Authentifizierung | Google-Konto, OAuth 2.0, Workspace-SSO |
| Self-Hosting | ❌ Nicht möglich |
| Kosten | Kostenlos (Privatkonten), kostenpflichtig mit Google Workspace |
