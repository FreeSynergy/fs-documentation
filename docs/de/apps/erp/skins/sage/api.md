# Sage - API Dokumentation

## Übersicht

**Es gibt nicht „die“ Sage-API.** Zugänge pro Produkt:

| Produkt | API-Zugang | Status |
|---------|-----------|--------|
| Sage Business Cloud (Accounting/CRM) | REST (developer.sage.global), OAuth2, Webhooks | offiziell |
| Sage 100 | „Sage 100 Connector/SDK“, teils DB-Lesezugriff (lizenzpflichtig) | kommerziell |
| Sage 50 | Import-/Export-Schnittstellen (Dateiformate), keine offene REST | eingeschränkt |
| Sage X3 | REST-/Middleware-Schicht (versionsspezifisch), Batch-Abläufe | offiziell (Projektgeschäft) |

## Sage Business Cloud (repräsentativ)

**Auth**: OAuth2 (App-Registrierung im Developer Portal), `Authorization: Bearer`.

**Kernendpunkte** (Produktvarianten unterscheiden sich — Endpunktlisten im Portal):

| Methode | Endpoint (Beispiel) | Beschreibung |
|---------|---------------------|--------------|
| `GET` | `/contacts` | Kunden/Lieferanten |
| `GET/POST` | `/sales-invoices` | Ausgangsbelege |
| `GET` | `/accounts` | Kontenplan |
| `POST` | `/webhooks` | Ereignisabos |

**Beispiel:**

```http
GET /sales-invoices?where=total_gt(1000)&pageSize=50 HTTP/1.1
Authorization: Bearer <token>
```

Response (JSON): Belegliste mit `id`, `contact`, `total`, `status` — Feldkatalog je Endpunkt im Portal dokumentiert.

## Sage 100/X3 (Praxis)

- Integration über offizielle **Connector-Lizenzen** oder Export-Routinen (CSV/ASCII, GOBD-/DATEV-Formate)
- X3: REST-Funktionsaufrufe + „Abläufe“ (Batches) über Middlelayer des Projektpartners — Detailverträge projektindividuell

## Rate Limits

Cloud-Portal dokumentiert Limits pro App/Tenant (moderat; 429-Backoff).

## Skin-Hinweis

Sage-Skin = **Adapter-Muster**: ein dünner Konverter pro Sage-Linie auf FreeSynergy-Standardmodelle; niemals „Sage allgemein“ modellieren ([modelle.md](../../../../data/modelle.md) + Produktswitch).
