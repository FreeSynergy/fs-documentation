# Föderation

[← Zurück zum Index](../INDEX.md) | [Rechte-System](rechte.md) | [Node](../programme/node/README.md)

---

## Was ist eine Föderation?

Eine Föderation ist ein freiwilliger Zusammenschluss von Projekten und/oder anderen Föderationen. Jedes Mitglied behält seine Souveränität und entscheidet selbst, was es teilt.

## Struktur

```
Föderation "FreeSynergy Europa"
  ├── Föderation "FreeSynergy Deutschland"
  │   ├── Projekt "Helfa Köln" (node1.helfa.org)
  │   ├── Projekt "Helfa Berlin" (node1.helfa-berlin.org)
  │   └── Projekt "Community XY" (node.community-xy.de)
  │
  ├── Föderation "FreeSynergy Österreich"
  │   └── Projekt "Wien Community" (node.wien-community.at)
  │
  └── Projekt "Solo-Projekt" (solo.example.com)
```

**Föderationen können:**
- Projekte enthalten
- Andere Föderationen enthalten
- Eigene Services hosten (auf eigenen oder freigegebenen Hosts)
- Einen Auth-Broker haben (OAuth2 Proxy / OIDC Provider)

## Voraussetzungen

| Typ | Braucht Domain? | Braucht Proxy? |
|---|---|---|
| Projekt (lokal, ein Rechner) | Nein | Nein |
| Projekt (öffentlich) | Ja (empfohlen) | Ja |
| Föderation | **Ja, MUSS** | **Ja, MUSS** |

Eine Föderation braucht IMMER eine Domain, weil:
- Subdomains für Projekte: `helfa-koeln.federation.freesynergy.net`
- Subdomains für Services: `auth.federation.freesynergy.net`
- Der Auth-Broker auf der Föderation-Domain erreichbar sein muss

## Auth-Broker

Die Föderation braucht einen zentralen Auth-Punkt der das User-Management zwischen den Mitgliedern koordiniert. Das ist KEIN zentraler IAM — es ist ein **Broker** der zwischen den IAMs der Mitglieder vermittelt.

Technisch: Ein OAuth2/OIDC Proxy der Token-Exchange zwischen den IAMs der Projekte durchführt. Wenn sich ein User aus "Helfa Köln" bei einem Service in "Helfa Berlin" anmelden will, geht der Request über den Auth-Broker der Föderation.

## Proxy und Routing

Der Proxy der Föderation:
- Verwaltet die Subdomains der Mitglieder
- Routet Requests an die richtigen Projekt-Nodes
- Kann Redirects machen (wenn ein Projekt seinen eigenen Proxy hat)
- Terminiert TLS für die Föderations-Domain

Jedes Projekt-Mitglied hat auch seinen eigenen Proxy (z.B. Zentinel). Die Föderation routet zum Projekt-Proxy, der Projekt-Proxy routet zum Service.

## Beitritt

Man kann einer Föderation beitreten über:
1. **Einladung** — Die Föderation generiert eine Invite-Datei (wie beim Node-Join)
2. **Anfrage** — Das Projekt stellt eine Beitrittsanfrage, die Föderation genehmigt

## Rechte-Kaskade

Siehe [Rechte-System](rechte.md). Zusammengefasst: Rechte können nur abnehmen, nie zunehmen. Alles ist standardmäßig privat. Freigaben müssen explizit gemacht werden.

## Föderale Suche

Die [Suche](../programme/search/README.md) in einer Föderation funktioniert in Schichten:
1. **Lokal**: Service durchsucht seine eigenen Daten
2. **Projekt**: Bus aggregiert Ergebnisse aller lokalen Services
3. **Föderation**: Föderation aggregiert Ergebnisse aller Projekte
4. **Überföderationen**: Falls die Föderation Teil einer größeren ist

Jede Schicht filtert nach den Rechten: Nur Daten mit `search`-Recht werden durchsucht.

---

Weiter: [Bus](bus.md) | [Node](../programme/node/README.md)
