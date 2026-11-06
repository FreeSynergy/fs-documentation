# 0052 – Eine Person mit Rollen; Rollen sind standardisiert oder selbst definiert; Vertrauen sichtbar machen

Status: akzeptiert (2026-11-06) · ergänzt ADR 0050 · öffentlich: `docs/en/interfaces/roles.md`

## Entscheidung (Nutzer)
1. **`fs-people` verwaltet alle Menschen, einmal je Person, mit mehreren Rollen** (Kontakt, Kunde, User …) statt Vererbung.
2. **Rollen dürfen und müssen Standards entsprechen, wo es sie gibt.** Sie werden vorher überlegt und öffentlich gemacht.
3. **Eigene Rollen sind möglich und genauso definiert** wie unsere.
4. **Wir brauchen etwas, das zeigt, wann ein Mensch sicher ist.** Das geht über Web of Trust. Es könnte auch gegen Betrug durch
   Bots helfen, etwa bei Telegram, sobald wir groß werden und zusammenarbeiten. Das Risiko von Sperren durch Telegram bei
   Userbots sagen wir ausdrücklich.

## Vorschlag (Opus)
- Trennung: **Beziehung** zu mir (vCard `RELATED`, JSContact `relatedTo`) und **Rolle** in einer Gruppe (W3C `org:Role`,
  `org:Membership`). „Freund“ ist damit genormt, „Kunde“ bleibt eine Lücke.
- `fs-people` hält die Person, der Besitzer der Rolle hält deren Felder.
- Vertrauen als eigene Schnittstelle im Katalog, Grundlage Web of Trust.
