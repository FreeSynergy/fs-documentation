# Salesforce - Description

## What the program does

Salesforce operates CRM as a multi-layer platform: a multi-tenant object data core, sales/service processes (flows), analytics and portals on top, and an API landscape with which almost everything can be externalized. Customers rent tenants (editions) and extend them via configuration or Apex.

## Advantages

- **Platform rather than tool**: custom objects/apps without changing provider
- **Ecosystem**: AppExchange, certifications, admin/developer community
- **API maturity** — reference class for integrations

## Differentiation

| System | Difference |
|--------|-------------|
| **HubSpot** | marketing/content-centric, easier entry; Salesforce is process- and enterprise-heavy |
| **EspoCRM/SuiteCRM** | own infrastructure, GPL; Salesforce is SaaS with quotas |
| **Odoo CRM** | CRM as part of an ERP kit; Salesforce without its own inventory management |

## Technical details

- **Model**: multi-tenant SaaS, instances ("orgs") by region; sandbox environments
- **Modeling**: Object Manager, page layouts, record types; Metadata API for deployment (SFDX/sf CLI)
- **Programming**: Apex (Java-like, separate transaction boundaries), Lightning Web Components
- **Authentication**: user + password/SSO (SAML/OIDC); API: OAuth2 (JWT Bearer, web server flows)
- **Pricing**: license models per cloud/edition; API and storage quotas

## Suitable for

- Companies with admin resources and integration needs
- FreeSynergy skins: the Salesforce data model (Account/Contact/Opportunity) is the de facto vocabulary for [CRM mapping](../../../../../../data/models.md)
