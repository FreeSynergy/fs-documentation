# Glossary

Short explanations of the words we use. Behind the words are decisions you can read in [Decisions](../decisions/index.md).

**App.** What people see and install. Everything is called an app on the outside, whether it is a program, a facet or a frontend. "Facet" and "program" are words for us and for this documentation.

**Program.** The engine for one topic: people, tasks, files, messages. It owns the data, the rules and one open standard. Example: `fs-people`. See [Programs](../programs/index.md).

**Facet.** A part of a program that looks like an app of its own, with its own name, logo and menu entry, and a fixed filter on the program's data. It has no data of its own. Example: Contacts and Users are facets of `fs-people`. A facet is the opposite of a suite. Each facet also has a command of its own, for example `fs-contacts` ([ADR 0061](../decisions/0061-facetten.md), [ADR 0063](../decisions/0063-ein-programm-ein-befehl.md)).

**Frontend.** One way of looking at a program or a facet: very simple, classic, familiar, or complete. There are many for each; you can switch at any time and your data stays where it is.

**Admin frontend.** The frontend with every setting. Each program and facet has one. If a simple frontend hides something you need, the admin frontend can always put it right.

**Component.** A piece of screen that shows something without knowing what the data means, such as a calendar grid or a chart. Frontends are built from components. See [Components](../components/index.md).

**Workbench.** A large component that is a whole working area, such as a file manager.

**Suite.** Several programs put together for one purpose, for example groupware, project management, CRM.

**Contract (interface).** The agreed way programs talk to each other, one per topic. It is a target, not something that keeps growing: a change is a jump to a new version. See [Interfaces](../interfaces/index.md).

**Hub.** The program that lets the programs on one device find each other and keeps the activity log.

**Store.** FreeSynergy.Store, the app from which you install, update and extend everything else. See [the Store](../programs/platform/store.md).

**Catalog.** The list of packages a source offers: name, logo, description, versions and facets, in the open AppStream format, with signatures. See [ADR 0062](../decisions/0062-paket-repos-in-git.md).

**Pre-release.** A first version for trying and testing, published openly and labelled honestly. It can be wrong.
