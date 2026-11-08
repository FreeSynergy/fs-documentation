# Resources

## Kurz gesagt

Resources hält fest, was eine Gruppe hat und was sie braucht: Dinge, Räume, Material auf Lager und die Zeit von Menschen. Du kannst etwas für einen Zeitraum reservieren, einen Bedarf einstellen oder ein Angebot einstellen. Es beantwortet die Frage: Was haben wir, was brauchen wir, und wer hat Zeit? Zwei Personen können denselben Raum nicht versehentlich doppelt buchen, und niemand sonst kann deine Zeit vergeben.

## Was hier anders ist

- Deine eigene Kapazität, also deine Zeit, gehört dir. Nur du entscheidest, was angezeigt und zugeteilt wird. Was eine Gruppe sieht, ist ein Anteil, den du freigibst.
- Eine Reservierung wird in einem Schritt geprüft, sodass zwei Personen zusammen nicht überbuchen können.
- Material, das verbraucht ist, wird als verbraucht gezählt.
- Dinge und die Zeit von Menschen sind absichtlich ein Programm, weil sie dieselbe Planung teilen.
- Für ein Ressourcenmodell wurde kein Standard gefunden. Resources besitzt seine Schnittstelle selbst, `resources.capnp` in `fs-interfaces`, ein als vorläufig markierter Entwurf.

## Wo es heute steht

Neuester Tag: `v0.2.0`. Es gibt **noch kein Fenster und noch keinen Server**. Ein Server muss deine Kapazitätsaufrufe ablehnen, solange er nicht weiß, wer fragt.

Heute verwaltet es Dinge, Räume und Material, wobei der Bestand aus abgeschlossenen Vorgängen berechnet wird. Reservierungen können nicht überbucht werden, und das Abschließen einer Reservierung gibt das Ding frei oder verbraucht das Material. Es kann die freie Zeit eines Dings über einen Zeitraum zeigen, deine eigene Kapazität, Zuteilungen und Freigaben an Gruppen in einem eigenen Speicher halten und die Auslastung einer Gruppe über die Groups-Schnittstelle berechnen. Bedarfe und Angebote funktionieren, und das Annehmen eines Angebots legt die Reservierung an. Es hat 115 Tests und wurde in vier Runden von einer unabhängigen Prüferin oder einem unabhängigen Prüfer geprüft.

Noch nicht vorhanden: Kosten, Unterstützung für MSPDI (ein Dateiformat für Projektpläne) und Fähigkeiten. Es gibt keine Lager, Chargen oder Bewertung. Hier geht es um Verfügbarkeit, nicht um ein ERP.

`FreeSynergy.Resources` (`fs-resources`) beantwortet die Frage: **Was haben wir, was brauchen wir, und wer hat Zeit?**

**Status: [Kern](https://github.com/FreeSynergy/fs-resources) v0.2.0, keine GUI; vorläufiger Entwurf der Schnittstelle (2026-11-06).** Siehe den [Gesamtplan](../roadmap.md).

## Warum

Projekte brauchen Menschen und Dinge. Ein Demokratie-Projekt im größeren Maßstab braucht das auch, und später ERP. Die [Recherche](https://github.com/FreeSynergy/fs-documentation/blob/main/temp/research/projectmanagement-landscape.md) zeigt, dass Kapazitätsplanung und vollständige Baselines in den untersuchten Open-Source-Werkzeugen entweder bezahlte Funktionen sind oder fehlen. Das ist also eine echte Lücke.

## Was es abdeckt

| Zweck | Hinweise |
|-------|----------|
| Dinge: Ausrüstung, Räume, Material | Verleih und Reservierungen beziehen sich auf den Kalender |
| Zeit und Kapazität von Menschen | Sensibel: die Person soll sie sehen und steuern können |
| Bedarf und Angebote | „Dieses Projekt braucht 3 Zelte“, und wer sie geben kann |

## Kosten

Ein Kostenmodul kann später dazukommen. Die Recherche legt nahe, dass es drei getrennte Werte braucht: geplant, zugesagt und tatsächlich. Wir werden analysieren, was solche Programme tun, bevor wir entscheiden, wo es lebt.

## Standards

Für ein Ressourcenmodell wurde kein offener Standard gefunden. MSPDI ist ein Kandidat für Import und Export, aber seine Passung ist bisher eine Annahme. Noch zu recherchieren.

## Offene Fragen

Die Antworten bisher sind vorläufig. Details: [`DESIGN.md`](https://github.com/FreeSynergy/fs-resources/blob/main/DESIGN.md).

1. Dinge und die Zeit von Menschen sind **ein Programm**.
2. Verfügbarkeit nutzt eine einfache Bestandszahl. Alles andere aus ERP gehört hier nicht hin.
3. Kosten bleiben draußen, bis sie analysiert sind.

## Zeit mit einer Gruppe zu teilen heißt, deren Mitgliedern zu vertrauen

Das Teilen ist standardmäßig aus und wird pro Gruppe eingestellt. Eine Gruppe sieht nur Summen, aber **Summen schützen niemanden vor einem Mitglied, das es darauf anlegt.** Ein Mitglied kann die genauen Stunden einer abwesenden Person in einer von zwei Wochen herausfinden, indem es die eigene Kapazität in kleinen Schritten ändert. Eine Prüfung hat das erfolgreich getan. Runden hilft nicht. Teile deshalb nur mit Menschen, denen du vertraust.

**Bekannter offener Punkt:** Ein Fehler beim Annehmen eines Angebots, gefolgt von einer Aktion an der Reservierung und einer wiederholten Entscheidung, kann dazu führen, dass Angebot und Reservierung nicht mehr übereinstimmen.
