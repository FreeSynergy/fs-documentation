# ERPNext - API

The Frappe framework offers a REST interface. Sources: [REST API](https://docs.frappe.io/framework/user/en/api/rest), retrieved 2026-11-10.

| Part | Use |
|------|-----|
| `/api/resource/<doctype>` | list (filters, fields, order, paging) and create |
| `/api/resource/<doctype>/<name>` | read, partial update, delete |
| `/api/method/<dotted.path>` | call a whitelisted server method |
| file upload | multipart upload endpoint |

## Authentication

- API key and secret in the `Authorization` header; requests run with that user's roles.
- Password login with a session cookie.
- OAuth bearer access token.

Rate limits and webhooks: Open (the page does not cover them).
