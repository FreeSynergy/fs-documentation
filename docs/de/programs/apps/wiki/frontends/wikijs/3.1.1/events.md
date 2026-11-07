# Wiki.js 3.1.1: Ereignisse

Ereignisse, die das Wiki verlassen, und Live-Aktualisierungen in der Oberfläche. Die Webhook-Liste der alten Seite (`page.create`, `page.update`, `page.move`, `page.revert`, …) ist für 3.1.1 falsch. Die richtigen Namen stehen unten.

## Ausgehende Webhooks

Konfiguriert in Admin → Webhooks. Jeder Webhook hat eine URL, eine Liste von Ereignissen und einen optionalen Authorization-Header. Die Zustellung ist ein HTTP-POST mit einem JSON-Body. Quelle: `backend/models/hooks.ts`, `HOOK_EVENTS` (https://github.com/requarks/wiki/blob/3.1.1/backend/models/hooks.ts).

### Ereignisnamen (die 14 in `HOOK_EVENTS`)

| Ereignis | Ausgelöst, wenn | Aufrufstellen (Anzahl) |
|-------|--------------|-------------------------|
| `page:create` | eine Seite angelegt wird | 2 |
| `page:edit` | der Inhalt einer Seite gespeichert wird | 1 |
| `page:rename` | eine Seite verschoben oder umbenannt wird | 1 |
| `page:delete` | eine Seite gelöscht wird | 2 |
| `asset:upload` | eine Datei hochgeladen wird | 2 |
| `asset:edit` | eine Datei bearbeitet wird | 1 |
| `asset:rename` | eine Datei umbenannt wird | 1 |
| `asset:delete` | eine Datei gelöscht wird | 2 |
| `comment:new` | ein Kommentar gepostet wird | 2 |
| `comment:edit` | ein Kommentar bearbeitet wird | 1 |
| `comment:delete` | ein Kommentar gelöscht wird | 2 |
| `user:join` | ein Nutzerkonto angelegt wird | 1 |
| `user:login` | ein Nutzer sich anmeldet | 1 |
| `user:logout` | ein Nutzer sich abmeldet | 1 |

Der Kommentar in `hooks.ts` sagt, dass jedes Ereignis einen `emit()`-Aufruf im Server hat. Die Zahlen oben stammen aus einer grep-Suche im Serverquellcode; es sind Anzahlen der Aufrufstellen, keine Verhaltenstests.

### Nutzlast

```
{ "hookId": <id>, "event": "<event name>", "data": { ... }, "instance": <instance id> }
```

Quelle: `backend/models/hooks.ts` (`payload: { hookId, event, data, instance }`). Die Form von `data` hängt vom Ereignis ab; die Daten je Ereignis wurden nicht gelesen.

### Zustellung

| Eigenschaft | Wert | Quelle |
|----------|------|--------|
| Methode | POST | `hooks.ts` |
| Content-Type | `application/json` | `hooks.ts` |
| User-Agent | `Wiki.js/<version>` | `hooks.ts` |
| Authorization | übernommen aus der Einstellung `authHeader` des Webhooks, wenn gesetzt | `hooks.ts` |
| Signaturheader | keiner gefunden | `hooks.ts` |
| Wiederholungsregeln | nicht gelesen | — |
| Zustellstatus | je Webhook gespeichert (`hooks.ts`, „recording the outcome on the webhook“) | `hooks.ts` |
| TLS | eine Option, nicht vertrauenswürdige Zertifikate zu akzeptieren, existiert (`acceptUntrusted`) | `hooks.ts` |

Hinweis für uns: ohne Signatur muss sich ein Empfänger auf den Authorization-Header oder ein privates Netz verlassen.

## Benachrichtigungskategorien (innerhalb des Wikis)

Diese speisen den Posteingang und E-Mails, nicht externe Systeme. Quelle: `backend/notifications/categories/`.

| Kategoriedatei | Bedeutung |
|---------------|---------|
| `pageCreated` | neue Seite |
| `pageDeleted` | gelöschte Seite |
| `pageLifecycle` | Ereignis einer Lebenszyklusregel |
| `watchedPage` | Änderung auf einer beobachteten Seite |
| `watchedPageComment` | Kommentar auf einer beobachteten Seite |
| `commentReply` | Antwort auf einen Kommentar |
| `mention` | ein Nutzer wurde erwähnt |
| `reviewRequested` | eine Prüfung wurde angefordert |
| `feedbackStatus` | eine Feedback-Idee hat den Status geändert |

Nutzer können Kategorien abschalten (`ProfileNotifications.vue`, `AdminNotifications.vue`).

## Live-Aktualisierungen in der Oberfläche

| Funktion | Transport | Quelle |
|---------|-----------|--------|
| Gemeinsames Bearbeiten (Markdown, Visual, Excalidraw) | Websocket mit Yjs | `backend/controllers/collab.ts`, `frontend/src/composables/collab.js`, `frontend/src/editor/visual/collab.js`, `frontend/src/editor/excalidraw/collab.js` |
| Live-Cursor und Markierungen „recent edits“ | derselbe Websocket (Awareness) | Versionshinweise von 3.0.0-beta.705 („show live cursors only on hover + dotted underline for recent edits“), https://github.com/requarks/wiki/releases/tag/3.0.0-beta.705 |
| Benachrichtigungsabzeichen im Header | abgerufen; Push nicht verifiziert | `HeaderNav.vue` (`notificationsStore.badge`) |
| Koordination mehrerer Instanzen | Postgres LISTEN/NOTIFY auf getrennten Kanälen (Zusammenarbeit) und den Ereignisbus | Kommentar in `backend/index.ts`, `backend/core/db.ts` |

Es wurde kein Endpunkt für Server-Sent Events gefunden. Nicht verifiziert: ob das Benachrichtigungsabzeichen per Polling aktualisiert wird.

## Was wir für unser Frontend lernen können

- Verwende dieselben Ereignisnamen wie Wiki.js nur, wenn wir kompatibel sein wollen. Unser eigener Vertrag (`fs-interfaces/schema/texts.capnp`) nutzt `subscribe` mit einem `ChangeListener` und einer `Change`-Union aus `created`, `updated`, `deleted` (`common.capnp`). Siehe `dependencies.md`.
- Ein Webhook ohne Signatur braucht den Authorization-Header oder ein privates Netz. Unser eigener Entwurf sollte eine Signatur ergänzen.
