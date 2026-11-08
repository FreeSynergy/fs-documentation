# 0014 – Standards zuerst, ActivityStreams 2.0 als gemeinsame Basis

Status: akzeptiert (2026-11-05) · festigt ADR 0006 Punkt 3.2 und Protokoll §3

## Kontext
Jedes Programm soll allein laufen und trotzdem an alle Daten der anderen kommen (ein Kontakt ist
in Messenger, Projektmanagement und ERP derselbe). Das geht nur, wenn die Daten in offenen
Standards liegen, die auch andere Software lesen kann.

## Entscheidung
1. **Gibt es einen Standard, wird er benutzt.** Eigene Formate nur, wo keiner existiert.
2. **ActivityStreams 2.0 (W3C, AS2)** ist die gemeinsame Basis: Objekte, Akteure und Aktivitäten
   (wer hat was mit welchem Objekt getan). Fachstandards wie JSContact (RFC 9553) oder
   JSCalendar (RFC 8984) liefern den **Inhalt** eines Objekts, AS2 die **Hülle** und die
   Aktivitäten. Die genaue Abbildung je Domäne steht in `data/<domain>/standards.md`.
3. **Fehlt ein Standard**, schreiben wir eine eigene Spezifikation in `data/` (offen, versioniert)
   und reichen sie, wenn sie trägt, als **Internet-Draft (IETF)** oder **W3C Community Group**
   ein. Kandidaten werden in `data/standards.md` unter „Gaps“ gesammelt.
4. Die Wahl eines Standards geht vor die Wahl eines Crates (Brückenprinzip, ADR 0006).

## Folgen
- `data/standards.md` bekommt die Spalte „AS2-Abbildung“ und den Abschnitt „Gaps“.
- Pro Datendomäne (contacts, events, messages, identity, geodata, projects, profile, login) ist
  die AS2-Abbildung offen und kommt in den Plan (Phase 2).
- Details zur Datenhaltung (zentral/pro Programm, Protokoll §3) bespricht der Nutzer gesondert.
