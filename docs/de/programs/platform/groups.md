# Gruppen

`fs-groups`: Zusammengehören und entscheiden, wer was darf.

**Status: geplant, noch kein Code (2026-11-06).** Zurück zum [Gesamtplan](../apps/roadmap.md).

## Warum es früh kommt

Aufgaben, Kontakte, Umfragen, Dateien und Freigaben hängen alle davon ab. ADR 0037 sagt, dass Ordner, Gruppe und Verteiler ein Konzept sind, und dieses Programm ist der Ort, an dem dieses Konzept lebt. Freigeben heißt dann, mit einer Gruppe zu teilen.

## Idee

- Gruppen können Gruppen enthalten. Eine Umfrage kann in einer kleinen Gruppe beginnen und sich auf eine übergeordnete Gruppe ausweiten.
- **Eine Person, die allein anfängt, und eine Gruppe nutzen dieselben Programme.** Jedes Objekt hat einen Besitzer, eine Person oder eine Gruppe, und es kann ohne jede Umwandlung von einem zum anderen wechseln.
- **Läuft ohne Kanidm.** Ein Programm muss allein funktionieren (ADR 0024). Ist Kanidm vorhanden, werden Gruppen dorthin gespiegelt.

## Daten

| Teil | Standard | Hinweise |
|------|----------|----------|
| Gruppe | AS2 `Group` | Actor, damit eine Gruppe handeln kann |
| Austausch | SCIM `Group` (RFC 7643) | Nur zum Spiegeln; Verschachtelung überträgt sich über SCIM zwischen Systemen nicht zuverlässig |
| Rollen, Hierarchie, Einladungen | Lücke | Eigene Spezifikation |

## Was wir behalten, was Kanidm behält

Aus der [Kanidm-Recherche](https://github.com/FreeSynergy/fs-documentation/blob/main/temp/research/kanidm-control.md), Quelltext gelesen bei 1.13.0-dev:

| Bedarf | In Kanidm? | Also |
|--------|------------|------|
| Name, Mitglieder, Verschachtelung | Ja | Gespiegelt |
| Baum ohne Zyklen | Akzeptiert Zyklen | Wir erzwingen es |
| Typ, übergeordnete Gruppe, Rollen, eigene Felder | Nein, keine eigenen Attribute angeboten | Wird hier gehalten, über die Gruppen-ID zugeordnet |
| Einladungen | Nein (offenes Issue) | Unsere |
| Feinkörnige Delegation | Alles oder nichts | Unsere |
| Föderation zwischen Gruppen | Nein | Unsere (ADR 0035) |

Gewinnt Kanidm eines davon, geben wir es zurück, wie in ADR 0047 festgelegt.

## Offene Fragen

1. Muss eine Hierarchie ein Baum sein, oder kann eine Gruppe mehrere Eltern haben? Eine Arbeitsgruppe kann zu zwei Abteilungen gehören.
2. Wer darf eine Umfrage auf eine übergeordnete Gruppe ausweiten: ihre Initiatoren oder die übergeordnete Gruppe?
3. Wie werden Entscheidungen über Gruppenmitgliedschaft getroffen: durch Ernennung oder durch eine Abstimmung mit `fs-surveys`?
