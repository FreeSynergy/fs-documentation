# Homarr - API Documentation

## Overview

Homarr does not provide a classic, freely documented REST API, but a **typed tRPC interface** that the frontend of the web interface uses. These procedures are publicly referenced (OpenAPI reference on the project page) and can be addressed with HTTP clients. In addition there are the auth routes of NextAuth as well as internal integration endpoints through which Homarr forwards requests to connected services.

**API types at a glance**

| Type | Use | Status |
|-----|------------|--------|
| tRPC (`/api/trpc/...`) | boards, widgets, apps, users, integrations | Officially referenced |
| NextAuth routes (`/api/auth/...`) | login, session, OIDC callback | Standard of NextAuth |
| Integration proxy | requests to Docker, Sonarr, Pi-hole etc. with stored keys | Internal, referenced |
| Webhooks | ❌ Not available | — |

## Authentication

- **Session cookie**: after login, NextAuth sets a session cookie. All tRPC calls in the browser use this cookie.
- **OIDC / Keycloak**: when single sign-on authentication is configured, the identity provider is used; the session then also runs via the cookie.
- **Header authentication**: behind a reverse proxy Homarr can evaluate trusted headers (caution: only sensible with a hardened proxy).
- **API keys**: there are **no official long-lived API tokens**. Scripts therefore work with a valid session (cookies) or with a separately created account.
- **Roles**: read access follows the board shares; administrative procedures (users, invitations, instance settings, certificates) require the administrator role.

## Endpoints

The procedures follow the pattern `router.procedure`. Read procedures are called via `GET` with `?input=<URL-encoded JSON>`, write procedures via `POST` with a JSON body.

### Apps (links)

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/api/trpc/appRouter.getPaginated` | List apps with pagination |
| `GET` | `/api/trpc/appRouter.byId` | Single app by ID |
| `GET` | `/api/trpc/appRouter.search` | Search apps by search text |
| `GET` | `/api/trpc/appRouter.selectable` | Apps selectable for widgets |
| `POST` | `/api/trpc/appRouter.create` | Create app |
| `POST` | `/api/trpc/appRouter.update` | Change app |
| `POST` | `/api/trpc/appRouter.delete` | Delete app |

### Boards and layout

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/api/trpc/boardRouter.getAllBoards` | List accessible boards |
| `GET` | `/api/trpc/boardRouter.getBoardSettings` | Read board settings |
| `POST` | `/api/trpc/boardRouter.createBoard` | Create new board |
| `POST` | `/api/trpc/boardRouter.changeBoardVisibility` | Change visibility/sharing |
| `POST` | `/api/trpc/boardRouter.deleteBoard` | Delete board |
| `POST` | `/api/trpc/boardRouter.setHomeBoard` | Set start board (desktop) |
| `POST` | `/api/trpc/boardRouter.setMobileHomeBoard` | Set start board (mobile) |
| `POST` | `/api/trpc/boardRouter.savePartialBoardSettings` | Change board settings partially |
| `POST` | `/api/trpc/boardRouter.saveBoard` | Save board content |
| `POST` | `/api/trpc/boardRouter.saveLayouts` | Save layouts (desktop/mobile) |
| `POST` | `/api/trpc/boardRouter.addItem` | Add widget to a board |
| `POST` | `/api/trpc/boardRouter.updateItemLayout` | Move or enlarge widget |
| `POST` | `/api/trpc/boardRouter.resetLayout` | Reset layout |

### Users, invitations and instance

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/api/trpc/userRouter.getAll` | List all users (admin) |
| `POST` | `/api/trpc/userRouter.create` | Create user (admin) |
| `POST` | `/api/trpc/userRouter.changePassword` | Change password |
| `POST` | `/api/trpc/userRouter.delete` | Delete user (admin) |
| `POST` | `/api/trpc/userRouter.changeColorScheme` | Switch colour scheme |
| `POST` | `/api/trpc/inviteRouter.createInvite` | Create invitation (admin) |
| `GET` | `/api/trpc/serverSettingsRouter.getBoardSettings` | Global board defaults |
| `POST` | `/api/trpc/serverSettingsRouter.updateBoardSettings` | Change global board defaults (admin) |
| `GET` | `/api/trpc/infoRouter.getInfo` | Server/instance information |

### Integrations

| Method | Endpoint | Description |
|---------|----------|--------------|
| `POST` | `/api/trpc/integration.request` | Request to a connected service, using stored credentials |
| `POST` | `/api/trpc/integration.testConnection` | Connect and test a stored integration |

### Authentication (NextAuth)

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/api/auth/providers` | Available auth providers |
| `GET` | `/api/auth/csrf` | CSRF token for login calls |
| `POST` | `/api/auth/callback/credentials` | Sign in with username/password |
| `GET` | `/api/auth/callback/<oidc-provider>` | Return from the single sign-on provider |
| `GET` | `/api/auth/session` | Current session (role, name) |
| `POST` | `/api/auth/signout` | Sign out |

## Examples

### List boards (GET with input)

```bash
curl -s \
  --cookie "homarr-session=<session-cookie>" \
  "http://localhost:7575/api/trpc/boardRouter.getAllBoards"
```

Response (shortened):

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

### Add widget (POST with JSON body)

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

Response:

```json
{ "result": { "data": { "json": { "id": "w-42", "type": "app" } } } }
```

### Connection test of an integration

```bash
curl -s -X POST \
  --cookie "homarr-session=<session-cookie>" \
  -H "Content-Type: application/json" \
  -d '{"json": {"id": "int-7"}}' \
  "http://localhost:7575/api/trpc/integration.testConnection"
```

### curl with sign-in via NextAuth

```bash
# Reuse the session cookie of an existing sign-in
curl -s --cookie "homarr-session=<session-cookie>" \
  "http://localhost:7575/api/trpc/infoRouter.getInfo"
```

## Rate limits

- Homarr ships **with no own rate limit** for the API.
- Limiting via the reverse proxy is recommended, for example in nginx (`limit_req`) or Traefik (middleware `ratelimit`).
- Integration calls are limited by the query intervals of the widgets; intervals that are too short burden the connected services.
- Recommended direction: few requests per minute for scripts, intervals of 30 seconds and more for status widgets.

## Webhooks and internal eventing

- **No webhooks**: Homarr sends no events to external systems.
- **Internal eventing**: the frontend calls procedures during interaction steps and updates the display by querying again; changes to the layout are saved to the database immediately.
- **Workaround for automation**: cron scripts that call tRPC procedures, or external monitoring systems that check the services directly.

## SDKs and client libraries

- **No official SDK** for Homarr.
- The **OpenAPI reference** on the project page can be used as a starting point for code generation (OpenAPI generators).
- The tRPC client used in the project is an internal TypeScript library; for own scripts, `fetch`/`axios` with the `input` parameter is the more practical route.
- For the **integrations themselves**, the SDKs of the connected services apply (Docker API, Sonarr/Radarr APIs, Pi-hole API, Jellyfin API).

## Notes for operation

- Use HTTPS: session cookies and secrets are not secure without transport encryption.
- Keep `SECRET_PASSWORD` stable, otherwise stored integration keys can no longer be decrypted.

## See also

- [menu.md](menus.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](layout.md)
- [shortcuts.md](shortcuts.md)
