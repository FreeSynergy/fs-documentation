# 0021 – Schnittstelle: ein Vertrag, viele Zugänge

Status: akzeptiert (2026-11-05) · Protokoll §9, §21.5

## Entscheidung
- **Daten:** Standards sind die Quelle der Wahrheit (ADR 0014).
- **Schnittstelle:** das schnellste Transportformat ist die Quelle der Wahrheit — **Cap'n Proto**
  (Schema mit eingebauten Regeln, wie man erweitert, ohne zu brechen). JSON-API, CLI und
  MCP-Tools werden **daraus erzeugt**, nicht von Hand parallel gepflegt.
- Programm ↔ Frontend wie Backend ↔ Frontend im Web, nur lokal (Unix-Socket / Named Pipe);
  entfernt über JSON/HTTPS.
- Für alles andere: **Voreinstellungen und Empfehlungen**, damit Menschen es einfach haben.
- Ein **Frontend ist ein Paket** mit Manifest (benötigte Fähigkeiten, Vertragsversion);
  installieren → es ist da. Das Programm bietet Fähigkeiten an; das Frontend nutzt sie oder nicht
  (Mails nur anzeigen und wegwischen ↔ voller Outlook-Nachbau mit Matrix und Telegram).

## Erweiterung für MCP (Nutzer, 2026-11-07)
- **Risikomarken im Vertrag,** je Methode und Union-Mitglied, gesetzt von der Engine und nie vom Aufrufer.
- **Ereignisse und Dateien** werden MCP-Ressourcen, keine Werkzeuge.
- **Geheimnisse sind von der Erzeugung ausgeschlossen:** Für sie entsteht kein Werkzeug und keine Ressource.
- **Lesen ist nicht harmlos,** siehe ADR 0054, Abschnitt „Lesen ist nicht harmlos“. Der MCP-Hinweis `readOnlyHint` sagt nichts darüber, ob etwas gefahrlos ist.

## Folgen
- Fähigkeitenliste (Protokoll §9) wird aus dem Schema erzeugt und ist über API/CLI/MCP abfragbar.
