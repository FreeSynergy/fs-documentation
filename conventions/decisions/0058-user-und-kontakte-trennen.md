# 0058 – User und Kontakte sind zwei verschiedene Dinge

Status: Grundsatz akzeptiert (Nutzer, 2026-11-07), Umsetzung Vorschlag · ändert ADR 0052 Punkt 1, ADR 0055 Punkt 3, ADR 0056 Punkt 8 · kein Umbau im Sprint

## Entscheidung (Nutzer)
„Wir müssen zwischen zwei Sachen unterscheiden: der Kartei, wo wir die Leute nur sammeln, als Adresskarten, und die, die tatsächlich bei uns mitmachen. […] dass wir das trennen müssen: User und Contacts. (Namen können geändert werden.)“
„Also brauchen wir neben `fs-people` doch `fs-contacts` und `fs-users`. Die Frage ist, ob dann `fs-people` noch Sinn macht? Als Frontend ja, aber insgesamt?“

## Vorschlag (Strategie, Entscheidung offen)
- **Kontakt:** was ich über jemanden weiß, eine Adresskarte (JSContact). Die Person weiß es vielleicht nicht, und sie hat dadurch keine Rechte.
- **User:** wer selbst mitmacht, mit Identität, Schlüssel und Rechten, auch eine KI. Nur hier gibt es Einladung und Beitritt (SCIM `User`, RFC 7643). Vor Kanidm, das nur Spiegel bleibt.
- **Zwei Programme, kein drittes:** `fs-people` wird `fs-contacts`, weil es heute schon JSContact hält. `fs-identity` wird `fs-users`. „Menschen“ bleibt als Frontend, das beide zeigt (Facade über zwei Traits); eigene Daten hätte ein drittes Programm nicht (ADR 0049).
- **Verbindung:** Eine Karte verweist auf den User (`describes`). Beide können dieselbe Person betreffen, müssen es aber nicht.
- **Rollen:** bleiben beim Eigentümer (ADR 0052): Rollen in einer Gruppe bei `fs-groups`. Wohin Kunde und Lieferant gehören, ist offen.

## Reihenfolge
1. Nutzer entscheidet die Namen. 2. Verträge: `contacts.capnp`, `users.capnp`; Muster und Trait zuerst. 3. Umzug mit Weiterlesen alter Daten. 4. Frontend. Die KI-Markierung darf dabei nie ausfallen (ADR 0054).
