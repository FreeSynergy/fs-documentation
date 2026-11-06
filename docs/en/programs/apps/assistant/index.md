# Assistant

A chat with AI that can work with all our programs. It is how we want to talk to our own tools, and to each other, soon.

**Status: idea (2026-11-06), no code yet.** Name `fs-assistant` is a proposal. See the [overall plan](../roadmap.md). ADR 0053.

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
| Strata | Very pleasant appearance | Several products bear this name; to be identified |
| CodeAF | Shows all AIs, including subagents | Not found yet; to be identified |
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

## Open questions

1. Is this a program or the component only? It would own conversations with AI, so by our rule it is a program. Should those
   conversations be ordinary messages in `fs-messenger`?
2. Which programs are Strata and CodeAF exactly?
3. Do agents become people in `fs-people`, with a role? This would make them first-class in tasks and messages.
