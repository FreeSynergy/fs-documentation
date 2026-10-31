# Synology DSM - API Dokumentation

## Übersicht

DSM stellt eine **HTTP/JSON-API** über einen einzigen Eingangspunkt bereit: `entry.cgi`. Jede Anfrage beschreibt die gewünschte API, ihre Version und die Methode:

GET/POST http://<nas>:5000/webapi/entry.cgi?api=SYNO.<Modul>.<Name>&version=<n>&method=<name>
```

Die API ist in den **Entwicklerhandbüchern der Pakete** dokumentiert (FileStation, Download Station, Surveillance Station, WebStation …) und **nicht als stabile Produkt-Schnittstelle zugesagt**: Namen und Versionen ändern sich zwischen DSM-Hauptversionen.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| `SYNO.*`-APIs über `entry.cgi` | Auth, System, Benutzer, Freigaben, Pakete, FileStation | in Entwicklerhandbüchern dokumentiert |
| `query.cgi` (`SYNO.API.Info`) | verfügbare APIs und Versionen abfragen | dokumentiert |
| Paket-eigene Endpunkte | Drive, Chat, Surveillance, Container Manager | teils **nicht öffentlich dokumentiert** |
| Webhooks | ❌ Nicht vorhanden (Ereignisskripte stattdessen) | — |

## Authentifizierung

**`SYNO.API.Auth`** (Versionen 1–7, je DSM-Stand) erzeugt eine Sitzung:

| Parameter | Beschreibung |
|-----------|--------------|
| `account` / `passwd` | Benutzername und Kennwort (über HTTPS und URL-kodiert übergeben) |
| `format` | `sid` (Sitzungskennung im Antwortkörper) oder `cookie` (Sitzung per HTTP-Cookie) |
| `session` | Name des Zielbereichs (z. B. `FileStation`), begrenzt die Sitzung auf diesen Kontext |
| `expire` | Sitzungsdauer, `always` für unbegrenzt (je nach Einstellung erlaubt) |
| `otp_code` | 6-stelliger TOTP-Code, wenn das Konto zwei-Faktor-Authentifizierung nutzt |
| `enable_syno_token` | `yes` liefert das Anti-CSRF-Token (`SynoToken`) im Login-Ergebnis |

**Sitzungsbehandlung**

- Bei `format=sid` kommt `sid` im Antwortkörper; jede Folgeanfrage übergibt ihn als `_sid=<wert>`.
- Bei `format=cookie` setzt DSM ein HttpOnly-Sitzungscookie (in aktuellen Versionen `id`); der Browser sendet es automatisch.
- **Schreibende `POST`-Anfragen** verlangen zusätzlich den Header **`SynoToken`** mit dem Wert des Cookies `_SynoToken`; fehlt er, wird die Anfrage abgelehnt.
- Abmelden: `method=logout` mit `session=<name>` (und `_sid` im SID-Modus). Sitzungen laufen mit Timeout ab; Mehrfachanmeldung kann eine ältere Sitzung beenden (Fehler `107`).

## Fehlercodes

**Allgemeine Fehler (API-übergreifend)**

| Code | Bedeutung |
|------|-----------|
| 100 | unbekannter Fehler |
| 101 | `api`, `version` oder `method` fehlt |
| 102 | angeforderte API existiert nicht |
| 105 | angemeldete Sitzung hat keine Berechtigung |
| 106 | Sitzungs-Timeout |

**`SYNO.API.Auth`**

| Code | Bedeutung |
|------|-----------|
| 400 | kein solches Konto oder falsches Kennwort |
| 401 | Konto deaktiviert |
| 402 | Berechtigung verweigert |
| 403 | Zwei-Faktor-Code erforderlich |
| 404 | Zwei-Faktor-Code abgelehnt |
| 406–409 | erweiterte Schutzfälle (Konto- oder IP-Sperre nach häufigen Fehlversuchen); **je nach DSM-Version unterschiedlich dokumentiert** |

## Endpunkte

### Authentifizierung und API-Übersicht

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET`/`POST` | `/webapi/entry.cgi?api=SYNO.API.Auth&version=6&method=login` | Anmeldung, liefert `sid` und optional `SynoToken` |
| `GET`/`POST` | `/webapi/entry.cgi?api=SYNO.API.Auth&version=6&method=logout` | Sitzung beenden |
| `GET` | `/webapi/query.cgi?api=SYNO.API.Info&version=1&method=query&query=all` | verfügbare APIs und Versionen abfragen |

### System, Benutzer, Pakete (`SYNO.Core.*`)

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `api=SYNO.Core.System&version=1&method=info` | Modell, DSM-Version, Uptime, Laufwerke |
| `GET` | `api=SYNO.Core.System.Utilization&version=1&method=get` | CPU-, RAM-, Netzwerk- und Volume-Werte |
| `GET` | `api=SYNO.Core.Share&version=1&method=list` | Freigegebene Ordner und Einstellungen |
| `GET` | `api=SYNO.Core.Package&version=1&method=load_all` | installierte Pakete mit Status |
| `POST` | `api=SYNO.Core.Package.Control&version=1&method=start` / `stop` | Paket starten oder stoppen |
| `GET` | `api=SYNO.Storage.CGI.Storage&version=1&method=load_info` | Pools, Volumes, Laufwerke, Warnungen |

### Dateioperationen (`SYNO.FileStation.*`)

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `POST` | `api=SYNO.FileStation.List&version=2&method=list` | Inhalt eines Ordners |
| `POST` | `api=SYNO.FileStation.Download&method=download` | Datei herunterladen (`mode=open\|download`) |
| `POST` | `api=SYNO.FileStation.Upload&method=upload` | multipart-Hochladen (`path`, `overwrite`, `create_parents`) |
| `POST` | `api=SYNO.FileStation.CreateFolder&method=create` | Ordner anlegen (Aufgabe) |
| `POST` | `api=SYNO.FileStation.Delete&method=delete` | löschen, liefert `taskid` |
| `POST` | `api=SYNO.FileStation.CopyMove&method=start` / `status` / `stop` | kopieren oder verschieben |

## Beispiele

### Anmelden (mit OTP und SynoToken)

```bash
curl -s -k "https://nas.example.internal:5001/webapi/entry.cgi" \
  --data-urlencode "api=SYNO.API.Auth" --data-urlencode "version=6" \
  --data-urlencode "method=login" --data-urlencode "account=scripts" \
  --data-urlencode "passwd=geheim" --data-urlencode "format=sid" \
  --data-urlencode "session=FileStation" \
  --data-urlencode "enable_syno_token=yes" --data-urlencode "otp_code=123456"
```

Antwort:

{
  "data": { "is_portal_port": false, "sid": "aG9tZXBhZ2U6MTcw…", "synotoken": "sFQ7m2YzQpXk…" },
  "success": true
}
```

### Auslastung abfragen

```bash
curl -s -k "https://nas.example.internal:5001/webapi/entry.cgi?api=SYNO.Core.System.Utilization&version=1&method=get&_sid=$SID"
```

Antwort (gekürzt):

```json
{
  "success": true,
  "data": {
    "cpu": { "user_load": 8, "system_load": 3, "fg_cpu_load": 11 },
    "memory": { "total_real_ram": 17179869184, "actual_utilization": 42 },
    "volume": [ { "id": "/volume1", "size_free": 4123168604160, "size_total": 7988631699456 } ]
  }
}
```

### Ordnerinhalt auflisten und Aufgabe verfolgen

```bash
curl -s -k "https://nas.example.internal:5001/webapi/entry.cgi" \
  -H "SynoToken: $SYNOTOKEN" \
  -d "api=SYNO.FileStation.List&version=2&method=list&folder_path=/video" \
  --data-urlencode "_sid=$SID"
```

Antwort (gekürzt):

```json
{
  "success": true,
  "data": {
    "offset": 0, "total": 1,
    "files": [ { "name": "Film.mkv", "path": "/video/Film.mkv", "isdir": false } ]
  }
}
```

```json
```

## Rate Limits und Limits

- **Keine öffentlich dokumentierten Ratenzahlen** für `entry.cgi`; praktisch begrenzen CPU, I/O und die Anzahl gleichzeitiger Sitzungen.
- **Konto-Schutz**: nach fehlgeschlagenen Anmeldungen sperrt DSM die Quell-IP (Systemsteuerung → Sicherheit → Schutz); bei OTP-Fehlversuchen sperrt das Konto vorübergehend.
- Empfehlung: Anfragen serialisieren, Ergebnisse cachen, Aufgaben-APIs (`taskid`) statt vieler Einzelaufrufe nutzen, Sitzungen sauber beenden.

## Ereignisse und Webhooks

- **Keine Webhooks**: DSM sendet keine HTTP-Ereignisse nach außen.
- **Benachrichtigungen**: E-Mail, Push über Synology Notification, Portal-Glocke; je Ereignis konfigurierbar.
- **Aufgabenplanung mit benutzerdefinierten Ereignissen** (Systemstart, Herunterfahren, knapper Speicherplatz, SSD-TRIM, USB-Gerät): darauf folgen Bash- oder PowerShell-Skripte, die ihrerseits ein `curl` an ein externes System senden.

## SDKs und Client-Bibliotheken

- **Kein offizieller SDK-Download**; die Entwicklerhandbücher (PDF je Paket) sind die Referenz.
- **Community-Bibliotheken** (Auswahl, Wartung außerhalb von Synology): `python-synology`/`SynoApi` (Python), `py-synologydsm-api` (Python), `synology-api` (Go), `Synology.Api.Client` (C#).
- **Integrationshilfe**: Die Homepage-Bibliothek besitzt einen DSM-Handler für `SYNO.API.Auth` und `entry.cgi`, siehe [../gethomepage/structure.md](../gethomepage/structure.md).

## Hinweise für den Betrieb

- **HTTPS über Port 5001** verwenden; Klartext-Anmeldungen über 5000 nur in segmentierten Netzen.
- **`SynoToken` bei POST** immer mitschicken, sonst schlagen schreibende Aufrufe fehl.
- **Sitzungen beenden** (`method=logout`), um Sitzungskollisionen (Fehler `107`) zu vermeiden.

## Siehe auch

- [description.md](description.md)
- [features.md](features.md)
- [menu.md](menu.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
