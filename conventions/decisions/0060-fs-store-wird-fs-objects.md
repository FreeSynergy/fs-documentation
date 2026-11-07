# 0060 – Die Datenablage heißt `fs-objects`; `fs-store` wird der Laden

Status: akzeptiert (Nutzer, 2026-11-07), Umbau nach dem Sprint · ändert ADR 0019, 0020, 0036

## Entscheidung (Nutzer)
„`fs-store` wäre perfekt“ für den Laden aus ADR 0036, „denn da geht es ja um einen Laden, wo du Sachen holen kannst.“ Die heutige Datenablage (Objekte, Aktivitätsprotokoll, Rückgängig) heißt künftig **`fs-objects`**. Der Launcher heißt dann **`fs-store`**; bis dahin liegt er nur lokal als `fs-launcher`.

## Reihenfolge (Strategie)
`fs-store` steckt am 2026-11-07 in 18 anderen Repos an rund 1.500 Stellen (Cargo-Abhängigkeit per Git-Adresse, Crate `fs_store`, Doku).
1. Repo `fs-store` auf GitHub in `fs-objects` umbenennen (GitHub leitet die alte Adresse weiter), Crate `fs-objects` / `fs_objects`, neuer Tag.
2. Alle 18 Repos umstellen: Git-Adresse, Crate-Name, Doku; per Skript, danach `gates.sh` grün und je ein neuer Tag.
3. **Erst wenn kein Repo mehr auf `fs-store` zeigt,** entsteht das neue Repo `fs-store` für den Laden. Vorher nicht: Ein neues Repo mit dem alten Namen beendet die Weiterleitung, und alle Builds würden den Laden statt der Datenablage holen.

Frühere ADRs behalten den alten Namen im Text; dieser ADR erklärt ihn.
