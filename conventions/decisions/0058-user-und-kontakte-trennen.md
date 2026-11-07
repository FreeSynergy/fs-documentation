# 0058 – Kontakte sind Profile

Status: Idee vom Nutzer (2026-11-07), Ausgestaltung Vorschlag bis zur Bestätigung · präzisiert ADR 0052 · kein Umbau im Sprint

## Entscheidung (Nutzer)
Erst: „Wir müssen zwischen der Kartei, wo wir die Leute nur sammeln, und denen, die tatsächlich mitmachen, unterscheiden.“ Dann, nach Abwägung von zwei Programmen und einem Status auf derselben Karte: „Ich habe die Lösung: Profile. Kontakte sind Profile. So einfach ist das.“

## Vorschlag (Strategie)
`fs-people` bleibt ein Programm. Es gibt kein `fs-contacts` und kein `fs-users`.
- **Profil:** eine Sicht auf jemanden, mit einem Autor (AS2 `Profile`, `attributedTo`, `describes`). Karten sind im Code schon genau das (`Profile`, `describes`, Daten in JSContact).
- **Kontakt:** ein Profil, das ich selbst geschrieben habe, oder das mir jemand zeigt. Jede Person kann mehrere zeigen, die Dating-App ein anderes als die Arbeit.
- **User:** wer hinter einem Profil steht und mitmacht. Schlüssel, Rechte und Anmeldung stehen nie in einem Profil, sie gehören zur Identität (`data/login`, `data/identity`, Kanidm über `fs-identity`). „Ist User“ wird nicht gespeichert, es ergibt sich aus dem Verweis.
- **Meine Notizen** sind ein eigenes Profil oder eine Anmerkung von mir und landen nie in dem Profil, das mir jemand zeigt. Die Person sieht sie nicht, **außer ich teile sie** (Nutzer, 2026-11-07): „Wir können alle Daten teilen. Damit haben wir die volle Kontrolle.“ Geheimnisse und Schlüssel gehören nicht in Profile und sind davon nicht betroffen.
- **Einladung:** aus meinem Kontakt heraus per Link. Nimmt die Person an, verweist mein Kontakt auf sie, und ich sehe, was sie mir zeigt. Das belegt nur, dass der Link angekommen ist.

## Folgen
- ADR 0056 Punkt 8 bleibt gültig: Jeder in Kanidm hat ein Profil in `fs-people`, nicht umgekehrt.
- `data/profile` nennt bisher nur, was man über sich zeigt; das wird erweitert.
- **Mehrere Profile (Nutzer, 2026-11-07):** Zu einer Person kann man mehrere Profile speichern und sie zusammenlegen; wie, entscheidet man selbst. Mein selbst geschriebener Kontakt bleibt also neben ihrem Profil.
