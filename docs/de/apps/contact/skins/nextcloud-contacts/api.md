# Nextcloud Contacts - API Dokumentation

## Übersicht

Kontaktzugriff läuft über **CardDAV (RFC 6352)** auf `remote.php/dav/`; Freigabe-/Kreismetadaten über **OCS**. Eine separate REST-„Contacts“-API existiert nicht.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| CardDAV | Adressbücher, Kontakte (CRUD) | offiziell |
| OCS Share / Circles | Freigaben, Kreise, gelbes Buch | offiziell |
| Status-API | Nutzerstatus-Anzeigen im Kontaktbild | offiziell-intern |
| REST „/api/contacts“ | — | ❌ Nicht vorhanden |

## Authentifizierung

- **Basic-Auth** über HTTPS (Benutzer + App-Passwort empfohlen)
- Session-Cookies im Browser; Bearer für OCS aus App-Passwort möglich
- Two-Factor: App-Passwörter nötig

## CardDAV-Endpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/.well-known/carddav` | Discovery → `/remote.php/dav/` |
| `PROPFIND` | `/remote.php/dav/addressbooks/users/<user>/` | Adressbücher inkl. `addressbook-color`, `sync-token` |
| `REPORT` | `<addressbook-url>` | `addressbook-multiget` / `sync-collection` |
| `GET` | `<addressbook-url>/<uid>.vcf` | einzelne vCard |
| `PUT` | `<addressbook-url>/<uid>.vcf` | Kontakt anlegen/ändern |
| `DELETE` | `<addressbook-url>/<uid>.vcf` | Kontakt löschen (Papierkorb-Logik serverseitig) |
| `MKCOL` | `/remote.php/dav/addressbooks/users/<user>/<name>/` | neues Adressbuch |

## Beispiel: vCard anlegen

```http
PUT /remote.php/dav/addressbooks/users/anna/contacts/andrea.vcf HTTP/1.1
Content-Type: text/vcard; charset=utf-8

BEGIN:VCARD
VERSION:3.0
UID:andrea
N:Berg;Andrea;;;
FN:Andrea Berg
TEL;TYPE=CELL:+49 170 000000
EMAIL;TYPE=WORK:andrea@example.org
END:VCARD
```

Response: `201 Created`, `ETag`.

## OCS (Freigaben/Kreise)

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/ocs/v2.php/apps/circles/circles` | Kreise auflisten |
| `POST` | `/ocs/v2.php/apps/files_sharing/api/v1/shares` | Freigabe (auch Adressbuch-Freigaben, Typen variant) |
| `GET` | `/cloud/user-status` | Status der Nextcloud-Benutzer |

OCS verlangt Header `OCS-APIRequest: true`.

## Rate Limits

Nextcloud-Throttling auf Login-Endpunkten; DAV selbst ohne feste Limits (Bruteforce-Schutz aktiv).

## SDKs und Clients

- **JS**: `nextcloudContacts`-Community-Clients; `js-calendav`-Familie; offizielle Client-Beispiele im contacts-Repo (fetch + PROPFIND)
- **CLI**: `curl` mit DAV-Methoden; `vdirsyncer`
- **PHP**: `sabre/dav` (serverseitig Referenz)

## Skin-Hinweis

Skin-Mapping auf das Contact-Modell ([modelle.md](../../../../data/modelle.md)), Feldnamen gemäß vCard 3.0 ([felder.md](../../../../data/felder.md)).
