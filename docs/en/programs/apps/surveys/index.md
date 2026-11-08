# Surveys

## In short

FreeSynergy Surveys lets a person or a group ask questions, collect answers and read the result. It answers the question: how can we decide together, and be sure an anonymous answer stays anonymous? Answers can carry a name or be anonymous.

## What is different here

- Anonymous answers do not go into the ordinary store. They go into a separate box that keeps no log and no time, with answers shuffled.
- Results appear only in batches of at least a minimum group size, so reading twice cannot reveal one person's answer.
- If held-back answers could change the outcome, the program says it cannot name a winner yet.
- A survey can start in a small group and later widen to the larger group around it, keeping the answers already given.
- A decision can be linked to the tasks that follow from it. Surveys owns its open interface.

## Where it stands today

Latest tag: `v0.3.0`. Today it is the core, without a window. You can create and edit surveys with questions and conditions through the stages draft, open and closed. Named answers can be saved as a draft, resumed, submitted and replaced while open. Anonymous answers go into the separate box, with one-time tokens for "one answer per invited person". Results offer a summary, an evaluation with counting methods such as plurality, approval, majority and supermajority, and a CSV export. Surveys can be widened over groups, and a decision can be linked to task identifiers. It has 107 tests with real stores and was checked by an independent reviewer over three rounds.

Not there yet (planned): a window and a server. Tokens have no real delivery until the messenger plugs in. Public links and embedding are not possible, and DDI export is not supported. Anonymity has stated limits: someone running the machine can still read memory while a ballot passes, and a window must show these limits. Only one survey store per process. The interface is a draft, marked provisional, because no survey frontends have been analysed yet.

`FreeSynergy.Surveys` (`fs-surveys`) builds surveys and polls, collects answers and shows results, with anonymity where
it is needed.

See the [roadmap](../roadmap.md) for the plan; the current state is under "Where it stands today" above.

- [Design](design.md): how it is built, anonymity, open questions
- [Requirements](requirements.md): what it must do (provisional)

No frontends have been analysed for this category yet. Candidates for the analysis are LimeSurvey, Nextcloud Forms,
Formbricks, Framadate, Google Forms and Microsoft Forms. The [democracy suite](../../suites/democracy/index.md) is a
related area.
