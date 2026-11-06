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

Function analysis only, as with all programs (ADR 0013). Named by the project owner, still to be analysed:

| Program | Idea | Status |
|---------|------|--------|
| [Strata](https://github.com/Niko1221/Strata) | Very pleasant appearance | To be analysed. MIT, C++, local inference |
| [CodeAF](https://github.com/Agent-Field/CodeAF) | Shows all AIs, including subagents | To be analysed. Apache-2.0, Go |
| Zed | Output that is easy to read at length | To be analysed |

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

We do not restrict what an AI may think or say; that is not our job. But anyone must be able to **lock AIs out completely**,
because of attacks. The strategy for this is open. A mark only tells you about honest AIs, since an attacker will not mark
itself. So this also needs the opposite direction: admitting only proven people, through [Web of Trust](../../../interfaces/index.md).

## Open questions

1. How do we lock out AIs reliably, and who decides: a person, a group?
2. Is anything left that needs its own data here? If not, this page becomes the description of a frontend.
3. How exactly is an AI marked? A role in `fs-people`, plus JSContact `kind` `application` (to be checked).
