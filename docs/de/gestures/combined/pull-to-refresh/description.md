# Pull to Refresh (Ziehen zum Aktualisieren)

## Beschreibung

Pull to Refresh ist eine Kombination aus **Drag an der Obergrenze** eines
scrollbaren Bereichs und einer Ladeaktion: Der Nutzer zieht den Inhalt nach
unten (bzw. an der jeweiligen Startkante), ein Lade-Indikator erscheint, beim
Loslassen startet die Aktualisierung.

Android-Referenz: `SwipeRefreshLayout`, iOS: `UIRefreshControl`.

## Verwendung

- Feed-/Listen-Aktualisierung (E-Mail, Social, Chat)
- Synchronisation von Datenansichten
- Ersatz für einen Aktualisieren-Button auf kleinen Bildschirmen

## Kanten

| Kante | Beschreibung |
|-------|--------------|
| Oben (Standard) | Liste am Anfang, ziehen nach unten |
| Unten | „Load more“ am Listenende (Pull for More) |
| Links/Rechts | seitliche Aktualisierung (Kalender, Chat-Verlauf) |

## Dauer

- Auslöse-Distanz: typisch 60–100px
- Halten des Indikators: bis Antwort da ist
- Indikator-Ausblenden nach Abschluss: 300ms

## Erkennung

| Methode | Beschreibung |
|---------|--------------|
| **Scroll-Edge + Drag** | Drag nur möglich, wenn Scroller an der Startkante |
| **Trigger-Distance** | ab Distanz: Indikator arretiert, Lock-Zustand |
| **Over-Scroll-Grenze** | Gummiband-Bereich wird zur Ladezone |

## Zustände

| Zustand | Beschreibung |
|---------|--------------|
| **Idle** | normale Liste |
| **Pulling** | Indikator wächst mit Zugdistanz |
| **Armed** | Threshold erreicht, „Loslassen zum Aktualisieren“ |
| **Refreshing** | Indikator rotiert, Liste bleibt stehen |
| **Done** | Indikator verschwindet, Inhalt aktualisiert |

## Unterschied zu Drag

- **Drag**: Element oder Inhalt wird bewegt und bleibt bewegt
- **Pull to Refresh**: Bewegung an fixierter Grenze, löst Ladeaktion aus

## Barrierefreiheit

Immer einen expliziten Aktualisieren-Button anbieten; `prefers-reduced-motion`
reduziert den Gummiband-Effekt (WCAG 2.5.7 für die Drag-Komponente).
