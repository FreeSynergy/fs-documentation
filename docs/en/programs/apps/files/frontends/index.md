# Files — Frontends

Frontends of well-known programs in this category, analysed for their **functions** — nothing is copied (ADR 0013). A program is documented here because it is widely learned or because it has a notable idea. Our own program for this category is `FreeSynergy.Files` (ADR 0017); its capabilities and status live in [requirements](../requirements.md).

## Programs

| Program | Versions | What it is |
|---------|----------|------------|
| [Dolphin](dolphin/index.md) | — | The file manager of KDE Plasma. |
| [Dropbox](dropbox/index.md) | [latest](dropbox/latest/description.md) | Dropbox is a commercial cloud storage service with web, desktop and mobile clients and a developer API. |
| [Everything](everything/index.md) | [latest](everything/latest/description.md) | Everything (voidtools) is a free search program for Windows that finds files and folders by name while you type ✅. |
| [Files (Files App for Windows)](files-community/index.md) | [latest](files-community/latest/description.md) | A free, open-source file manager for Windows, built by a community (repository `files-community/Files`, WinUI, C#/.NET) ✅. |
| [Finder](finder/index.md) | — | The file manager of macOS. |
| [Google Drive](google-drive/index.md) | — | Cloud storage by Google: web, apps and a desktop client. |
| [Nautilus (GNOME Files)](nautilus/index.md) | — | The file manager of the GNOME desktop. |
| [Nextcloud Files](nextcloud-files/index.md) | — | The Files app of Nextcloud: web interface, desktop and mobile sync, WebDAV, on a server you run. |
| [rclone (and the S3-browser type)](rclone/index.md) | — | A command-line program that copies, syncs, mounts and serves files across many storage services. |
| [Seafile](seafile/index.md) | — | Open-source file sync, share and document collaboration. |
| [Syncthing](syncthing/index.md) | [latest](syncthing/latest/description.md) | Syncthing is a free program that keeps chosen folders identical between devices directly, with no central server ✅ (concept; the intro page does not state it, see Open). |
| [Total Commander](total-commander/index.md) | [latest](total-commander/latest/description.md) | A paid (shareware) two-pane file manager for Windows by Christian Ghisler ✅ (home page links to ordering and shareware sites; price not stated there; Wikipedia: shareware on Windows, freeware on An… |
| [Windows Explorer (File Explorer)](windows-explorer/index.md) | [latest](windows-explorer/latest/description.md) | The file manager of Windows. |

## File set per program (ADR 0012)

```
programs/apps/files/frontends/<program>/
├── index.md        what it is, notable ideas, documented versions, sources
├── changelog.md    changes between documented versions (≥ 2 versions)
└── <version>/
    ├── description.md    required · Detailed description, differentiation, who it suits
    ├── features.md       required · What the program can do — and what not
    ├── layout.md         required · Window structure, regions, panels
    ├── menus.md          required · Menu structure, context menus, menus by role
    ├── shortcuts.md      required · Keyboard shortcuts
    ├── api.md            required · APIs and protocols, authentication, rate limits
    ├── themes/index.md   required · Themes: colours, typography, spacing — what can be rebuilt
    ├── interaction.md    if needed · Hover, focus, drag, gestures (finger, mouse, pen)
    ├── states.md         if needed · UI states and transitions
    ├── events.md         if needed · Events to the outside (webhooks, push, streams)
    ├── limits.md         if needed · Known limitations
    ├── i18n.md           if needed · Localisation, writing direction
    ├── dependencies.md   if needed · Which of our components a frontend in this style needs
    ├── dialogs.md        if needed · Every dialog: purpose, fields, buttons, default, cancel
    ├── workflows.md      if needed · Step-by-step workflows: goal, prerequisites, steps, failures, undo
    ├── acceptance.md     if needed · Acceptance checklist: each workflow as a yes/no click test
    └── gaps.md           if needed · What our program cannot do for these workflows, and what it needs
```

Protocols (Matrix, IMAP, CalDAV, …) are not frontends; they are described under [data](../../../../data/standards.md).
