# Project management landscape: purposes, modules, gaps

Research note, 2026-11-06. Function analysis in own wording; nothing is copied (ADR 0013).
Builds on, and does not repeat: `docs/en/programs/apps/projectmanagement/` (8 tools analysed:
Trello, Wekan, Planka, Taiga, Jira, Asana, OpenProject, Redmine), `docs/en/programs/apps/kanban/requirements.md`
(board-only requirements) and `docs/en/data/projects/standards.md` (standards search of 2026-11-02/05).

Evidence key:
- **[S#]** = fetched on 2026-11-06, see source list at the end.
- **[repo]** = already in our own docs.
- **⚠️** = not verified in this session (general knowledge, vendor claim, or only a search snippet). Treat as a lead, not a fact.

Scope limit: the web search tool was rate-limited partway through. Closed tools (Jira, Asana, Monday, ClickUp, Linear,
Notion, Basecamp, Smartsheet, Wrike) were **not** re-fetched; their entries are ⚠️ unless they come from [repo].

---

## 0. Verified state of the tools the owner knows

| Tool | Finding | Evidence |
|------|---------|----------|
| **Tenzu** | Not a fork of today's Taiga (Taiga 6). It is the continuation of "Taiga Next" (Kaleidos' rewrite). In mid-2024 Kaleidos handed Taiga Next to the worker cooperative BIRU (France); renamed Tenzu on 2024-09-05. Code base was taken over and modernised (Django 5 + Django Ninja, Angular 18 + Angular Material). So: **successor/relative of Taiga, rewritten, not a fork of the Taiga 6 repo.** | [S1] [S2] |
| Tenzu: active? | **Yes.** Changelog: v2.0.0 2026-01-30, v2.1.0 2026-02-13, v3.0.0 2026-06-04, v3.1.0 2026-07-13, v3.2.0 2026-10-19. Backend repo last updated 2026-10-29 (613 commits, 90 stars). | [S3] [S4] |
| Tenzu: scope today | **Kanban only** with workspaces, projects, custom statuses, swimlanes (import), live collaborative editing of stories, tags, Taiga import. "Scrum and issue tracking coming in 2026" (README). No Gantt, no time/cost. Not yet accepting code contributions. AGPL-3.0, stated "never open core". | [S4] [S5] |
| Tenzu: stated direction | Few metrics, decision-oriented "project health" with remediation hints; usable by teams without PM know-how; accessibility. This is a *purpose* idea worth noting (see 4.6). | [S1] |
| Taiga (6) | Continues under "TaigaCloud Services" (SaaS/private cloud). ⚠️ current release cadence not checked. | [S1] |
| **Leantime** | AGPL-3.0 core plus **open core**: program management, strategy boards, custom fields are paid marketplace plugins (per a third-party review). Core: kanban, Gantt, calendar, goals/OKR, Lean Canvas, timesheets, wiki; built with ADHD/autism/dyslexia in mind. v3.13.2 released 2026-10-31. US company (Leantime, Inc.). | [S6] (third-party; ⚠️ gating list to confirm on leantime.io) |
| **OpenProject** | Community (GPL) + Enterprise add-ons. Verified gated: **Resource management** (Premium/Corporate plans); full **baseline** comparison (any date range; Community only gets "compare to yesterday"). Community has: Gantt, scheduling, boards, Scrum, meetings, time tracking, **costs, budgeting**, wiki, documents, reports (listed in plan comparison; the Community column of that table was garbled in the fetch, so the Community-vs-paid split of costs/budgets is ⚠️). Prices €5.95 / €10.95 / €15.95 per user per month, minimum 25/25/100 users. | [S7] [S8] [S9] |
| **Plane** | Community Edition AGPL-3.0, "at par with the Free tier"; paid plans need the **separate, closed-source Commercial Edition** with a distinct code base and release cycle. | [S10] |
| **Huly** | EPL-2.0, all-in-one (issues, chat, docs, CRM, HR, recruiting); repo 28k stars, updated within hours of retrieval. | [S11] |
| **Vikunja** | Go, repo active (updated 2026-11-06, ~6k stars, 250 open issues). ⚠️ licence (believed AGPL-3.0) and views not re-verified. | [S12] |
| **Kanboard** | MIT, PHP, **maintenance mode** (fixes only, feature set frozen). | [S13] |
| **Focalboard** | Handed by Mattermost to the community Aug 2024; no release since June 2024 and no active maintainer (as of July 2026). **Treat as dead.** | [S14] |
| **Loomio** | Decision tool for groups; repo active (updated 2026-11-06), Ruby. ⚠️ licence believed AGPL, not verified from upstream. | [S15] |
| **MS Project Online** | Retired 2026-09-30 (announced 2025-09-05). Desktop Project unaffected. Microsoft points to Planner/Project Server SE. | [S16] |
| **Height** | Shut down September 2025 (per a competitor blog; no primary statement found). ⚠️ | [S17] |
| Wekan, Planka, Redmine, Taiga, Trello, Jira, Asana | See [repo] frontend analyses. Planka: free Community + paid Pro (mixing, see requirements.md notes). | [repo] |

Not checked at all: GitLab/Forgejo issues, AppFlowy, Notion, ClickUp, Linear, Basecamp, Smartsheet, Wrike, Monday (⚠️ everything below about them is general knowledge).

---

## 1. By purpose

"Purpose" = the question the person is trying to answer. Strength: ● serves it well, ◐ partly, ○ barely.

| # | Purpose (the question) | Serves it well | Weak spots | Suggested FreeSynergy program |
|---|------------------------|----------------|-----------|-------------------------------|
| 1 | **What do I do next?** (one ordered, trustworthy list) | ● Vikunja (⚠️), Todoist-style tools (⚠️, not in scope), Asana "My tasks" [repo], Linear (⚠️), Plane cycles ⚠️; ◐ Leantime (built for focus) [S6] | Boards show *state*, not *order of attention*. Almost every tool needs the user to build their own filters (OpenProject saved queries [repo]). | `fs-tasks` ("my list" view across all projects; same `Task`, JSCalendar) |
| 2 | **Are we on track?** (plan versus reality) | ● OpenProject Gantt + baseline (full baseline gated) [S8]; MS Project ⚠️; Smartsheet ⚠️; ◐ Taiga (timeline is only a presentation, no critical path) [repo]; ○ Tenzu, Planka, Wekan | Most "burndown" and "velocity" charts answer *Scrum* progress, not *deadline risk*. Tenzu's stated aim (health + remediation) is not delivered yet [S1][S4]. | `fs-tasks` timeline view + a "schedule" module (dependencies RFC 9253) |
| 3 | **Who does what?** (split work among people) | ● Jira, Asana, OpenProject, Redmine (assignees, roles, groups) [repo]; Planka/Wekan boards | Assignment is one person per task or a flat list. Little for "claim", "offer", "needs two people", or shared roles. | `fs-tasks` + `fs-groups` |
| 4 | **Do we have the people/time?** (capacity) | ● OpenProject Resource management, but **paid** (Premium+) [S9]; Asana Workload ⚠️ paid; ClickUp/Monday workload ⚠️; MS Project resource pool ⚠️ | In open source: effectively only OpenProject Enterprise; Taiga explicitly has none [repo]. | `fs-resources` |
| 5 | **Where does the money go?** (budget, cost, billing) | ◐ OpenProject costs + budgets [S8]; ◐ Redmine time logging [repo], budget via plugins ⚠️; Leantime timesheets [S6]; Toggl (time only) ⚠️ | Tools mix three things: *time logged*, *money planned*, *money paid*. No open tool treats them as separate ledgers (section 5). | costs module of `fs-resources` (separate ledger crate, see section 5) |
| 6 | **What happened / why did we decide this?** (memory) | ◐ Redmine journals, OpenProject activity, Jira history [repo]; wikis (Taiga, Redmine, OpenProject) | History is per ticket, locked in the tool, mostly not exportable. No "what did *I* do last week" across tools. Decision *reasons* live in comments. | `fs-history` (AS2 activity log shown as timeline) + `fs-wiki` |
| 7 | **Report upwards** (status for people who do not use the tool) | ● Asana/Monday/Smartsheet dashboards ⚠️; OpenProject reports + project status [S8]; Jira dashboards [repo] | Reports are charts of counts. Little narrative; little "export for people without account". Tenzu wants decision-oriented health [S1]. | `fs-reports` view over `fs-tasks`/`fs-history`, output via `fs-documents` |
| 8 | **My own goals** (personal, long-horizon, not a team project) | ◐ Leantime goals/OKR/canvas [S6]; Notion/Obsidian-style (⚠️); Vikunja for lists | Personal and team tools are separate worlds. Moving a personal goal into a shared project means copy-paste. | `fs-tasks` personal scope + `fs-goals` (view) |
| 9 | **Decide together** (choose, vote, consent) | ● Loomio (dedicated, not PM) [S15]; Decidim/CONSUL-style (⚠️, civic) | No PM tool has a decision as a first-class object linked to tasks. See 4.4. | surveys program + decision objects in `fs-groups` |
| 10 | **Think visually** (brainstorm, map) | Miro/Mural ⚠️; Huly/AppFlowy docs ⚠️; Excalidraw (⚠️) | Whiteboard sticky notes never become tasks without manual copying. | whiteboard program; "sticky -> task" action |
| 11 | **Collect requests** (intake from outside) | Asana forms ⚠️/[repo]; Jira Service Management ⚠️; Redmine/OpenProject mail intake [repo]; Wekan webhook intake [repo] | Few open tools have real forms with routing and a public status page. | surveys/forms program feeding `fs-tasks` |

Observation: almost all tools are built for purpose 3 (split work) and call it "project management". Purposes 1, 6 and 8 (personal order, memory, own goals) are served by *different* products, which is the root of the "personal versus group" split the owner wants to remove.

---

## 2. Modules

"Belongs in" follows the owner's plan: `fs-tasks`, `fs-history`, `fs-resources`, `fs-groups`, surveys, whiteboard, `fs-wiki`; plus candidate new programs marked **(new)**. Open-source/closed columns list tools that have the module; "(paid)" = gated behind a paid edition where verified.

| Module | Purpose | Open source with it | Closed with it | Belongs in |
|--------|---------|--------------------|----------------|-----------|
| Tasks / work items (fields, status, assignee, subtasks) | Basic unit of work | all (Vikunja, Plane, Taiga, Tenzu, Wekan, Planka, Redmine, OpenProject, Leantime, Huly) | all | `fs-tasks` |
| Boards (kanban) | See state of work, move it | Wekan, Planka, Taiga, Tenzu, Kanboard, Vikunja ⚠️, OpenProject, Plane ⚠️, Leantime; Focalboard (dead) | Trello, Jira, Asana, Monday, Linear, ClickUp | `fs-tasks` (view) -> `fs-kanban` per [repo] |
| Lists / tables / calendar views | Same data, other shape | OpenProject, Redmine, Plane ⚠️, Vikunja ⚠️ | Asana, Monday, ClickUp, Notion | `fs-tasks` (views) |
| Gantt / timeline, dependencies | Order work in time | OpenProject, Redmine, Leantime, Vikunja ⚠️, Plane ⚠️ (Taiga: presentation only) | MS Project, Smartsheet, Asana, Monday, ClickUp, Wrike | `fs-tasks` (timeline view) |
| Auto-scheduling, critical path | Move dependents automatically | OpenProject (automatic mode) [S8] | MS Project, Smartsheet, Wrike ⚠️ | `fs-tasks` schedule engine (separate crate) |
| Baselines / change management | Compare plan versus now; record approved changes | OpenProject: "compare to yesterday" free, full baseline gated [S8] | MS Project, Smartsheet ⚠️ | `fs-history` (snapshots) + `fs-tasks` |
| Sprints / cycles / backlog / burndown | Time-boxed team work | Taiga, OpenProject [S8], Plane ⚠️, Huly ⚠️; Tenzu planned 2026 [S4] | Jira, Linear, ClickUp, Azure Boards ⚠️ | `fs-tasks` (iteration as a view/filter) |
| Epics / roadmap / milestones | Group work, show direction | Taiga, OpenProject, Plane ⚠️ | Jira, Linear, Asana | `fs-tasks` (parent relation) + calendar `Event` |
| Time tracking / timesheets | Know effort spent | OpenProject, Redmine, Leantime [S6], Vikunja ⚠️ | Toggl, Harvest, ClickUp, Jira (add-ons) ⚠️ | `fs-resources` (time ledger) |
| Costs, budgets, rates, invoicing | Money planned/spent | OpenProject (costs, budgets) [S8]; Redmine only via plugins ⚠️ | MS Project, Smartsheet, Wrike, Monday ⚠️ | `fs-resources` costs module |
| Resources, skills, availability, capacity | Staffing | OpenProject (paid: Premium+) [S9]; availability/working schedule in Community [S9] | Asana workload, Monday, Smartsheet, MS Project, Wrike ⚠️ | `fs-resources` |
| Risks / issues / decisions register | Name what could go wrong | OpenProject (type "risk") [repo]; Redmine via tracker ⚠️ | Smartsheet, MS Project templates ⚠️ | `fs-tasks` type + `fs-groups` (decisions) |
| Documents / files | Attach evidence | OpenProject (documents, live editing), Redmine, Taiga [repo]; Huly ⚠️ | Notion, Confluence ⚠️, Basecamp | `fs-documents`, `fs-files` |
| Wiki / knowledge | Remember how and why | Taiga, Redmine, OpenProject, Leantime [repo][S6] | Notion, Confluence, Coda | `fs-wiki` |
| Meetings (agenda, minutes, action items) | Turn talk into tasks | OpenProject [S8] | Notion, Asana ⚠️ | `fs-groups` + `fs-calendar`; action items = `fs-tasks` |
| Goals / OKR / strategy canvases | Link work to aims | Leantime (core) [S6] | Asana Goals, Lattice, Monday ⚠️ | `fs-goals` **(new)** or `fs-tasks` view |
| Portfolio / programme | Several projects at once | OpenProject (portfolio overview, paid parts), Leantime (paid plugin) [S6][S8] | Asana, Monday, Smartsheet, MS Project | `fs-tasks` cross-project query + `fs-reports` |
| Forms / intake | Outside requests | few: Redmine/OpenProject mail intake [repo] | Asana, Jira SM, Monday ⚠️ | surveys program |
| Automation / rules | Remove clicks | Wekan none; Planka ⚠️; Taiga webhooks [repo]; Huly ⚠️ | Trello Butler, Jira, Asana, Monday, ClickUp [repo] | rule model over AS2 events (platform, ADR 0021) |
| Reporting / dashboards | Show status | OpenProject, Redmine, Taiga stats [repo] | all closed | `fs-reports` **(new)** |
| Notifications / watchers | Keep informed | all | all | platform + messenger |
| Permissions / roles / groups | Who may see/do | OpenProject (groups, roles), Redmine (per-role workflows) [repo] | Jira, Asana | `fs-groups` |
| Custom fields, templates | Fit own process | OpenProject, Redmine, Planka/Wekan [repo] | all | `fs-tasks` |
| Whiteboards / mind maps | Visual thinking | (outside PM; Excalidraw etc. ⚠️) | Miro, Mural, Notion ⚠️ | whiteboard program |
| Surveys / polls / voting | Gather opinions | (outside PM; Loomio [S15]) | Typeform, Doodle ⚠️ | surveys program |
| Activity feed / audit trail | Memory | Redmine journals, OpenProject activity [repo] | Jira, Asana | `fs-history` |
| Import / export | Escape lock-in | Taiga JSON dump, Vikunja ZIP [repo]; Tenzu imports Taiga [S3]; MSPDI import/export ⚠️ in several | closed tools: partial CSV | per program; MSPDI adapter (section 5) |
| Integrations (forge, chat) | Link to code/talk | Taiga, Redmine, Plane ⚠️, Huly (GitHub) [S11] | Jira, Linear | platform (AS2/ForgeFed) |
| AI assist | Summaries, triage | Asana/Jira cloud [repo]; Height (gone) ⚠️ | Notion, ClickUp, Linear ⚠️ | local model only (ADR 0029) |
| Personal inbox / daily planning | Order my day | Vikunja ⚠️, Leantime ("my work") ⚠️ | Asana "My tasks" [repo], Todoist ⚠️ | `fs-tasks` personal scope |
| Customer / CRM link | Link tasks to clients | Huly (CRM), Taiga CRM module [repo][S11] | Monday, Notion ⚠️ | `fs-contacts` reference |
| Helpdesk / tickets | Support work | Redmine, Huly ⚠️ | Jira Service Mgmt ⚠️ | separate `helpdesk` category (already in index) |

---

## 3. What open source lacks

Each point: claim, then evidence. Ordered by how much it matters for FreeSynergy.

1. **Capacity planning is paid where it exists, and absent elsewhere.** OpenProject's resource management is an Enterprise add-on, only in Premium and above [S9]. Taiga states it has none [repo]. Of the open-source tools checked, no free one offers it. (Not exhaustive: Redmine plugins ⚠️ not examined.)
2. **Full baselines are paid.** OpenProject Community compares only to "yesterday"; any date range is Enterprise [S8].
3. **Open core is the norm for the "scaling" features.** Leantime sells program management, strategy boards and custom fields as plugins [S6]; Plane keeps paid features in a closed Commercial Edition with a *separate code base* [S10]; OpenProject gates add-ons [S7]; Planka mixes Pro features [repo]. Only Tenzu states "never open core" [S5], but it is kanban-only so far [S4].
4. **Abandonment risk is real.** Focalboard dead since 2024 [S14]; Kanboard frozen in maintenance mode [S13]; Tenzu not yet taking outside contributions and still lacks Scrum/issues [S4]. Choosing a base to fork is risky; this supports building our own (ADR 0013).
5. **No board or project interchange standard.** Our standards search found none [repo standards.md]; each tool exports its own JSON (Taiga dump, Vikunja ZIP). Tenzu's Taiga import proves the work is per-pair [S3].
6. **Dependency vocabulary is thin in the standards** ("blocks"/"duplicates" are not in JSCalendar `relatedTo`) [repo]. Tools therefore invent their own sets (OpenProject, Redmine).
7. **Personal and group use are separate products.** Open-source personal task apps (Vikunja ⚠️) and team tools (OpenProject, Taiga) do not share a data model; the transfer is by export/import. ⚠️ General observation, no quantified source.
8. **Cost data is time-only in most tools.** Redmine tracks hours and an estimate [repo]; budgets and unit costs exist in OpenProject [S8] but no tool checked separates planned, committed and actual money (section 5). ⚠️ for tools not opened.
9. **Decisions are not first-class.** None of the analysed tools [repo] has a decision, vote or consent object; Loomio does it, outside PM [S15].
10. **Per-field and per-task permissions are coarse** in Taiga ("coarse permission model, no field permissions") [repo]. ⚠️ other tools not compared.
11. **Offline and decentralised work are rare.** Our analysis notes Jira, Planka, OpenProject have no offline mode [repo]. No tool checked federates between instances. ⚠️ ForgeFed `TicketDependency` (draft) is the only federation-native task model we know of [repo standards.md].
12. **Reports are counts, not answers.** Tenzu's own announcement says the same about "many metrics that don't give decision-oriented information" [S1].

---

## 4. What nobody does well (ideas)

Marked **idea** = our proposal, not found in any tool. Each states the purpose first.

### 4.1 One task, many lenses (personal and group on the same data)
Purpose: a person plans their own day; a group plans the project; it is the same work.
- A task has one owner object; *scopes* decide who sees it (me only, my group, a project). Promoting a private task to a shared one changes visibility, not the object. Because a card is already a JSCalendar `Task` shared with `fs-calendar` [repo kanban/design.md], this is mostly a policy and sharing question.
- "Don't decide up front": start in personal scope, later invite people; nothing is copied. **idea**
- Open sub-question: what does a collaborator see of my private subtasks of a shared task? (fine-grained visibility, see 3.10.)

### 4.2 History as a first-class view ("what did we do")
Purpose: remember, report, learn. Tools keep per-ticket journals only [repo]. `fs-history` can be a timeline over AS2 activities across tasks, wiki, surveys and files, filterable "me" / "us" / "this project", exportable as a status report. **idea** (storage comes for free from the activity log, kanban design.md).

### 4.3 Plan scenarios, not only a baseline
Purpose: "what if we drop X or add a person?" MS Project and others offer baselines (record of an approved plan) [S8 for OpenProject]. A *branch* of the plan that can be compared and merged is rarer. ⚠️ whether any tool offers it was not checked. With an object-level sync store this is conceptually close to a branch. **idea**

### 4.4 Decisions inside projects, democratically
Purpose: choose among options with legitimacy and a record.
- Decision object linked to tasks: question, options, who may vote, method (simple majority, consent, ranked), deadline, result, reasons. Result can spawn tasks. **idea**
- Methods to offer: yes/no/abstain/block (consent style, as in Loomio-type tools [S15], ⚠️ methods list not verified), ranked choice, quadratic voting ⚠️ (concept only).
- Group role changes (who may approve budgets) are themselves decisions in the log. Fits `fs-groups` + surveys.
- Caution: anonymity versus audit trail needs an explicit rule per decision. Open question for the owner.

### 4.5 Decentralised work
Purpose: cooperating across organisations without one shared server.
- Tasks as AS2/ForgeFed objects can live on each party's instance and be referenced by link; the only existing federated work-item model we know is ForgeFed tickets with `TicketDependency` (draft) [repo]. ⚠️ maturity unknown.
- Offline-first editing with merge per object [repo ADR 0019].
- A task assigned to a person at another instance is a delegation with its own accept/decline state. **idea**

### 4.6 Project health with remediation, not charts
Purpose: "what should I change?" Tenzu names the goal [S1] but has not shipped it [S4]. A rule set over existing data (blocked count, unowned tasks, overdue load, over-allocation, decision pending) that says what to do about it. **idea**

### 4.7 Workload honesty for people with variable energy
Purpose: plan realistically. Leantime targets ADHD/autism/dyslexia in UX [S6]. Beyond UX: capacity that counts *focus hours*, part-time and caring duties, instead of a flat 8-hour day. OpenProject has working schedule and availability [S9]. **idea**: let each person set and own their capacity, groups see aggregated numbers only.

### 4.8 Whiteboard and survey outputs that become work
Sticky to task, survey result to decision to task, meeting action to task, all through the same `Task` and a link back for provenance. **idea** (no tool checked links all three).

### 4.9 Money in three ledgers (see 5.3)

### 4.10 Intake with a public status page
A form (surveys program) creates a task; the requester sees only status through a link, no account. ⚠️ Jira Service Management does similar for closed tools (unverified).

### 4.11 Calm defaults
Few columns, plain language, no gamification; "what is next" first. Supports non-PMs, which Leantime and Tenzu both claim as goal [S1][S6].

---

## 5. Costs and resources

### 5.1 What the modules do (function)

| Function | What it answers | Typical behaviour seen |
|----------|-----------------|------------------------|
| Time tracking | How much effort was spent, by whom, on what | Log hours per task with an activity type (Redmine) [repo]; OpenProject also has "my time tracking", unit costs, and reports [S8] |
| Estimates | How much effort is expected | Hours or story points per task; Redmine shows remaining = estimate minus bookings [repo] |
| Rates | What an hour/unit costs | Per user or role, valid from a date ⚠️ (OpenProject cost-rate concept, details not re-fetched) |
| Budget | How much may be spent | OpenProject: plan labour and unit costs per project and compare [S8] |
| Cost types / unit costs | Non-labour items (licence, travel) | OpenProject "unit costs" [S8] |
| Availability / working schedule | When a person can work | OpenProject: working hours, future changes, time off [S8][S9] |
| Resource planning | Who works on what, when, versus capacity | OpenProject resource planners with timeline and card views, allocate work by user or filter, staffing [S9] |
| Skills | Who can do what | OpenProject user attributes: job title, key skills, languages [S8] |
| Reports | Planned versus actual | OpenProject time and cost reports [S8] |

### 5.2 Data these modules need

| Entity | Fields (suggested) | Linked to |
|--------|--------------------|-----------|
| Person / role | identity ref (`fs-contacts`), roles, skills, job title | groups |
| Working schedule | weekly pattern, exceptions, absences, time zone | calendar (JSCalendar events for absence) |
| Capacity | hours or "focus hours" per period, set by the person | person |
| Allocation | person or role, task or project, period, amount, status (tentative/confirmed) | task |
| Time entry | person, task, date, duration, activity, billable, note | task |
| Rate | subject (person/role/unit), amount, currency, valid-from, valid-to | cost entry |
| Cost entry | task/project, type, quantity, unit price, currency, date, status (planned/committed/actual) | budget |
| Budget | project, lines, currency, period, approver | decision record |
| Estimate | task, duration (RFC 10051 estimated duration), basis | task |
| Baseline | snapshot of dates/estimates/budget at approval | history |

Rule of design **idea**: dates, durations and relations stay in the JSCalendar `Task` and RFC objects [repo]; resources and money live in *separate* objects that reference the task, so a personal user who never touches money has no dead fields on the task.

### 5.3 Why three ledgers (idea)
Planned (budget, estimate), committed (ordered, allocated) and actual (time entered, invoice paid) differ in who writes them and when. Tools checked mostly combine planned and actual in one report [S8]; separating them keeps audit clear and lets a group decide (4.4) on a budget change. ⚠️ whether any tool already does this was not verified.

Money must use decimal/integer minor units and ISO 4217 currency codes ⚠️ (standard named from general knowledge; not in standards.md; confirm before adopting).

### 5.4 Relevant standards

Already recorded in `docs/en/data/projects/standards.md` and **not re-searched**: JSCalendar 2.0 `Task`; RFC 9253 (relations incl. `FINISHTOSTART` with lead/lag); RFC 10051 (task status, estimated duration); ForgeFed `TicketDependency` (draft); ISO 21511:2018 (WBS guidance, vocabulary); ISO 21502:2020 (guidance, role vocabulary, no data format); schema.org `Project` (export projection only); MSPDI (`mspdi_pj12.xsd`, de-facto XML; durations in tenths of a second, not an open standard). No standard for boards.

What this means for cost and resource data (analysis, not new search):
- **MSPDI** is the only widely used exchange format that carries *resources, assignments, rates and baselines* (⚠️ from general knowledge of the schema; the repo only records tasks, calendars and durations). It is the realistic import/export target for the costs module. MS Project Online's retirement (2026-09-30) [S16] raises demand for migration paths, a point in favour of an MSPDI adapter. Treat it as an adapter, not the internal model.
- **RFC 9253** covers task-to-task dependency with lead and lag, enough for the schedule engine; nothing for resources.
- **JSCalendar** has `estimatedDuration` and `timeZone` ⚠️ (field names to be checked against RFC 8984 / 10051) but no cost, rate or allocation fields: resources and money need our own spec (section candidate extension of no. 3), using vendor properties only where the data really is a task attribute.
- **ISO 21502** is process guidance; use it for vocabulary (roles, "baseline", "change control") only [repo].
- **Not looked at (open)**: ISO 4217 (currencies), OpenAPI/OData-style PSA exchange formats, EVM (earned value) definitions in PMI/ANSI material, UN/CEFACT or Peppol for invoicing. All ⚠️ not verified; a short standards pass would be needed before the costs module is specified.

### 5.5 Placement
Resources, capacity, time, rates and costs form one program (`fs-resources`) with two crates: `resources` (people, skills, availability, allocation) and `costs` (rates, cost entries, budgets). Reasons: capacity and cost share rates and time entries; the owner suggested "possibly a costs module", so keeping it separable lets personal users run without it. Reports about them go to `fs-reports`. **idea**

---

## Sources (all retrieved 2026-11-06)

| ID | URL | Used for |
|----|-----|----------|
| S1 | https://community.taiga.io/t/launching-tenzu-taiganext-new-identity/3940 | Tenzu origin, stack, vision (2024-09-05); TaigaCloud keeps Taiga6 |
| S2 | https://tenzu.net/en/who-are-we/ (only the search snippet read) | Tenzu origin, consistent with S1 ⚠️ |
| S3 | https://github.com/BIRU-Scop/tenzu-docs/blob/main/docs/changelog.md | releases v2.0.0 to v3.2.0 |
| S4 | https://github.com/BIRU-Scop/tenzu-back | features, "Scrum and issues coming in 2026", contribution policy; plus GitHub repo metadata (updated 2026-10-29) |
| S5 | https://europeanpurpose.com/tool/tenzu (reviewed 2026-10-27) | AGPLv3, "never open core", pricing, SCOP. Third-party review |
| S6 | https://www.opentechhub.io/leantime/ | Leantime licence, open-core plugins, release v3.13.2. Third-party review |
| S7 | https://www.openproject.org/pricing/ | plan names, prices, minimum users |
| S8 | https://www.openproject.org/pricing/ (feature table, text mode) | feature list; baseline statement. Community column garbled, so gating of costs/budget unverified |
| S9 | https://www.openproject.org/docs/user-guide/resource-management/ and https://www.openproject.org/docs/user-guide/time-and-costs/ | resource management is Enterprise add-on, Premium/Corporate; planner views; time and cost docs |
| S10 | https://developers.plane.so/self-hosting/editions-and-versions | Plane editions, AGPL Community, separate closed Commercial |
| S11 | https://github.com/hcengineering/ (search snippet) and https://www.opensourcealternatives.to/item/huly | Huly EPL-2.0, scope. Snippets only |
| S12 | GitHub repository metadata for go-vikunja/vikunja via GitHub API | activity, stars. Licence not verified |
| S13 | https://openappscout.com/apps/kanboard/ (search snippet) | Kanboard MIT, maintenance mode |
| S14 | https://github.com/mattermost-community/focalboard/issues/4983 and https://freealternatives.to/focalboard/free-plan | Focalboard unmaintained (snippets) |
| S15 | GitHub repository metadata for loomio/loomio via GitHub API | active; licence from fork READMEs only ⚠️ |
| S16 | https://www.velosio.com/blog/microsoft-project-online-retirement-what-to-do-before-september-30-2026/ and https://mc.merill.net/message/MC1148537 (via web search summary) | Project Online retirement 2026-09-30 |
| S17 | https://www.shortcut.com/blog/alternatives-to-height-app/ (search summary, competitor) | Height shutdown Sept 2025 ⚠️ |
| repo | `docs/en/programs/apps/projectmanagement/*`, `.../frontends/*/latest/features.md`, `docs/en/programs/apps/kanban/{requirements,design}.md`, `docs/en/data/projects/standards.md` | existing analyses and standards |

## Open items for the owner or a follow-up pass
1. Closed tools (Asana, Monday, ClickUp, Linear, Notion, Basecamp, Smartsheet, Wrike, MS Planner) need a direct check of workload, goals, portfolio, forms and automation before they are cited as facts.
2. OpenProject: confirm which of costs/budgets are Community versus Enterprise on the vendor's add-on list.
3. Leantime: confirm the paid-plugin list on leantime.io.
4. Vikunja, Plane, Huly: confirm licence and views from upstream READMEs.
5. Standards pass for money (ISO 4217), earned value, MSPDI resource/assignment/baseline elements, invoicing formats.
6. Decide the anonymity rule for decisions (4.4) and the privacy rule for private subtasks (4.1).
