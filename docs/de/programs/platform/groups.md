# Gruppen

## Kurz gesagt

Gruppen hält fest, wer zusammengehört: eine Familie, ein Team, ein Verein, eine Abteilung innerhalb einer größeren. Es beantwortet auch, wer was darf. Du kannst Personen einladen, und nur die eingeladene Person kann annehmen.

## Was hier anders ist

- Gruppen funktionieren allein. Es ist kein Verzeichnisserver nötig. Wenn du einen wie Kanidm betreibst, kann Gruppen dessen Stand dorthin spiegeln, aber das Verzeichnis entscheidet nie.
- Gruppen können verschachtelt werden, und eine Gruppe kann mehrere Eltern haben. Eine Schleife wird abgelehnt, und die Antwort nennt den Pfad.
- Mitgliedschaft zählt über Verschachtelung, und die Antwort sagt, wie eine Person hineingekommen ist.
- KI-Agenten sind niemals Administratoren einer Gruppe.

## Wo es heute steht

Neueste Version: `v0.3.0`. Du kannst Gruppen anlegen, verschachteln und löschen, Mitglieder mit einer Rolle hinzufügen, Einladungen mit Ablaufdatum verschicken sowie Rechte delegieren und widerrufen. Es gibt noch kein Fenster und noch keinen Server. Delegierte Rechte beantworten nur Fragen; niemand setzt sie durch, und noch niemand ist authentifiziert. Einige Regeln sind noch vorläufig, während die Projektverantwortlichen sie entscheiden. Das Folgen zwischen Gruppen ist geplant, aber nicht gebaut.

`fs-groups`: Zusammengehören und entscheiden, wer was darf.

**Status: Kern `v0.3.0` in [`fs-groups`](https://github.com/FreeSynergy/fs-groups), kein Fenster; die Schnittstelle ist ein Entwurf in [`fs-interfaces`](https://github.com/FreeSynergy/fs-interfaces).** Zurück zum [Gesamtplan](../apps/roadmap.md).

## Warum es früh kommt

Aufgaben, Kontakte, Umfragen, Dateien und Freigaben hängen alle davon ab. ADR 0037 sagt, dass Ordner, Gruppe und Verteiler ein Konzept sind, und dieses Programm ist der Ort, an dem dieses Konzept lebt. Freigeben heißt dann, mit einer Gruppe zu teilen.

## Idee

- Gruppen können Gruppen enthalten. Eine Umfrage kann in einer kleinen Gruppe beginnen und sich auf eine übergeordnete Gruppe ausweiten.
- **Eine Person, die allein anfängt, und eine Gruppe nutzen dieselben Programme.** Jedes Objekt hat einen Besitzer, eine Person oder eine Gruppe, und es kann ohne Umwandlung von einem zum anderen wechseln.
- **Läuft ohne Kanidm.** Ein Programm muss allein funktionieren (ADR 0024). Ist Kanidm vorhanden, werden Gruppen dorthin gespiegelt.

## Daten

| Teil | Standard | Hinweise |
|------|----------|----------|
| Gruppe | AS2 `Group` | Actor, damit eine Gruppe handeln kann |
| Austausch | SCIM `Group` (RFC 7643) | Nur zum Spiegeln; Verschachtelung überträgt sich über SCIM zwischen Systemen nicht verlässlich |
| Rollen, Hierarchie, Einladungen | Lücke | Eigene Spezifikation |

## Maßgebliche Quelle

`fs-groups` entscheidet, welche Gruppen existieren und wer darin ist (ADR 0055). Ein Mitglied, das Kanidm in einer gespiegelten Gruppe hat, `fs-groups` aber nicht, wird bei der nächsten Synchronisierung entfernt.

## Rechte weitergeben

Jede Gruppe entscheidet selbst, ob ihre Rechte weitergegeben werden und in welche Richtung: gar nicht, an die Gruppen darunter oder an die Gruppen darüber (ADR 0055).

**In Kanidm werden Rechte immer von Kind zu Eltern weitergegeben.** Verschachtelung wird also nur dort gespiegelt, wo eine Gruppe ihre Rechte tatsächlich weitergibt; sonst bekommt Kanidm eine flache Liste. Diese Grenze gibt es nur in Kanidm (ADR 0056). Wenn du die andere Richtung brauchst, baue den Baum andersherum auf.

**Entschieden von der Projektverantwortlichen (2026-11-07): Folgen ist einseitig.** Wenn ich dir folge, entscheide ich, was du mit meinen Dingen tun darfst, und du musst das nicht bestätigen. Ich gebe nur Rechte weiter, die mir gehören, und nie mehr, als ich habe. Ich bekomme von dir nichts dadurch, dass ich dir folge.
**Der Code macht noch die ältere, sichere Lesart:** Hängt man eine Gruppe unter eine andere, braucht es die Zustimmung des Elternteils. Eine Gruppe auf „gar nicht“ gibt nie etwas weg, und im Zweifel ist die Antwort nein. **Folgen ist kein Baum (Projektverantwortliche, 2026-11-07).** Es ist keine Hierarchie. Es funktioniert wie ein Repository, nur umgekehrt: Du abonnierst nicht, du lieferst. Wenn ich dir Zugriff auf meine Daten gebe, bekommst du eine Einladung, und dein Server nimmt mich als Repository auf. Du musst lernen, dass du darfst, aber du musst es nicht bestätigen, und zwei Gruppen können einander folgen. Wer etwas empfängt, darf es nur weitergeben, wenn ich es erlaube, auch wenn nichts verhindern kann, dass jemand es abtippt. „Gehört zu“ mit Eltern bleibt, für innerhalb einer Organisation; Folgen ist für unabhängige Parteien. Noch nicht gebaut.

**Noch nicht durchgesetzt.** Das ist, was die Rechteprüfung beantwortet, keine Grenze, die jemand durchsetzt. Wer zustimmt, ist bisher nur ein Textfeld, niemand ist authentifiziert, und das Erteilen von Rechten ist ungeschützt. Durchsetzen braucht eine echte Identität über den Identitäts-Wrapper. `fs-groups` erwartet außerdem vorerst nur einen einzigen Schreiber.

## Administratoren

Wer das System installiert, ist der oberste Administrator. Innerhalb von Gruppen kann der Administrator auch andere zu Administratoren machen. **Ein KI-Agent kann niemals Administrator werden, erst recht nicht oberster Administrator** (ADR 0056). Administratorstatus für Menschen nach dem Grad ihrer Beteiligung zu vergeben, ist eine Idee, die wir behalten, aber keine Entscheidung.

## Wer Rechte bekommt

Jemand bekommt Rechte nur, wenn ein Administrator es erlaubt. Kanidm listet nur Personen auf, die tatsächlich die Rechte haben. Alle in Kanidm sind auch in `fs-people`, aber nicht alle in `fs-people` sind in Kanidm (ADR 0056).

## Was wir behalten, was Kanidm behält

Aus der [Kanidm-Recherche](https://github.com/FreeSynergy/fs-documentation/blob/main/temp/research/kanidm-control.md), Quelltext gelesen bei 1.13.0-dev:

| Bedarf | In Kanidm? | Also |
|--------|------------|------|
| Name, Mitglieder, Verschachtelung | Ja | Gespiegelt |
| Baum ohne Zyklen | Akzeptiert Zyklen | Wir erzwingen es |
| Typ, Eltern, Rollen, eigene Felder | Keine eigenen Attribute angeboten | Wird hier gehalten, über die Gruppen-ID zugeordnet |
| Einladungen | Nein (offenes Issue) | Unsere |
| Feinkörnige Delegation | Alles oder nichts | Unsere |
| Föderation zwischen Gruppen | Nein | Unsere (ADR 0035) |

Wenn Kanidm eines davon bekommt, geben wir es zurück, wie in ADR 0047 festgelegt.

## Offene Fragen

1. Muss eine Hierarchie ein Baum sein, oder kann eine Gruppe mehrere Eltern haben? **Bestätigt von der Projektverantwortlichen (2026-11-07):** Mehrere Eltern sind erlaubt, da eine Arbeitsgruppe zu zwei Abteilungen gehören kann; Zyklen werden abgelehnt.
2. Wer darf eine Umfrage auf eine übergeordnete Gruppe ausweiten: ihre Initiatoren oder die übergeordnete Gruppe?
3. Wie werden Entscheidungen über Gruppenmitgliedschaft getroffen? **Entschieden (2026-11-07):** Jede Gruppe legt es selbst fest: nur auf Einladung, offen für alle oder auf Antrag mit Bestätigung; eine Abstimmung über `fs-surveys` ist möglich, wo die Gruppe sie will.
