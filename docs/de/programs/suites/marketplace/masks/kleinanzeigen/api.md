# Kleinanzeigen - API Dokumentation

## Übersicht

**Öffentliche API: keine.** Automatisiertes Auslesen/Einstellen verstößt gegen die Plattformbedingungen — diese Doku dokumentiert nur legitime Wege.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST/Webhooks öffentlich | — | ❌ |
| Partner-/Gewerbe-Feeds | Anzeigen-Import großer Händler (vertraglich) | kommerziell |
| DSGVO-Datenexport | eigene Anzeigen/Daten anfordern | rechtlicher Anspruch |
| GraphQL | — | ❌ |

## Legitime Austauschwege

```
eigene Anzeigen      → DSGVO-Auskunft/Export (Konto-Funktion/Anfrage)
gewerbliche Angebote → Partner-Feed-Vertrag (CSV/XML-Feed nach Vorgabe)
Referenz für Skins   → Kategorien-/Umkreis-Modell als eigenes Datenmodell
                       (see ../../data/modelle.md)
```

Beispiel-Feedformat (nur Partner, schematisch — Vorgabe des Betreibers maßgeblich):

```
offer_id;title;description;price;currency;latitude;longitude;category
1001;Sofa 3er;guter Zustand;120;EUR;52.517;13.404;möbel
```

## Rate Limits

entfällt (keine offene API).

## Skin-Hinweis

Kleinanzeigen-Skin = **eigener Mini-Marktplatz-Skin** in FreeSynergy (Angebote + Umkreissuche via Maps-Skins) statt Anbindung: Kategorien-/Umkreismuster kopieren, nicht andocken.
