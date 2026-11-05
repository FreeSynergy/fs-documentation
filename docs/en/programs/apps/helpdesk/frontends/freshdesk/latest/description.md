# Freshdesk - Description

## What the program does

Freshdesk provides support as a subscription: mailboxes become ticket sources, agents work through a task list, rules handle routine. The rest is like Zendesk, but in cheaper tiers and with more tightly integrated Freshworks siblings (Freshchat, Freshcaller, Freddy).

## Advantages

- **cheap entry**, solid free/omni tiers
- **less configuration ballast** than Zendesk — quickly productive
- **API + webhooks** for automation without a forced app

## Differentiation

| System | Difference |
|--------|------------|
| **Zendesk** | A larger ecosystem, deeper customization; Freshdesk is leaner in the standard |
| **Zammad** | Data sovereignty + free code instead of a SaaS subscription |
| **Help Scout** | A mailbox/team-inbox philosophy without a classic ticket mask |

## Technical details

- **Model**: SaaS (multi-region), subdomain `firma.freshdesk.com`
- **Authentication**: email/password, SSO SAML; API key per account/agent; OAuth2 (developer platform)
- **Plans**: free → growth → pro → enterprise; omnichannel bundles
- **Data residency**: EU/US/IN/AU per account selection (check plan dependency)

## Who it suits

- SMEs and growing teams that start without an admin team
- FreeSynergy scenarios that need SaaS ticket APIs (REST v2) as a skin model
