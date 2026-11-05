# 0019 – Datenhaltung: `fs-store` in jedem Programm, `fs-hub` pro Gerät

Status: akzeptiert (2026-11-05) · Abschnitt „Erkennung“ = Vorschlag, wartet auf Bestätigung ·
Turso-Details nach Recherche `temp/research/turso-sync.md` · Protokoll §3, §21.1

## Kontext
Jedes Programm soll allein laufen (lokal oder übers Web); wo das Programm ist, liegt seine
Datenbank. Mehrere Programme auf einem Gerät sollen sich die Arbeit teilen: ein Kontakt aus dem
PM wird mit einem Kontakt aus Contacts angeglichen, weil beide standardisiert sind (ADR 0014).

## Entscheidung
1. **`fs-store`** — eine Rust-Abstraktion für Objekte (lesen, schreiben, abfragen, abonnieren).
   Programme sprechen nie direkt SQL oder Turso. Erste Implementierung: Turso/libSQL, eingebettet.
   Weitere Backends möglich, auch eine **entfernte** Datenbank (dann über JSON/HTTPS statt lokal).
2. **Jedes Programm hat seine eigene Datenbank.** Ohne Hub speichert es nur lokal — wahlweise
   **verschlüsselt oder nicht** (Einstellung, wie bei Writer), siehe ADR 0024.
3. **`fs-hub`** — ein kleiner Dienst (Daemon) **einmal pro Gerät** (früher „der Server“, §3).
   Er sammelt die Objekte aller Programme in seiner eigenen Datenbank, führt Angleichungen
   durch und ist später der Punkt für Föderation/P2P zwischen Instanzen.
4. **Abgleich auf Objektebene**, nicht auf Zeilen/Seiten: Jedes Programm führt ein
   Aktivitätsprotokoll (ADR 0020); der Hub sammelt und verteilt es. Dieselbe Mechanik gilt
   zwischen Programm ↔ Hub und Instanz ↔ Instanz.
5. **Angleichen statt Verschmelzen:** Der Hub schlägt Gleichheit vor (gleiche E-Mail, Telefon,
   DID …), der Mensch bestätigt, dann entsteht eine Verknüpfung. Originale bleiben.

## Erkennung (Vorschlag)
- Programme **suchen einander nicht** — nur der Hub kennt alle (sonst wächst die Logik mit der
  Zahl der Programme quadratisch).
- Der Hub wird mit **jedem** Programm ausgeliefert, aber nur einmal installiert; er lauscht an
  einer festen Adresse (z. B. `$XDG_RUNTIME_DIR/freesynergy/hub.sock`) und wird bei Bedarf
  gestartet (Socket-Aktivierung).
- Ein Programm schaut beim Start nach dem Hub: **da** → anmelden mit Manifest (welche Datentypen
  es liest/schreibt) und Protokoll abgleichen; **nicht da** → allein arbeiten, Protokoll weiter
  führen, später nachreichen.
- Im Hub liegt nur verbindende Logik (sammeln, indexieren, angleichen, verteilen, föderieren),
  keine Fachlogik — die bleibt in den Programmen.

## Folgen
- Neue Repos `fs-store` und `fs-hub` (ADR 0017).
- Hub-Port/Socket festlegen; Kollision mit llama.cpp (8080) vermeiden.
- Turso-Sync wird höchstens als Transport genutzt; Konfliktregel und Freigaben liegen bei uns.
