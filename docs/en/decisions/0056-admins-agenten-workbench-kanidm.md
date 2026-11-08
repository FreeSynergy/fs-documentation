# 0056 – Oberster Admin; Agenten werden nie Admin; Workbench gibt Kontext; Kanidm flach

Status: akzeptiert (2026-11-06) · ergänzt ADR 0005, 0021, 0037, 0049, 0054, 0055 · öffentlich: `docs/en/programs/platform/groups.md`

## Entscheidung (Nutzer)
1. **Der Admin, der installiert, ist der oberste Admin.** In den Gruppen kann er weiteren den Admin-Status geben.
2. **Gespiegelt wird nach Option B.** Verschachtelung geht nur dorthin, wo Rechte wirklich weitergegeben werden. In unseren Gruppen ist die Weitergabe einstellbar.
   **Bei Kanidm geht das nicht:** Dort werden Rechte immer vom Kind nach oben weitergegeben. Wo das nicht gewollt ist, gibt es dort eine **flache Liste**. Das gilt nur für Kanidm.
3. **Andere Richtung:** Wer es andersherum braucht, baut den Baum andersherum auf, statt einzelne Ausnahmen zu vergeben.
4. **Eine Workbench gibt immer einen Kontext zurück;** sie läuft nicht für sich allein. Aber aus einer Workbench wird schnell eine App (etwa Editor oder Schreibprogramm): Die Workbench füllt
   den ganzen Bildschirm, mit Menü und weiteren Primitives, Widgets oder Workbenches, auch wenn es nur eine Ansicht ist (Beobachter mit verschiedenen Ansichten). Damit ist der Widerspruch zwischen `CONVENTIONS.md` §2 und ADR 0005 geklärt.
5. **Agenten laufen immer in einer eigenen Sandbox unter eigenem Systembenutzer.**
6. **Ein Agent darf niemals Admin werden,** und erst recht nicht Superadmin.

7. **Rechte bekommt jemand nur, wenn der Admin es zulässt.** Offen ist, welche: Kanidm kennt `entry_managed_by` (wer verwaltet) und Claims (welche Berechtigung jemand mitbekommt). In beiden Fällen vergibt ein Admin. Ausnahme wäre ein Modus „je mehr man mitmacht, desto mehr Rechte“; wie der geht, ist offen.
8. **In Kanidm stehen nur Menschen, die die Rechte haben.** Nicht jeder in `fs-people` kommt nach Kanidm, aber jeder in Kanidm ist auch in `fs-people`.
9. **Mail bietet auch ältere Verschlüsselung an:** zusätzlich zu OpenPGP v6 auch v4-Schlüssel und das ältere Verfahren an v4-Empfänger. Unverschlüsselt geht weiterhin nichts hinaus.

## Einseitig folgen (Entscheidung des Nutzers, 2026-11-07)
**Es braucht keine Zustimmung beider Seiten.** „Wenn ich dir folge, dann bestimme ich, was du bei mir darfst. Warum musst du bestätigen, dass ich dir das erlaube? […] Natürlich ist es schön, wenn beide da sind, aber das muss nicht sein.“
Damit ist der Vorschlag unten, die Verbindung gelte erst nach Zustimmung beider, abgelehnt. Es gilt: Wer folgt, gibt nur eigene Rechte, und nie mehr, als er selbst hat. Bei dem anderen bekommt er dadurch nichts.
Bestätigt: mehrere Eltern je Gruppe, Zyklen verboten.

**Folgen ist kein Baum (Nutzer, 2026-11-07):** „Das ist kein Baum, es ist keine Hierarchie, es ist ein Repository, nur umgekehrt. Nicht du abonnierst etwas, sondern du lieferst.“ „Wenn ich jemandem erlaube, dass er auf meine Daten zugreifen kann, dann bekommt er eine Invitation und sein Server trägt ihn als Repository ein. Oder das Bild einer verketteten Liste.“
Also: Der andere muss mitbekommen, dass er darf, er muss es aber nicht bestätigen. Gegenseitig ist erlaubt, weil es kein Baum ist. Vorschlag: AS2 `Invite` als Nachricht.
**Weitergeben (Nutzer, 2026-11-07):** B darf das von A Gelieferte nur an C weitergeben, wenn A es ausdrücklich erlaubt. Einschränkung des Nutzers: „Wir können nichts tun, wenn jemand das dann abtippt und trotzdem weitergibt.“
**„Gehört zu“ bleibt (Nutzer, 2026-11-07):** innerhalb einer Organisation mit Eltern und ohne Zyklen; Folgen gilt zwischen Unabhängigen. Für „gehört zu“ bleibt die Zustimmung der Eltern vorläufig, die Absage an „beide müssen zustimmen“ galt dem Folgen.

## Einhängen einer Gruppe (früherer Stand: Nutzer dachte noch nach, Vorschlag Opus)
Nutzer: Wer sich einhängt, sagt, was der andere bei ihm darf. Sagt der andere nichts, darf man bei ihm nichts; er darf aber bei mir schauen. Meldet er sich auch, darf man bei ihm. Ob er mich trotzdem akzeptieren muss, ist offen.
**Vorschlag:** Rechte verschenken geht einseitig, nie mehr, als man selbst hat, und jederzeit widerrufbar; der andere sieht es und kann ablehnen. Die Verbindung im Baum (wer zu wem gehört) gilt erst, wenn beide zugestimmt haben, sonst könnte sich jede Gruppe als Teil einer anderen ausgeben.

## Später gesondert besprechen (Nutzer)
- **Zu viele Server:** Wenn jeder Kanidm hat, gibt es zu viele Server, und niemand will auf einen fremden. Idee Opus: Nur wer sich an einem Server anmelden muss, bekommt dort ein Konto; alle anderen kommen mit ihrer eigenen Identität vom eigenen Gerät (ADR 0029, 0035) und tragen dort nur Rechte.
- **Admin-Status nach Beteiligung:** Wer sehr oft dabei ist und etwas tut, könnte ihn bekommen. Die Idee bleibt erhalten, entschieden ist nichts.
- **Sicherheit und Recht bei KI:** Wer haftet, wenn eine KI etwas Strafbares übersieht oder falsch entscheidet? Rechtlich belangen lässt sie sich nicht. Zugleich kann sie viel früher eingreifen als ein Mensch.
  Und wäre sie Superuser und würfe alle hinaus, bliebe nur Neuinstallation, und alle Daten wären weg.

## Zu klären
- Ob nach „Trennung in zwei Einstellungen“ und „Zustimmung beider Seiten“ (Fragen B und C an den Nutzer) so gebaut wird.
- Wo die Daten eines Users liegen: `fs-people` oder Identitäts-Wrapper.
