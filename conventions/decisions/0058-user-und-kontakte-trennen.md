# 0058 – Kontakte sind Profile

Status: akzeptiert (Nutzer, 2026-11-08: „Kontakte sind immer Profile. Immer.“) · präzisiert ADR 0052

## Entscheidung (Nutzer)
Erst: „Wir müssen zwischen der Kartei, wo wir die Leute nur sammeln, und denen, die tatsächlich mitmachen, unterscheiden.“ Dann, nach Abwägung von zwei Programmen und einem Status auf derselben Karte: „Ich habe die Lösung: Profile. Kontakte sind Profile. So einfach ist das.“

## Vorschlag (Strategie)
`fs-people` bleibt ein Programm. Es gibt kein `fs-contacts` und kein `fs-users`.
- **Profil:** eine Sicht auf jemanden, mit einem Autor (AS2 `Profile`, `attributedTo`, `describes`). Karten sind im Code schon genau das (`Profile`, `describes`, Daten in JSContact).
- **Kontakt:** ein Profil, das ich selbst geschrieben habe, oder das mir jemand zeigt. Jede Person kann mehrere zeigen, die Dating-App ein anderes als die Arbeit.
- **User:** wer hinter einem Profil steht und mitmacht. Schlüssel, Rechte und Anmeldung stehen nie in einem Profil, sie gehören zur Identität (`data/login`, `data/identity`, Kanidm über `fs-identity`). „Ist User“ wird nicht gespeichert, es ergibt sich aus dem Verweis.
- **Meine Notizen** sind ein eigenes Profil oder eine Anmerkung von mir und landen nie in dem Profil, das mir jemand zeigt. Die Person sieht sie nicht, **außer ich teile sie** (Nutzer, 2026-11-07): „Wir können alle Daten teilen. Damit haben wir die volle Kontrolle.“ Geheimnisse und Schlüssel gehören nicht in Profile und sind davon nicht betroffen.
- **Einladung:** aus meinem Kontakt heraus per Link. Nimmt die Person an, verweist mein Kontakt auf sie, und ich sehe, was sie mir zeigt. Das belegt nur, dass der Link angekommen ist.

## Verknüpfen (Nutzer, 2026-11-08)
- **Jeder Kontakt ist ein Profil.** Ein Profil ist mit einem Eintrag in `fs-people` (einer Person) verknüpft oder nicht.
- **Unverknüpft bleibt es ein Profil,** bis das System übereinstimmende Daten findet: Telefonnummer, E-Mail-Adresse oder einige andere Angaben. Dann **fragt es den Benutzer**, ob es dieselbe Person ist und verknüpft werden soll. Nie ohne Rückfrage.
- **Der Benutzer kann jederzeit selbst verknüpfen** (und wieder lösen).
- **Was nach dem Verknüpfen übernommen wird, ist eine eigene Frage:** Es hängt an der Freigabe der Person (Schnittstelle Sharing). Verknüpfen heißt nicht übernehmen.
- Muster (Vorschlag Strategie): Specification für „passt zusammen“ (Regeln je Merkmal, normalisierte Nummern/Adressen), der Vorschlag als eigener Zustand (State: vorgeschlagen → bestätigt/abgelehnt; abgelehnte Paare werden nicht erneut vorgeschlagen).

## Folgen
- ADR 0056 Punkt 8 bleibt gültig: Jeder in Kanidm hat ein Profil in `fs-people`, nicht umgekehrt.
- `data/profile` nennt bisher nur, was man über sich zeigt; das wird erweitert.
- **Mehrere Profile (Nutzer, 2026-11-07):** Zu einer Person kann man mehrere Profile speichern und sie zusammenlegen; wie, entscheidet man selbst. Mein selbst geschriebener Kontakt bleibt also neben ihrem Profil.
