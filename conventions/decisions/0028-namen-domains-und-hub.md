# 0028 – Namen, Domains und Erreichbarkeit über den Hub

Status: akzeptiert (2026-11-05) · technische Einzelheiten = Vorschlag · ADR 0019

## Kontext
Programme und Hub sind ohnehin Server. Sie sollen nicht nur lokal laufen, sondern auch übers Netz
(per WebAssembly als Website) — ein **freies Netz**, das jeder unter eigenem Namen betreiben kann.

## Entscheidung (Nutzer)
- **Standard-Domain: `freesynergy.net`** — „das Netz von FreeSynergy“. Gilt, wenn nichts eingegeben wird.
- **Der Hub verwaltet Namen und Erreichbarkeit** (kein weiterer Server): eigene DNS-Namen darauf
  zeigen lassen, bei einem Domain-Hoster anmelden, auch intern.
- Bei der Installation wird nach dem Namen gefragt; jedes Programm trägt seinen Namen beim Hub
  ein, der Hub veröffentlicht ihn. Wer den Namen ändert, schreibt sein eigenes Netz dorthin.

## Zwei verschiedene Namen (wichtig)
| | Zweck | Wert |
|---|---|---|
| **Instanz-Domain** | wo eine Instanz erreichbar ist, IRIs `https://<instanz>/…` | frei wählbar, Standard unter `freesynergy.net` |
| **Vokabular-Präfix** | wer ein eigenes Feld *definiert* hat (JSContact `<domain>:<name>`, RFC 9553 §1.8.1) | **immer `freesynergy.net`** — sonst hieße `lifecycle` auf jeder Instanz anders und niemand verstünde den anderen |

## Vorschlag zur Technik
- Lokal/LAN: mDNS + DNS-SD (RFC 6762/6763) — Hub und Programme finden sich ohne DNS-Server.
- Im Netz: eigener Name per DNS; Zertifikate per ACME (RFC 8555); Akteure auffindbar per WebFinger (RFC 7033).
- `freesynergy.net` als Standard-Netz: Unterdomain je Instanz (`<name>.freesynergy.net`), Eintrag
  über den Hub. ⚠️ Setzt voraus, dass `freesynergy.net` dem Projekt gehört — zu bestätigen.
