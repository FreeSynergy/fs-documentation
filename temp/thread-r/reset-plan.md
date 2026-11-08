# Version reset to 0.0.x (prepared, NOT executed; waits for user approval)
Dependency order (computed from Cargo.toml git deps, .scratch/tr/deps.txt):
1. fs-capnpc, fs-jscalendar, fs-objects
2. fs-interfaces
3. fs-components, fs-files, fs-maps, fs-messenger, fs-resources, fs-streaming, fs-whiteboard
4. fs-people, fs-tasks, fs-wiki, (fs-store = new Store/launcher repo, check name)
5. fs-calendar, fs-groups
6. fs-hub, fs-identity, fs-surveys
7. fs-history
Not Rust-dep: fs-documentation, fs-release, fs-launcher.
Per repo: workspace version -> 0.0.1; every `tag = "vX"` of FreeSynergy deps -> v0.0.1 (via tags.txt-like map); commit; gates (clean clone); push; tag v0.0.1; only then next level.
Cross-version dependencies (hub-history alias on objects 0.5, calendar tasks pin, wiki interfaces) collapse to one version per crate: remove aliases.
Afterwards (separate, destructive, needs explicit OK): delete old tags and GitHub releases (gh release delete --cleanup-tag), per repo; branches pinned to old tags (48 converted branches, gui/client) need their pins moved when rebased.
Open risks: published releases/drafts (fs-tasks 0.8.2-rc.*), signed files refer to old versions; Cargo.lock in tags.
