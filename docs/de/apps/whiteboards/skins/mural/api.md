# Mural - API Dokumentation

## Übersicht

Mural hat **keine breit geöffnete öffentliche Content-API**: Export/Import erfolgt über PNG/PDF und Workspace-Verwaltung, Automatisierung primär über Zapier/Apps. Für Skins gilt: Mural ist Referenz für UI-Muster, nicht für API-Mapping.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST (api.mural.co) | Workspace-/Nutzerverwaltung (SSO-Betrieb), einzelne Endpunkte | eingeschränkt/teilöffentlich |
| SCIM/SAML | Provisioning/SSO | offiziell (Enterprise) |
| Content-CRUD (Notizen/Shapes) | — | ❌ nicht öffentlich |
| Webhooks | — | ❌ nicht dokumentiert |

## Authentifizierung

- Betriebs-Endpunkte: API-Token je Workspace (Admin) bzw. OAuth-App für Partnerintegrationen; Detailreferenz im Mural-Kundensupport (nicht öffentlich vollständig publiziert — bewusst nicht erfunden)

## Austauschwege (praktisch)

1. Mural exportieren (PNG/PDF) → Weiterverarbeitung
2. Aktivitäten-Log (CSV, Enterprise) → Analyse
3. Zapier-Connector (Create mural, Membership) → Automatisierungs-Skins

## Rate Limits

Nicht öffentlich dokumentiert.

## Skin-Hinweis

Für API-getriebene Whiteboard-Skins better **Miro** oder **tldraw** als Pate nehmen; Mural liefert die Moderations-/Sequence-Muster ([components/Abläufe](../../components/)).
