# 0055 – Sprechende Namen statt IDs; `fs-groups` ist die Quelle der Wahrheit für Gruppen

Status: akzeptiert (2026-11-06) · ergänzt ADR 0047, 0050, 0052 · öffentlich: `docs/en/programs/apps/files/design.md`, `docs/en/programs/platform/groups.md`

## Entscheidung (Nutzer)
1. **Sprechende Namen sind immer besser als IDs.** „Wir machen Systeme für Menschen, und die sollen es einfacher haben.“
   Im lokalen Ordner liegen Dateien deshalb unter ihrem Namen, nicht unter der Objekt-ID.
2. **Namen in einem Ordner: so, wie das Betriebssystem es zulässt.** Erstmal; den Rest sehen wir später.
3. **Unser Programm ist die Quelle der Wahrheit.** `fs-groups` legt Gruppen und ihre Menschen fest, `fs-people` kümmert sich um
   die Menschen und konfiguriert die User. Der Kanidm-Abgleich entfernt also Mitglieder gespiegelter Gruppen, die nicht in `fs-groups` stehen.
4. **Beim Verschieben eines Wiki-Ordners wandert alles darunter mit,** so wie man es erwartet.
5. **Bei Orten reicht vorerst der umschließende Rahmen.**

## Zu klären
- `docs/en/interfaces/roles.md` nennt bisher den Identitäts-Wrapper als Besitzer der Rolle User. Punkt 3 sagt: `fs-people` konfiguriert die User. Wie sich das zum Wrapper verhält, ist offen.
- S3 und andere Speicher: Gilt Punkt 1 auch dort? Bis zur Klärung: lokal sprechend, S3 unverändert.
- Wie Änderungen von außen im lokalen Ordner erkannt werden, ist offen (`files/design.md`).
