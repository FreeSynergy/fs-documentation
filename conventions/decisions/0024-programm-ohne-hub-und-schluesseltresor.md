# 0024 – Programm ohne Hub: lokale Daten, Verschlüsselung, Schlüsseltresor, SCIM

Status: akzeptiert (2026-11-05) · Protokoll §3, §21.3 · ADR 0015, 0019

## Entscheidung
- Ein Programm **ohne Hub** speichert lokal, **wahlweise verschlüsselt** (Einstellung).
- **Schlüsseltresor** (eigene Workbench und/oder eigenes Programm, noch zu bauen): nimmt die
  Schlüssel auf; kann sie mit Kanidm abgleichen oder nicht — dann nur auf diesem Rechner.
- **Jedes Programm kann OAuth2, SSO und SCIM** von Haus aus, ohne Umweg.
- Wer Daten hinter einer Wand (Firewall, Mehrbenutzer) betreiben will, installiert den Server
  (Hub + Kanidm). Mehrmandantenfähigkeit = **Instanzen**, nicht Mandanten in einer Instanz.
- **Niemals Paywall** (ADR 0016).
- Zwischen Instanzen: **DID** als Identität, **Web of Trust** als Vertrauensstufen; Föderation
  über Listen, die wie ein Identity-Broker sagen, was Menschen/Gruppen dürfen — je mehr
  Vertrauen, desto mehr Freigaberegeln.

## Folgen
- Neue Kategorie für den Schlüsseltresor (Programm und/oder Workbench) planen.
