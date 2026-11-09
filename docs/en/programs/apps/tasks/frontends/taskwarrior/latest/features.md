# Taskwarrior - Features

## Main features

- Urgency terms: next tag, due date (overdue counts more), priority (high/medium/low), blocking other tasks, scheduled, started, age, annotations, tags, project; waiting and blocked reduce it.
- Defaults listed in the docs: next tag 15.0, due 12.0, blocking 8.0, high priority 6.0, medium 3.9, low 1.8, scheduled 5.0, active 4.0, age 2.0, annotations 1.0, tags 1.0, project 1.0, waiting -3.0, blocked -5.0.
- Every coefficient is configurable; 0 disables a term; some can be set per project.
- Tag and annotation counts scale their term (0.8 for one, 0.9 for two, 1.0 for more).
- Dependencies, recurrence, annotations: named in the urgency doc; detail Open.
