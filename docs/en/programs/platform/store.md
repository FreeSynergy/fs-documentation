# FreeSynergy.Store

**One place to get FreeSynergy, with every download checked before it touches your machine.**

The Store is the app from which you install, update and extend everything else: programs, frontends, components and themes. You install the Store once, by hand ([how](../../start/install.md)), and then you do not install anything by hand again. It keeps itself and everything else up to date, rolls an update back if it fails, and never replaces a program while it is running.

Status: **pre-release, early.** See "Where it stands today" below before you try it.

## What is different here

- **Signed, or not at all.** Every package must carry a valid OpenPGP signature from a trusted key, or it cannot be installed. This is not a warning you can click away: in the code, an unsigned package cannot even be handed to the installer. A checksum alone does not count as a signature.
- **Packages live in Git** ([ADR 0062](../../decisions/0062-paket-repos-in-git.md)). A catalog repository holds the list of apps in the open AppStream format, with signed metadata following the TUF specification (The Update Framework). Each version of a package is a Git tag with the finished packages and their signatures. The Store fetches only that one tag, never the whole history. Any place that can host Git can be a mirror; trust hangs on the signatures, not on the place. HTTPS stays a second way, for example GitHub releases.
- **Facets are apps of their own** ([ADR 0061](../../decisions/0061-facetten.md)). The catalog lists every facet, such as Contacts, as an app with its own logo. Installing it installs the program behind it, here People. Installing a second facet of the same program adds only its menu entry and frontends.
- **One program, one command** ([ADR 0063](../../decisions/0063-ein-programm-ein-befehl.md)). The Store is the command `fs-store`. Without arguments it opens the window. With subcommands it works like `git`: `fs-store sources`, `fs-store available`, `fs-store install <package>`, `fs-store update`, `fs-store installed`. Each facet gets a command of its own, a link to its program (`fs-contacts` for `fs-people`), which the Store creates on install.
- **Your list of sources.** Packages come from a list of Git sources. You can add your own. The built-in FreeSynergy source can be switched off but never removed, so the way back always stays.

## Where it stands today

- Pre-releases exist on GitHub ([releases](https://github.com/FreeSynergy/fs-store/releases)). Version numbers are being reset to `0.0.N` ([ADR 0064](../../decisions/0064-versionen-ab-0-0-1.md)); the older `0.1.0-rc.N` builds are marked "do not use" or will be removed.
- The core works: the source list, reading the catalog, the signature check against the project key, installing from a `tar.gz` into your home folder, switching to the new version in one step and keeping the old one, and a check that the program is not running. It has been tried against a real signed package of Tasks through a local Git catalog.
- The command line works for the subcommands above. The window is first and provisional.
- Installing an rpm through `dnf` and `pkexec` is written but has not been run for real (root is asked by the system, never by the Store).

## What is not there yet

- The full catalog: [fs-catalog](https://github.com/FreeSynergy/fs-catalog) offers only the Store, Tasks and People so far. What exists of the TUF metadata is in the Store's DESIGN.md.
- Replacing the running Store by itself.
- Facet commands (`fs-contacts` and the like): the format is provisional and not built.
- Windows, and checks for key expiry.
- The name and the crate names are provisional.

## Part of FreeSynergy

The Store is the part of the [platform](../index.md) that gets everything else onto your machine. The state table is in the repository's [DESIGN.md](https://github.com/FreeSynergy/fs-store/blob/main/DESIGN.md).
