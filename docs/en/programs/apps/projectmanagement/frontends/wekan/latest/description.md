# Wekan - Description

## What the program does

Wekan brings the Trello principle onto your own server: boards with cards, plus swimlanes
as an extra hierarchy level and webhooks in both directions. It is deliberately functional
rather than stylish — in exchange you get complete control of your data.

## Advantages

- **genuine self-hosted kanban** (MIT licence, Docker in minutes)
- **swimlanes** for organisational levels Trello does not offer
- **invoke hooks** = e-mail/alert pipeline without an extra tool

## Differentiation

| System | Difference |
|--------|------------|
| **Trello** | SaaS comfort/power-ups; Wekan has data sovereignty |
| **Planka** | leaner, modern React UI; Wekan is richer in fields (swimlanes/custom fields) |
| **Focalboard (discontinued)** | desktop-heavy; Wekan stays an active web service |

## Technical details

- **Stack**: Node/Meteor + MongoDB, React client (DDP real time)
- **Authentication**: password, LDAP, OAuth2 (Casdoor/Keycloak), SAML; API: personal token
- **Deploy**: Docker/Snap/K8s; S3 backend for attachments
- **Licence**: MIT

## Who it suits

- devops/self-hosting environments with a kanban need and alert pipelines
- FreeSynergy frontends: board/list/card + swimlane as an extended kanban model
