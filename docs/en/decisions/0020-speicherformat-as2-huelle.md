# 0020 – Speicherformat: AS2-Hülle + Fachstandard + Aktivitätsprotokoll; Leihen = Live-Verweis

Status: akzeptiert (2026-11-05) · konkretisiert ADR 0014 · Protokoll §16, §17, §21.2

## Entscheidung
1. **Objekt = Hülle + Inhalt.**
   - *Hülle* (ActivityStreams 2.0): `id` (URI), `type`, `attributedTo`, `to`/`cc`/`bto`/`bcc`/
     `audience`, `published`, `updated`, `context`, Herkunft — als Spalten, damit abfragbar.
   - *Inhalt* = der Fachstandard (JSContact RFC 9553, JSCalendar RFC 8984, GeoJSON RFC 7946, …).
     Namen, Termine usw. liegen **immer** im Standard.
2. **Aktivitätsprotokoll**, nur anhängen: AS2-Aktivitäten (`Create`, `Update`, `Delete`, `Add`,
   `Remove`, `Offer`, `Accept`, `Reject`, `Undo`). Es ist zugleich Abgleich (ADR 0019), Verlauf
   und Freigabe.
3. **Adressierung (`to` …) ist Datenschutz-Angabe** am Objekt — wer es sehen soll.
4. **Leihen = Live-Verweis:** der Inhalt bleibt beim Verleiher, der Empfänger bekommt einen
   Verweis; Entziehen = Verweis ungültig (`Undo`). **Schenken** = Übergabe, neuer Besitzer,
   Herkunft bleibt vermerkt.
5. **Regeln werden angesagt, nicht erzwungen.** Was im Netz ist, kann kopiert, gehackt oder
   missbraucht werden (eine Einmal-Nachricht kann man abfotografieren). Wir sagen die Regeln an,
   an die man sich halten soll; Kandidat für die Form: ODRL (§17).

## Folgen
- `data/<domain>/standards.md` beschreibt je Domäne: Inhaltsstandard + AS2-Typ.
- Offene Feinheiten (Protokoll §18): Grabsteine, Konfliktzustand, Gruppen/Mitgliedschaft.
