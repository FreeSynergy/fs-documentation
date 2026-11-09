# Contact — Requirements

What `FreeSynergy.Contact` must and can do, derived from the [frontends](frontends/index.md)
(ADR 0006, 0013). Each capability names its data standard (ADR 0014) and our status.

Status: `implemented` · `planned` · `proposed`

## Required (common to the analysed programs)

| Capability | Seen in | Data / standard | Status |
|------------|---------|-----------------|--------|

## Optional (notable ideas)

| Capability | Seen in | Data / standard | Status |
|------------|---------|-----------------|--------|
| Suggest duplicates of one person and merge them one by one or all at once; merging can be undone (`contact.mergeSuggest`, `contact.merge`) | Google Contacts (Merge & fix); Apple Contacts (merge or hide duplicates) | JSContact RFC 9553 (merge result is a new card version); history via AS2 `Update` | proposed |
| Exchange own contact details in person, with a choice of which fields go out; receive-only possible; never overwrites an existing contact silently (`contact.shareNearby`) | Apple Contacts (NameDrop) | JSContact subset of the own card; transport open (ADR 0059 local transport) ⚠️ | proposed |
| Keep addresses of people only written to apart from the address book until promoted (`contact.promote`) | Google Contacts (Other contacts) | JSContact `kind`, vendor property `freesynergy.net:known` ⚠️ | proposed |
| Change history of a contact, with undo (`contact.history`) | Google Contacts (History) | AS2 `Update` log; history data area not yet defined ⚠️ | proposed |
| Remind to get back in touch; show when a person was last spoken to (`contact.keepInTouch`) | Monica (reminders, "last spoke") | JSCalendar `Task` / alert; last contact derived from the message and event log | proposed |
| Record life events and milestones of a person (`contact.lifeEvent`) | Monica | JSCalendar `Event` linked by `relatedTo` ⚠️ | proposed |

## Not planned (deliberately)
