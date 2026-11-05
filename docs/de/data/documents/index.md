# Dokumente

**Jeder Text ist ein Wiki-Eintrag** (ADR 0031). Technisch gibt es vier Bausteine (ADR 0034) —
ob etwas ein Buch, eine Webseite, eine Ablage oder ein Protokoll ist, ist gleichgültig; EPUB, Markdown
und HTML sind **nur Exportformate**. Gespeichert als Original + AS2-Envelope + Aktivitätsprotokoll (ADR 0020, 0030).

| Baustein | Was | AS2-Envelope |
|----------|-----|--------------|
| **passage** | extrahierbarer, benannter Teil (wie ein Block); anderswo wiederverwendbar | benannte Markierung (ADR 0033) / Blocktyp |
| **page** | ein Dokument | `Article` (nicht `Page`: AS2-`Page` = eine Webseite) |
| **collection** | Gruppe von Seiten/Sammlungen, können einander referenzieren (Graph), sperrbar | `Collection` / `OrderedCollection` |
| **shelf** | unabhängige Instanz (eigener Speicher, eigene Rechte) | Instanzgrenze (ADR 0019/0028) |

**Markierung** (ADR 0033): ein Mechanismus für alle Daten — ein Punkt fügt ein (Variable, Serienbrief),
eine Spanne benennt/ersetzt (eigene Erklärung statt des Originals, das leiser gestellt wird, wiederverwendbare
Passage). Baut auf W3C Web Annotation.

Details: [standards.md](standards.md) · [technical.md](technical.md) · [examples.md](examples.md)

## Offene Punkte

- Eigene Specs: Block-Dokumentformat (neutraler Name, bei IETF/W3C einzureichen), Markierungsvokabular,
  Collection-Profil, Hilfe-Schlüssel
- Versionsgeschichte: nur Aktivitätsprotokoll, oder gitoxide darunter (Gespräch läuft)
- Parser/Highlighter für den Code-Editor: pures Rust, passend zu Blinc (Recherche läuft)
- Ziel: unsere eigene Dokumentation läuft in unserem Wiki statt in mkdocs (ADR 0031)
