# 0064 – Versionsnummern beginnen bei 0.0.1

Status: akzeptiert (Nutzer, 2026-11-08: „Ja, zurücksetzen bitte.“) · ersetzt die bisherige Zählung (coding.md §8 bleibt: Abhängigkeiten über Git-Tags)

## Entscheidung (Nutzer, 2026-11-08: „0.9 glaubt uns niemand“)
1. Alle FreeSynergy-Repos zählen 0.0.N. Jeder Tag erhöht nur die letzte Stelle (v0.0.1, v0.0.2, …). Keine Minor- oder Major-Sprünge, solange die Regel unten nicht erfüllt ist.
2. **0.1.0** wird erst vergeben, wenn ein Programm für normale Menschen benutzbar ist **und** den Handtest des Nutzers (`todo/handtest.md`) besteht. Gilt je Programm; Kerne und Verträge folgen dem Programm, das sie braucht.
3. **1.0.0** wird erst vergeben, wenn die Schnittstelle (der Vertrag) von zwei voneinander unabhängigen Nutzern verwendet wird.
4. Vorabversionen (`-rc.N`) sind im Reset nicht vorgesehen; ein Entwurf trägt dieselbe Nummer wie der spätere Tag und wird erst mit dem Tag veröffentlicht.
5. Abhängigkeiten zeigen auf Tags, nicht auf Branches oder `rev` (Ausnahme nur mit Begründung in der `DESIGN.md`); je Crate gilt in einem Abhängigkeitsgraphen **eine** Version (keine Aliase auf zwei Versionen derselben Crate).

## Folgen
- Die bisherigen Tags und Releases (v0.1.x–v0.9.x, Entwürfe, Vorabversionen) werden gelöscht; der heutige Stand jedes Repos wird als v0.0.1 gesetzt, in Abhängigkeitsreihenfolge.
- rpm/deb: Version 0.0.1 ist kleiner als die bisherigen; wer alte Pakete installiert hat, entfernt sie einmal selbst (`dnf remove`), sonst gilt „Update“ nicht. Der Katalog (`fs-catalog`) führt nur noch 0.0.N.
- Signaturen: neue Tags werden neu signiert; alte signierte Dateien verlieren ihre Veröffentlichung.
- Offene Branches zeigen auf alte Tags; sie werden einmal mit einem Umstellungscommit auf v0.0.1 gezogen.

## Begründung
Eine hohe Nullversion (0.9) verspricht Reife, die nicht belegt ist. Der Nutzer will, dass Nummern etwas bedeuten: 0.0.N = Entwicklung, 0.1.0 = ein Mensch kann es benutzen, 1.0.0 = die Schnittstelle trägt zwei Nutzer.

## Verworfen
- Beibehalten der bisherigen Nummern: widerspricht der Aussage der Nummer.
- Eine gemeinsame Version für alle Repos: Repos reifen unterschiedlich schnell.
