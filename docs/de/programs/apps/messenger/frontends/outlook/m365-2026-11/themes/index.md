# Outlook m365-2026-11 — Themes

Was sich mit dem FreeSynergy-Theming (Tokens) nachbauen lässt und was nicht. Werte sind aus Screenshots geschätzt (ADR 0038); nichts wird kopiert (ADR 0013). Token-Namen sind unsere Vorschläge.

| Theme | Datei | Nachbaubar |
|-------|------|-------------|
| Hell (Standard) | [light](light.md) | ja |
| Dunkel | [dark](dark.md) | ja |
| Bild-Themes (Bild hinter den Bereichen, hell oder dunkel) | [picture](picture.md) | teilweise |

## Mechanismus des Themings
- **Modus**: hell, dunkel oder dem System folgen ✅ (Desktop-Einstellungen und Mobil, jeweils mit einer kleinen Vorschau) ✅.
- **Themes** über dem Modus: eine Akzentfarbe (eine helle Variante zeigt einen violetten Akzent statt Blau ✅) und **Bild-Themes**, die ein Bild hinter das Fenster legen ✅; KI-generierte Themes („benutzerdefiniert“, „Wetter“, „Standort“) ✅ auf Desktop und Mobil.
- **Dichte** (mobil: eigener Reiter neben Design ✅; Desktop: „Dichte“ unter Ansicht ✅).
- Der mobile Kopfbereich kann das Theme-Bild tragen ✅.
- Microsofts Designsystem ist Fluent 2 ⚠️ (tokenbasiert: neutrale Farben, Markenfarben, Statusfarben).

## Nicht nachbaubar / Grenzen
- KI-generierte sowie standort- und wetterabhängige Themes (brauchen einen Generatordienst) — nein.
- Exakter Fluent-Icon-Satz und die Schriften Segoe/Aptos — lizenzgebunden; wir verwenden unseren Icon-Satz und eine freie serifenlose Schrift mit ähnlichen Maßen ⚠️.
- Acryl-/Mica-Transluzenz des Windows-Fensterrahmens — Plattformeffekt; nur eine Annäherung mit Unschärfe, falls der Renderer das unterstützt ⚠️.
