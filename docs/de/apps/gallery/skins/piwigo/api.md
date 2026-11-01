# Piwigo - API Dokumentation

## Übersicht

Piwigo bietet einen Webservice unter `ws.php?method=<name>` (Parameter per GET/POST, Antwort XML oder JSON). Er wird von den offiziellen Apps und zahlreichen Plugins genutzt.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| Webservice `ws.php` (`format=php`/`json`) | Kategorien, Bilder, Tags, Kommentare, Benutzer | offiziell |
| Plugin-Hooks (`$events`) | serverseitige Erweiterungen | offiziell |
| OAuth2 / Mobile-App-Endpunkte | App-Zugriff | über Plugins |
| GraphQL / Webhooks | — | ❌ |

## Authentifizierung

- **REST-artig**: `ws_login` liefert `pwg_token` + Cookiesession
- **API-Key-Methode**: Parameter `format=json` mit `check_cookie`-Session
- **Signaturen**: Plugin-basiert (HMAC) für mobile Clients; Standard ist Benutzer/Passwort
- Rollen bestimmen die erlaubten Methoden (Gast/Benutzer/Webmaster/Admin)

## Kernmethoden

| Methode | Beschreibung |
|---------|--------------|
| `pwg.wsdologin` / `pwg.session.login` | Anmeldung, liefert Session |
| `pwg.getCategories` | Kategorien inkl. Bildzahlen |
| `pwg.getImages` | Bilder je Kategorie, `image_ids`, `per_page`, `page` |
| `pwg.getImagesets` | Sets nach Tag, Datum, Suche, „recent“ |
| `pwg.getImage` / `getImageInfo` | Detail mit URLs für TH/CU/LI |
| `pwg.addImage` | Bild hochladen (Base64/Multipart) |
| `pwg.editImage` | Titel, Autor, Status, Kategorien |
| `pwg.deleteImage` | Bild entfernen |
| `pwg.addCategory` / `pwg.editCategory` / `pwg.deleteCategory` | Kategorienbaum |
| `pwg.addTag` / `pwg.assignTags` / `pwg.getTags` | Schlagwörter |
| `pwg.addComment` / `pwg.getComments` | Kommentare |
| `pwg.getConfig` / `pwg.setConfig` | Galerie-Einstellungen (Admin) |

## Beispiel

Request:

```http
POST /ws.php?format=json HTTP/1.1
Content-Type: application/x-www-form-urlencoded

method=pwg.getImages&category_id=17&per_page=20&page=1
```

Response (JSON):

```json
{
  "stat": "ok",
  "result": {
    "category_id": 17,
    "images": [
      { "id": 1204, "permalink": "https://galerie.example/photo/1204",
        "representative": { "source": "https://…/CU/IMG_1204.jpg" } }
    ],
    "nb_images": 137
  }
}
```

## Rate Limits

Keine eingebauten Limits; empfohlen werden Begrenzung im Webserver (`mod_qos`, nginx `limit_req`) und Session-Timeouts.

## SDKs und Client-Bibliotheken

- **offiziell**: Piwigo-Apps (iOS/Android) nutzen `ws.php`
- **Community**: Python `piwigo-api`, PHP-Wrapper in Plugin-Beispielen
- **Importe**: Piwigo-Export/Import, Piwigo-Companion für Uploads

## Skin-Hinweis

Category/Image/Tag/Group entsprechen dem Standardmodell ([modelle.md](../../../../data/modelle.md)); benutzerdefinierte Felder folgen [felder.md](../../../../data/felder.md).
