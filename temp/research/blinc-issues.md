# Blinc — git-bug issues (read 2026-11-05)

Read-only: `git fetch origin 'refs/bugs/*:refs/bugs/*'` in `.research-blinc/`, parsed without git-bug CLI
(each `refs/bugs/<id>` commit holds an `ops` JSON blob). **Do not re-fetch for the same questions.**

Total 255 · open 126 · closed 129

Open by label: `bug` 69, `debt` 49, `area:dsl` 27, `area:gpu` 24, `area:layout` 17, `area:cn` 11, `area:text` 9, `area:build` 8, `area:portal-ui` 8, `perf` 8, `area:css` 7, `area:core` 6, `area:platform` 5, `priority:high` 4, `area:web` 4, `area:app` 3, `area:debugger` 1, `area:animation` 1

## Relevant for FreeSynergy

| Id | Topic | Note |
|----|-------|------|
| bf7c901 | cn component backlog: 14 widgets planned | toggle, toggle_group, number_input, table, calendar, date_picker, form, … (input_otp done) |
| c422b97 | blinc_cn → blinc_layout widget promotion plan | interaction primitives move to `blinc_layout`, CSS-overridable, theme-neutral — **exactly our component layer idea** |
| 41da437 / 96b7192 | DSL bindings / reactive props for cn widgets | migration in progress |
| 1d26f07 | code editor: last stateful-callback widget, 3,000 lines | rewrite pending → chance for a pluggable whole-buffer highlighter |
| e864f0c | mobile IME compose candidates not wired | blocks CJK on mobile; desktop preedit also ignored (code TODO) |
| 883ead2, 982879f, af473a1, 4e110cb | mobile platform gaps | bridges, camera demo, iOS/Pixel jitter, Android resume |
| — | accessibility | **no dedicated issue**; AccessKit only mentioned in 4405aa3 and c422b97 |
| 4375436, 5bedc70 | high priority: Windows Computed panic, animations stall until mouse moves | |

## All open issue titles

- `3d67d23` .foreground() + CSS animation silently breaks composite promotion — fg prims strand outside — area:gpu, bug
- `b03973a` 176 integration-test binaries each link the whole stack, bloating target/ — area:build, debt
- `c3e8700` @flow elements render past scroll containers, overlay clips, and window edges — — area:gpu, bug
- `9fee179` A full tree rebuild has no owner scope, so what its widgets create is never disposed — area:core, bug
- `f1a93f8` A line breaks a word that fits, when the container's width came from rounding — area:text, bug
- `0f87b96` A stateful subscribed to context fields that are only BOUND PROPS re-renders the whole — area:dsl, bug
- `9bcdaf6` An @fsm component rendered nothing - the scope bracket's result local took the widget — area:dsl, bug
- `a33d2b9` An imported view never gets its instance-id parameter — area:dsl, bug
- `4e110cb` Android (blinc_platform_android + android-activity NativeActivity): resume 'goes black + — area:platform, bug
- `5bedc70` Animations stall until the mouse moves; overlays, tabs and drags look wrong — area:app, bug, priority:high
- `9f9aa69` Asymmetric border widths with rounded corners show corner artifacts — area:gpu, bug
- `3c7afb9` BLINC_DAMAGE_RECT path: text/SVG/image dispatch is now wired (Phase 3.B, commit 1608a571), — area:gpu, bug
- `d5d4d78` Bare signal reads inside computed{} bodies are never rewritten to getters — rewrite_expr — area:dsl, bug
- `5e711e5` Blinc DSL as a blinc_abi language SDK, rendered by blinc_gpu: what moves, what stays — area:dsl, area:gpu, debt
- `2103fd6` Blinc reactive architecture v2 — unified property channel, signal-bound modifiers, — area:core, debt
- `ae520cf` Book examples read an animated value once at build time, so they never move — area:animation, debt
- `12cb642` Bumping one package's git pin without its inter-package pins builds two copies of a shared — area:portal-ui, bug
- `21cb5fa` CI resolves dependencies fresh, so a yank upstream fails every workflow — area:build, debt
- `0cb0250` CI's Documentation/Android/Coverage/iOS Compile jobs fail on a yanked zip crate — bug, priority:high
- `c62aae9` CSS classes are hashed NOWHERE in blinc_layout/src/diff.rs, and — area:layout, bug
- `404320a` Calling OverlayHandle::is_live() / is_exiting() / close() inside a held — area:layout, bug
- `008a9e3` Canvas overlay paints above the static-cache blit; siblings declared after a canvas in tree — area:gpu, bug
- `8502881` Canvases nested inside an is_overlay_root subtree must dispatch AFTER — area:gpu, bug
- `ea7d722` Canvases re-run their draw callback every frame off the scheduler. The compositor fast path — area:gpu, bug
- `8ad53a2` Class-based CSS rules don't apply consistently — animations don't start, clip-path makes — area:css, debt
- `7125718` Closure / lambda bodies in zyntax bypass TypedCfgBuilder — control-flow statements silently — area:dsl, bug
- `8115bf5` Combobox/dropdown option items don't show hover bg or selected highlight until the user — area:cn, bug
- `9008028` Content built inside a Stateful callback cannot rely on inherited CSS: a bound cn.Badge — area:css, bug
- `7a333ad` Coverage hung once in blinc_core's tests; it is the only job running them as threads — area:build, debt
- `a83d4c5` Current state of Blinc's layout-tree stability layer. Three pieces shipped — LayoutNodeId — area:layout, debt
- `33ed667` DSL `lower_reactive_args` must recognize wrapped getter Shape A' — area:dsl, bug
- `da6d1ec` DSL collections stop at Vec<T> for scalar T; a list of structs needs a layout — area:dsl, debt
- `697cd8e` DSL has no router: no route declarations, params or nested outlets — area:dsl, debt
- `da3511e` DSL has no standard library beyond what a view body needs — area:dsl, debt
- `5938a7e` DSL match works in a widget body but mounts nothing directly under view {} with no container — area:dsl, bug
- `2ba20e5` DSL mounts one Stateful at the view root, so @stateful on any component re-renders the — area:dsl, debt
- `3a1aea5` DSL while-with-children in a view body still emits nothing — area:dsl, bug
- `5ea6ac8` Debugger tree panel still renders a placeholder — area:debugger, debt
- `4405aa3` Declarative physics: bind cloth, fluid and wave simulations from CSS — area:gpu, debt
- `fe4be84` Deferred DSL bodies resolve FSM context through a captured handler context; the scope — area:dsl, debt
- `b06a4bf` Desktop subtree rebuilds skip CSS class-only @keyframes animations on the first — area:css, bug
- `036fa25` Div::on_unmount handlers never run in a real app; the live unmount signal is the stable-id — area:layout, bug
- `6c086bf` Drive the DSL's FSMs through Zyntax fibers and effects — area:dsl, debt, priority:high
- `41da437` Eight cn widgets still have no DSL binding — area:dsl, debt
- `6f7b001` Engine simplification: adopt the model ashui's blinc_abi proves, not its line count — area:css, area:layout, debt
- `438ff15` EventRouter::set_event_callback in windowed.rs Input arm uses a raw pointer to a — area:layout, bug
- `3542e12` Every kit.hit_rect call clones the entire SpatialIndex via State::update — O(R²) clone — area:portal-ui, perf
- `b106ffb` Expose a cheap version check on Signal<T> for change detection without a clone — area:core, perf
- `b2e0138` FSM event codes collide with widget pointer events — area:dsl, bug
- `096ca99` FSM identity is (module, name) but the compiler hardcoded "main" — area:dsl, bug
- `7cabafe` Fluent methods should beat the stylesheet, with a component-default tier below app CSS — area:cn, area:css, area:layout, debt
- `746993e` Future architectural project — Solid-style Show / For primitives that bring per-child — area:core, debt
- `fd4c558` Glyph atlas never reclaimed space, so a cold glyph held its slot until clear() — area:text, perf
- `8683361` Glyph rasterisation followed the post-transform size with no floor — at canvas zoom 0.1 a — area:gpu, bug
- `85e5070` Group header chrome chips (edit / × / chevron) align to the title line only — when the — area:portal-ui, bug
- `b83df48` Inline shadows in sdf_core and sdf_notch, and circle shadows, keep the unblurred-shadow faults — area:gpu, bug
- `e0a7502` Layer groups lose isolation when their children are routed into separate batches — area:gpu, bug
- `c4ccde2` Layout widgets cannot ship their own default CSS — area:css, debt
- `9ab9dc6` Lost clicks/drags when a rebuild fires between mouse-down and mouse-up — router state must — area:layout, bug
- `e589562` Make SVG text optional so embedders can drop fontdb — area:build, debt
- `f39a76d` Merging canvas-overlay and dynamic-batch primitives into one composite_frame SDF dispatch — area:gpu, bug
- `e864f0c` Mobile IME compose candidates are not wired — area:platform, debt
- `883ead2` Mobile bridge examples missing: push, location, biometrics, status bar — area:platform, debt
- `af473a1` Mobile browsers: subtree-update jitter on iOS, scroll artifacts on Pixel — area:platform, bug
- `2294533` Multi-module .blinc compilation plan — area:dsl, debt
- `ec39bb2` No AOT pipeline or standalone CLI for shipping a DSL app — area:dsl, debt
- `982879f` No camera demo example for mobile — area:platform, debt
- `4e9dd6e` No first-party `blinc dev`: hot reload still needs dx serve — area:app, debt
- `f567e5c` No scrubber widget for the debugger timeline — area:cn, debt
- `12cc7ac` One failing test hides most of the suite in CI — area:build, debt
- `91e1a8d` PENDING_SUBTREE_REBUILDS holds raw LayoutNodeIds; a full tree build restarts the slotmap so — area:cn, bug
- `8947c34` Plan for hot-reloading .blinc files. Zyntax's per-function hot_reload is the wrong tool; — area:dsl, debt
- `3669560` Portal-UI animations now register a no-op tick_callback with the animation scheduler so the — area:portal-ui, bug
- `8fdf5f5` Portal-UI widget backlog tracks blinc_node_editor::config::PropertyDefinition variants. The — area:portal-ui, debt
- `bc1256a` Queued performance tasks bundled together — layout-ID stability refactor and per-paint cost — area:gpu, perf
- `a2958f3` Reactive<bool> props bound to an FSM ctx field silently fell back to LITERAL: the bool — area:dsl, bug
- `5cad2fe` Recompiling into a live BlincDsl re-runs the changed module but the entry keeps calling the — area:dsl, bug
- `0006aac` Resolve inherited text colour in the paint walk, not by copying into props — area:layout, debt
- `2c565dc` Retire stateful closures: what they stand in for, and the property-channel gaps behind them — area:cn, area:layout, debt
- `cf8087c` Ruffle 2D finish plan (post-M7) — area:gpu, debt
- `309f5a2` SDF CSG, @effect presets and calc() math helpers never landed — area:css, debt
- `0457f8f` SVG text shapes with system fonts, not the ones blinc_text loaded — area:text, bug
- `70f74fd` ScrollPhysics::update_scrollbar_visibility recreated the opacity spring every frame, — area:layout, perf
- `288a87f` ScrollState::Scrolling can latch forever after wheel events — area:layout, perf
- `3d90a31` Secondary windows never drain property updates, and node ids collide across trees — area:app, area:layout, bug
- `1854094` Slint-inspired renderer rework — adoption candidates — area:gpu, debt
- `ea2707f` Special Unicode chars (⌘, ⇧, ⌥, ⌃ — Apple modifier glyphs and similar symbol-font — area:text, bug
- `3031fd9` Text min-content measurement inflated flex-parent heights — area:text, bug
- `f3046f2` Text soft on standard-DPI (1x) displays, crisp on retina (2x): glyph quad origins were — area:text, bug
- `cba8887` TextInput cursor lands in the wrong place after a window resize — area:layout, bug
- `6909945` The SDF shaders are twelve hand-maintained copies of one body of code — area:gpu, debt
- `1d26f07` The code editor is the last widget built through a stateful callback, and its module is 3,000 lines — area:layout, debt
- `d58924b` Toast exit motion doesn't play on web (wasm); enter motion works, exit snaps — area:web, bug
- `436d0ad` Web runner swallowed right-clicks unless a text input owned focus. mousedown listener — area:web, bug
- `4477494` WebGL2 fallback status — area:gpu, debt
- `eb465ff` Wheel-bearing rAFs unconditionally invalidating render cache + draining all layer textures — area:web, bug
- `4375436` Windows: nested Computed panics with "RefCell already borrowed" — area:core, bug, priority:high
- `9bcdf2f` Zyntax's Cranelift backend only widened int-vs-int binary operands, so an int literal in a — area:dsl, bug
- `c551e84` apply_binding_deltas only set visible_anim_active=true, never cleared, so once the walker — area:gpu, bug
- `c422b97` blinc_cn → blinc_layout widget promotion plan — area:cn, debt
- `08ee2e9` blinc_layout's crate-level allow(unused, dead_code) hides dead code; extracting any module — area:build, debt
- `ed82fbb` blinc_node_editor node title drifts down as content body grows — centered on full bounds — area:portal-ui, bug
- `a917f17` blinc_portal_ui chart tooltip value pills read bottom-heavy — TextBaseline::Middle centers — area:portal-ui, bug
- `8afa8a9` blinc_portal_ui's per-widget `Response.clicked` uses a global region_id→timestamp map — area:portal-ui, bug
- `92dc5f5` canvas_demo Canvas Text sample draws its plate but not its headings — area:text, bug
- `178a63b` clip-path has no fill rule, and the renderer silently assumes nonzero — area:gpu, debt
- `bf7c901` cn component backlog: 14 widgets still planned — area:cn, debt
- `96b7192` cn reactive-prop migration: 14 of 19 DSL widgets take Reactive props — area:cn, debt
- `3c1cea3` cn.Dialog/Sheet/Drawer in the DSL — the signal is the overlay handle; keyed by signal, not — area:dsl, debt
- `dd18071` cn::input / cn::textarea CSS `:focus` outline ring transition only plays on the first focus — area:cn, bug
- `0b1d200` cn::switch had no deps() subscription — only its own click retargeted the thumb springs, so — area:cn, bug
- `5bfc932` cn::tree_view expand animation freezes mid-flight, leaving only some children rendered — area:cn, bug
- `b87fce3` cn_demo's three spinners pinned ~60% CPU because rotation_timeline kept is_any_animating() — area:text, perf
- `98d7824` current_call_id() is ZERO for a DSL widget with children — the pass that brackets a lowered — area:dsl, debt
- `004b024` gpu-alloc 0.6.1 was published as a patch but introduces a breaking AsRef<MD> bound that — area:build, bug
- `05ec980` hash_composite_scratch must hash layer_commands or CSS-animated layer-opacity freezes the — area:gpu, bug
- `a782b47` html_view() widget — phased plan — area:layout, debt
- `e750fa9` number_input has no keyboard stepping — area:layout, debt
- `aa77aa4` render_layer_range_tight skipped mesh aux_data offset — area:gpu, bug
- `291329f` render_tree_with_motion + render_static_layer gated render_paths_overlay_msaa on — area:gpu, bug
- `09d4c56` render_tree_with_motion_opt's z-layered no-glass branch built a temporary z0_batch with — area:gpu, bug
- `483c864` use_state_keyed with per-open/monotonic keys leaks signals — keyed-state store and reactive — area:core, bug
- `42897d0` web.rs runner never called invalidate_render_cache_tagged anywhere — composite-layer + — area:web, bug
- `d6037ec` wgpu-hal 26.0.6 regresses vkAcquireNextImage latency 156x via PR — area:build, perf
- `662bea6` word-spacing is measured but never drawn — area:text, bug
- `7e448d6` zyntax translate_closure seeds var_types but not var_typed_ast_types for lambda params — — area:dsl, bug
