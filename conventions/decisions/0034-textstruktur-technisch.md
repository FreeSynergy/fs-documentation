# 0034 – Textstruktur technisch denken: Absatz, Seite, Kollektion, Regal

Status: akzeptiert (2026-11-05) · präzisiert ADR 0031

## Kontext
„Seite, Buch, Bibliothek“ war ein Bild. Technisch spielt es keine Rolle, ob etwas ein Buch, eine
Webseite, eine Buchführung oder ein Log ist. EPUB, Markdown, HTML sind **nur Exportformate**.

## Entscheidung
Vier technische Bausteine:

| Baustein | Was | Beispiel |
|----------|-----|----------|
| **Absatz** | extrahierbarer, benannter Teil (wie ein Block); markieren → als Absatz definieren → Namen geben → anderswo wieder einsetzen (ADR 0033) | Warnhinweis, der in zehn Hilfetexten steht |
| **Seite** | ein Dokument (jede Wiki-Seite) | Hilfe-Eintrag, Protokoll, Rechnungstext |
| **Kollektion** | Gruppe von Seiten/Kollektionen; Kollektionen **können aufeinander verweisen** (Graph, kein starrer Baum); kann **gesperrt** werden | Handbuch, Buchführungsjahr, Log eines Dienstes |
| **Regal** | **unabhängige Instanz** (eigener Speicher, eigene Rechte) | Bibliothek des Vereins, Hilfe-Bibliothek der Programme |

- Bücher, Kapitel, Webseiten sind **Sichten/Exporte** darauf, keine eigenen Datentypen.
- AS2: Seite = `Article`; Kollektion = `Collection`/`OrderedCollection`; Absatz = benannte Marke
  (ADR 0033) bzw. eigener Typ in der Block-Spezifikation; Regal = Instanz-Grenze (ADR 0019/0028).
- schema.org `Book`/`Chapter`, EPUB 3.3, Markdown nur bei Export/Import.

## Folgen
- Eigene Spezifikation für den Blockinhalt (Arbeitstitel siehe `data/documents/standards.md`) mit
  neutralem Namen, damit sie bei IETF/W3C eingereicht werden kann.
