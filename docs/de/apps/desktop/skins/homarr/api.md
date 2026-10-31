# Homarr - API Dokumentation

## Übersicht

Homarr stellt keine klassische, frei dokumentierte REST-API bereit, sondern eine **typisierte tRPC-Schnittstelle**, die das Frontend der Weboberfläche verwendet. Diese Verfahren sind öffentlich referenziert (OpenAPI-Referenz auf der Projektseite) und lassen sich mit HTTP-Clients ansprechen. Dazu kommen die Auth-Routen von NextAuth sowie interne Integrations-Endpunkte, über die Homarr Anfragen an angebundene Dienste weiterreicht.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| tRPC (`/api/trpc/...`) | Boards, Widgets, Apps, Nutzer, Integrationen | Offiziell referenziert |
| NextAuth-Routen (`/api/auth/...`) | Login, Session, OIDC-Callback | Standard von NextAuth |
| Integrations-Proxy | Anfragen an Docker, Sonarr, Pi-hole usw. mit gespeicherten Schlüsseln | Intern, referenziert |
| Webhooks | ❌ Nicht vorhanden | — |

## Authentifizierung

- **Session-Cookie**: Nach dem Login setzt NextAuth ein Sitzungs-Cookie. Alle tRPC-Aufrufe im Browser nutzen dieses Cookie.
- **OIDC / Keycloak**: Bei konfigurierter Single-Sign-On-Authentifizierung wird der Identitätsanbieter bedient; die Sitzung läuft danach ebenfalls über das Cookie.
- **Header-Authentifizierung**: Hinter einem Reverse Proxy kann Homarr vertrauenswürdige Header auswerten (Vorsicht: nur mit gehärtetem Proxy sinnvoll).
- **API-Schlüssel**: Es gibt **keine offiziellen langlebigen API-Tokens**. Skripte arbeiten deshalb mit einer gültigen Session (Cookies) oder mit einem eigens angelegten Konto.
- **Rollen**: Lesezugriff folgt den Board-Freigaben; Verwaltungsverfahren (Nutzer, Einladungen, Instanzeinstellungen, Zertifikate) erfordern die Administratorrolle.

## Endpunkte

Die Verfahren folgen dem Muster `router.procedure`. Lesende Verfahren werden per `GET` mit `?input=<URL-kodiertes JSON>` aufgerufen, schreibende per `POST` mit JSON-Body.

### Apps (Verknüpfungen)

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/trpc/appRouter.getPaginated` | Apps mit Paginierung auflisten |
| `GET` | `/api/trpc/appRouter.byId` | Einzelne App anhand der ID |
| `GET` | `/api/trpc/appRouter.search` | Apps nach Suchtext durchsuchen |
| `GET` | `/api/trpc/appRouter.selectable` | Für Widgets auswählbare Apps |
| `POST` | `/api/trpc/appRouter.create` | App anlegen |
| `POST` | `/api/trpc/appRouter.update` | App ändern |
| `POST` | `/api/trpc/appRouter.delete` | App löschen |

### Boards und Layout

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/trpc/boardRouter.getAllBoards` | Zugängliche Boards auflisten |
| `GET` | `/api/trpc/boardRouter.getBoardSettings` | Board-Einstellungen lesen |
| `POST` | `/api/trpc/boardRouter.createBoard` | Neues Board anlegen |
| `POST` | `/api/trpc/boardRouter.changeBoardVisibility` | Sichtbarkeit/Freigabe ändern |
| `POST` | `/api/trpc/boardRouter.deleteBoard` | Board löschen |
| `POST` | `/api/trpc/boardRouter.setHomeBoard` | Start-Board (Desktop) setzen |
| `POST` | `/api/trpc/boardRouter.setMobileHomeBoard` | Start-Board (Mobil) setzen |
| `POST` | `/api/trpc/boardRouter.savePartialBoardSettings` | Board-Einstellungen teilweise ändern |
| `POST` | `/api/trpc/boardRouter.saveBoard` | Board-Inhalt speichern |
| `POST` | `/api/trpc/boardRouter.saveLayouts` | Layouts (Desktop/Mobil) speichern |
| `POST` | `/api/trpc/boardRouter.addItem` | Widget zu einem Board hinzufügen |
| `POST` | `/api/trpc/boardRouter.updateItemLayout` | Widget verschieben oder vergrößern |
| `POST` | `/api/trpc/boardRouter.resetLayout` | Layout zurücksetzen |

### Nutzer, Einladungen und Instanz

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/trpc/userRouter.getAll` | Alle Nutzer auflisten (Admin) |
| `POST` | `/api/trpc/userRouter.create` | Nutzer anlegen (Admin) |
| `POST` | `/api/trpc/userRouter.changePassword` | Passwort ändern |
| `POST` | `/api/trpc/userRouter.delete` | Nutzer löschen (Admin) |
| `POST` | `/api/trpc/userRouter.changeColorScheme` | Farbschema umschalten |
| `POST` | `/api/trpc/inviteRouter.createInvite` | Einladung erzeugen (Admin) |
| `GET` | `/api/trpc/serverSettingsRouter.getBoardSettings` | Globale Board-Vorgaben |
| `POST` | `/api/trpc/serverSettingsRouter.updateBoardSettings` | Globale Board-Vorgaben ändern (Admin) |
| `GET` | `/api/trpc/infoRouter.getInfo` | Server-/Instanzinformationen |

### Integrationen

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `POST` | `/api/trpc/integration.request` | Anfrage an einen angebundenen Dienst, mit gespeicherten Zugangsdaten |
| `POST` | `/api/trpc/integration.testConnection` | Gespeicherte Integration verbinden und testen |

### Authentifizierung (NextAuth)

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/auth/providers` | Verfügbare Auth-Anbieter |
| `GET` | `/api/auth/csrf` | CSRF-Token für Login-Aufrufe |
| `POST` | `/api/auth/callback/credentials` | Anmeldung mit Benutzername/Passwort |
| `GET` | `/api/auth/callback/<oidc-provider>` | Rückkehr vom Single-Sign-On-Anbieter |
| `GET` | `/api/auth/session` | Aktuelle Sitzung (Rolle, Name) |
| `POST` | `/api/auth/signout` | Abmelden |

## Beispiele

### Boards auflisten (GET mit Input)

```bash
curl -s \
  --cookie "homarr-session=<session-cookie>" \
  "http://localhost:7575/api/trpc/boardRouter.getAllBoards"
```

Antwort (gekürzt):

```json
{
  "result": {
    "data": {
      "json": [
        {
          "id": "b1c0f2e4-...",
          "name": "Homelab",
          "visibility": "public",
          "owner": { "id": "u-1", "name": "alice" }
        }
      ]
    }
  }
}
```

### Widget hinzufügen (POST mit JSON-Body)

```bash
curl -s -X POST \
  --cookie "homarr-session=<session-cookie>" \
  -H "Content-Type: application/json" \
  -d '{
    "json": {
      "boardId": "b1c0f2e4-...",
      "type": "app",
      "layout": { "x": 0, "y": 0, "width": 2, "height": 1 }
    }
  }' \
  "http://localhost:7575/api/trpc/boardRouter.addItem"
```

Antwort:

```json
{ "result": { "data": { "json": { "id": "w-42", "type": "app" } } } }
```

### Verbindungstest einer Integration

```bash
curl -s -X POST \
  --cookie "homarr-session=<session-cookie>" \
  -H "Content-Type: application/json" \
  -d '{"json": {"id": "int-7"}}' \
  "http://localhost:7575/api/trpc/integration.testConnection"
```

### curl mit Anmeldung über NextAuth

```bash
# Session-Cookie einer bestehenden Anmeldung wiederverwenden
curl -s --cookie "homarr-session=<session-cookie>" \
  "http://localhost:7575/api/trpc/infoRouter.getInfo"
```

## Rate Limits

- Homarr bringt **keine eigene Ratenbegrenzung** für die API mit.
- Begrenzung über den Reverse Proxy empfehlenswert, zum Beispiel in nginx (`limit_req`) oder Traefik (Middleware `ratelimit`).
- Integrations-Aufrufe sind durch die Abfrageintervalle der Widgets begrenzt; zu kurze Intervalle belasten die angebundenen Dienste.
- Empfohlene Richtung: wenige Anfragen pro Minute für Skripte, Intervalle von 30 Sekunden und mehr für Statuswidgets.

## Webhooks und internes Eventing

- **Keine Webhooks**: Homarr versendet keine Ereignisse an externe Systeme.
- **Internes Eventing**: Das Frontend ruft Verfahren bei Bedienschritten auf und aktualisiert die Anzeige über erneutes Abfragen; Änderungen am Layout werden sofort in der Datenbank gespeichert.
- **Workaround für Automatisierung**: Cron-Skripte, die tRPC-Verfahren aufrufen, oder externe Monitoring-Systeme, die die Dienste direkt prüfen.

## SDKs und Client-Bibliotheken

- **Kein offizielles SDK** für Homarr.
- Die **OpenAPI-Referenz** auf der Projektseite kann als Ausgangspunkt für Codegenerierung (OpenAPI-Generatoren) genutzt werden.
- Der im Projekt verwendete tRPC-Client ist eine interne TypeScript-Bibliothek; für eigene Skripte sind `fetch`/`axios` mit `input`-Parameter der praktikablere Weg.
- Für die **Integrationen selbst** gelten die SDKs der angebundenen Dienste (Docker-API, Sonarr/Radarr-APIs, Pi-hole-API, Jellyfin-API).

## Hinweise für den Betrieb

- HTTPS verwenden: Sitzungs-Cookies und Secrets sind ohne Transportverschlüsselung nicht sicher.
- `SECRET_PASSWORD` stabil halten, sonst lassen sich gespeicherte Integrations-Schlüssel nicht mehr entschlüsseln.

## Siehe auch

- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
