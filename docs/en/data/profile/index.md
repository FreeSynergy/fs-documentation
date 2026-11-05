# Profile

What one **wants to show about oneself** — the publicly visible, audience-controlled view of the person data.

## Basic model (decisions 1+2)

A profile is **not a second copy of the person data** but a **projection**:

- Data at rest: JSContact `Card` in [contacts/](../contacts/)
- Social identity: AS2 `Actor` (`id` = URI per decision 3, `name`, `preferredUsername`, `publicKey`)
- Visibility: the **audience fields** `to`/`cc`/`bto`/`bcc` decide which fields are released to whom — disclosure control, not access control (decision 2)

## Standards in this domain

| Standard | Evidence | Role in FreeSynergy |
|----------|----------|---------------------|
| **AS2 `Actor` / `Profile`** | ✅ Actor read; `Profile` type ⚠️ section still to evidence | wrapper of the public view |
| **JSContact `Card`** | ✅ | source of the displayed fields |
| **schema.org `Person` / `name`** | `name` ✅, `Person` ⚠️ | export projection for web/SEO |
| **AS2 audience (`to`/`cc`/`bto`/`bcc`)** | ✅ Core read | audience rules per field/field group |

## Open points

- Field-group model ("work", "private", "public") as our own decision? Not yet decided.
- Profile changes (`Update` on the actor) and following (`Follow`) belong in the envelope, not here.

## See also

- [contacts/](../contacts/index.md), [identity/](../identity/index.md)
- [standards.md → activities](../standards.md)
