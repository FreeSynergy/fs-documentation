# 0029 – Schutzbedürftige Daten müssen gekennzeichnet werden

Status: akzeptiert (2026-11-05) · Form der Kennzeichnung = Vorschlag · ADR 0019, 0020

## Kontext
Verknüpfen (gleiche Person in mehreren Programmen, `owl:sameAs`) soll es geben. Aber manche Daten
können Leben gefährden: sexuelle Orientierung aus einem Dating-Portal kann in Uganda die
Todesstrafe bedeuten. Verknüpfung + solche Daten = Gefahr.

## Entscheidung (Nutzer)
- Schutzbedürftige Daten **dürfen** gespeichert werden, **müssen** aber **gekennzeichnet** sein.
- Gleichheit zweier Kontakte heißt technisch `owl:sameAs` (AS2 `Relationship`).
- Absicherung ist mehrfach: OAuth/SSO (Login) + DID (Identität) + Web of Trust (Vertrauen) —
  die Kombination macht es; paarweise DIDs (RLTP) sind gewollt.

## Vorschlag zur Umsetzung
- Kennzeichnung je **Feld oder Objekt** mit Kategorien der besonders geschützten Daten
  (DSGVO Art. 9: sexuelle Orientierung, Gesundheit, Religion, politische Meinung, Herkunft, …);
  Vokabular-Kandidat: W3C **Data Privacy Vocabulary (DPV)** ⚠️ ungeprüft.
- Gekennzeichnete Daten:
  1. werden **nie automatisch** verknüpft — der Hub schlägt keine `owl:sameAs`-Verbindung vor, die
     sie mit anderen Kontexten zusammenführt;
  2. verlassen das Gerät nur mit **ausdrücklicher** Freigabe je Empfänger;
  3. sind standardmäßig **verschlüsselt** gespeichert (ADR 0024);
  4. werden in Frontends sichtbar markiert.
