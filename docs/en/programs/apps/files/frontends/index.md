# Files — Frontends

Frontends of well-known programs in this category, analysed for their **functions** — nothing is copied (ADR 0013). A program is documented here because it is widely learned or because it has a notable idea. Our own program for this category is `FreeSynergy.Files` (ADR 0017); its capabilities and status live in [requirements](../requirements.md).

## Programs

| Program | Versions | What it is |
|---------|----------|------------|
| [Dolphin](dolphin/index.md) | — | The file manager of KDE Plasma. |
| [Dropbox](dropbox/index.md) | [latest](dropbox/latest/description.md) | Cloud storage with web, desktop and mobile clients; file requests let outsiders send files without an account. |
| [Everything](everything/index.md) | [latest](everything/latest/description.md) | Windows program that finds files by name as you type, using a name index. |
| [Finder](finder/index.md) | — | The file manager of macOS. |
| [Google Drive](google-drive/index.md) | — | Cloud storage by Google: web, apps and a desktop client. |
| [Nautilus (GNOME Files)](nautilus/index.md) | — | The file manager of the GNOME desktop. |
| [Nextcloud Files](nextcloud-files/index.md) | — | The Files app of Nextcloud: web interface, desktop and mobile sync, WebDAV, on a server you run. |
| [rclone (and the S3-browser type)](rclone/index.md) | — | A command-line program that copies, syncs, mounts and serves files across many storage services. |
| [Seafile](seafile/index.md) | — | Open-source file sync, share and document collaboration. |
| [Syncthing](syncthing/index.md) | [latest](syncthing/latest/description.md) | Folder sync directly between devices, without a central server, controlled by a local web GUI. |
| [Windows Explorer (File Explorer)](windows-explorer/index.md) | — | The file manager of Windows. |

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
    └── dependencies.md   if needed · Which of our components a frontend in this style needs
```

Protocols (Matrix, IMAP, CalDAV, …) are not frontends; they are described under [data](../../../../data/standards.md).
