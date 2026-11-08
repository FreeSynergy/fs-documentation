# Tasks — Requirements

What `FreeSynergy.Tasks` ([`fs-tasks`](https://github.com/FreeSynergy/fs-tasks), [design](design.md)) must and can do,
derived from the analysed [project-management frontends](../../suites/projectmanagement/frontends/index.md) (ADR 0006, 0013).
Each capability names its data standard (ADR 0014) and our status. The analysis was made when this was planned as
`fs-kanban`. That plan is replaced (ADR 0049): the kanban board is a **view of `fs-tasks`**, not a program. The tables
below are the board view. Function analysis only, own wording, nothing copied.

**Owners (ADR 0050).** `fs-tasks` owns the JSCalendar `Task` and the board model. Everything else is reached through the
owner's interface and not repeated here: events and calendar views by `fs-calendar`, files by `fs-files`, people by
`fs-people`, groups, members and rights by [`fs-groups`](../../platform/groups.md), history by
[`fs-history`](../history/index.md), places by `fs-maps`, messages by `fs-messenger`, sign-in by the
[identity wrapper](../../platform/identity.md).

**Ids.** The contract (`tasks.capnp`) names the item capabilities `task.create`, `task.edit`, `task.assign`,
`relation.create`, `label.assign` (provisional, see the repo's `DESIGN.md`). The `card.*` ids below are the board-view
names of the same actions. Both kept for now; the owner is to settle them.

Status: `implemented` · `planned` · `proposed`. **"core"** = built in `fs-tasks-core` (latest tag v0.0.2, no GUI, interface
still a draft). Boards, columns and `task_link` are not started: the `Boards` interface is a placeholder without methods.

**Seen in** — analysed frontends: [Tr](../../suites/projectmanagement/frontends/trello/index.md) Trello ·
[We](../../suites/projectmanagement/frontends/wekan/index.md) Wekan ·
[Pl](../../suites/projectmanagement/frontends/planka/index.md) Planka ·
[Ta](../../suites/projectmanagement/frontends/taiga/index.md) Taiga ·
[Ji](../../suites/projectmanagement/frontends/jira/index.md) Jira ·
[As](../../suites/projectmanagement/frontends/asana/index.md) Asana ·
[Op](../../suites/projectmanagement/frontends/openproject/index.md) OpenProject ·
[Re](../../suites/projectmanagement/frontends/redmine/index.md) Redmine.
*arch.* = required by our architecture or principles, not by counting.
⚠️ = unreliable or unclear in the feature file, to be verified.
Only board-related capabilities are counted. Issues and work packages of the tracker-style
frontends (Ji, Op, Re) count as "card" where the capability is about the task itself; board
capabilities (columns, move) are counted only where a board exists. Redmine has **no board in
its core** (kanban only by plugin), so it appears only in card-level rows.

**Rule:** a capability is *Required* when at least four of the eight frontends show it, or when
our architecture needs it. The capability id in backticks (`<object>.<action>`) is a proposal —
a capability is an action on the object, never a menu item or a gesture (ADR 0037).

**Core facts:** a card **is** a JSCalendar 2.0 `Task`, owned by `fs-tasks`. `fs-calendar` shows it through the
`fs-tasks` interface and has no copy or Task model. Board structure has no standard: own spec candidate no. 3 (`Project`, `Board`, `List`,
`Relation`; owned by `fs-tasks`; a `task_link` assigns a task to exactly one list). A *column* here is the `List`
model. Moving a card is an AS2 activity.

Data references: [projects index](../../../data/projects/index.md) ·
[projects standards](../../../data/projects/standards.md) ·
[projects technical](../../../data/projects/technical.md) ·
[events (Task)](../../../data/events/index.md).

## Required (common to the analysed programs)

| Capability | Seen in | Data / standard | Status |
|------------|---------|-----------------|--------|
| Create, edit and open a board (`board.create`, `board.edit`, `board.open`) | Tr, We, Pl, Ta, Ji, As, Op | own `Board` model (no standard, spec candidate no. 3); belongs to a `Project` | proposed |
| Add, rename and reorder columns (`column.create`, `column.rename`, `column.move`) | Tr, We, Pl, As (sections), Op; Ta, Ji (columns = statuses) | own `List` model; `position` = sortable in-between value (own decision, open) | proposed |
| Create a card (`card.create`) | Tr, We, Pl, Ta, Ji, As, Op, Re | JSCalendar `Task` in `calobj`; `task_link` puts it in one column | implemented (core, as `task.create`; `task_link` not started) |
| Edit title and description of a card (`card.edit`) | Tr, We, Pl, Ta, Ji, As, Op, Re | JSCalendar `title`, `description` | implemented (core, as `task.edit`) |
| Move a card to another column or position (`card.move`) | Tr, We, Pl, Ta, Ji, As, Op | `Update` on `task_link`, not on the task (technical.md); AS2 `Move` (origin/target) is a candidate ⚠️ open; envelope event `task.moved` | proposed |
| Set the status of a card (`card.setStatus`) ⚠️ column vs. status is not settled: in Ta, Ji columns are statuses, in Tr, Pl free lists | Ta, Ji, Op, Re | JSCalendar `progress`; RFC 10051 `PENDING`/`FAILED`, `VSTATUS` (vendor property until JSCalendar has it) | proposed |
| Assign people to a card (`card.assign`) | Pl, As, Op, Re | JSCalendar `participants` (role); the person comes from the `fs-people` interface | implemented (core, as `task.assign`) |
| Set a due date (`card.setDue`) | Tr, We, Pl, As, Op, Re | JSCalendar `due` | implemented (core; queries by due range too) |
| Show cards with a due date in the calendar, without copying (`card.setDue` effect) | Tr, Pl, As, Op, Re (calendar views); We (iCal feed); *arch.* | same `Task`; `fs-calendar` reads it through the `fs-tasks` interface (ADR 0050) | proposed |
| Label cards with name and colour (`label.assign`) | Tr, We, Pl, As (tags) | JSCalendar `keywords` on the task; label name and colour defined on the board: gap → own | partly: keyword implemented (core, as `label.assign`); board colours not started |
| Break a card into small steps with progress (`subtask.add`) — checklists (Tr, We, Pl) and subtasks (Ta, Ji, As) are counted together; Tr says cards cannot contain cards | Tr, We, Pl, Ta, Ji, As | `Relation` `kind: parent` (proposal: no `parent_id` on the Task); progress from the children | partly: relation implemented (core); progress from children not started |
| Link cards: depends on, blocks, relates to (`relation.create`) | Ji, As, Op, Re | RFC 9253 `DEPENDS-ON`, `FINISHTOSTART` etc.; "blocks" is a **gap** (`relatedTo` only first/next/child/parent) → own `Relation` `kind` enum | partly: RFC 9253 relations implemented (core, `relation.create`); "blocks" not |
| Attach files to a card (`attachment.add`) | Tr, We, Pl, Ta, Op, Re | JSCalendar `links`; the file itself is kept by `fs-files` and reached through its interface | proposed |
| Comment on a card (`comment.add`) | Tr, We, Pl, Op, Re | AS2 `Note` with `inReplyTo` the card | proposed |
| Watch a card or board and get changes (`card.watch`) | Tr, Pl, Op, Re | subscription list: gap → own | proposed |
| Notify about changes to watched or assigned cards (`card.notify`) | Tr, We, Pl, Ta, As, Op, Re | AS2 activity as source; delivery channel is a platform matter ⚠️ not defined in data/projects | proposed |
| Show the history of a card and a board (`card.history`) | Tr, We, Pl, Ta, Op, Re | AS2 activities of the card, read through the `fs-history` interface (it owns history); shown as a timeline view | proposed |
| Define and fill custom fields (`field.define`, `card.setField`) | We, Pl, Ji, As, Op, Re (Tr via Power-Up) | JSCalendar vendor properties `freesynergy.net:<name>`; definition lives on the board | proposed |
| Start a board from a template (`template.apply`) | Tr, We, Pl (pro), As | own `Board` copy; JSON of the board structure | proposed |
| Invite members to a board and give them a role — owner, contributor, observer (`member.add`, `member.role`) | Tr, We, Pl, Ta, Op, Re | membership and rights belong to `fs-groups` (ADR 0055), reached through its interface; board roles are only names for what it grants; login stays platform identity | proposed |
| Send board events to outside systems (`webhook.create`) | Tr, We, Pl, Ta, Ji, As, Op; Re (plugin only) | AS2 activity as payload (envelope topic, index.md) | proposed |
| Export a board (`board.export`) | We (JSON), Pl (PDF/HTML), As, Op, Re (CSV) | own board JSON + JSCalendar `Task`; CSV/PDF derived | proposed |
| Changes appear live for everyone and work offline (`board.sync`) | We, Pl (real-time); *arch.* (ADR 0019); Ji, Pl, Op have no offline mode | `fs-store` + `fs-hub`, object-level sync; live view of others as in the roadmap | partly: `subscribe` (`TaskFeed`) implemented (core); the rest proposed |
| Script and automate through our own contract, no separate API (`Capabilities` contract) | Tr, We, Pl, Ta, Ji, As, Op, Re (REST); *arch.* ADR 0021 | Cap'n Proto → JSON / CLI / MCP | partly: draft contract `tasks.capnp` and Rust traits done; the capnp-rpc server is not written |

## Optional (notable ideas)

| Capability | Seen in | Data / standard | Status |
|------------|---------|-----------------|--------|
| Swimlanes: a second axis across columns (`swimlane.create`) | We, Ta | gap → own addition to `Board` | proposed |
| WIP limit per column (`column.limit`) | Ji, Op | gap → own `List` property | proposed |
| Epics: group cards under a larger card (`epic.create`) | Ta, Ji, Op | `Relation` `kind: parent` | proposed |
| Mark a card as duplicate (`relation.create` with duplicates) | Re | "duplicates" is a **gap** → own `Relation` `kind` | proposed |
| Card types (bug, task …) with own fields (`card.type`) | Ji, Op, Re | JSCalendar `categories`; fields per type: gap | proposed |
| Allowed status transitions per role (`workflow.define`) | Ji, Re; Op (admin workflows) | gap → own rule model | proposed |
| Priority of a card (`card.priority`) | Op, Re | JSCalendar `priority` | proposed |
| Reminder before the due date (`card.remind`) | Tr | JSCalendar `alerts` | proposed |
| Recurring cards (`card.repeat`) | Pl (pro) | JSCalendar `recurrenceRules` | proposed |
| Mention a person in a comment (`comment.mention`) | Tr | AS2 `tag` of type `Mention` | proposed |
| Card location, shown on a map (`card.locate`) | Tr (map view, premium) | JSCalendar `locations`; place and map owned by `fs-maps` | proposed |
| Copy a card, also into another board (`card.copy`) ⚠️ Pl "one card in several boards" conflicts with `task_link` (exactly one list) | Pl, Op, Re | new `Task` + `task_link`; shared card: model change needed | proposed |
| Share a card by link (`card.share`) | Op, Re | URL `/projects/<uuid>` (decision 3); access check open | proposed |
| Card templates (`template.apply` on a card) | Tr, Pl (pro) | JSON of a `Task` | proposed |
| Archive instead of delete (`card.archive`, `board.archive`) | Pl | own flag; JSCalendar `status` is not meant for it ⚠️ | proposed |
| Board background and card colour (`board.style`) | Pl, Tr | JSCalendar `color` for the card; board background: own | proposed |
| Filter and search cards, save a filter (`card.search`, `query.save`) | Op, Re, Ji (JQL), As | stored query over `calobj` fields; no query language planned | proposed |
| Table view of the cards (`board.open` as table) | Tr, As, Op | view parameter of `board.open` | proposed |
| "My cards" across all boards (`card.list` filtered) | As, Pl (dashboard), Re (my page) | stored query | proposed |
| Rules: when a card moves, then set/notify (`rule.create`) | Tr (Butler), Ji, As; We has none | trigger = AS2 activity; rule model: gap | proposed |
| Create a card by incoming webhook (`card.create` over contract) | We | same contract as the rest (ADR 0021) | proposed |
| Create a card from e-mail (`card.create` from `message`) | Op (mail intake) | the message is borrowed through the `fs-messenger` interface (live reference) ⚠️ | proposed |
| Intake form that creates cards (`form.submit`) | As | gap | proposed |
| Link commits to a card (`card.linkCommit`) | Ta, Ji, Re | JSCalendar `links`; forge side not evaluated | proposed |
| Import a board from other tools (`board.import`) | We (Trello, CSV), Ta (Jira, Asana, Trello, GitHub), Pl (version-dependent) | mapping to be written ⚠️ | proposed |

## Not planned (deliberately)

| Feature | Seen in | Why not |
|---------|---------|---------|
| Gantt and timeline inside the board view | Tr, Pl, As, Ta, Ji, Op, Re | a separate view of `fs-tasks` and `fs-calendar` (workbench `timeline-gantt`, [design](design.md#views)), not the board |
| Baselines, critical path | Tr, Pl, As, Ta, Ji, Op, Re | capacity and baselines belong to [`fs-resources`](../resources/index.md) ([design](design.md)); critical path: open |
| Time tracking, stopwatch, estimates | Tr (Power-Up), Pl, Op, Re | open: `fs-tasks` or `fs-history` ([design](design.md#open-questions)); proposed as history |
| Budgets, costs, cost rates | Op | not in `fs-tasks`; the project management suite may add costs (ADR 0049, to be checked) |
| Portfolios, workloads, goals, roadmaps of several projects | As, Op, Ji | the project management suite; workloads: `fs-resources` |
| Milestones, versions, roadmap | Ta, Op, Re, Ji | project level, the project management suite; a milestone is an `Event`, owned by `fs-calendar` |
| Scrum: backlog, sprints, points, velocity, burndown | Ta, Ji, Op | not board-only; may follow in the project management suite (open) |
| Reports and charts (cycle time, throughput) | Tr, Ta, Ji, Op, Re | the [charts component](../../../components/charts.md) in the project management suite |
| Own calendar view or iCal feed in `fs-tasks` | Tr, Pl, As, Re, Op; We, Op, Re (iCal) | `fs-calendar` shows the same `Task` through the `fs-tasks` interface (ADR 0050) |
| Subprojects, project hierarchy | Re, Op | `Project` level, the project management suite |
| Wiki, forums, news, meetings, documents | Ta, Op, Re | separate programs (`fs-wiki`, `fs-messenger`, `fs-files`) |
| Repository browsers | Re | not a board function |
| Chat/push integrations built in (Slack, Telegram, 100+ services) | Ta, As, Pl | notifications go through the platform and messenger |
| Cloud AI summaries | As, Ji | local model only (ADR 0029) |
| Paid tiers that unlock views, guests, SSO | Tr, Pl, Ji, Op | free forever (ADR 0016) |
| Own login, 2FA, LDAP/SAML | Pl, Re, We | the [identity wrapper](../../platform/identity.md) over Kanidm, not the program |
| App marketplaces and plugin systems | Tr, Ji, As, Re | other programs share standard data; automation via the contract (ADR 0017, 0021) |

## Notes on the sources

- ⚠️ Planka mixes community and pro features without a clear line (templates, guests, views, recurring cards are pro); the file says versions differ. Rows citing Pl for such features are marked.
- ⚠️ Wording in some files is garbled (Jira "No native Gantt cannon", Planka "No darkroom for anonymous opening", Wekan "trough levels" = swimlanes); read as meant, to be verified.
- ⚠️ Taiga, Jira, Asana files do not name card-level detail (assignees, comments); absent there does not mean absent in the product.
