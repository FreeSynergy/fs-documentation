# Cap'n Proto code generation without C++ — checked 2026-11-05 (Opus)

| Item | Finding | Evidence |
|------|---------|----------|
| `capnp` runtime crate | pure Rust | known; capnproto-rust repo |
| `capnpc::CompilerCommand` | **calls the external `capnp` tool** (C++): "When this method is not called, the command looks for a name 'capnp' on the system (… PATH)" — method `capnp_executable` | ✅ docs.rs/capnpc/latest/capnpc/struct.CompilerCommand.html |
| `capnpc::codegen::CodeGenerationCommand` | generates Rust from a `CodeGeneratorRequest` — the Rust half is pure Rust; only **schema parsing** needs the C++ compiler | ✅ (used in capnpc-embedded example) |
| **`capnpc-embedded`** 0.2.0+1.4.0 (2026-07-15), MIT, by rickardp, ~5.5k downloads | the official C++ schema compiler (capnp 1.4.0) **compiled to WebAssembly** (`capnp.wasm`, ~800 KB) and run in-process by a **pure-Rust WASM engine** — no system `capnp`, no C/C++ toolchain, no subprocess, no network; returns the `CodeGeneratorRequest` for `capnpc::codegen` | ✅ docs.rs/capnpc-embedded, crates.io API |
| pure-Rust schema compiler | none mature found; `SuperInstance/capnp-schema` = schema modelling library, not a compiler ⚠️ | search 2026-11-05 |
| capnproto-rust releases | 0.23 (2025-10-28, `Rc<Self>` in RPC methods), 0.22 (async methods) | ✅ dwrensha.github.io/capnproto-rust |

Note: with capnpc-embedded no C/C++ runs natively, but the compiler logic is still C++ (as a WASM blob).
