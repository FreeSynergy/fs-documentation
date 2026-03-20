# AI-Inferenz (lokale LLMs)

FreeSynergy integriert lokale LLM-Inferenz über **Mistral.rs** — einen nativen Rust-Binary-Service mit OpenAI-kompatibler API. Er läuft direkt auf der Hardware, ohne Container-Overhead.

---

## Paket

| Eigenschaft   | Wert                                  |
|---|---|
| Store-ID      | `ai/mistral`                          |
| Typ           | `binary` (kein Container)             |
| Port          | `1234`                                |
| API           | OpenAI-kompatibel (`/v1/chat/completions` etc.) |
| Quelle        | `FreeSynergy/mistral.rs` (Fork von `EricLBuehler/mistral.rs`) |

```bash
fsn store install ai/mistral
```

---

## Empfohlene Modelle (CPU, 16 GB RAM)

| Modell                                  | Größe  | Wofür                            |
|---|---|---|
| `Qwen2.5-Coder-7B-Instruct-Q4_K_M.gguf` | ~4.5 GB | Code schreiben, reviewen, erklären |
| `Qwen2.5-7B-Instruct-Q4_K_M.gguf`       | ~4.5 GB | Allgemeine Fragen, Dokus, Planung  |
| `Qwen2.5-Coder-1.5B-Instruct-Q8_0.gguf` | ~1.6 GB | Schnelle Code-Completions          |

Herunterladen von HuggingFace:
```bash
# Beispiel: Qwen2.5-Coder-7B herunterladen
huggingface-cli download bartowski/Qwen2.5-Coder-7B-Instruct-GGUF \
  Qwen2.5-Coder-7B-Instruct-Q4_K_M.gguf \
  --local-dir /srv/fsn/data/mistral/models/
```

Das Modell wird einmalig heruntergeladen und bleibt lokal gespeichert.

---

## Konfiguration

Nach der Installation (`fsn store install ai/mistral`) fragt der Setup-Wizard nach:

- **Model File Path** — Absoluter Pfad zur `.gguf`-Datei
- **Max Concurrent Sequences** — Standard: `4` (empfohlen für 16 GB RAM)
- **Domain** — Optional, für Proxy-Zugriff

---

## Start / Stop

```bash
fsn start ai/mistral     # starten
fsn stop ai/mistral      # stoppen (gibt RAM frei)
fsn status ai/mistral    # Status anzeigen
```

Mistral.rs kann jederzeit gestoppt werden, um RAM freizugeben — z.B. für andere speicherintensive Tasks. Beim nächsten Start lädt es das Modell wieder in den RAM (dauert ~5–15 Sekunden).

---

## Workflow: Claude + Mistral + Entwickler

```
Entwickler
   │
   ├── Claude Code (Anthropic API)
   │     └── Wofür: Architektur, komplexe Bugs, neue Features,
   │                Cross-Repo-Arbeit, unbekannte Probleme
   │
   └── Mistral.rs (lokal, localhost:1234)
         └── Wofür: Code-Completions im Editor, kleine Fragen,
                    Boilerplate, Datei-Erklärungen, Docs-Drafts
```

**Token-Sparregel:**
- Mistral zuerst für: Dateien lesen/erklären, kleine Fixes, Templates
- Claude für: Architektur-Entscheidungen, schwierige Bugs, neue Konzepte

---

## Editor-Integration (Continue.dev)

Continue.dev in VSCode auf den lokalen Endpunkt zeigen:

```json
{
  "models": [
    {
      "title": "Mistral.rs (lokal)",
      "provider": "openai",
      "model": "qwen2.5-coder-7b",
      "apiBase": "http://localhost:1234/v1",
      "apiKey": "none"
    }
  ]
}
```

---

## Build (FSN Fork)

Mistral.rs wird aus unserem eigenen Fork (`FreeSynergy/mistral.rs`) gebaut:

- CI: `.github/workflows/fsn-build.yml`
- Targets: Linux x86\_64, Linux aarch64, macOS x86\_64 (Accelerate), macOS aarch64 (Metal), Windows x86\_64
- Features: CPU-only (`--no-default-features`) + plattformspezifische Hardware-Beschleunigung
- Release-Tag: `v{version}-cpu` (CPU-Build, CUDA-Builds folgen separat)
