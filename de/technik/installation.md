# Installation & Invite-System

[← Zurück zum Index](../INDEX.md) | [Node](../programme/node/README.md)

---

## Zwei Installationspfade

### 1. Node (Server)

1. Neues Netzwerk erstellen ODER bestehendem beitreten
2. Bei Beitritt: Invite-Datei einlesen (Token + Host-Adresse + CA-Hash)
3. IP-Typ (statisch → aktiver Modus, dynamisch → passiver Modus)
4. Sprachen auswählen
5. Zeitzone (nur für Anzeige — Server laufen immer UTC)
6. Store-Quellen konfigurieren
7. IAM wählen (Kanidm empfohlen)
8. Proxy wählen (Zentinel empfohlen)
9. Services installieren

### 2. Desktop (Client)

1. Invite-Datei einlesen (Token + Host-Adresse + CA-Hash)
2. TLS-Verbindung aufbauen (CA-Hash verifiziert)
3. IAM-Login via OAuth2/OIDC
4. Fertig — Desktop ist API-Client, kein Admin

## Invite-Datei

```toml
[invite]
token = "a1b2c3.x9y8z7w6v5u4t3s2"
ca_hash = "sha256:4f8a..."
host = "node1.example.com:9443"
network_id = "uuid-..."
created_at = "2026-03-16T12:00:00Z"
expires_at = "2026-03-17T12:00:00Z"
permissions = "full"    # full | readonly | desktop-only
```

Die Datei ist verschlüsselt. Der Port kann für jede Einladung verschieden sein. Der Port wird nur solange geöffnet wie die Einladung gültig ist.

## mDNS Discovery (optional)

Im LAN: `_freesynergy._tcp.local` — findet Nodes automatisch. Token trotzdem erforderlich.

---

Weiter: [Sicherheit](sicherheit.md) | [Node](../programme/node/README.md)
