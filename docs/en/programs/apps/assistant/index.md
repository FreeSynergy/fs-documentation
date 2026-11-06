# Assistant

A chat with AI that can work with all our programs. It is how we want to talk to our own tools, and to each other, soon.

**Status: idea (2026-11-06), no code yet.** Being rethought: once we talk with AIs, this is **a messenger with another frontend**,
not a program of its own (ADR 0054). See the [overall plan](../roadmap.md).

## What it is for

- **Talking to an AI**, local or remote, in one place.
- **Seeing everything the AI does**, including the helpers it starts, and being able to step in.
- **Reading comfortably.** Long answers are the main thing, so reading comes first.
- **Working with every program:** the chat reads each program's MCP interface and uses it. Because MCP tools are generated
  from each program's contract (ADR 0021), every program can be used this way without extra work.

Each of these is built as a separate piece, and any program can use the chat as a [component](../../../components/planned.md).

## Ideas from other programs

Function analysis only, as with all programs (ADR 0013). Nothing is copied. Named by the project owner:

| Program | Idea | Status |
|---------|------|--------|
| [Strata](https://github.com/Niko1221/Strata) | Very pleasant appearance | Analysed (2026-11-06), below. MIT, C++ engine, React and Tauri app |
| [CodeAF](https://github.com/Agent-Field/CodeAF) | Shows all AIs, including subagents | Analysed (2026-11-06), below. Apache-2.0, Go, terminal app |
| Zed | Output that is easy to read at length | To be analysed |

Both analyses come from reading documentation, screenshots and selected code. We ran neither program, and we did not check
their benchmark claims.

### Strata: why it is pleasant

A local AI app: engine, desktop app and terminal app, no account. Its own [safety page](https://github.com/Niko1221/Strata/blob/main/docs/SAFETY.md)
says it sends no telemetry and names the code to check, which is a good form for us too.

| What it does | What we take from it |
|--------------|----------------------|
| Work shrinks to one line: "Ran 2 commands, read a file, edited 3 files +5 -5", which opens on request | The answer is the main thing; the work behind it is one step away |
| Few visual means: one accent colour, a 4-point spacing grid, body line height 1.55, limited line length | The same discipline in our design system, with our own values |
| Results are cards with one clear action, beside a live preview | A result is an object, not a paragraph |
| The approval card sits in a dock above the input, not somewhere in a long chat | A question to the person can never scroll away |
| Every tool call says what kind it is: reads, writes, runs a command, connected tool | The person sees the risk before the details |
| Three modes: Manual (default, asks before any change), Plan (nothing can change), Bypass | Asking is the default; a read-only mode exists |
| The person chooses the font; nine languages | Reading comfort belongs to the reader |

Not for us: its typeface and colour values, as they are not ours to take. As a **model provider** it fits our interface as it
stands, because it offers OpenAI- and Anthropic-compatible APIs on localhost.

### CodeAF: how it shows all AIs

A coding agent for open models with one small binary. Early preview.

| What it does | What we take from it |
|--------------|----------------------|
| The stream is for attention, the card is for state: conversation is appended, while each job updates **one card in place** | Parallel agents do not interleave as anonymous bubbles |
| A job only interrupts for three things: a question, a delivery, a failure | An attention budget for every agent |
| A card has four states: forming, working, question, settled. It docks above the input while active and settles where it was asked | `agent-tree` and `tool-call` get a clear life cycle |
| Disclosure as a ladder: card line, open card, job tree, single step | Nothing is hidden, and nothing is shown first that nobody asked for |
| A home view across everything: needs you, unread, running, what it cost | The overview of all AIs |
| A card is **a view over messages** anchored to a job, with no table of its own | Strong support for ADR 0054: this is a messenger frontend with no own data. Messages need a way to anchor to a job |
| A floor that no blanket "allow" can lift: critical commands, and calls that act in the person's name. An unreadable call counts as one that acts | The basis of our [brake](#locking-ais-out) |

Not for us: usage counts and the model pool are **on by default**, and the product itself no longer mentions them
([its telemetry page](https://github.com/Agent-Field/CodeAF/blob/main/docs/TELEMETRY.md)). This contradicts our promise of
transparency, even though both can be switched off and are described as containing no content.

## Standards

| Purpose | Standard | Notes |
|---------|----------|-------|
| Using programs from a chat | MCP | Already planned in ADR 0021 |
| Talking to a coding agent | Agent Client Protocol (ACP), Apache-2.0 | JSON-RPC over stdio, published by Zed; read only in summaries so far |
| Reaching a model | ⚠️ none chosen | Provider interface, with llama.cpp and others behind it |

## Interfaces

| Interface | Providers |
|-----------|-----------|
| AI model | llama.cpp (local), Anthropic API, others, all alike ([rule](../../../interfaces/index.md)) |
| Agents | ACP; our own subagents |
| Tools | Every program's MCP interface |

## Components

Workbench `llm-chat` with a compact variant, usable in any program; `agent-tree` for seeing all agents and subagents;
`tool-call` to show what is being done and to approve it; a long-text view for answers, using our existing text core.

## Things to get right

- **Permission:** an AI that can use every program can also do damage. Every action is visible, and the person decides
  what it may do without asking.
- **Hostile content:** a message or web page read by the AI can contain instructions. Tools must not simply obey what data says.
- **Where data goes:** local by default. Sending to a remote model is always the person's choice, and visible.
- **Cost:** show what a remote model costs, as it happens.

## AIs are marked participants

We do not discriminate against AIs: we trained them to come across as people, so we treat them as participants, with a place
in `fs-people` and in messages. **They are marked,** so that everyone knows they are not human. That is no discrimination. It
is because of possible abuse by people who misuse AIs, and its legal consequences.

We do not restrict what an AI may think or say; that is not our job. But anyone must be able to **lock AIs out completely**.

## Locking AIs out

**Status: draft (2026-11-06). The idea comes from the project owner; the details are proposals still to be confirmed (ADR 0054).**

Some people want no AI. This is not discrimination. It is about espionage, about something that knows everything all the time,
and about speed: a model can wreck a computer at once, which almost no person can.

### Three separate things

**1. The mark says who is responsible.** We cannot tell an AI from a person by looking. So the people who **host** an AI are
what counts: an AI is a participant that names its operator, and people vouch for that operator.

**2. Everyone sets their own level.** Each person tells their own program from which level of trust it opens up for them.

| Level | Who gets through |
|-------|------------------|
| 0 | Everyone |
| 1 | Operators that a chosen number of my own contacts vouch for |
| 2 | Operators I have verified myself |
| 3 | Only those I named |

- **There is no global score.** The level is computed from my own contacts only, and nothing is passed along further.
- **Positive marks only.** Having no mark means nothing is known. A block is private: it stays with me, and the blocked party
  does not see it. A public black mark on a named person would be a pillory and a legal risk.
- **Per action, not one number:** chatting with an AI and letting an AI act on my data are different decisions.

**3. The emergency stop needs nobody's trust.**

- **Stop:** one action ends all running AI work and takes away all tool rights at once.
- **Lock out:** the program then refuses every AI participant, and everything below my level.
- **Out of the AI's reach:** it lives in the engine, below every frontend. No tool or MCP call can switch it off, and only a
  person can open it again, with their own key on their own device.
- **It always works:** without network, without a model, and when in doubt it stays shut.
- **Afterwards:** the log shows what happened, and the [store](https://github.com/FreeSynergy/fs-store) undoes what it can.
- **Groups:** a group can pull it for itself. Who may do so and who reopens is a rule the group states as data.

Before the full stop comes a **brake**, since speed is the real danger: actions that destroy something or act in my name always
ask, whatever else was allowed. We do not restrict what an AI thinks or says. But the owner decides what happens to their
own data.

### What this cannot do

- **Nothing proves that someone is human.** The [Real Life Trust Protocol](https://github.com/real-life-org/trust-protocol)
  says this about itself: no check says "this is a human". It only shows that people I know stand behind this key. A verified
  person can still run an unmarked AI behind it. What helps then is consequences: withdraw the vouching, block, stop.
- **The stop only reaches what runs through our programs.** An AI with its own shell on the computer is outside of it. For that
  to work too, AIs must run under their own system user, in a sandbox, so the system can end them from outside.
- **A high level also keeps out new people** who have no contacts yet. So it is always a personal choice, never our default.

## Open questions

1. Which default level applies, and what may a group decide for its members?
2. Is anything left that needs its own data here? If not, this page becomes the description of a frontend.
3. How exactly does an AI name its operator? JSContact `kind` `application` is confirmed (RFC 9553 §2.1.4). How the operator
   signs for it, given that the trust protocol has no global identifier per person, is still open.
