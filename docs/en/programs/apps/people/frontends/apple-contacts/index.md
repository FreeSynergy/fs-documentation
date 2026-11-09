# Apple Contacts

> Category: [people](../../index.md) · Type: contact manager (iPhone, iPad, Mac, Apple Watch) · Vendor: Apple · Licence: proprietary

## What it is

Apple Contacts is the address book built into Apple's operating systems. It syncs contacts between devices and with added accounts, offers a "Me" card for your own details, and shares contact information between nearby devices.

## Notable ideas

Why this program is documented here (ADR 0013):

- **NameDrop**: two devices held close together exchange contact details. The person chooses which details go out; by Apple's description only the name, one chosen phone number or e-mail address and the contact poster are sent, not home address or birthday. It sends new contact data and does not update an existing contact. Relevant for us as an example of exchanging contacts in person without typing and with a deliberate choice of fields.
- **Own card ("Me")**: sharing is built around one card the person controls and edits.
- **Merge or hide duplicates** is part of the same app.

## Documented versions

| Version | Documented on | Status |
|---------|---------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ from help pages and an Apple safety guide; no device inspected. iOS 17 introduced NameDrop; guide versions 17, 18, 26, 27 exist |

## Protocols and standards used

Contact data standards: [data/people](../../../../data/people/index.md). NameDrop is part of AirDrop (Apple-internal, no open standard known; Open).

## Sources

| Source | Kind | Retrieved |
|--------|------|-----------|
| https://support.apple.com/guide/personal-safety/ips97e16d3b1/web ✅ | Apple guide (what NameDrop shares, how to cancel) | 2026-11-10 |
| https://support.apple.com/guide/iphone/add-and-use-contact-information-iph3d3da1b3c/ios ✅ | Apple iPhone User Guide, Contacts section (topic list only) | 2026-11-10 |
| https://support.apple.com/guide/iphone/namedrop-iphone-share-contact-info-iph1b6c664b7/ios ⚠️ | NameDrop article; body could not be read, title only | 2026-11-10 |
| https://support.apple.com/en-ca/guide/watch/apd46c6e11cf ⚠️ | Apple Watch guide, seen via search result only | 2026-11-10 |
