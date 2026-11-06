# Apple Mail iOS 26 — Themes

Was sich mit dem FreeSynergy-Theming (Tokens) nachbauen lässt und was nicht. Werte sind aus Screenshots geschätzt (ADR 0038); nichts wird kopiert (ADR 0013).

| Theme | Datei | Nachbaubar |
|-------|------|-------------|
| Hell | [light](light.md) | teilweise (Glas-Effekt) |
| Dunkel | — nicht gesehen ⚠️ | — |

## Mechanismus des Themings
- Mail folgt dem Systemerscheinungsbild (hell/dunkel) ⚠️; keine Theme-Auswahl innerhalb von Mail ✅ (keine gesehen).
- Akzentfarbe ist das Systemblau ✅; Kontaktkarten übernehmen einen Farbton aus dem Kontaktposter ✅.
- iOS 26 „Glas“: durchscheinende, unscharfe, schwebende Bedienelemente mit weichem Glanzrand ✅.
- Textgröße folgt dem System (Dynamic Type) ⚠️.

## Nicht nachbaubar / Grenzen
- Echtzeit-Brechung und Unschärfe des Glas-Materials — nur eine Annäherung mit Unschärfe und Transparenz, falls der Renderer das unterstützt ⚠️.
- SF Pro Schrift und SF Symbols — Apple-Lizenz; wir verwenden eine freie serifenlose Schrift und eigene Icons.
- Memoji-Avatare — Apple-Inhalte.
