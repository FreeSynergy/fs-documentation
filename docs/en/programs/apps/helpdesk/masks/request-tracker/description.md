# Request Tracker - Description

## What the program does

RT turns every email into a ticket and organises work through queues, rights and scrips. Its core is uncompromisingly log-oriented: ticket state, participants and history are kept as transactions; automation happens as a Perl script on the transaction.

## Advantages

- **scales extremely**: in operation since 1996 at installations with > 1 million tickets
- **everything scriptable**: email address aliases, scrips, REST/CLI — automation without a plugin zoo
- **auditable**: every change is a transaction with author, time, reason

## Differentiation

| System | Difference |
|--------|------------|
| **Zammad** | The same underlying problem, but a modern UI + Elasticsearch; RT is more "unixy" |
| **osTicket** | Simpler, less automation |
| **GLPI** | Helpdesk + assets; RT focuses on the ticket workflow |

## Technical details

- **Backend**: Perl (the Mason web framework), MySQL/PostgreSQL/Oracle
- **Frontend**: server-generated HTML, RT 5 with a newer MUI framework
- **Authentication**: internal, LDAP, ExternalAuth (Shibboleth/OIDC modules)
- **Hosting**: classic app server (Apache/mod_perl or starman), cron `rt-crontool`
- **Licence**: GPL (community), Best Practical offers GPL-compliant support subscriptions

## Who it suits

- Technology-heavy organisations with their own ops team
- Migration cases in which every email address is meant to be a workflow
- FreeSynergy skins that want to model "ticket as transaction log"
