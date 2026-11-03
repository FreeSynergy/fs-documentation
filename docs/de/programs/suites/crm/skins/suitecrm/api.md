# SuiteCRM - API Dokumentation

## Übersicht

SuiteCRM stellt eine **modulorientierte REST-Schnittstelle (v8)** sowie eine ältere **SOAP-Schnittstelle** bereit. Beide arbeiten mit Benutzernamen und Passwort der Instanz, nicht mit API-Schlüsseln. Die offiziellen Beschreibungen der Methoden und Felder stehen im Entwicklerhandbuch unter `developers.suitecrm.com`; Details und Verhalten sind versionsabhängig.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST v8 (`/service/v8/rest.php`) | Datensätze aller Module lesen, schreiben, löschen, Beziehungen pflegen | Offiziell dokumentiert |
| SOAP (`/service/v4/soap.php`) | Gleiche Verfahren wie REST, XML-basiert | Veraltet, aber verfügbar |
| Neue REST-Routen in SuiteCRM 8 | Zugriff über die 8er-Shell | versionsabhängig, in der Entwicklerdoku nachschlagen |
| Webhooks | ❌ Nicht vorhanden | — |
| GraphQL, OData, CalDAV, CardDAV | ❌ Nicht vorhanden | — |

## Authentifizierung

- **Kein API-Key-System**: es gibt keine langlebigen API-Tokens und (in 7.x) kein OAuth2.
- **REST v8**: Zugriff wahlweise mit dem Header `User-Auth: benutzer::passwort` pro Anfrage oder über eine Session-ID, die vorher mit `login` geholt wurde.
- **Session-ID**: Antwort von `login` enthält ein Feld `id`; dieses wird als `session` in folgenden Aufrufen mitgegeben.
- **SOAP**: Session-ID als erstes Argument jeder Methode.
- **Rechte**: alle Aufrufe unterliegen den Rollen und Teams des Kontos; ein API-Aufruf sieht Daten nur, wenn das Konto sie in der Oberfläche sehen dürfte.
- **OAuth/LDAP**: LDAP betrifft die Anmeldung in der Oberfläche, nicht die API. Externe OAuth-Systeme sind nur über Erweiterungen möglich.

### Login-Flow (REST v8)

1. `login` mit Benutzername und Passwort aufrufen
2. zurückgegebene Session-ID (`id`) speichern
3. weitere Methoden mit `session` ausführen
4. am Ende `logout` aufrufen

## Endpunkte

### Basis

```
GET/POST /service/v8/rest.php
```

Parameter werden als Formularfelder oder Query-Parameter übergeben: `method`, `input_type=JSON`, `response_type=JSON`, `session`, `module`, weitere methodenspezifische Felder.

### Verfahren (REST v8)

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `POST` | `/service/v8/rest.php?method=login` | Anmeldung, liefert Session-ID |
| `POST` | `/service/v8/rest.php?method=logout` | Sitzung beenden |
| `POST` | `/service/v8/rest.php?method=authenticate` | Prüfen, ob Zugangsdaten gültig sind |
| `GET` | `/service/v8/rest.php?method=get_module_list` | Verfügbare Module auflisten |
| `GET` | `/service/v8/rest.php?method=get_metadata` | Felddefinitionen und Formular-Layout eines Moduls |
| `GET` | `/service/v8/rest.php?method=get_entry_list` | Datensätze eines Moduls mit Filter, Sortierung, Paginierung |
| `GET` | `/service/v8/rest.php?method=get_entry_count` | Anzahl Treffer für einen Filter |
| `GET` | `/service/v8/rest.php?method=get_entry` | Einzelnen Datensatz anhand der ID laden |
| `POST` | `/service/v8/rest.php?method=set_entry` | Datensatz anlegen oder ändern |
| `POST` | `/service/v8/rest.php?method=set_entries` | Mehrere Datensätze in einem Aufruf schreiben |
| `POST` | `/service/v8/rest.php?method=delete_entry` | Datensatz löschen |
| `POST` | `/service/v8/rest.php?method=relationship_add` | Beziehung zwischen zwei Datensätzen anlegen |
| `POST` | `/service/v8/rest.php?method=relationship_remove` | Beziehung trennen |
| `GET` | `/service/v8/rest.php?method=get_related` | Verknüpfte Datensätze laden (Subpanel-Inhalte) |

### Module der CRM-Kategorie

| Modul | Bedeutung in der Oberfläche |
|-------|-----------------------------|
| `Leads` | Interessenten (Konvertierung zu Contact/Account/Opportunity) |
| `Contacts` | Kontakte |
| `Accounts` | Firmen |
| `Opportunities` | Verkaufschancen / Deals |
| `Calls`, `Meetings`, `Tasks` | Aktivitäten |
| `Cases`, `Bugs` | Support-Vorgänge |
| `Emails`, `Notes` | Kommunikation |
| `Products`, `Quotes` | Produktkatalog und Angebote |

### SOAP

```
POST /service/v4/soap.php
```

Methodennamen entsprechen den REST-Verfahren (`login`, `get_entry_list`, `set_entry`, ...), erstes Argument ist stets die Session. Die WSDL wird über die Instanz ausgeliefert; genaue Pfadangaben sind versionsabhängig.

## Beispiele

### Lead suchen (curl)

```bash
curl -s -X POST "https://crm.example.com/service/v8/rest.php" \
  -d "method=get_entry_list" \
  -d "input_type=JSON" \
  -d "response_type=JSON" \
  -H "User-Auth: api_user::geheim" \
  -d "module=Leads" \
  -d "query=last_name LIKE '%Meyer%'" \
  -d "max_num=10" \
  -d "order_by=date_modified DESC" \
  -d "offset=0"
```

Antwort (gekürzt):

```json
{
  "module_list": [
    { "Leads": { "id": "5f1a...", "first_name": "Anna", "last_name": "Meyer", "status": "New" } }
  ],
  "result_count": 1,
  "current_entry": 0
}
```

### Lead anlegen (curl)

```bash
curl -s -X POST "https://crm.example.com/service/v8/rest.php" \
  -d "method=set_entry" \
  -d "input_type=JSON" \
  -d "response_type=JSON" \
  -H "User-Auth: api_user::geheim" \
  -d "module=Leads" \
  --data-urlencode 'name_value_list=[{"name":"first_name","value":"Anna"},{"name":"last_name","value":"Meyer"},{"name":"status","value":"New"},{"name":"account_name","value":"Meyer AG"}]'
```

### Opportunity mit Session (Python)

```python
import requests

BASE = "https://crm.example.com/service/v8/rest.php"

# 1. Login
r = requests.post(BASE, data={
    "method": "login", "input_type": "JSON", "response_type": "JSON",
    "user_auth": "api_user::geheim",
})
session_id = r.json()["id"]

# 2. Offene Deals laden
r = requests.get(BASE, params={
    "method": "get_entry_list", "input_type": "JSON", "response_type": "JSON",
    "session": session_id, "module": "Opportunities",
    "query": "sales_stage NOT IN ('Closed Won','Closed Lost')",
    "max_num": 50, "order_by": "date_expected_close ASC",
})
for row in r.json()["module_list"]:
    print(list(row.values())[0]["name"], list(row.values())[0]["amount"])

# 3. Logout
requests.post(BASE, data={"method": "logout", "session": session_id,
                          "input_type": "JSON", "response_type": "JSON"})
```

## Rate Limits

- SuiteCRM bringt **keine eingebaute Ratenbegrenzung** für REST oder SOAP mit.
- Schutz über den Webserver oder Reverse Proxy empfohlen: nginx `limit_req`, Apache `mod_ratelimit`, Fail2ban auf Fehlermeldungen.
- Begrenzend wirken außerdem die PHP-Einstellungen (`max_execution_time`, `memory_limit`, `post_max_size`) und die Leistung der Datenbank; große `set_entries`-Aufrufe und breite `get_entry_list`-Abfragen sind die üblichen Engpässe.
- Empfohlene Richtung: wenige, gebündelte Aufrufe pro Minute statt vieler Einzelabfragen; `max_num` und `offset` sempre nutzen.

## Webhooks und Automatisierung

- **Keine Webhooks**: SuiteCRM versendet keine Ereignisse an externe Systeme.
- **Eigene Automatisierung**: Workflow-Modul (Trigger, Bedingungen, Aktionen) und Scheduler (`cron.php`) laufen in der Instanz.
- **Logic Hooks**: PHP-Funktionen an Modell-Ereignissen (`before_save`, `after_save`, `after_delete`) sind der übliche Weg, um bei Änderungen ein externes System per HTTP anzusteuern.
- **Workaround für ausgehende Ereignisse**: Cron-Skript, das geänderte Datensätze über den Feldverlauf ermittelt und per REST an ein Zielsystem meldet.

## SDKs und Client-Bibliotheken

- **Kein offizielles SDK** von SuiteCRM für Programmiersprachen.
- REST v8 ist reines HTTP mit Formularparametern, daher genügen `curl`, `requests` (Python), `axios`/`fetch` (JavaScript), Guzzle (PHP).
- SOAP-Clients (SoapClient in PHP, suds/zeep in Python) funktionieren gegen die SOAP-Schnittstelle.
- Community-Bibliotheken für SuiteCRM/SugarCRM existieren, sind aber nicht amtlich gepflegt; Version und Abdeckung vor Nutzung prüfen.

## Hinweise für den Betrieb

- API-Konto mit eigenen Rechten anlegen und auf benötigte Module beschränken.
- HTTPS erzwingen; der Header `User-Auth` enthält sonst Klartext-Passwörter.
- Nach Updates Metadaten-Cache leeren, sonst liefert `get_metadata` veraltete Felddefinitionen.
- Eigene Felder heißen in der API so, wie Studio sie anlegt (Feldname aus `get_metadata` lesen, nicht raten).

## Siehe auch

- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
