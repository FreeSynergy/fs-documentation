# KAddressBook - API Dokumentation

## Übersicht

KAddressBook ist Client — es stellt **keine API** bereit. Programmiert wird gegen die KDE-Bibliotheken (`KABC` für vCards, Akonadi-Server via D-Bus/IPC) und gegen die Ressourcen-Protokolle (CardDAV, LDAP, IMAP). Ein FreeSynergy-Skin dockt deshalb an **Akonadi-Exporte bzw. die darunterliegenden Server-APIs** an, nicht am Programm selbst.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| KABC / KPim-APIs (C++) | Kontakte programmatisch lesen/schreiben | offiziell (Bibliothek) |
| Akonadi-control / D-Bus | Verwaltung der Ressourcen, Testzugriff | halböffentlich |
| CardDAV/LDAP/IMAP der Ressourcen | echter Datentransfer | Standard-Protokolle |
| vCard/LDIF/CSV-Dateien | Austauschformat | offiziell |
| REST-API | — | ❌ Nicht vorhanden |

## Authentifizierung

Keine eigene — Ressourcen-Logik: CardDAV-Basic mit App-Passwort, LDAP-Bind-DN, IMAP-OAuth; alles im **KWallet**.

## KABC-Kern (C++)

```cpp
KABC::Addressee a;
a.setFormattedName(QStringLiteral("Andrea Berg"));
a.insertEmail(QStringLiteral("andrea@example.org"), true);
KABC::AddressBook *book = KABC::standardAddressBook();
book->insertAddressee(a);
book->save();   // schreibt in die Akonadi-Datenbank
```

- `KABC::AddressBook` aggregiert alle Akonadi-Kontaktordner
- `KPim::Mime`/`KTp` ergänzen vCard-/iPIM-Handling

## CLI-Hebel

| Werkzeug | Zweck |
|----------|-------|
| `akonadi-console` | graphischer Blick auf Collection-Struktur |
| `akonadi-control --help` | Agenten/Ordner verwalten |
| `kabc-export` (neuere Versionen) | Ordner als vCard-Dateien ziehen |

## Beispiel: vCard-Austauschweg

1. Adressbuch → „Alle als vCard speichern“ → `.vcf`-Stapel
2. Stapel mit jedem vCard-Tool/REST-Konverter mappen
3. Rückimport über Import-Assistent mit Duplikatcheck

## Rate Limits

Nur relevant für die Ressourcen-Server (CardDAV-/LDAP-Limits des Servers).

## Skin-Hinweis

Das vCard-Feldvokabular ist die gemeinsame Sprache ([felder.md](../../../../data/felder.md), [Contact-Modell](../../../../data/modelle.md)); ein „KAddressBook-Skin“ bildet Liste/Baum/Editor nach und liest `.vcf`-Stapel oder CardDAV.
