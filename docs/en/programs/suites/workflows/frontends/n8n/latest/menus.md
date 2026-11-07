# n8n - Menu items

## Editor top bar

| Element | Content |
|---------|--------|
| Workflow name/arrows | Save, **Execute Workflow**, Activate/Deactivate |
| Node palette (`Tab`) | Integrations, core nodes (Webhook, HTTP Request, Code, IF, Switch, Merge, Schedule) |
| ⋯ menu | Import/export (JSON), copy to clipboard, downloads, settings, tags |

## Node context menu (double-click)

- Parameter panel on the right; operation/resource selection
- "Execute node" (test individually), "Pin" (fix test data), "Run once per item"

## Left sidebar

| Menu | Content |
|------|---------|
| Workflows | List, templates (thousands of templates), folders |
| Credentials | Credentials vault (OAuth2/API keys) |
| Executions | History list with individual log |
| Credentials/templates search | Community templates |

## Instance level (⚙, self-hosted)

| Area | Content |
|------|---------|
| Users & Authentication | Roles (owner/admin/member/viewer), LDAP/SAML/SSO |
| Settings | Time zone, execution pruning, queue mode info, create API keys |
| Source control (Enterprise) | Git sync of workflows |
| External secrets (Enterprise) | Vault/1Password/… |

## Menus by role

Owner/admin: instance settings; member: own workflows/credentials; viewer: view only.
