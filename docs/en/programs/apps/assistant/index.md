# Assistant

A chat with AI that can work with all our programs. It is how we want to talk to our own tools, and to each other, soon.

**Status: idea (2026-11-06), no code yet.** Being rethought: once we talk with AIs, this is **a messenger with another frontend**,
not a program of its own (ADR 0054). See the [overall plan](../roadmap.md).

## What it is for

- **Talking to an AI**, local or remote, in one place.
- **Seeing everything the AI does**, including the helpers it starts, and being able to step in.
- **Reading comfortably.** Long answers are the main thing, so reading comes first.
- **Working with every program:** the chat reads each program's MCP interface and uses it. MCP tools are generated from each
  program's contract (ADR 0021). This works, but the contracts need a few marks first ([below](#mcp-the-contract-as-tools)).

Each of these is built as a separate piece, and any program can use the chat as a [component](../../../components/planned.md).

## Ideas from other programs

Function analysis only, as with all programs (ADR 0013). Nothing is copied. Named by the project owner:

| Program | Idea | Status |
|---------|------|--------|
| [Strata](https://github.com/Niko1221/Strata) | Very pleasant appearance | Analysed (2026-11-06), below. MIT, C++ engine, React and Tauri app |
| [CodeAF](https://github.com/Agent-Field/CodeAF) | Shows all AIs, including subagents | Analysed (2026-11-06), below. Apache-2.0, Go, terminal app |
| [Zed](https://github.com/zed-industries/zed) | Output that is easy to read at length | Analysed (2026-11-06), below. GPL-3.0-or-later for the agent panel, Rust, code editor |

All three analyses come from reading documentation, screenshots or selected code. We ran none of these programs, and we did not
check their benchmark claims. For Zed we read its documentation, default settings and agent panel code, and saw no screenshots.

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

### Zed: how it keeps long output readable

A code editor with an agent panel. Its own agent and outside agents (over ACP) share one thread view.

| What it does | What we take from it |
|--------------|----------------------|
| Content is limited to a maximum width and centred in a wide panel, 850 pixels by default, and this can be switched off | Every long-text view has a line-length limit |
| The AI's text and the person's text each have their own font and size setting | Reading comfort belongs to the reader, and it is clear at once who is speaking |
| Reasoning is separate from the answer. By default it is open while it streams and folds when it ends. Three other settings exist: preview, always open, always closed | The answer comes first, and the reasoning stays one step away. A message needs its own place for reasoning |
| Edits and terminal output are cards. A setting per card type says if they start open | The reader decides how much work to see. Strata starts closed and Zed starts open, so this is a choice, not a fixed rule |
| A long thread is a thing to move through: buttons to the start and the last prompt, keys from prompt to prompt, scrolling from the input box, and search inside the thread | The person's own messages are the table of contents |
| A bar above the input gathers changed files, the plan, queued messages and open permission questions | Same result as Strata: a question can never scroll away |
| All changes collect in one review view, and each change is accepted or rejected on its own | A result is an object that can be reviewed outside the talk |
| A shortened context appears as an entry that opens to show the summary | Nothing is hidden, even when the AI forgets |
| One answer can be copied, and the whole thread opened as a Markdown file | Text can always leave the view |
| A subagent gets a card with a small window on its latest entries (8 at most) | One more form for `agent-tree` |
| Surprising Unicode in a sandbox permission prompt blocks "allow" until it is acknowledged | A question must show what it really asks |

Not for us: what only makes sense in an editor, such as following the agent from file to file. Its limits are also a warning.
Fixed rules cover only recursive deletion of a few central folders in its terminal tool, and a global "allow" removes most other
questions. Its sandbox covers only its own agent, not outside agents. Our [brake](#locking-ais-out) must reach further.

## Standards

| Purpose | Standard | Notes |
|---------|----------|-------|
| Using programs from a chat | Model Context Protocol (MCP), revision 2026-07-28 (current) | Planned in ADR 0021. Works with limits, [see below](#mcp-the-contract-as-tools) |
| Talking to a coding agent | Agent Client Protocol (ACP), protocol version 1 (stable), Apache-2.0 | JSON-RPC 2.0, stdio only so far. Version 2 is a draft. Governance is interim, by Zed and JetBrains. [See below](#acp-coding-agents-in-the-messenger) |
| Reaching a model | ⚠️ none chosen | Provider interface, with llama.cpp and others behind it |

## What ACP and MCP mean for us

Read from the specifications and documentation (2026-11-06), **not run**. Nothing here was tested against a real agent or client.

**The main finding:** neither protocol can enforce our rule. In both, asking the person is a matter for the program that holds
the AI, and that program may be the AI's own. So release and the brake must live **in our engine, at the point where the action
happens**, and an AI must have no other way to act.

### ACP: coding agents in the messenger

ACP connects a client (a user interface) to a coding agent that usually runs as its subprocess. It defines:

- **Setup:** version and capability exchange, login, sessions with a working folder and a list of MCP servers.
- **A prompt turn:** the client sends a prompt, and the agent streams updates: message text, reasoning, tool calls, plan, usage.
- **Questions:** permission requests with options, and forms for structured input.
- **Optional services by the client:** reading and writing files, and terminals. Version 2 removes these.

Only stdio is defined. A remote transport is still a proposal. Subagents are also still a proposal, and they appear only in the
unstable schemas.

Showing and driving an agent fits ADR 0054 well. The agent becomes a **provider**, like mail or Matrix (ADR 0045). The provider
starts a subprocess, so it belongs in the engine, not in a frontend. The operator must come from our own launch settings and the
person's card, because the agent's self-description is self-reported.

| ACP | `fs-messenger` today | What is needed |
|-----|----------------------|----------------|
| Session, with an absolute working folder | `Conversation` | Keep the session id and folder in the provider |
| Sending a prompt | `Draft.send` | Fits |
| Streamed message text, Markdown by default | `bodyText`, and `updated` events carry only a summary | An event with a text chunk, and the media type of the body |
| Reasoning text | Nothing | Its own field |
| Tool call with ten kinds | `ToolCall` with four kinds. Until draft 0.1 the default of `kind` was `reads`, the harmless one; since draft 0.2 it is `unknown` | A separate `risk` field whose default is `unknown`, set by the engine and never by the agent. `unknown` always asks |
| Status: pending, in progress, done, failed | `settled` does not say how it ended | An outcome field |
| Title, plus full command, paths and content | `summary` only | A detail field. Commands and paths are shown in full, and the title is marked as written by the agent |
| Permission request with options | State `question`, with no options and no way to answer | Options on the call, and a new `MessageAction` to decide. Only a person's device may send it |
| Tool call updates | `ToolCall` is not in any event | An event for one changed tool call |
| Cancelling a turn | Nothing | A stop method on `Conversation` |
| Context use and cost | Nothing | Usage on the conversation |
| Subagents (proposal only) | Nothing | A `jobRef` on each message, as CodeAF showed. This form holds whichever way the proposal ends |

All of this can be appended under the Cap'n Proto rules. Message ids are optional in ACP, so the provider must create its own.
Replaying a session sends the old messages again, so the provider must not store them twice.

**Why ACP alone cannot carry the brake:**

- The agent **may** ask, but need not. The specification calls permission requests advisory, and it says an agent can act without
  asking.
- A remembered "allow always" is **owned by the agent**. After that we never hear about the action again, so we must never choose
  it, for any tool call.
- `kind` and `title` are written by the agent, so we cannot base a decision on them.
- File and terminal services by the client are a real control point, but only for what the agent chooses to send there, and
  version 2 removes them.
- ACP does not sandbox anything, and Zed's sandbox does not cover outside agents either.

So the page's existing limit becomes a condition: a coding agent needs **its own system user and a sandbox**, and its only way to
reach our programs is our MCP interface. We build against version 1 and keep version 2 in mind. Its updates work in place, which
suits our `ToolCall`.

### MCP: the contract as tools

ADR 0021 **holds**. A tool is a name, a description, a JSON Schema for input and optionally for output. Our capability ids such
as `message.send` are valid tool names, and `Problem` fits a result marked as an error. The generator has to solve these problems:

| # | Problem | Answer we propose |
|---|---------|-------------------|
| 1 | **No approval in the protocol.** The specification says a person should be able to refuse, in the client's interface, and says MCP cannot enforce this. The server never learns if anyone was asked | The server decides, see below |
| 2 | **Risk is not in our contracts.** Hints exist (read-only, destructive, idempotent, open world), but the schema has no data for them. Without data, a tool counts as destructive. They are also only hints, untrusted by default | Cap'n Proto annotations on methods and union members. Our compiler supports annotations |
| 3 | **"Acts in my name" has no hint.** `Draft.send` adds something and destroys nothing | Our own risk class, carried in the tool's `_meta` and enforced by the engine |
| 4 | **One method, mixed risk.** `Conversation.act` covers flagging as well as deleting and forwarding | One tool per union member |
| 5 | **Capabilities become handles.** `open` returns a live object and `Draft` holds state. MCP has only plain arguments | Flat tools with handle arguments. Authorisation is checked on every call, and handles expire |
| 6 | **No callbacks.** Servers send no requests, and subscriptions cover only list and resource changes. `Listener` has no direct form | Events and `Blob` become resources, not tools. ADR 0021 mentions only tools |
| 7 | **Secrets in arguments.** `AccountSetup.secret` would pass through the model. MCP forbids asking for secrets by form | A mark that excludes a field or method from generation |
| 8 | **Who is calling?** Self-description proves nothing, stdio takes credentials from the environment, and the tool list may vary only by credentials | Locally, a Unix socket with the system user as identity, which fits ADR 0054. The MCP specification suggests stdio framing there. Remotely, Streamable HTTP with its OAuth flow |
| 9 | **Outside clients expect stdio or HTTP** | A small stdio bridge to our socket |
| 10 | **The protocol moves fast.** 2026-07-28 removed sessions and the handshake, older clients still use them, and sampling, roots and logging are deprecated | Target this revision. Support for older clients is a separate choice |
| 11 | **Tool results carry hostile text.** Message bodies reach the model, and nothing in the protocol marks them as data | Keep them clearly separate in the result, and never let them widen a right |
| 12 | **Size.** The messenger contract alone has 31 methods, and we have not measured what that costs a model | Tools grouped by capability, offered as the person releases them |

**How a tool call gets approved.** The tempting way is MCP's form request (elicitation): the server returns `input_required`, the
client asks, then retries with the answer. This **cannot be our brake**. The answer comes from the client, the specification allows
"other sources", and the client may be the AI's own program. An `accept` proves nothing about a person.

So we propose (a design, not tested):

1. A tool call reaches the engine, and the engine looks up the risk from the contract, never from the caller.
2. If it needs release, the engine puts a `question` tool call into `fs-messenger`, for the person.
3. The person answers on their own device, with their own key. The answer does not pass through the AI's client.
4. The MCP call returns `input_required` with only a `requestState`, or an error result that says "waiting" for clients that
   cannot do this. The state is protected against tampering. It is bound to the caller, a short expiry and a digest of the exact
   arguments. It can be used once, and the engine enforces that.
5. A retry runs only if the person agreed to exactly these arguments. Any change asks again.

Destructive actions and actions in the person's name have no "always" option at all. A release from the person can cover the other
classes. The emergency stop simply makes the engine refuse every call.

What we cannot check from reading: whether real clients retry on a bare `input_required`. The official Tasks extension names
approval as a use, but it is optional, so we do not depend on it.

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

**Status: agreed for now by the project owner (2026-11-06), may change when it becomes important (ADR 0054).**

Some people want no AI. This is not discrimination. It is about espionage, about something that knows everything all the time,
and about speed: a model can wreck a computer at once, which almost no person can.

### Three separate things

**1. The mark says who is responsible.** We cannot tell an AI from a person by looking. So the people who **host** an AI are
what counts: an AI is a participant that names its operator, and people vouch for that operator.

**Nothing hidden.** We do not do user bots, as that would not be transparent. We want only people, or intelligences where you
know who it is. A real name is not needed. But it must be one person, not several accounts. How to establish that without
removing anonymity is an **open question**.

**An AI comes by invitation.** I create a profile for it, and that profile is the invitation. Then I can tell it what I want.
For it to do anything at all, I must release that. The rating is how I know who it is.

**2. Everyone sets their own level.** Each person tells their own program from which level of trust it opens up for them.

| Level | Who gets through |
|-------|------------------|
| 0 | Everyone |
| 1 | Operators that a chosen number of my own contacts vouch for |
| 2 | Operators I have verified myself |
| 3 | Only those I named |

- **There is no global score.** The level is computed from my own contacts only, and nothing is passed along further.
- **Marks count only where they were given.** Having no mark means nothing is known. A black mark exists only for the program
  where someone is hosted, like a ban today: it applies where you are, not everywhere. A ban across everything would be neither
  fair nor possible, and we do not do it.
- **Per action, not one number:** chatting with an AI and letting an AI act on my data are different decisions.

**3. The emergency stop needs nobody's trust.**

- **Stop:** one action ends all running AI work and takes away all tool rights at once.
- **Lock out:** the program then refuses every AI participant, and everything below my level.
- **Out of the AI's reach:** it lives in the engine, below every frontend. No tool or MCP call can switch it off, and only a
  person can open it again, with their own key on their own device.
- **It always works:** without network, without a model, and when in doubt it stays shut.
- **Afterwards:** the log shows what happened, and the [store](https://github.com/FreeSynergy/fs-store) undoes what it can.
- **Who may pull it** is a normal permission setting. If someone gives everyone that right, everyone may. If not, not.

Before the full stop comes a **brake**, since speed is the real danger: actions that destroy something or act in my name always
ask, whatever else was allowed. We do not restrict what an AI thinks or says. But the owner decides what happens to their
own data.

### What this cannot do

- **Nothing proves that someone is human.** The [Real Life Trust Protocol](https://github.com/real-life-org/trust-protocol)
  says this about itself: no check says "this is a human". It only shows that people I know stand behind this key. A verified
  person can still run an unmarked AI behind it. What helps then is consequences: withdraw the vouching, block, stop.
- **The stop only reaches what runs through our programs.** That is why agents always run under their own system user, in a sandbox, so the system can end them from outside (ADR 0056). An agent can never become an admin.
- **A high level also keeps out new people** who have no contacts yet. So it is always a personal choice, never our default.

## Open questions

1. How do we make sure it is one person and not several accounts, without removing anonymity?
2. Is anything left that needs its own data here? If not, this page becomes the description of a frontend.
3. How exactly does an AI name its operator? JSContact `kind` `application` is confirmed (RFC 9553 §2.1.4). How the operator
   signs for it, given that the trust protocol has no global identifier per person, is still open.
4. **For the project owner:** must a coding agent over ACP run under its own system user in a sandbox, without exception? The
   proposal is yes, since otherwise the brake does not hold for it. The cost is more setup, and some agents may not run that way.
5. **For the project owner:** ADR 0021 needs an addition: risk marks in every contract, events and blobs as MCP resources, and an
   exclusion mark for secrets. Is that agreed?
