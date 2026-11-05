# Profile – technical explanation

## Projection pipeline (no second data store)

```
JSContact card (contacts/)            AS2 actor (handle, publicKey)
        │                                      │
        └──────────► field-group rules ◄───────┘
                          │
              audience A: public view
              audience B: work context
              audience C: dating context
```

- **Only these are stored:** the handle row (`id` IRI ↔ account from [login/](../login/index.md) ↔ `self_card_id`) and the **rules** (field groups → audience). Field values themselves stay exclusively in the card.
- A projection is **computed on demand**, not stored permanently (otherwise there would be copies with an expiry date — against decision 4).

## Field groups and purpose binding (our own decision — not yet decided, open in [requirements.md §6.3](../requirements.md))

Proposal: every card field reference gets exactly one field group:

| Field group | Examples | Default audience |
|-------------|----------|------------------|
| `public` | `name` (display name), avatar `media` | everyone |
| `work` | `organizations`, `titles`, work email | project/work audience |
| `private` | private email, phone, postal address | contact audience |
| `sensitive` | e.g. parts of `personalInfo` such as sexual orientation | **only** an explicitly chosen audience (e.g. dating context) |

**Rule (dating example):** the work/calendar projection **never** pulls in `sensitive`, not even when the audience is "all colleagues". Legally this touches special categories of personal data (GDPR/BDSG) — ⚠️ the individual legal bases are **not evidenced** in this documentation; the data-model rule stands independently of that.

## Flow

1. Create the handle: actor IRI per decision 3, linked to the account and the card.
2. The person changes the card → the projections change **immediately** (single source).
3. The person changes the **rules** → `Update` on the actor rules (envelope).
4. Externals only see the computed view; `publicKey` belongs in every view (docking point for [identity/](../identity/index.md)).

## Open technical points

- Decide the field-group model as our own decision (open so far)
- `bto`/`bcc`: AS2 treats them as disclosure to named parties — enforcement per resource stays separate (decision 2)
- Multilingual profiles (`nameMap`) — mechanism ✅, which fields are translatable is open
