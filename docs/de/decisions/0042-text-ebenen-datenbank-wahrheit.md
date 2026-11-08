# 0042 – Text + Ebenen; die Datenbank ist die Wahrheit, Dateien sind Exporte

Status: akzeptiert (2026-11-05) · präzisiert ADR 0020, 0030, 0031, 0033, 0034, 0039

## Kontext (Gespräch 2026-11-05)
Markdown-Dateien, Code und Block-Dokumente sollen ein Modell haben. Formatierung, Namen, Links,
Variablen und Erklärungen sollen als Ebenen über dem Text liegen, nicht im Text versteckt.

## Entscheidung
1. **Alles ist Text + Ebenen.** Eine `.md`-, `.rs`- oder sonstige Datei ist ein Block-Dokument mit
   **einem** Block, der auf den Text verweist. Code-Modus und Block-Modus sind zwei Ansichten
   desselben Modells.
2. **Ebenen** (Formatierung, Namen, Links, Variablen, eigene Erklärungen) sind Markierungen
   (ADR 0033) und liegen **nur in der Datenbank** — die Dateien bleiben sauber, nichts wird darin
   versteckt.
3. **`fs-store` ist die Wahrheit** für alle eigenen Texte: Text, Ebenen, Verlauf.
4. **Dateien sind Exporte**, geschrieben bei jedem Speichern (für Git, andere Programme, Compiler).
   Keine zusätzliche Kopie.
5. **Änderungen von außen** an einer exportierten Datei (anderer Editor, Git-Pull) sind ein
   **Import**: Vergleich mit dem Stand in der Datenbank, Unterschiede werden als normale Änderungen
   übernommen.
6. **Gelöschter Text nimmt seine Markierungen mit** — wie in jedem Editor; rückgängig machbar.
7. **Benannte Teile** werden mit ihrer Fundstelle in der Datenbank geführt (wiederverwendbar,
   einbindbar); Rückgängig entfernt sie wieder.
8. **Links:** im Text der lesbare Pfad; in der Datenbank eine **Link-Tabelle** (Quelle, Stelle,
   Ziel-UUID, Pfad, Titel). Beim Verschieben werden alle Links automatisch umgeschrieben;
   Rückverweise aus derselben Tabelle.
9. **Vorlagen:** Markdown mit Platzhaltern; Blöcke mit festen Teilen + Platzhaltern aus der
   Datenbank oder Eingabe (Eingabe geht in Datenbank und Dokument zugleich).
10. **Rückgängig ist dauerhaft** (Aktivitätsprotokoll, ADR 0020) — übersteht Neustarts —, aber
    **begrenzt**, damit die Datenbank nicht volläuft:
    - Die Menschen wählen selbst: **zeitlich** (z. B. 30 Tage), **nach Anzahl** (z. B. 500 Schritte)
      oder **beides**.
    - Ältere Schritte werden zusammengefasst (der aktuelle Stand bleibt, nur die Zwischenschritte
      fallen weg); was für den Abgleich mit dem Hub noch gebraucht wird, bleibt bis zum Abgleich.
    - **Beim Speichern wird daran erinnert**, dass man den Rückgängig-Verlauf zurücksetzen kann
      (Nutzer). *Hinweis Opus:* unaufdringlich zeigen (z. B. Anzeige der Verlaufsgröße), damit es
      nicht bei jedem Speichern stört.
11. Was **von außen empfangen** wird (Mail, vCard-Import …), bleibt unverändert als Original (ADR 0030).
