# n8n - Menüpunkte

## Editor oben

| Element | Inhalt |
|---------|--------|
| Workflow-Name/Pfeile | Save, **Execute Workflow**, Activate/Deactivate |
| Nodes-Palette (`Tab`) | Integrationen, Core-Nodes (Webhook, HTTP Request, Code, IF, Switch, Merge, Schedule) |
| ⋯-Menü | Imports/Export (JSON), Copy to clipboard, Downloads, Settings, Tags |

## Node-Kontextmenü (Doppelklick)

- Parameter-Panel rechts; Operations/Resource-Auswahl
- „Execute node“ (einzeln testen), „Pin“ (Testdaten fixieren), „Run once per item“

## linke Seitenleiste

| Menü | Inhalt |
|------|--------|
| Workflows | Liste, Templates (tausende Vorlagen), Ordner |
| Credentials | Zugangsdaten-Tresor (OAuth2/API-Keys) |
| Executions | Verlaufsliste mit Einzel-Log |
| Credentials/Templates-Suche | Community-Vorlagen |

## Instanz-Ebene (⚙, self-hosted)

| Bereich | Inhalt |
|---------|--------|
| Users & Authentication | Rollen (Owner/Admin/Member/Viewer), LDAP/SAML/SSO |
| Settings | Timezone, Execution-Pruning, Queue-Modus-Info, API-Keys erzeugen |
| Source Control (Enterprise) | Git-Sync der Workflows |
| External Secrets (Enterprise) | Vault/1Password/… |

## Menüs nach Rolle

Owner/Admin: Instanzeinstellungen; Member: eigene Workflows/Credentials; Viewer: nur Ansehen.
