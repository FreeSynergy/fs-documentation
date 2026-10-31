# Decidim - API Dokumentation

## Übersicht

Decidim setzt auf **GraphQL** (`/graphql`, öffentlich mit Introspektion; schreibende Mutationen nur mit Session/Token). Ein Webhook-Modul liefert Ereignisse nach außen. Frühere REST-Pläne existieren nicht mehr als Standard.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| GraphQL `/graphql` | Queries (Prozesse, Vorschläge, Kommentare, Meetings) + Mutationen (Session) | offiziell (Kern-API) |
| Webhooks-Modul (`decidim-webhooks`) | Vorschlag erstellt/kommentiert… → POST | offiziell (Modul) |
| REST | — | ❌ (nicht Kern) |
| Action-Text-Exporte | JSON/CSV-Auswertungen Admin | offiziell |

## Authentifizierung

- Lesen: keine (öffentliche Inhalte; private Prozesse ausgenommen)
- Mutationen: Sessions/Cookies; API-Tokens je Version (Doku prüfen)

## GraphQL-Beispiele

Query (Vorschläge eines Prozesses):

```graphql
query {
  component(id: 42, type: "Decidim::Proposals::ProposalComponent") {
    ... on Decidim::Proposals::ProposalConnection {
      nodes { title body supportsCount createdAt }
    }
  }
}
```

Webhook-Payload (Modul):

```json
{ "event": "proposal_created", "resource": {
    "id": 1234, "title": "Mehr Radwege", "component_id": 42 } }
```

## Kern-Typen (Auswahl)

| Typ | Beschreibung |
|-----|--------------|
| `ParticipatorySpace`/`Process` | Beteiligungsbehälter |
| `Component` (Proposals, Budgets, Meetings…) | Modulinstanz |
| `Proposal`, `Comment`, `Meeting` | Kernobjekte |
| `User` (nur öffentliche Felder) | Teilnehmende |

## Rate Limits

nicht eingebaut (Instanz-/Proxy-Limits).

## Skin-Hinweis

GraphQL = perfekter Feed für Beteiligungs-Dashboards (Read-Only-Skin); Webhook→n8n-Kette für Benachrichtigungs-Skins ([modelle.md](../../../../data/modelle.md): Antrag→Support→Phase).
