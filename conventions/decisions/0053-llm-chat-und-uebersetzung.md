# 0053 – LLM-Chat als Component und Programm; Übersetzung vorerst nicht; Projektadresse

Status: akzeptiert (2026-11-06) · ergänzt ADR 0011, 0021, 0037 · öffentlich: `docs/en/programs/apps/assistant/index.md`

## Entscheidung (Nutzer)
1. **LLM-Chat:** Component und eigenes Programm, damit wir demnächst darüber kommunizieren können. Der Chat kann das MCP der
   Programme lesen und damit arbeiten. Features aus verschiedenen Programmen: Aussehen von Strata, Anzeige aller KIs samt
   Subagents von CodeAF, Lesbarkeit der Ausgabe von Zed.
2. **Die 253 älteren Dateien werden nicht ins Englische übersetzt:** Wir nutzen wenn nötig die deutsche Fassung und schreiben
   das Buch ohnehin ständig neu. Übersetzen wird später llama oder die API, nicht jetzt, weil sich alles noch ändert.
3. **`support@freesynergy.net` ist die Projektadresse** für alles.

## Vorschlag (offen)
- Name `fs-assistant`. Nach ADR 0049 ist es ein Programm, weil es Gespräche mit KI besitzt; ob diese normale Nachrichten sind, ist offen.
- Strata und CodeAF sind noch nicht eindeutig gefunden.

## Folgen
- ADR 0011 gilt weiter: `en/` ist die Quelle. Die Lücke `de/`-nur bleibt, bis jemand die Seite ohnehin neu schreibt.
