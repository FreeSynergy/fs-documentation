# Surveys, polls and group decisions: landscape research

Retrieved: 2026-11-06. Written for FreeSynergy (ADR 0013: analyse functions, copy nothing). Own wording throughout.

Conventions:
- `[Sn]` points to the source list at the end. A claim without `[Sn]` is my own analysis or inference and says so.
- ⚠️ = unverified, partial, from memory or from a thin or stale source. Treat as a lead, not a fact.
- Many pages were read through a summarising fetch tool, not in full. Where a page was longer than the tool's window, the unread part is not covered. The Wikipedia pages in particular were only partly read.

## 0. Scope: what was and was not covered

Read (at least one primary or encyclopedic page each): LimeSurvey, Formbricks, Nextcloud Forms (thin), Framadate, Rallly, KoboToolbox (server repo only), ODK, Loomio, OpenSlides (thin), Decidim, Pol.is, LiquidFeedback, Helios, Slido, Mentimeter, Typeform (stale page), Doodle, Qualtrics (two help pages), Google Forms (one help page), Tally (page missing), SurveyMonkey (one help page, little content), Jotform (landing page only).

Not covered or only by name: OpenForms (Dutch gov. form builder, not looked up), Microsoft Forms, Tally features, Framaforms, Survey-Solutions, Limesurvey internals, Kialo, Thoughtexchange, Consul Democracy, CiviCRM surveys, Your Priorities, Adhocracy, Cobudget, Snapshot (token voting), Belenios, Civs, Condorcet Internet Voting Service, StrawPoll, Zoom/Teams polls, Google Forms quiz mode, Airtable/Notion forms, Wufoo, Formstack, Alchemer, Zoho Survey, Survicate, Hotjar, Delib/Citizen Space. A real survey of "all" tools is not possible; roughly 25 tools were touched, about 15 with real depth.

Search tool was rate-limited for part of the session, so some searches returned nothing and were replaced by direct page fetches.

## 1. By purpose

Purpose first. The tool names are examples seen, not a ranking.

| Purpose (what people need) | Typical shape | Tools seen |
|---|---|---|
| Quick group decision ("where do we eat") | one question, few options, link shared in a chat, result in minutes | Framadate (date polls and classic polls; "quick decisions" is its own wording) [S20]; Loomio simple poll [S10]; StrawPoll-like tools ⚠️ not read |
| Find a common time | participants mark availability on a grid, organiser picks | Doodle [S19], Rallly (no account needed to vote) [S16], Framadate [S20], Loomio time poll [S10] |
| Group decision with accountability (a team, club, co-op) | discussion thread plus a proposal, positions with reasons, recorded outcome | Loomio (proposal, sense check, advice, consent, consensus) [S10, S11, S12] |
| Decision by consent / low objection | collect objections early, revise, decide when no reasoned objection stays | Loomio consent template [S12]; sociocracy practice [S27]; systemic consensing as a method [S13] |
| Opinion research / market research | many anonymous respondents, structured questionnaire, statistics | LimeSurvey [S1], SurveyMonkey, Qualtrics [S3], Typeform, Google Forms [S6] (closed ones: ⚠️ feature claims beyond the cited pages are from general knowledge) |
| Customer or product feedback in context | short question shown inside an app or site to selected users | Formbricks (link, website and in-app surveys) [S2] |
| Field data collection (health, aid, agriculture, census) | offline phones, GPS/photos/barcodes, sync later, role-based access | ODK [S7], KoboToolbox (server part read) [S8], ODK XForms spec [S9] |
| Elections with secrecy and verifiability | roll of eligible voters, secret ballot, public proof of the tally | Helios [S14], Belenios ⚠️ not read |
| Assembly work (motions, agenda, elections, projected) | people in a room or call, chair, motions in order | OpenSlides [S22] |
| Live audience interaction (talk, lesson, event) | short questions on screen, instant results, join with a code, Q&A upvote, quiz | Slido (five poll types, Q&A upvote, moderation, quizzes) [S17], Mentimeter (polls, word cloud, scales, open ended, Q&A, quizzes) [S18] |
| Large-scale deliberation / find common ground | many statements, each person votes agree/disagree/pass, map of opinion groups | Pol.is [S15] (open source, vTaiwan) |
| Participatory budgeting and citizen proposals | spaces (processes, assemblies), components (proposals, budgets, meetings, surveys), identity verification | Decidim [S21] |
| Long-running party/organisation opinion forming | initiatives with quorum, preferential voting, delegation per area | LiquidFeedback [S5, S23] |
| Forms that move money or documents | payment, signature, approval flows | Jotform (payment forms, sign, workflows) [S24] — this is form-filling more than surveying |

Observation (own analysis): the same shape of object ("a question with answer options and a way to collect answers") serves at least eight different purposes. What differs is (a) who may answer, (b) whether answers are secret, (c) how answers are combined, (d) what happens after. That points to one core object plus pluggable "who", "how combined" and "what next".

## 2. Capability catalogue

"Open source has it?" = Yes (seen in at least one open-source tool I read), Partly, No (not found; absence in my reading is not proof). IDs are `<object>.<action>`.

| Capability id | Purpose | Seen in | Open source has it? |
|---|---|---|---|
| `poll.create_choice` | one or many options, pick one/several | Loomio Choose [S10]; Framadate [S20]; Slido [S17]; Mentimeter [S18] | Yes |
| `poll.create_time` | find a time across participants and zones | Rallly [S16]; Framadate [S20]; Loomio time poll [S10]; Doodle [S19] | Yes |
| `poll.create_score` | rate every option on a shared scale | Loomio Score [S10] | Yes |
| `poll.create_allocate` | spend a fixed budget of points (dot vote) | Loomio Allocate [S10] | Yes |
| `poll.create_rank` | order options by preference | Loomio Rank [S10]; LiquidFeedback preferential voting [S5] | Yes |
| `poll.create_stv` | elect several people proportionally | Loomio STV [S10] | Yes |
| `proposal.respond_stance` | agree / abstain / disagree / block with reason | Loomio [S10, S12] | Yes |
| `proposal.sense_check` | cheap early temperature test before a formal proposal | Loomio sense-check [S12] | Yes |
| `proposal.object` | consent round with named objections | Loomio consent [S12] | Yes |
| `vote.score_resistance` | rate resistance 0–10 per option incl. a "do nothing" option | method [S13]; a dedicated "SK-App" is mentioned by [S13] ⚠️ licence unknown | Not found as a tool |
| `vote.delegate` | pass your vote to someone, per area, revocable | LiquidFeedback [S5, S23] | Yes |
| `vote.quadratic` | spend credits with rising cost per vote | method [S28]; Gitcoin / Colorado caucus used it [S28] | ⚠️ No general survey tool seen |
| `vote.verify_ballot` | voter gets a tracker to check own ballot in a public board | Helios [S14] | Yes |
| `vote.audit_ballot` | voter can test-decrypt a ballot to prove the device is honest | Helios [S14] | Yes |
| `vote.hide_identity` | anonymous votes | Loomio template option (name only) [S11]; Framadate anonymous voting [S20]; Qualtrics anonymise [S3] | Yes |
| `result.hide_until_closed` | stop herd effects | Framadate "hide results" [S20]; Loomio ⚠️ page did not confirm | Partly |
| `result.show_live` | audience sees bars/word cloud immediately | Slido, Mentimeter [S17, S18] | ⚠️ not found in open source |
| `result.cluster_opinions` | map participants into opinion groups, show cross-group consensus | Pol.is [S15] | Yes (one tool) |
| `result.flag_quality` | speeders, straightlining, gibberish, bots, duplicates, review queue | Qualtrics [S4]; Surveti [S25] ⚠️ product status unclear | ⚠️ not found in the open source tools read |
| `question.ask_live_upvote` | audience questions ranked by upvotes, optional moderation | Slido [S17] | ⚠️ not found |
| `question.show_one_at_a_time` | one question per screen to raise completion | Typeform [S26 ⚠️ stale page, 2018] | ⚠️ unknown |
| `question.branch` | show/skip questions based on earlier answers | LimeSurvey conditional routing [S1]; ODK conditional branching [S7]; FHIR `enableWhen` [S29] | Yes |
| `question.validate` | constraints on answers, calculations, repeating groups | ODK [S7]; FHIR `answerConstraint`, `maxLength` [S29] | Yes |
| `question.capture_media_gps` | photos, signatures, barcodes, points/lines/polygons | ODK [S7] | Yes |
| `form.collect_offline` | collect without network, sync later | ODK [S7] | Yes |
| `form.import_xlsform` | author forms in a spreadsheet | ODK/Kobo ecosystem [S9] ⚠️ Kobo relation not confirmed on read page | Yes |
| `form.in_app_target` | show a survey to a user segment inside a product | Formbricks [S2] | Yes (core is AGPL; enterprise parts gated) |
| `form.use_template` | start from ready-made form | LimeSurvey (900+ templates, per its README) [S1]; Formbricks [S2]; Loomio poll templates [S11] | Yes |
| `form.localize` | many languages in one survey | LimeSurvey 80+ [S1] | Yes |
| `access.token_invite` | unique code per invitee, uses-left, validity window | LimeSurvey [S3b] | Yes |
| `access.open_link` | anyone with link may answer, no account | Rallly [S16]; LimeSurvey public link [S1] | Yes |
| `access.limit_one_signed_in` | one response per account | Google Forms (forces Google sign-in) [S6] | n/a (needs accounts) |
| `access.limit_cookie` | one response per browser | Qualtrics [S4] | ⚠️ likely, not verified in open source |
| `access.password_shared` | single survey password | Qualtrics (no guess limit) [S4] | ⚠️ |
| `access.register_public` | visitor registers by email, gets token | LimeSurvey public registration [S3b] | Yes |
| `access.verify_citizen` | verify who may take part (authorisation) | Decidim [S21] | Yes |
| `guard.captcha` | stop automated sign-ups | LimeSurvey (registration, save, load forms) [S3b]; Qualtrics reCAPTCHA v3 score [S4] | Yes |
| `guard.proof_of_work` | stop mass submission by CPU cost | ALTCHA, mCaptcha as add-ons (not survey tools) [S30, S31] | Yes (libraries) |
| `guard.private_token` | prove "real device" without identity | Privacy Pass / Apple PAT [S32, S33] | Protocol is open; survey tools ⚠️ none seen |
| `group.nest` | groups inside groups with own members | Loomio subgroups [S34]; sociocracy circles [S27]; LiquidFeedback units/areas [S23] | Yes |
| `group.escalate` | move a running decision to the parent group with its results | none found (see section 5) | No |
| `result.export` | CSV and API access | Nextcloud Forms CSV [S35]; ODK REST API [S7]; LimeSurvey RemoteControl [S1]; Kobo API [S8] | Yes |
| `outcome.record` | timestamped decision, next steps, review date | Loomio [S12] | Yes |
| `integration.webhook` | trigger other tools on submission | Nextcloud Forms webhooks [S35]; Formbricks Slack/Zapier/n8n [S2] | Yes |
| `payment.collect` / `document.sign` / `workflow.approve` | forms that complete a transaction | Jotform [S24] | ⚠️ not examined in open source |
| `answer.federate` | send/receive votes across servers | Mastodon polls over ActivityPub [S36] | Yes (microblog only) |

## 3. Decision methods

Chart suggestions are my own proposals unless a source says what the tool shows. "Cited" marks what was read.

| Method | How it works (one line) | Suits | Fitting result chart |
|---|---|---|---|
| Simple majority / plurality | the option with most votes wins | low-stakes, two options, speed | horizontal bars with counts and %, winner marked |
| Supermajority | a threshold above 50 % (e.g. 2/3) is required | changes to rules, statutes, irreversible acts ⚠️ common practice; no source read for this row | bar with a threshold line and a "reached / not reached" mark |
| Consensus | decision stands only if everyone agrees or nobody blocks | small trusted groups, high commitment needed | stance matrix per person (agree/abstain/disagree/block), block highlighted. Loomio offers "consensus" as a proposal template [S10] |
| Consent / sociocracy | decide when no reasoned, paramount objection remains; objections improve the proposal; "good enough for now, safe enough to try" [S27] | team decisions that can be revised, roles, policies | list of objections with reasons, status per objector, resolved/open. Loomio: consent or objection, objector must give a reason [S12] |
| Systemic consensing (resistance scoring) | each person gives every option 0–10 resistance, "carry on as before" is always an option; lowest total wins; high single values are heard, not vetoed [S13] | conflicting interests, searching for the proposal the group can carry, hierarchy-sensitive groups (hidden collection recommended [S13]) | table or bars of total (or mean for varying group size) resistance per option with the maximum (people x 10) as scale, passive option as reference line; per-person dot strip to show outliers (the dot strip is my addition; the source shows a two-column table) |
| Approval voting | tick every option you accept; most ticks wins [S37] | many candidates, vote-splitting worry, simple counting | bars of approvals; cutoff dilemma and bullet voting are known weak spots [S37] |
| Score voting / range | rate each option on a scale; highest total or mean wins | measuring strength of support | mean with spread (box or strip) per option. Loomio Score compares strength of support [S10] |
| STAR (score then automatic runoff) | score 0–5; top two by total go to a runoff decided by who scored higher on more ballots [S38] | single winner where strength and majority both count | score bars plus a head-to-head pair for the finalists |
| Ranked: Schulze | rank options; strongest chain of pairwise preferences decides; elects the majority-preferred option if one exists; satisfies Condorcet, Smith, clone independence; used by Debian, KDE e.V., Kubernetes, German/Swedish Pirate Parties and others [S39] | single winner among many options, organisations with a technical culture | pairwise-win matrix (heatmap) and final order |
| Ranked: instant-runoff (IRV) | repeatedly drop the option with fewest first choices and move its ballots on [S40] | single-winner public elections where simple rule counts | round-by-round flow (sankey or stacked bars). Known to be non-monotonic and prone to centre squeeze [S40] |
| Ranked: Borda | points for each position, sum wins [S41] | quick preference order, awards, ranking lists | points bars. Open to clone and burying tactics [S41] |
| Ranked: STV | ranked ballots, transfer of surplus and eliminated votes, several winners [S10 names the method in Loomio] | committees, boards, proportional representation | round table with quota line and transfers |
| Quadratic voting | credits budget; n votes cost n² credits, so intensity counts but spreading is cheaper [S28] | prioritising many items where passion differs; needs equal artificial currency and sybil resistance, otherwise cheap fake identities break it (the source does not discuss sybil attacks; the link is my inference) | bars of net votes per option, plus a "credits spent" view |
| Dot voting / allocation | fixed points to distribute freely | workshop prioritisation | stacked bar of points per option. Loomio "Allocate" [S10] |
| Delegation / liquid democracy | vote yourself or hand your vote to a proxy, per topic or all, passed on in chains, revocable [S42]. Risks: power piling up with few people, delegation cycles, weaker correctness in some cases [S42] | long-running bodies with many topics and low individual attention | delegation graph with weights, and a table "direct votes vs. carried votes" per delegate; LiquidFeedback offers delegation per unit, area and issue [S23] |
| Deliberative clustering | participants vote agree/disagree/pass on short statements written by others; a map separates opinion groups; statements that all groups accept surface as common ground [S15, partial] | contentious topics, many participants, finding common ground rather than a winner | 2-D scatter of participants coloured by cluster, plus a ranked list of statements with agreement per cluster. ⚠️ The use of PCA and clustering is from memory of the Polis paper; the pages I read did not mention it |
| Sense check / temperature | quick pulse: looks good / question / concerned [S12] | before a formal proposal | three-segment bar |
| Meeting (availability) poll | each person marks free times; most overlap wins [S10, S16] | scheduling | participants x slots grid with counts per column |
| Open ranking of ideas (Q&A upvote) | audience questions ranked by upvotes [S17] | events | sorted list |

Not found or not read: ranked pairs, Kemeny, Copeland, majority judgment, consensus-by-fist-of-five (⚠️ known practice, no source read), "Gradients of agreement" (⚠️ same), Condorcet-with-delegation hybrids.

## 4. Open surveys without login, and abuse protection

Goal from the owner: surveys that need no login, while one party cannot post a million answers.

Core truth (my analysis, consistent with [S4], [S32]): without an identity, you cannot tell two answers from different people apart from two answers by one person. Every technique therefore does one of three things: (a) make each answer cost something, (b) tie answers to a scarce thing (a device, a token, a person), (c) detect and discount fakes afterwards. No technique gives "one human, one answer, no identity, no third party" for free. Choose the strength to match the stakes.

### 4.1 Technique list

| Technique | How | Strength | Weakness | Privacy cost | Self-hostable, no third party? | Used by (as far as read) |
|---|---|---|---|---|---|---|
| Rate limit per IP / subnet | cap submissions per address in a time window | cheap, stops naive floods | shared addresses (NAT, campus, mobile carrier) block honest users; botnets or IPv6 rotate addresses | IP is stored or hashed at least briefly | Yes | Surveti flags duplicate IPs in a window [S25]; SurveyMonkey can block or allow IPs [S43] |
| Global rate limit / backpressure | cap total submissions per minute per survey, slow down when busy | protects the server and the tally from floods | an attacker can still fill the global quota and starve honest users | none | Yes | ⚠️ general practice, no source read |
| Proof of work (hashcash type) | client must find a hash with leading zero bits before submit; cost doubles per extra bit, check is one hash [S44] | no third party, no tracking, cost scales with attack volume | hardware gap: phones vs. GPUs/ASICs; attacker with cloud pays little per answer; hurts old devices [S44] | none | Yes | ALTCHA (silent PoW, MIT widget, no cookies, no fingerprinting per its own claims) [S30]; mCaptcha (adaptive PoW, AGPL, Rust, no stable release yet) [S31] |
| Adaptive difficulty | raise PoW difficulty when traffic is high | honest users unaffected in calm times; about 2 s under attack per mCaptcha [S31] | attacker who starts slowly and ramps up; global difficulty harms everyone during attack | none | Yes | mCaptcha [S31] |
| Per-device token (cookie / local storage) | after submit, set a marker; refuse second submit | stops casual repeats | removed by clearing storage, other browser, private window [S4] | low (a marker) | Yes | Qualtrics "prevent multiple submissions" [S4] |
| Signed one-time link / invite token | each invitee gets a unique code, marked used | strong one answer per code | needs a list of people, so not "open"; sharing tokens | token links answer to invitee unless separated | Yes | LimeSurvey tokens (uses left, valid-from/until, "completed"); anonymous surveys keep no link between token and answer [S3b] |
| Public registration by email | visitor enters email, gets token | filters most bots; one per mailbox | disposable and plus-addressed mailboxes; email is stored | email known to organiser (token table) | Yes (own mail) | LimeSurvey [S3b] |
| Account required | answers tied to sign-in | strong | not open; identity cost | high | Yes (own accounts) | Google Forms "limit to 1 response" forces Google sign-in [S6] |
| Shared password | one password for all respondents | keeps casual outsiders away | no guess limit in Qualtrics, shared, leaks [S4] | none | Yes | Qualtrics [S4] |
| Classic captcha (image / checkbox) | human test | stops simple bots | solvable by humans-for-hire and increasingly by AI; accessibility and burden [S45] | depends on provider | Only self-hosted variants | LimeSurvey [S3b] (provider ⚠️ not stated on read page) |
| reCAPTCHA v3 score | invisible behavioural score; flag if under 0.5 [S4] | no user effort | third party (Google), tracking; threshold tuning | high | No | Qualtrics bot detection [S4] |
| Cloudflare Turnstile | non-interactive browser checks including PoW and API probes; widget can be used without proxying traffic through Cloudflare [S46] | friction-free for most | third-party service and browser-signal collection (Cloudflare says only data needed for security is processed [S46]) | medium, claims minimal | No | Surveti [S25]; Turnstile docs [S46] |
| Privacy Pass / Private Access Tokens | an attester vouches the client is real, an issuer signs a blinded token, the origin verifies without learning who [S32, S33]. Four roles can be split across parties (Client, Attester, Issuer, Origin) | unlinkable proof of "real device/person"; reduces captchas [S33] | needs attesters and issuers; PAT on iOS 16 / macOS Ventura as stated by Apple [S33]; tokens can be hoarded and shared; concentration of power in few issuers [S32] | low by design | Protocol yes; useful attesters are mostly platform vendors ⚠️ | Cloudflare, Fastly as issuers [S33]; no survey tool seen |
| Attestation by own community (blind-signature token) | a trusted party (group admin) issues each member one blind-signed token, spent when answering | one answer per member, answers unlinkable to member (design idea based on [S32]'s mechanism; blind-signature use is from [S33] only for RSA type 2) | needs a member list; admin must be trusted not to issue extras | low | Yes | none in surveys seen ⚠️ |
| Statistical anomaly detection | speed vs. median (Qualtrics: more than 2 SD from median, needs 100+ responses), straightlining (3 matrices and 80 %), gibberish text, duplicates [S4] | catches sloppy mass fakes; keeps open access | clever attackers pass; flags change as data grows [S4]; false positives | low (timestamps, answer patterns) | Yes | Qualtrics [S4]; Surveti with manual accept/reject review [S25] |
| Volume anomaly | sudden burst of answers with similar content, same timing, same user-agent | flags the "million answers" attack in the tally | late; needs rollback ability | low | Yes | ⚠️ own proposal, no source |
| Honeypot / time trap | hidden field or too-fast submit | cheap | defeated by targeted bots | none | Yes | mentioned in the Qualtrics list I asked for, but the page I read did not cover it ⚠️ |
| Web of trust / social graph | members vouch for each other; weight answers by trust | resists fake identities if graph is honest | hard to confirm that links are not sybils; weak against small attacks [S47] | reveals social links | Yes | no survey tool seen; see proof-of-personhood [S47] |
| In-person pseudonym party | people meet, each gets one credential | one person one credential | inconvenient; hard to federate [S47] | low | Yes | encointer [S47] |
| Government/strong ID | verified identity then anonymised | strong | surveillance and exclusion risk; trusting the verifier [S47] | high | No | Decidim has "verification and authorization" [S21]; mechanisms ⚠️ not read |
| Biometric proof of personhood | iris scan with zero-knowledge proof | strong uniqueness | hardware, scale, privacy worry [S47] | high | No | World ID, Humanode [S47] |
| Credit weighting (cost per vote) | quadratic cost with a budget [S28] | reduces gain from one huge push, not from many identities | sybils still multiply the budget | none | Yes | not an abuse tool alone |

### 4.2 What tools actually use (from what I read)

- LimeSurvey: tokens (single use by default, validity window), public registration by email, captcha on registration/save/load forms; anonymous mode severs token and answer [S3b]. The read page did not describe IP or cookie limits ⚠️.
- Qualtrics: cookie, reCAPTCHA v3 score, flags for duplicates, speeders, straightlining, gibberish; password with no guess limit [S4].
- Google Forms: signed-in limit only [S6].
- Surveti (product): Turnstile at the door plus scoring and a review queue [S25].
- Rallly, Framadate: open links; Framadate relies on secret links for editing/deleting a poll [S16, S20]. I did not find a stated anti-abuse mechanism on those pages ⚠️.
- Mastodon polls: votes are counted per option if not previously voted for that option; identity is the account [S36].
- Helios: voter roll, one-time password per voter by email, login before casting [S14].

### 4.3 What can be done with no third-party service

All of: global and per-subnet rate limits; self-hosted PoW with adaptive difficulty (ALTCHA, mCaptcha both self-hostable per their claims [S30, S31]); signed one-time links; email registration with own mail server; device marker; statistical and volume anomaly checks with a review queue; own-community blind-token issuance (design idea above); web of trust inside a group.

Cannot be done without a third party: proving "this is a unique real human" on a wide-open public link. The cheapest honest approach (my recommendation as a hypothesis to test): layered. (1) adaptive PoW plus global rate limit as the gate, (2) device marker as a soft limit, (3) every answer stored with a quality score, not deleted, (4) result shown in two numbers: "all answers" and "answers passing checks", with the gap itself displayed as a signal, (5) optional upgrade of the survey to token or blind-token mode when stakes are higher. Stakes decide: a quick lunch poll needs (1) only; a binding vote needs tokens.

A "million answers" attack is mostly a volume attack. Hashcash's economic point is that cost scales with attack size [S44]; but note that one cloud GPU is cheap, so PoW only slows, it never proves uniqueness. The hash must also bind to the survey and a server nonce so work cannot be reused across surveys [S44 mentions checks for date, recipient and reuse].

## 5. Escalation (small group widening to parent groups, carrying results)

Result: **no tool found that does this.**

What exists close to it:
- Loomio: groups can have subgroups with own membership and admins. Members of the parent group can optionally read private subgroup threads without joining and without voting rights. The subgroup page does not describe moving or escalating a discussion or poll to the parent [S34]. The sociocracy page says a person belonging to both a circle and its parent can represent one in the other, but says no formal escalation process is described; subgroups require the Pro plan [S12b].
- Sociocracy method: double linking and a higher circle made up of representatives for decisions affecting several circles [S27]. This is process, not software.
- LiquidFeedback: organisational units, subject areas, delegation per unit/area/issue [S23, S5]. Whether an initiative can be lifted to a larger unit was not stated on the page read ⚠️.
- Decidim: participatory spaces (processes, assemblies, initiatives) [S21]. Moving a proposal across spaces: not found ⚠️.
- Pol.is: per-conversation, no hierarchy found [S15].

Idea (my design inference, not found elsewhere): an escalation step on a decision: small group decides or fails to decide, then the decision (with votes, objections, resistance values, discussion links) is offered upward as a pre-filled input to the parent; the parent group sees "child group result" as a labelled block next to its own vote and can adopt, override or ask for more; the child result stays fixed and signed. For systemic consensing this fits well: resistance sums from the child become the starting information of the parent.

## 6. Gaps in open source

Found in closed tools, not found in open ones I read (my reading may have missed projects):
1. Live audience layer: instant results display, Q&A with upvote and pre-moderation, quizzes with leaderboard, word cloud (Slido [S17], Mentimeter [S18]). Open-source options were not found in this session ⚠️ (I did not search).
2. Response quality scoring with a review queue (Qualtrics [S4]; Surveti [S25]; ⚠️ whether Surveti is open source is unclear).
3. Bot detection score built in (Qualtrics reCAPTCHA v3 [S4]) — not privacy-friendly; the idea is useful, the means are not.
4. Forms that complete a transaction (payment, sign, approval) (Jotform [S24]).
5. One question per screen with logic jumps and hidden fields (Typeform [S26], stale source ⚠️).
6. Large integration markets (Slido inside Webex [S17]).

Ideas I did not find anywhere (hypotheses; absence of evidence only):
1. Open, login-free poll with built-in layered abuse protection and a displayed gap between "all" and "checked" answers (section 4).
2. A decision-method switch on the same ballot: collect once, show the result under several methods (e.g. same rankings shown under Schulze, IRV, Borda), exposing when methods disagree. Each method's page I read mentions failure modes that make this informative [S39–S41].
3. Systemic consensing as a first-class method with passive option, outlier view and "re-run after improvement" loop. Only the method description and an "SK-App" mention were found [S13].
4. Escalation with carried-over results (section 5).
5. Quadratic voting inside a small survey tool with sybil-aware credits (QV mentioned for caucus and grants only [S28]).
6. Federation of polls between servers beyond microblog polls (Mastodon polls exist [S36]); a general survey with signed answers across servers: not found.
7. A purpose field on every survey ("what is this for", decision vs. opinion vs. data) that selects sensible defaults: anonymity, result visibility, method. Loomio's templates are the nearest idea [S11].
8. Cross-method result charts as shared, standard components (section 3 column).
9. Offline-first collection for non-field uses (small co-ops) — ODK has offline for fields only [S7].

## 7. Standards

### 7.1 What I read and what I did not

| Standard | Read | Not read |
|---|---|---|
| ActivityStreams 2.0 Vocabulary (W3C Recommendation 23 May 2017), `Question` [S48] | `Question` definition, `oneOf`/`anyOf`/`closed`, examples, reply-as-answer section; the Mastodon extension page [S36] | the AS2 Core spec; JSON-LD processing; second half of the vocabulary page (24k characters after 100k offset were partly read, no mention of `votersCount` there) |
| FHIR Questionnaire (HL7 FHIR, version string on page: R5 5.0.0, maturity level 5, STU) [S29]; QuestionnaireResponse [S29b] | element list, `enableWhen`, `answerConstraint`, `answerOption`, QuestionnaireResponse elements; first ~200k characters of a 312k page | full `item.type` value set (page showed group, display, boolean, decimal, integer, date, dateTime, "+"); SDC (Structured Data Capture) implementation guide; extensions list; the fetch tool reported a "changes from R4" note that `choice`/`open-choice` were removed and `question`/`coding` added ⚠️ this needs checking against the current build, I cannot confirm which release that note belongs to |
| IMS/1EdTech QTI 3.0 (Final Release, issued 1 May 2022, spec version 3.0, document version 1.0) [S49] | overview page only | the information model, XML binding, interaction list, response processing, scoring |
| DDI-Lifecycle: 3.3 is "latest", 4.0 is an upcoming development version (docs index, no dates given) [S50]; 4.0 `QuestionItem` model page [S51] | QuestionItem structure (question text, intent, response domain, cardinality, parameters, estimated response time, references to variables and concepts) | 3.3 pages (the first URL guess returned 404), instruments, control constructs (Sequence, IfThenElse etc.), DDI-Codebook, DDI-CDI, XML or other bindings, any release dates |
| ODK XForms spec 1.0.0 (2019-11-11), subset of W3C XForms 1.0 plus additions [S9] | overview page | the full spec; XLSForm |

### 7.2 Assessment

Purposes the single interface must cover (from sections 1 and 3): choose among options with a method, collect arbitrary structured answers, collect over open links, federate.

| Candidate | What it is | Fit for a "decision or poll" | Fit for "questionnaire/data collection" | Weak points |
|---|---|---|---|---|
| AS2 `Question` | tiny activity vocabulary: a question with `oneOf` (exclusive) or `anyOf` (inclusive) options, `closed`, answers as replying objects; result may be described via `result` [S48, S36] | very good for choose-one/choose-many; already federates; Mastodon's real-world extension adds `endTime`, `votersCount`, and per-option reply counts [S36] | none: no typed questions, no branching, no scales | no ranking, score, allocate, resistance values; no secrecy model; a vote is a public reply Note, so secret ballots need extension; "must not have both oneOf and anyOf" [S48] |
| FHIR `Questionnaire` + `QuestionnaireResponse` | organised collection of questions with order, grouping, constraints, `enableWhen` logic, answer options, typed answers; response separated from definition and carries only answers [S29, S29b] | medium: can express choice items | strong generic form model with logic; response has optional `author`, `source`, `subject`; anonymity not explicitly addressed on the read page ⚠️ [S29b] | health-care vocabulary (subject types, patient), heavy; maturity "trial use" [S29]; no decision-method concept |
| QTI 3.0 | data model for items and tests with scoring and response processing, results reports [S49] | scoring and correct answers are the focus; ill fitting for opinions | good for graded questions | exam centric; interaction list not read |
| DDI-Lifecycle | metadata model for survey design and data documentation: question items with intent, text, response domains, links to variables and concepts [S51] | none | best in class for documenting research surveys and reuse of questions, variables | metadata for research archives, not a runtime/wire interface; large; 4.0 still in development [S50] |
| ODK XForms | form definition with branching, validation, calculations, repeats [S7, S9] | none | strong for field collection, simple authoring via XLSForm | W3C XForms subset, XML; no decision methods |

My judgement (inference from the above, not an official claim):
- No single standard covers everything. The cleanest layered answer is: **AS2 `Question` as the outer envelope and federation layer** (it already exists in the same world as FreeSynergy's ActivityPub-style identity, and Mastodon proves the pattern [S36]), with an **extension vocabulary for methods and typed answers** (ballot method, score ranges, rank, allocation, resistance), and **FHIR `Questionnaire`'s item/`enableWhen` structure as a reference for the typed-questionnaire part**. DDI is the better reference for metadata (question intent, response domain, link to concept) and for export to research archives, not as the runtime interface. QTI is relevant only if graded quizzes become a goal.
- Fit gaps to confirm before deciding: (a) AS2 secret-ballot model, (b) whether FHIR's current `item.type` set includes what we need, (c) licence/IP terms of each spec for reuse of terms (not checked), (d) DDI 3.3 and instrument/control constructs.

## Sources (all retrieved 2026-11-06)

- [S1] LimeSurvey repository README: https://github.com/limesurvey/limesurvey
- [S2] Formbricks repository README: https://github.com/formbricks/formbricks
- [S3b] LimeSurvey manual, survey participants: https://www.limesurvey.org/manual/Survey_participants
- [S3] (reserved; not used)
- [S4] Qualtrics survey protection: https://www.qualtrics.com/support/survey-platform/survey-module/survey-options/survey-protection/ ; response quality: https://www.qualtrics.com/support/survey-platform/survey-module/survey-checker/response-quality/
- [S5] LiquidFeedback feature list: https://liquidfeedback.com/en/full-feature-list.html
- [S6] Google Forms settings help: https://support.google.com/docs/answer/2839588
- [S7] ODK, Wikipedia: https://en.wikipedia.org/wiki/Open_Data_Kit
- [S8] KoboToolbox KPI repo: https://github.com/KoboToolbox/kpi (the Wikipedia and kobotoolbox.org fetches failed with 404 and 403)
- [S9] ODK XForms spec: https://getodk.github.io/xforms-spec/
- [S10] Loomio, poll types: https://www.loomio.com/docs/en/user_manual/polls/proposal_types
- [S11] Loomio, poll templates: https://www.loomio.com/docs/en/user_manual/polls/poll_templates
- [S12] Loomio sociocracy page: https://www.loomio.com/sociocracy ; [S12b] same page, escalation/subgroup plan note
- [S13] Systemic consensing, Impact Institut: https://impactinstitut.com/widerstandsabfrage/ ; also found in search, not fully read: https://www.gemeinschaftskompass.de/wp-content/uploads/2023/04/Systemisches-Konsensieren.pdf
- [S14] Helios Voting, Wikipedia: https://en.wikipedia.org/wiki/Helios_Voting ; original paper (PDF, fetch returned unreadable stream, not read): https://www.usenix.org/legacy/event/sec08/tech/full_papers/adida/adida.pdf
- [S15] Pol.is: https://en.wikipedia.org/wiki/Pol.is ; https://github.com/compdemocracy/polis
- [S16] Rallly repository: https://github.com/lukevella/rallly
- [S17] Slido: https://en.wikipedia.org/wiki/Slido ; https://www.slido.com/features
- [S18] Mentimeter: https://en.wikipedia.org/wiki/Mentimeter ; https://www.mentimeter.com/features
- [S19] Doodle: https://en.wikipedia.org/wiki/Doodle_(website)
- [S20] Framadate: https://framagit.org/framasoft/framadate/framadate (archived per page)
- [S21] Decidim: https://en.wikipedia.org/wiki/Decidim ; https://github.com/decidim/decidim
- [S22] OpenSlides: https://github.com/OpenSlides/OpenSlides
- [S23] LiquidFeedback (same as S5), plus Wikipedia on Schulze use by Pirate Parties: see S39, S42
- [S24] Jotform: https://www.jotform.com/help/
- [S25] Surveti fraud detection: https://www.surveti.com/features/fraud-detection
- [S26] Typeform (2018 Wikipedia disambiguation page): https://en.wikipedia.org/wiki/Typeform
- [S27] Sociocracy: https://en.wikipedia.org/wiki/Sociocracy
- [S28] Quadratic voting: https://en.wikipedia.org/wiki/Quadratic_voting
- [S29] FHIR Questionnaire: https://hl7.org/fhir/questionnaire.html ; [S29b] https://hl7.org/fhir/questionnaireresponse.html
- [S30] ALTCHA: https://altcha.org/
- [S31] mCaptcha: https://github.com/mCaptcha/mCaptcha
- [S32] RFC 9576 Privacy Pass architecture (June 2024, Informational): https://www.rfc-editor.org/rfc/rfc9576.html
- [S33] Apple, Private Access Tokens: https://developer.apple.com/news/?id=huqjyh7k
- [S34] Loomio subgroups: https://www.loomio.com/docs/en/user_manual/groups/subgroups ; privacy search snippet: https://www.loomio.com/docs/en/user_manual/groups/settings/privacy
- [S35] Nextcloud Forms: https://github.com/nextcloud/forms
- [S36] Mastodon ActivityPub spec: https://docs.joinmastodon.org/spec/activitypub/
- [S37] Approval voting: https://en.wikipedia.org/wiki/Approval_voting
- [S38] STAR voting: https://en.wikipedia.org/wiki/STAR_voting
- [S39] Schulze method: https://en.wikipedia.org/wiki/Schulze_method
- [S40] Instant-runoff voting: https://en.wikipedia.org/wiki/Instant-runoff_voting
- [S41] Borda count: https://en.wikipedia.org/wiki/Borda_count
- [S42] Liquid democracy: https://en.wikipedia.org/wiki/Liquid_democracy
- [S43] SurveyMonkey collector options: https://help.surveymonkey.com/en/surveymonkey/send/collector-options/
- [S44] Hashcash: https://en.wikipedia.org/wiki/Hashcash
- [S45] Proof of personhood (online Turing tests section): see S47
- [S46] Cloudflare Turnstile docs: https://developers.cloudflare.com/turnstile/
- [S47] Proof of personhood: https://en.wikipedia.org/wiki/Proof_of_personhood
- [S48] W3C Activity Vocabulary (Recommendation, 23 May 2017): https://www.w3.org/TR/activitystreams-vocabulary/ (version URL https://www.w3.org/TR/2017/REC-activitystreams-vocabulary-20170523/)
- [S49] 1EdTech QTI 3.0 overview: https://www.imsglobal.org/spec/qti/v3p0/oview
- [S50] DDI product documentation: https://docs.ddialliance.org/DDI-Lifecycle/
- [S51] DDI-Lifecycle 4.0 QuestionItem: https://docs.ddialliance.org/DDI-Lifecycle/dev/model/item-types/QuestionItem/

Notes on weak sourcing: most tool facts come from Wikipedia or README pages passed through a summariser. Closed-tool feature claims are from a single marketing or help page each. Where a table cell has no `[Sn]`, it is my analysis. Items to verify before relying on them: Loomio "hide results until closed"; LimeSurvey IP/cookie limits; whether a free "SK-App" exists and its licence; Polis PCA/clustering details; FHIR item.type current set; DDI 3.3 instrument constructs; Helios paper details; Google Forms/Microsoft Forms/Tally abuse controls.
