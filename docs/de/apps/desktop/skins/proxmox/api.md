# Proxmox VE - API Dokumentation

## Übersicht

Die Proxmox-REST-API ist die vollständige, offizielle Schnittstelle der Plattform: Jeder Knopf der Weboberfläche entspricht einem API-Aufruf. Basis ist `https://<host>:8006/api2/json` (JSON-Ausgabe; `/api2/exttype` liefert formatspezifische Ausgaben). Authentifiziert wird wahlweise mit **Login-Ticket + CSRF-Token** (interaktiv) oder **API-Token** (für Skripte, empfohlen). Lange Aktionen sind asynchron und liefern eine Task-ID (UPID).

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST `/api2/json` | gesamtes Verwaltungsspektrum | Offiziell, stabil dokumentiert (pve-api-docs) |
| `pvesh` CLI | REST-Aufrufe direkt auf der Node | Offiziell |
| `qm` / `pct` / `pvesm` / `pveum` | Domänen-Kommandos | Offiziell |
| Webhooks | — | ❌ Nicht vorhanden |

## Authentifizierung

### Ticket-Login (Browser/Skript-Simulation)

```bash
curl -sk -X POST https://pve1:8006/api2/json/access/ticket \
  -d 'username=root@pam' -d 'password=SECRET'
```

Antwort (gekürzt):

```json
{ "data": {
    "ticket": "PVE:... uzun",
    "CSRFPreventionToken": "3A2B...",
    "username": "root@pam"
} }
```

Folgende Requests senden das Ticket als `Cookie: PVEAuthCookie=<ticket>` (alternativ `Authorization: PVEAuthCookie=<ticket>`).
- Für **jede Nicht-GET-Anfrage** zusätzlich `X-CSRF-Prevention-Token: <token>`.
- Tickets laufen nach wenigen Stunden ab — für Automatisierung API-Tokens verwenden.

### API-Token (empfohlen)

Anlegen in der UI (Datacenter → Permissions → API Tokens) oder per CLI:

```bash
pveum user token add automation@pve ci-token --privsep 0
```

Jeder Request trägt:

```
Authorization: PVEAPIToken=automation@pve!ci-token:<uuid-secret>
```

- Token-Rechte über Rollen/ACL einschränkbar, optional Node-Bindung und Ablaufdatum.
- Das Secret ist **nur bei Erstellung** sichtbar; verloren → neuen Token erzeugen.

### Realms

`pam` (Linux-User der Node), `pve` (eigener Store), `ldap`, `ldap2`, `ad`, `keycloak`/OIDC (versionabhängig). Tokens existieren pro Benutzer, unabhängig vom Realm.

## Endpunkte (Auswahl)

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api2/json/version` | Versionsinfo der API |
| `GET` | `/cluster/status` | Nodes, Quorum, Cluster-Name |
| `GET` | `/cluster/resources?type=vm` | alle VMs/Container (Inventory) |
| `GET` | `/nodes` | Nodes mit Status |
| `GET` | `/nodes/{node}/qemu` | VMs der Node |
| `POST` | `/nodes/{node}/qemu` | VM anlegen (Parameter als JSON) |
| `GET` | `/nodes/{node}/qemu/{vmid}/config` | VM-Konfiguration |
| `SET/PUT` | `/nodes/{node}/qemu/{vmid}/config` | VM-Einstellung ändern |
| `POST` | `/nodes/{node}/qemu/{vmid}/status/start` | VM starten |
| `POST` | `/nodes/{node}/qemu/{vmid}/status/shutdown` | VM herunterfahren |
| `POST` | `/nodes/{node}/qemu/{vmid}/status/stop` | Notaus |
| `POST` | `/nodes/{node}/qemu/{vmid}/migrate` | (Live-)Migration |
| `GET` | `/nodes/{node}/qemu/{vmid}/snapshots` | Snapshots auflisten |
| `POST` | `/nodes/{node}/qemu/{vmid}/snapshot` | Snapshot anlegen |
| `GET` | `/nodes/{node}/lxc` | Container der Node |
| `POST` | `/nodes/{node}/lxc/{ctid}/status/start` | Container starten |
| `GET` | `/nodes/{node}/storage` | Storage-Status der Node |
| `GET` | `/storage` | Storage-Pools (API-Version 8.x) |
| `GET` | `/cluster/backup` | Backup-Jobs |
| `POST` | `/nodes/{node}/vzdump` | Backup einer VM anstoßen |
| `GET` | `/cluster/tasks` | Task-Verlauf (UPIDs) |
| `GET` | `/nodes/{node}/tasks/{upid}` | Einzeltask-Status |
| `GET` | `/access/users` | Benutzer (Admin) |
| `GET` | `/access/realms` | Realms (Admin, versionabhängig) |
| `GET` | `/access/acl` | ACL-Zuweisungen |
| `GET` | `/pools` | Pools |

## Beispiele

### Inventar mit Token abrufen

```bash
curl -sk -H 'Authorization: PVEAPIToken=automation@pve!ci-token:SECRET' \
  'https://pve1:8006/api2/json/cluster/resources?type=vm' \
  | jq -r '.data[] | "\(.vmid) \(.name) \(.status)"'
```

### VM starten (asynchron)

```bash
curl -sk -X POST \
  -H 'Authorization: PVEAPIToken=automation@pve!ci-token:SECRET' \
  https://pve1:8006/api2/json/nodes/pve1/qemu/101/status/start
```

Antwort: `202 Accepted`, `data` = UPID, z. B.

```json
{ "data": "UPID:pve1:0012AB34:00005678:4C9D0001:start:101:qemu:root@pam:" }
```

Status nachverfolgen:

```bash
curl -sk -H 'Authorization: PVEAPIToken=...' \
  https://pve1:8006/api2/json/nodes/pve1/tasks/UPID:pve1:0012AB34:00005678:4C9D0001:start:101:qemu:root@pam:
```

### VM mit Ticket + CSRF erstellen

```bash
TICKET=... ; CSRF=...
curl -sk -X POST https://pve1:8006/api2/json/nodes/pve1/qemu \
  -H "Cookie: PVEAuthCookie=$TICKET" \
  -H "X-CSRF-Prevention-Token: $CSRF" \
  -d 'vmid=200' -d 'name=testvm' -d 'memory=2048' -d 'cores=2' \
  -d 'disk=local-lvm:32'
```

### pvesh (auf der Node)

```bash
pvesh get /cluster/resources --type vm --output-format json
pvesh set /nodes/pve1/qemu/101/status/start
pvesh create /nodes/pve1/qemu --vmid 201 --name demo
```

## Rate Limits und Betriebshinweise

- **Keine eingebaute Ratenbegrenzung** der API — Schutz über Firewall-Regeln, Reverse Proxy oder fail2ban (GUI-/Ticket-Logins).
- Fehler `401/403` bei falschem Token/fehlenden ACLs; `429` nur, wenn vorgeschaltete Systeme begrenzen.
- Asynchrone Aktionen: auf UPID-Finish prüfen statt Schlafintervalle zu raten.
- API-Doku der eigenen Version: Reiter *Documentation → API Viewer* in der UI oder `pvesh help`.
- HTTPS-Zertifikate prüfen (`-k` nur in Laboren), Token getrennt nach Zweck verwalten.

## Webhooks und Benachrichtigungen

- **Keine Webhooks** (weder eingehend noch ausgehend) dokumentiert.
- Ab Proxmox VE 8.1 existiert ein **Notification-System** (Reiter *Notifications*): Matching-Regeln senden Alerts an Mail-/Jabber-/SMS-Ziele (versionabhängig) — kein generisches HTTP-Callback.
- Automatisierungs-Workaround: Cron/Poller gegen `/cluster/tasks` oder Monitoring-Agenten (Prometheus-Exporter) auf den Nodes.

## SDKs und Client-Bibliotheken

| Bibliothek | Sprache | Anmerkung |
|------------|---------|-----------|
| `proxmoxer` | Python | de-facto Standard, unterstützt Ticket- und Token-Auth |
| Terraform-Provider `bpg/proxmox` | HCL | deklarative VM-/Container-Verwaltung |
| Ansible-Sammlung `community.proxmox` (Nachfolger der alten `proxmox`-Module) | YAML | VM-/Storage-Module |
| Perl `PVE::API2` | Perl | direkt auf den Nodes |
| `pvesh` | CLI | offiziell, JSON-fähig, ideal für Skripte |

## Siehe auch

- [index.md](index.md)
- [description.md](description.md)
- [features.md](features.md)
- [menu.md](menu.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
