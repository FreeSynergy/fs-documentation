# XWiki - API Dokumentation

## Übersicht
XWiki bietet ein umfangreiches REST API und ein proprietäres Java-basiertes API für den Zugriff auf alle Wiki-Funktionen. Es unterstützt auch einen JavaScript Client und WebSocket-basierte Echtzeitfunktionen.

## Authentifizierung
XWiki unterstützt folgende Authentifizierungsmethoden:

- **Basic Authentication**: Benutzername und Passwort
- **XWiki Authentication Token**: Token-basierte Authentifizierung
- **SSO**: SAML, LDAP, OAuth2, OpenID Connect
- **Anonymous Access**: Für öffentliche Inhalte

### Auth Header (Basic)
```
Authorization: Basic base64(username:password)
X-XWiki-Auth-token: your-auth-token
```

## Endpunkte

### Pages (Seiten)
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/rest/wikis/{wiki}/spaces/{space}/pages/{page}` | Holt eine Seite |
| GET | `/rest/wikis/{wiki}/spaces/{space}/pages` | Listet Seiten in einem Space |
| POST | `/rest/wikis/{wiki}/spaces/{space}/pages` | Erstellt eine neue Seite |
| PUT | `/rest/wikis/{wiki}/spaces/{space}/pages/{page}` | Aktualisiert eine Seite |
| DELETE | `/rest/wikis/{wiki}/spaces/{space}/pages/{page}` | Löscht eine Seite |
| GET | `/rest/wikis/{wiki}/spaces/{space}/pages/{page}/content` | Holt Seiteninhalt |
| GET | `/rest/wikis/{wiki}/spaces/{space}/pages/{page}/versions` | Listet Versionen |

### Documents (Dokumente)
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/rest/documents/{documentReference}` | Holt ein Dokument |
| POST | `/rest/documents` | Erstellt/aktualisiert Dokument |

### Objects (Objekte)
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/rest/objects/{documentReference}` | Listet Objekte |
| POST | `/rest/objects/{documentReference}` | Erstellt Objekt |
| PUT | `/rest/objects/{objectReference}` | Aktualisiert Objekt |
| DELETE | `/rest/objects/{objectReference}` | Löscht Objekt |

### Classes (Klassen)
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/rest/classes/{classReference}` | Holt eine Klasse |
| GET | `/rest/classes/{classReference}/properties` | Listet Klassen-Eigenschaften |

### Users (Benutzer)
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/rest/users` | Listet Benutzer |
| GET | `/rest/users/{username}` | Holt einen Benutzer |
| POST | `/rest/users` | Erstellt Benutzer |
| PUT | `/rest/users/{username}` | Aktualisiert Benutzer |
| DELETE | `/rest/users/{username}` | Löscht Benutzer |

### Search
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/rest/searches/{searchName}` | Führt Suchanfrage aus |

### Authentication
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| POST | `/rest/authentication/login` | Einloggen |
| POST | `/rest/authentication/logout` | Ausloggen |
| GET | `/rest/authentication/currentuser` | Aktueller Benutzer |

### JavaScript Client
XWiki提供JavaScript Client library unter `/jsondoc/` für AJAX-Interaktionen.

## Beispiele

### Seite abrufen
```bash
curl -X GET "https://xwiki.example.com/rest/wikis/xwiki/spaces/Main/pages/WebHome" \
  -H "Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=" \
  -H "Accept: application/json"
```

### Seite erstellen
```bash
curl -X POST "https://xwiki.example.com/rest/wikis/xwiki/spaces/Main/pages" \
  -H "Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Neue Seite",
    "content": "# Titel\n\nInhalt",
    "parent": "Main.WebHome"
  }'
```

### Java Example (XWiki Scripting)
```java
// In einem XWiki Script (Groovy, Python, JavaScript)
import org.xwiki.document.Document;
import org.xwiki.model.reference.DocumentReference;

DocumentReference ref = new DocumentReference("xwiki", "Main", "NeueSeite");
Document doc = documentAccessor.createNewDocument(ref);
doc.setContent("# Titel\n\nInhalt");
doc.save();
```

### JavaScript Client
```javascript
// XWiki JavaScript API
var doc = XWiki.getDocument("Main.NeueSeite");
doc.setContent("# Titel\n\nInhalt");
doc.save({
    success: function() { console.log("Erfolg!"); },
    error: function(e) { console.error(e); }
});
```

## Rate Limits
- Standard: 100 Anfragen pro Minute pro Benutzer
- Konfigurierbar in `xwiki.properties`
- Rate Limiting kann pro IP oder Benutzer aktiviert werden

## Webhooks
XWiki unterstützt Webhooks über die Event-System:
- `document.created`: Dokument erstellt
- `document.updated`: Dokument aktualisiert
- `document.deleted`: Dokument gelöscht
- `document.moved`: Dokument verschoben
- `document.restored`: Dokument wiederhergestellt

Konfiguration in `xwiki.cfg` oder über Erweiterungen.

## SDKs und Client-Bibliotheken
- **Java**: Offizielles SDK (XWiki Platform)
- **JavaScript**: XWiki JavaScript API
- **Python**: `xwiki-python` (community)
- **PHP**: `xwiki-php-api` (community)
- **C#**: `XWiki.NET` (community)

## Siehe auch
- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (diese Datei)
