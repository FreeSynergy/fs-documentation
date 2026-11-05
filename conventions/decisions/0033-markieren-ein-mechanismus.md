# 0033 – Markieren: ein Mechanismus für alles (Punkt = einsetzen, Bereich = ersetzen/benennen)

Status: akzeptiert (2026-11-05) · ersetzt den Vorschlag „zwei Motivationen“ (`fs:supplementing`,
`fs:superseding`) · Standard-Basis: W3C Web Annotation

## Kontext
Eigene Erklärungen neben Texten (ADR 0031) sind nur ein Fall. Der Nutzer will **alle Daten so
markieren können, dass sie einen Sinn bekommen** — wie Variablen im Serienbrief, in beide Richtungen.

## Entscheidung
Eine **Marke** = *Anker* + *Name* + *Typ* + optional *Wert*:
- **Anker = Punkt** (nichts markiert) → hier wird **eingesetzt** (Platzhalter/Variable; Serienbrief).
- **Anker = Bereich** (Text markiert) → dieser Inhalt wird **benannt** und kann **ersetzt** werden
  (eigene Erklärung statt Original — das Original bleibt, ist nur stumm; ADR 0031).
- **Name** = Variablenname; **Typ** = ein Datentyp aus dem Darstellungs-Register (ADR 0023), z. B.
  „Erklärung“, „Datum“, „Kontakt“, „Betrag“.
- Beide Richtungen: Variable hineinschreiben → wird mit Inhalt gefüllt; Inhalt markieren → bekommt
  einen Variablennamen und kann **woanders wieder eingesetzt** werden (Wiederverwendung, Transklusion).
- Gilt für **alle** Daten, nicht nur Texte.

## Technik
- W3C Web Annotation: Anker = Selector (Punkt = Position ohne Länge, Bereich = Quote/Position/Range,
  Bildbereich = `SvgSelector`); Name/Typ/Wert im Body. **Eine** eigene Motivation genügt
  (`freesynergy.net`-Vokabular, `skos:broader` auf eine Standard-Motivation); was passiert (einsetzen
  oder ersetzen), folgt aus dem Anker.
- Einsatz u. a.: Serienbriefe, Vorlagen, eigene Erklärungen, wiederverwendbare Absätze, Formulare.
