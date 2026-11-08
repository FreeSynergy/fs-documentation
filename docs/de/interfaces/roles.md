# Rollen einer Person

**Status: Entwurf (2026-11-06), erster Anbieter in [`fs-people`](https://github.com/FreeSynergy/fs-people) v0.2.0.** Zurück zu den [Schnittstellen](index.md). ADR 0052.

## Idee

`fs-people` hält Personen. Eine Person gibt es einmal, egal wie viele Dinge sie für andere ist. Dieselbe Frau kann mein Kontakt, meine Kundin und eine Nutzerin eines Systems sein, ohne dreimal zu existieren. Sie hat einen Datensatz und mehrere **Rollen**.

Rollen folgen Standards, wo es einen gibt, und sie werden öffentlich definiert, bevor Programme sie nutzen. Jeder kann auch **eine eigene Rolle genauso definieren** wie unsere: Eine Rolle, die du machst, ist nicht zweitklassig.

## Zwei verschiedene Dinge

| Art | Frage | Standard |
|------|----------|----------|
| **Beziehung** | Was ist diese Person für mich? | vCard `RELATED` (RFC 6350 §6.6.6), JSContact `relatedTo` |
| **Rolle** | Was ist diese Person innerhalb einer Gruppe oder Organisation? | W3C Organization Ontology: `org:Role`, `org:Membership` (Recommendation, 2014) |

## Wo eine Rolle gespeichert wird

Eine Rollenzuordnung ist ein **eigenes Objekt** (AS2 `Relationship`), nie Teil der Karte der Person. So kann kein Export einer Karte eine Rolle verraten.

`fs-people` liefert bisher vier Rollendefinitionen: `ai`, `user`, `member` und `customer`. Lieferant, Angestellte und Ehrenamtliche sind recherchiert (siehe Tabelle unten), aber noch nicht ausgeliefert.

## Bekannte Rollen und Beziehungen

| Name | Art | Standard | Besitzer | Stand |
|------|------|----------|-------|-------|
| Kontakt, Freund, Bekannter, Kollege, Mitarbeiter-Kollege, Nachbar, Familie, Notfallkontakt | Beziehung | vCard-`RELATED`-Typen `contact`, `friend`, `acquaintance`, `colleague`, `co-worker`, `neighbor`, `kin`, `child`, `parent`, `sibling`, `spouse`, `emergency` | `fs-people` | Standard |
| Freund, Partner | Beziehung, persönlich und privat (ADR 0029) | vCard-`RELATED`-Typen `friend`, `spouse`, `sweetheart` (RFC 6350 §6.6.6) | `fs-people` | Standard. Welche Begriffe wir für eine Partnerschaft anbieten, ist noch zu klären |
| Mitglied oder Amtsträger eines Vereins oder Verbands | Rolle | `org:Role` mit `org:Membership` passt als Form; ❌ bisher kein eigener Begriff für einen Verein gefunden, nicht tiefer recherchiert | `fs-groups` | Noch zu recherchieren |
| Nutzer | Rolle | SCIM `User` (RFC 7643); Kanidm | `fs-people` konfiguriert Nutzer (ADR 0055); wie das mit dem Identitäts-Wrapper zusammenhängt, ist offen | Standard |
| Mitglied einer Gruppe | Rolle | `org:Membership`, AS2 `Group`, SCIM `Group` | `fs-groups` | Standard |
| Kunde | Rolle | Begriffe für eine Partei in einem Verkauf: UBL 2.3 `CustomerParty` (§2.4), schema.org `customer` (bei `Order` und `Invoice`), FIBO `Customer`. ❌ Kein Standard für Kunde als dauerhafte Rolle einer Person. Weder in vCard, JSContact, SCIM noch in `org` | später CRM | **Begriff vorhanden, Rolle ist eine Lücke: eigene Spezifikation** |
| Lead, Interessent | Rolle | ❌ nichts gefunden. Nur Anbieter, etwa die Lebenszyklus-Stufe von HubSpot. Kein Begriff in schema.org, UBL, FIBOs Produkt-Ontologie, vCard, JSContact oder SCIM | später CRM | **Lücke, eigene Spezifikation** |
| KI | markierter Teilnehmer, damit alle wissen, dass er kein Mensch ist; nennt die Person, die ihn betreibt (ADR 0054) | JSContact `kind` `application` (RFC 9553 §2.1.4); die Verbindung zum Betreiber ist noch eine Lücke | `fs-people` | Art bestätigt, Betreiber offen |
| Lieferant | Rolle | Begriffe für eine Partei in einem Verkauf: UBL 2.3 `SupplierParty` (§2.4), FIBO `Supplier`. schema.org hat nur `seller` und keinen Lieferanten-Begriff. ❌ Kein Standard für Lieferant als dauerhafte Rolle einer Person | später ERP | **Begriff vorhanden, Rolle ist eine Lücke: eigene Spezifikation** |
| Angestellte/r | Rolle | `org:Role` mit `org:Membership` (die Ontologie nennt Gehalt und Arbeitsvertrag, §2.2); schema.org `EmployeeRole`; SCIM `userType` (RFC 7643 §4.1.1) und die Enterprise-Erweiterung (§4.3); LDAP `employeeType` (RFC 2798 §2.5). In SCIM und LDAP ist der Wert freier Text. Bedeutung: ILO ICSE-18 | später ERP | Standard |
| Ehrenamtliche/r | Rolle | `org:Role` passt als Form, hat aber keinen Begriff für Ehrenamt. Bedeutung: ILO, 19. ICLS (2013), nur für Statistik. ❌ Kein Datenstandard für eine Person als Ehrenamtliche/r. Eine britische Ontologie (volunteeringdata.io) beschreibt Angebote, nicht Personen | andere, später | **Lücke, eigene Spezifikation** |

## Eine Rolle selbst definieren

`org:Role` ist eine Unterklasse von `skos:Concept` (`org` §5.3.5). Eine Rolle ist also ein beschriebenes Konzept. Die Ontologie erlaubt zusätzliche Eigenschaften über „Erweiterungsvokabulare“ (§5.3.5) und Profile, die Begriffe ergänzen (§3).

**Vom Projektinhaber entschieden (2026-11-07).** Innerhalb unserer Programme reist eine Rolle über Cap'n Proto (`people.capnp`), das auch von außen genutzt werden kann. Für alle anderen gibt es JSON-LD, weil das der Standard ist. Eine Rollendatei ist ein SKOS-Konzeptschema, geschrieben als JSON-LD. Unsere und deine haben dasselbe Format. Nur die Basisadresse unterscheidet sich, und die volle ID jeder Rolle ist diese Basis plus ihre kurze ID.

| Feld | Bedeutung | Entspricht |
|-------|---------|-----------|
| `id` | kurze ID, eindeutig in der Datei | `@id`, relativ zur Basis der Datei |
| `type` | `org:Role` für eine Rolle innerhalb einer Organisation, sonst `skos:Concept` | `@type` |
| `names` | Name je Sprache | `skos:prefLabel` |
| `description` | Klartext je Sprache | `skos:definition` |
| `broader` | optional: die allgemeinere Rolle, auch in einer anderen Datei | `skos:broader` |
| `closeMatch` | optional: dieselbe Idee in einer anderen Datei | `skos:closeMatch` |
| `standard` | der Standard, dem sie folgt, als Text; keiner bedeutet eine Lücke | `skos:note` |
| `standardRefs` | optional: Adressen der Begriffe des Standards | `rdfs:seeAlso` |
| `fields` | was bei einer Person in dieser Rolle zusätzlich gilt; jedes Feld nennt seinen Standard oder sagt, dass es keinen gibt | eigener Begriff `fs:roleField` |
| `owner` | das Programm, das dafür verantwortlich ist | eigener Begriff `fs:roleOwner` |
| `scope` | `personal`, `group` oder `public` | eigener Begriff `fs:roleScope` |
| `cardKind` | optional: das JSContact-`kind`, das Karten mit dieser Rolle haben müssen | eigener Begriff `fs:cardKind` |

Unsere Rolle:

```json
{
  "@context": ["https://freesynergy.net/ns/roles.jsonld",
               {"@base": "https://freesynergy.net/ns/roles/"}],
  "id": "",
  "type": "skos:ConceptScheme",
  "names": {"en": "FreeSynergy roles"},
  "roles": [{
    "id": "employee",
    "type": "org:Role",
    "names": {"en": "Employee", "de": "Mitarbeiter"},
    "description": {"en": "Someone who works for pay in an organisation."},
    "standard": "org:Role; schema.org EmployeeRole",
    "standardRefs": ["https://schema.org/EmployeeRole"],
    "fields": [{"name": "employeeNumber",
                "standard": "SCIM enterprise User (RFC 7643, section 4.3)"}],
    "owner": "ERP (later)",
    "scope": "group"
  }]
}
```

Deine Rolle, in einer Datei derselben Form:

```json
{
  "@context": ["https://freesynergy.net/ns/roles.jsonld",
               {"@base": "https://<instance>/roles/kal/"}],
  "id": "",
  "type": "skos:ConceptScheme",
  "names": {"de": "Meine Rollen"},
  "roles": [{
    "id": "treasurer",
    "type": "org:Role",
    "names": {"de": "Kassenwart"},
    "broader": "https://freesynergy.net/ns/roles/member",
    "owner": "kal",
    "scope": "personal"
  }]
}
```

Die Kontextdatei `roles.jsonld` gibt es noch nicht.

**Was dieser Vorschlag ändern würde.** Alle vier Definitionen in `known.json` behalten ihre Felder. Ein Test mit einem JSON-LD-Parser hat sie unverändert gelesen. Diese Dinge würden sich ändern:

- Die Datei wird ein Objekt für das Schema statt eines Arrays.
- Rollen werden über ihre volle ID gefunden. Heute ist `id` allein der Schlüssel, deshalb würde deine `customer` mit unserer kollidieren.
- Deine Datei muss neben unserer bestehen können. Heute ersetzt das Laden einer Datei alle Definitionen.
- `owner` enthält heute Platzhaltertext (`CRM (later)`), keine ID.

**Zuordnungen (Vorschlag).** Eine Rollenzuordnung nennt die Rolle über ihre volle ID. Eine Rolle vom Typ `org:Role` wird zusätzlich zum AS2-`Relationship` als `org:Membership` exportiert, weil `org` §3 keine anderen Begriffe anstelle der eigenen erlaubt, wo diese passen. Eine persönliche Rolle hat keine Organisation, deshalb ist sie nur ein `Relationship`.

**Nicht abgedeckt.** Kein hier gelesener Standard legt die Felder einer Rolle, ihren Besitzer oder ihren Geltungsbereich fest, deshalb sind das unsere eigenen Begriffe. Wertetypen für Felder sind noch nicht festgelegt. SHACL (W3C) ist ein Kandidat, ist aber noch nicht gelesen.

Definitionen sind Konfiguration, können also hinzugefügt werden, während die Programme laufen, und über ein git-Repository geteilt werden (ADR 0036, 0045).

## Entschieden (Projektinhaber, 2026-11-07)

1. **Format:** SKOS, mit Cap'n Proto im Inneren und auch von außen nutzbar, und JSON-LD nach außen als Standard. Dafür ist eine Änderung in `fs-people` nötig.
2. **Adresse:** `https://freesynergy.net/ns/roles/` ist die Basis unserer Rollen. Der Projektinhaber hält diese Domain. Bestehende Beispiele, die `https://freesynergy.net/ns#` verwenden, müssen noch geändert werden.
3. **Kunde und Lieferant:** `org:Role` meint eine Rolle „in einer Organisation“ (§5.3.5), und ein Kunde oder Lieferant steht außerhalb davon. Diese beiden haben den Typ `skos:Concept`.
4. **Firmen:** `fs-people` führt für diese beiden Rollen auch Karten der Art `org`.
5. **Lead und Interessent:** drei Rollen (Lead, Interessent, Kunde), nicht eine Rolle mit einer Stufe. Ein Lead ist keine Art von Kunde, und eine Person wechselt, indem sie eine Zuordnung beendet und die nächste beginnt.
6. **Mehr als Geschäft:** wir decken auch Vereine und Verbände, Freundschaften und Partnerschaften ab, also auch das persönliche und private Leben. Siehe die Tabelle oben.

## Offen

1. **Ist das Format der Rollendefinition selbst ein Standard?** Antwort: teilweise. SKOS ist eine W3C-Recommendation (2009) und deckt ID, Namen, Beschreibung, Hierarchie und Zuordnung ab (SKOS Reference §3 bis §10). `org:Role` ist bereits ein `skos:Concept`, also passt SKOS als Grundlage. SKOS hat keine eigene JSON-Form und wird als RDF ausgedrückt (§1.3). JSON-LD 1.1 (W3C Recommendation, 2020) gibt ihm eine, und seine Sprachzuordnungen (§4.6.2) haben dieselbe Form wie unsere `names`. SKOS deckt Felder, Besitzer und Geltungsbereich nicht ab. SKOS ist nicht als formale Wissenssprache gedacht (§1.3), beschreibt also eine Rolle und erzwingt nichts. Das Format oben ist unser eigenes Profil dieser Standards (`org` §3), kein Standard selbst. Es ist ein Vorschlag.
2. **Wem gehören Kundendaten:** dem Programm, das die Rolle hat, oder `fs-people`? Wir schlagen vor, dass `fs-people` die Person hält und der Besitzer jeder Rolle deren Felder hält.
3. **Sicherheit:** eine Rolle darf nie durchsickern. Dass ich jemandes Kunde bin, geht nicht alle etwas an (ADR 0029). **Bekannte Lücke:** der Hub entscheidet nach Objekttyp, also könnte ein Programm, das den Typ `Relationship` lesen darf, darüber Rollenzuordnungen sehen. Das gehört zur Freigabe-Schnittstelle und ist noch nicht gelöst.
