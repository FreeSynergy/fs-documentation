# Zed, ACP, MCP: source notes (2026-11-06)

Result page: `docs/en/programs/apps/assistant/index.md`. Function analysis only (ADR 0013). Nothing copied.

**Method.** Read from documentation, specifications and selected source code. **Nothing was built or run.** The repositories were
shallow clones in one new directory under `/tmp`, deleted afterwards.

| Source | Version read |
|--------|--------------|
| `github.com/agentclientprotocol/agent-client-protocol` | commit `67cde2d` (2026-11-06), changelog top 1.15.1 (2026-11-02) |
| `github.com/modelcontextprotocol/modelcontextprotocol` | commit `3835325` (2026-11-06), spec folder `2026-07-28` |
| `github.com/zed-industries/zed` (sparse: `docs/src/ai`, `crates/agent_ui/src`, `crates/agent_settings/src`) | commit `e231594` (2026-11-06) |
| `zed.dev/docs/ai/agent-panel`, `/tool-permissions`, `/external-agents` | fetched 2026-11-06 |
| `modelcontextprotocol.io/specification/versioning` | fetched 2026-11-06 |
| Ours: `fs-interfaces/schema/messenger.capnp`, `common.capnp`, ADR 0013, 0021, 0054 | working tree |

## Zed

| Claim on the page | Where verified |
|-------------------|----------------|
| Width limit, default 850 px, can be switched off | `assets/settings/default.json`: `limit_content_width`, `max_content_width` |
| Separate fonts and sizes for AI text and person's text | same file: `agent_ui_font_*`, `agent_buffer_font_*` |
| Reasoning: four display modes, default open while streaming, then folded | `crates/settings_content/src/agent.rs` (`ThinkingBlockDisplay`), `crates/agent_ui/src/entry_view_state.rs` |
| Edit and terminal cards, a setting per type, both open by default | `default.json`: `expand_edit_card`, `expand_terminal_card` |
| Jumping and scroll keys, start and last-prompt buttons | `docs/src/ai/agent-panel.md` |
| Search inside the thread | Code only: `conversation_view/thread_search_bar.rs`. Not on the agent panel docs page |
| Bar above the input with files, plan, queue, permission question | Code: `render_activity_bar` in `conversation_view/thread_view.rs`. "Above the input" comes from the agent panel docs for the changed-files bar and from the render order. **Not seen on screen** |
| Review view, per-change accept or reject | `agent-panel.md` |
| Opening compaction summary, copy, open thread as Markdown | `agent-panel.md` |
| Subagent card, window of 8 entries | `conversation_view/subagent_card.rs` and `MAX_PREVIEW_ENTRIES` in `thread_view.rs` |
| Unicode warning blocks "allow" | `render_permission_buttons` in `thread_view.rs`, `unicode_confusables.rs`. Documented there for sandbox prompts |
| Fixed rules narrow, global "allow" | `zed.dev/docs/ai/tool-permissions` |
| Sandbox excludes external agents | `docs/src/ai/sandboxing.md` |
| Licence of the panel code | `crates/agent_ui/Cargo.toml`: GPL-3.0-or-later |

**Not verified for Zed:** the look itself. No screenshots were viewed and the program was not run. Line height, colours and Markdown
styling of the thread were not examined. Whether readers find it pleasant is the owner's impression, and we did not test it.
Zed's external-agents page does not say how far tool permissions cover those agents.

## ACP

| Claim on the page | Where verified |
|-------------------|----------------|
| Protocol version 1 is stable, wire compatibility is the negotiated `protocolVersion` | `README.md`; `docs/docs.json` tags v1 "Latest", v2 "Draft" |
| v2 labelled draft, feature flags advised | `docs/protocol/v2/migration.mdx` |
| Apache-2.0 | `LICENSE` |
| Interim governance, Zed and JetBrains, two lead maintainers with veto | `docs/community/governance.mdx` |
| Only stdio defined, custom allowed, remote is an RFD | `docs/protocol/v1/transports.mdx`; RFD listed "Active" in `docs.json` |
| Methods and updates | `protocol/v1/overview.mdx`, `prompt-turn.mdx` |
| Ten tool kinds, four statuses, permission options | `protocol/v1/tool-calls.mdx` |
| Permission requests advisory, ACP does not sandbox, agent can act without asking, self-reported info | `protocol/v1/security.mdx` |
| Agent owns remembered decisions | `protocol/v1/tool-calls.mdx`, "Permission options" |
| Agent `MAY` request permission | same, "Requesting permission" |
| Message ids optional | `protocol/v1/prompt-turn.mdx`, "Message IDs" |
| Text is Markdown by default | `protocol/v1/content.mdx` |
| v2 removes client file and terminal APIs, updates are upserts | `protocol/v2/migration.mdx` |
| Subagents are a proposal | `rfds/subagents.mdx`, "Active"; 0 hits in both `schema.json`, 9 hits in both `schema.unstable.json` |

**Inference, not from the spec:** "we must never choose `allow_always`". A client can only choose among the agent's options, and an
agent's own settings may still skip the question. Mapping table to `fs-messenger` is our own work.

**Not verified for ACP:** behaviour of any real agent. Which agents actually ask, or accept running in a sandbox, is unknown.

## MCP

| Claim on the page | Where verified |
|-------------------|----------------|
| 2026-07-28 is the current revision | `modelcontextprotocol.io/specification/versioning`; `docs/docs.json`; `LATEST_PROTOCOL_VERSION` in `schema/2026-07-28/schema.ts` |
| Tool structure, naming characters (dot allowed), error results | `specification/2026-07-28/server/tools.mdx` |
| Person should be able to refuse (SHOULD) | `tools.mdx`, "User Interaction Model", "Security Considerations" |
| MCP cannot enforce at protocol level | `specification/2026-07-28/index.mdx`, which also says, in lower case, that hosts must get consent before any tool |
| Hints and their defaults | `ToolAnnotations` in `schema.ts` (`destructiveHint` default true, `readOnlyHint` default false) |
| Annotations untrusted unless from a trusted server | `tools.mdx`, MUST |
| Tool has `_meta` | `Tool` in `schema.ts` |
| Tool list varies only by authorization | `tools.mdx`, "Capabilities" |
| Handles for state, non-normative | `tools.mdx`, "Stateful Tools" |
| Servers initiate no requests; subscriptions | `basic/transports/index.mdx`, `changelog.mdx` items 4 and 7 |
| Form elicitation forbidden for secrets | `client/elicitation.mdx` |
| Client gathers input "from the user or other sources" | `basic/patterns/mrtr.mdx`, high-level flow |
| `input_required` may carry only `requestState`; client MAY retry at once | `mrtr.mdx`, server and client requirements |
| `requestState` is attacker-controlled, integrity, principal, expiry, digest, single use on the server | `mrtr.mdx` |
| stdio credentials from the environment | `basic/authorization/index.mdx` |
| Unix socket reuses stdio framing | `basic/transports/stdio.mdx`, `transports/index.mdx` |
| Sessions and handshake removed; deprecations | `changelog.mdx`, `deprecated.mdx` |
| Tasks extension names approvals | `docs/extensions/tasks/overview.mdx`. Full spec is in another repo, **not read** |

**Our design, not from the spec:** the approval flow (engine asks through `fs-messenger`, bare `input_required`, retry after release).
A bare `input_required` with no way for the client to see progress may behave poorly in real clients. Clients **MAY** retry at once,
so a tight retry loop is possible and needs a limit. **Untested.** Which clients support revision 2026-07-28 was not checked.

## Our side

- `messenger.capnp`: Cap'n Proto enums default to ordinal 0, so an unset `ToolCall.kind` reads as `reads`. Stated from Cap'n Proto
  rules as known, not re-read today.
- 31 methods counted in `messenger.capnp`, by pattern and by hand per interface.
- `fs-capnpc` has annotation code (`src/translator/annotations.rs`). Support for our exact use was not tested.
- No MCP generator exists yet in `fs-interfaces`. Only the schema comment mentions MCP.
