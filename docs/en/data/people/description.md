# Contacts – description

**What this domain is:** contact records for **people, organisations, groups and devices** — with reachability (email, phone, messenger, postal address) and name information. Canonical model: **JSContact** (RFC 9553, ✅).

**What it covers:**

- Creating, changing, patching and merging (`merge`) cards (`Card`)
- Names with components (not `firstName`/`lastName` — see [jscontact/description.md](jscontact/description.md))
- Organisations and the roles of a person (`organizations`, `titles`)
- Reachability: `emails`, `phones`, `onlineServices`, `impp`, scheduling addresses
- Postal addresses as part of the card (geometries and maps live in [geodata/](../geodata/index.md))
- Import/export via vCard/jCard, access/sync via CardDAV

**Differentiation from other domains:**

| Domain | What lives there | Why not here |
|--------|------------------|--------------|
| [login/](../login/index.md) | Account, sign-in, `sub` claim | A login is an access route, not a data model |
| [profile/](../profile/index.md) | What one **shows about oneself** (audience control) | The profile is a **projection** of the card, not a second copy |
| [identity/](../identity/index.md) | Whom one **trusts** (attestations, keys) | Mistrust cannot delete a card |
| [events/](../events/index.md) | Participants **at appointments** | The person is linked here (`sendTo`/`email`), not stored |
| [geodata/](../geodata/index.md) | Places as map features | The postal address **of a person** belongs to the card |

**Person vs. contact (decision candidate 6, open):** the "human who signs in" needs **no `person/` directory of its own** according to our proposal: the person is that JSContact `Card` (role `individual`) which is linked to the account from [login/](../login/index.md). So all person data stays in this domain. See [requirements.md → 6.4](../requirements.md).

**Lifecycle gap:** `lifecycle` (lead/prospect/customer/churned) exists in no standard (❌ evidenced) → planned as a JSContact `extensions` entry (⚠️ mechanism still to be evidenced). See [standards.md](standards.md).
