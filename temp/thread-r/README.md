# Thread R scripts and records (2026-11-08)
One-off tools of the rename (fs-store -> fs-objects, ADR 0060) and the version reset (v0.0.1, ADR 0064). Kept so the work can be repeated or audited; they assume the layout `/srv/FreeSynergy/<repo>` and the gates script `fs-release/scripts/gates.sh`.
- `run.sh`, `finish.sh`, `branch.sh`: rename step per repo / per open branch.
- `reset.sh`, `reset.py`: version reset per repo (versions, dependency tags and rev pins to v0.0.1, gates in a fresh clone, tag). `branchpins.sh`: the same for open branches (deps only).
- `delete.py`, `delete-list.md`, `executed.md`, `executed-delete.log`: the list of old tags/releases and what was deleted.
- `reset-plan.md`, `tags.txt`: plan and tag map.
