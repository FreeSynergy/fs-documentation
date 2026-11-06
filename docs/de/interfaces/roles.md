# Rollen einer Person

**Status: Entwurf (2026-11-06).** Zurück zu den [Schnittstellen](index.md). ADR 0052.

## Idee

`fs-people` hält Personen. Es gibt eine Person, einmal, egal wie viele Dinge sie für andere ist. Dieselbe Frau kann mein Kontakt, meine Kundin und Nutzerin eines Systems sein, ohne dreimal zu existieren. Sie hat einen Datensatz und mehrere **Rollen**.

Rollen folgen Standards, wo es einen gibt, und sie werden öffentlich definiert, bevor Programme sie nutzen. Jeder kann auch eine **eigene Rolle genau auf dieselbe Weise definieren** wie wir: Eine selbst angelegte Rolle ist keine Rolle zweiter Klasse.

## Zwei verschiedene Dinge

| Art | Frage | Standard |
|-----|-------|----------|
| **Beziehung** | Was ist diese Person für mich? | vCard `RELATED` (RFC 6350 §6.6.6), JSContact `relatedTo` |
| **Rolle** | Was ist diese Person innerhalb einer Gruppe oder Organisation? | W3C Organization Ontology: `org:Role`, `org:Membership` (Recommendation, 2014) |

## Bekannte Rollen und Beziehungen

| Name | Art | Standard | Besitzer | Stand |
|------|-----|----------|----------|-------|
| Kontakt, Freundschaft, Bekanntschaft, Kollegin, Mitarbeitende, Nachbarschaft, Familie, Notfallkontakt | Beziehung | vCard `RELATED`-Typen `contact`, `friend`, `acquaintance`, `colleague`, `co-worker`, `neighbor`, `kin`, `child`, `parent`, `sibling`, `spouse`, `emergency` | `fs-people` | Standard |
| Benutzer | Rolle | SCIM `User` (RFC 7643); Kanidm | Identitäts-Wrapper | Standard |
| Mitglied einer Gruppe | Rolle | `org:Membership`, AS2 `Group`, SCIM `Group` | `fs-groups` | Standard |
| Kunde, Lead, Interessent | Rolle | ❌ keiner in vCard oder JSContact gefunden; bisher eine Herstellereigenschaft (`lifecycle`) | Später CRM | **Lücke, eigene Spezifikation** |
| Lieferant, Angestellter, Ehrenamtlicher | Rolle | Noch zu recherchieren | Später ERP, andere | Offen |

## Eine Rolle selbst definieren

Nach `org:Role` ist eine Rolle ein beschriebenes Konzept, und die Ontologie erwartet, dass Fachgebiete ihre eigenen mitbringen. Eine Rollendefinition ist ein Objekt, sowohl für unsere als auch für selbst angelegte Rollen:

| Feld | Bedeutung |
|------|-----------|
| Id, Name, Beschreibung | Was die Rolle ist, in einfachen Worten und in mehreren Sprachen |
| Standard | Der Standard, dem sie folgt, falls vorhanden |
| Felder | Was bei einer Person in dieser Rolle zusätzlich gilt; jedes Feld nennt seinen Standard oder sagt, dass es keinen hat |
| Besitzer | Das Programm, das dafür verantwortlich ist |
| Geltungsbereich | Persönlich, eine Gruppe oder für alle veröffentlicht |

Definitionen sind Konfiguration. Sie können also hinzugefügt werden, während Programme laufen, und über ein git-Repository geteilt werden (ADR 0036, 0045).

## Offen

1. **Ist das Format der Rollendefinition selbst ein Standard?** Kandidaten: SKOS (worauf `org:Role` aufbaut). Noch nicht gelesen.
2. **Wem gehören die Kundendaten:** dem Programm, das die Rolle hat, oder `fs-people`? Wir schlagen vor, dass `fs-people` die Person hält und der Besitzer jeder Rolle deren Felder.
3. **Sicherheit:** Eine Rolle darf nie durchsickern. Dass ich jemandes Kunde bin, geht nicht alle etwas an (ADR 0029).
