# Profile – description

**What this domain is:** what one **wants to show about oneself** — the publicly visible, **audience-controlled** view. Per decisions 1+2 a profile is **not a second copy of the person data** but a **projection** of the JSContact card ([people/](../people/index.md)) into an AS2 `Actor`/`Profile` frame.

**What it covers:**

- the social handle: `id` (absolute IRI, decision 3), `name` (display name), `preferredUsername`, `publicKey`
- **audience rules**: which field/field group goes to which audience (`to`/`cc`/`bto`/`bcc` as disclosure control — not access control, decision 2)
- **purpose binding of sensitive fields**: the dating example from the conversation — in a dating context it can become **dangerous** if sexuality shows up in the work/calendar context. Sensitive fields do **not** automatically belong in every projection
- consequences of profile changes: `Update` on the actor, `Follow` — both are envelope operations

**Differentiation:**

| Topic | Where it lives |
|-------|----------------|
| The data at rest from which the profile is projected | [people/](../people/index.md) |
| The login that belongs to the account | [login/](../login/index.md) |
| Attestations about whether one may trust the handle | [identity/](../identity/index.md) |
| Follower relations, ActivityPub delivery mechanics | envelope (cross-cutting, not a domain) |

**Why this is a domain of its own:** the only real question of this domain is **visibility** ("which field, for whom, for what purpose"). These rules belong in a central definition so that not every app filters on its own.
