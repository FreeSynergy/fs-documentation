# Plausible - Description

## What the program does

Plausible answers the four big questions: who came from where, what was read, how successful was the campaign, how often the goal — as one honest page without cookie infrastructure.

## Advantages

- **Compliance-light** (cookieless, EU cloud), minimal maintenance effort
- The stats API = chart skins without an analytics project
- Imports make switching easy

## Differentiation

| System | Difference |
|--------|------------|
| **Matomo** | The full report depth (visitor logs!); Plausible is reduced |
| **GA4** | An attribution machine; Plausible is a facts page |
| **GoatCounter** | Even simpler/open source; Plausible has the feature edge (goals/funnels) |

## Technical details

- **Stack**: Elixir/Phoenix, ClickHouse (self-hosted), edge ingest
- **Authentication**: email/password + API keys (usable identically in cloud/self-hosted)
- **Licence**: AGPL (community), commercial cloud

## Who it suits

- Association/project websites that only want to understand traffic
- FreeSynergy skins: light stats widgets via the stats API
