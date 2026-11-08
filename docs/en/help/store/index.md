# Store help

The Store is the program you use to get everything else. You install programs, frontends, components and themes from it, and it keeps them up to date. Every download is checked against a signature before it touches your machine. You can use the Store as a window or as the command `fs-store`.

## Views of the window

The window shows one page at a time. You switch pages in the **Store** menu at the top.

- [Programs](programs.md): a card for every program, with Install, Open and Update.
- [Installing and updating](installing.md): the bar that shows the steps of a running job.
- [Sources](sources.md): the Git sources the Store reads, and the form to add one.
- [Settings](settings.md): when to look for updates, whether to install them, the daily timer.
- [About](about.md): name, version, licence and project address.

## Command line

- [Command line](command-line.md): `fs-store sources`, `available`, `install`, `update`, `installed` and the rest, each with an example.

## How to start

- For the window, run `fs-store` with nothing after it. The first start also puts the Store into your menu.
- For the command line, run `fs-store` with a subcommand, for example `fs-store installed`.
- Do not start it as root. The Store works in your own folders and asks for a password itself when it needs one.

New here? Read [Install the Store](../../start/install.md) first, and [what the Store is](../../programs/platform/store.md) for the longer story.

[Back to all help](../index.md)
