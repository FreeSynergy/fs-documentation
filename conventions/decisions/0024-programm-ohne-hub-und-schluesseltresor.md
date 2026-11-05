# 0024 – Programm ohne Hub: lokale Daten, Verschlüsselung, Schlüsseltresor, SCIM

Status: akzeptiert (2026-11-05) · Protokoll §3, §21.3 · ADR 0015, 0019

## Entscheidung
- Ein Programm **ohne Hub** speichert lokal, **wahlweise verschlüsselt** (Einstellung).
- **Schlüsseltresor** (eigene Workbench und/oder eigenes Programm, noch zu bauen): nimmt die
  Schlüssel auf; kann sie mit Kanidm abgleichen oder nicht — dann nur auf diesem Rechner.
- **Jedes Programm kann OAuth2, SSO und SCIM** von Haus aus, ohne Umweg.
- Wer Daten hinter einer Wand (Firewall, Mehrbenutzer) betreiben will, installiert den Server
  (Hub + Kanidm). **Mehrere Mandanten in einer Instanz** über OAuth2/SSO — mehrere Instanzen sind
  möglich, aber nicht nötig (Korrektur 2026-11-05). Kanidm läuft im Server und wird über seine
  REST-API gesteuert; was Kanidm (noch) nicht kann, programmieren wir dazu.
- **Niemals Paywall** (ADR 0016).
- Zwischen Instanzen: **DID** als Identität, **Web of Trust** als Vertrauensstufen; Föderation
  über Listen, die wie ein Identity-Broker sagen, was Menschen/Gruppen dürfen — je mehr
  Vertrauen, desto mehr Freigaberegeln.

## Folgen
- Neue Kategorie für den Schlüsseltresor (Programm und/oder Workbench) planen.
- Befund 2026-11-05 (`temp/research/geodata-projects-profile-login.md`): **Kanidm 1.12** kann SCIM nur
  als *Eingang* (Sync-Quelle), nicht als Provisionierungs-Server, und kein OpenID Federation →
  eigener SCIM-Server im Hub; Föderation zwischen Instanzen: **OpenID Federation 1.0** (final
  2026-02-17, Trust Anchors/Chains/Marks) als Kandidat — Vorschlag, wartet auf Entscheidung.
