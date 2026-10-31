# LiquidFeedback - API Dokumentation

## Übersicht

LiquidFeedback bietet **keine öffentliche API**. Automatisierung läuft über die MySQL-Datenbank (lesend), Protokoll-/Tabellen-Exporte und bei Bedarf Quellcode-Eingriffe. Für FreeSynergy-Skins gilt: LiQu ist Referenz für das **Delegationsmodell**, nicht für Integrations-APIs.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST/Webhooks | — | ❌ |
| MySQL-Schema (`issues`, `votes`, `delegations`) | Analyse-Auswertung (lesend) | Praxisweg (Versionsbruch möglich) |
| Export-Funktionen (Initiativ-Protokolle) | HTML/PDF | offiziell |
| GraphQL | — | ❌ |

## Muster: Auswertungs-Skin über DB-Reader

```sql
-- Beispielabfrage (Schema der eingesetzten LiQu-Version prüfen!)
SELECT i.id, i.title, i.current_state,
       SUM(v.rank = 1) AS yes, SUM(v.rank = -1) AS no
FROM issues i LEFT JOIN votes v ON v.issue_id = i.id
GROUP BY i.id, i.title, i.current_state;
```

Empfehlung: **Replikat** nutzen, niemals schreiben; Spaltennamen dokumentieren ([felder.md](../../../../data/felder.md)).

## Datenfluss-Skizze

```
LiQu-DB (lesend) → Export-Job → FreeSynergy-Statistikseiten
Initiativtexte manuell/protokollbasiert → Wiki-Spiegel (mit Quellenangabe)
```

## Rate Limits

entfällt (direkter DB-Zugriff).

## Skin-Hinweis

Delegations-/Quorum-Logik als Modell-Vorlage; für echte Integrationen eher moderne Forks/Gremien-Tools mit API erwägen.
