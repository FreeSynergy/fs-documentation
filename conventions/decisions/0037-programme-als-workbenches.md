# 0037 – Jedes Programm ist mindestens eine Workbench; Programme zeigen sich gegenseitig an

Status: akzeptiert (2026-11-05) · ergänzt ADR 0005, 0019, 0023

## Entscheidung (Nutzer)
1. **Alle Apps sind mindestens Workbenches.** So können Daten gleichzeitig und **über Programme
   hinweg** angezeigt werden.
2. **Beispiel Messages:** Die Messages-Workbench kommt in PM, Kontakten, Helpdesk usw. vor. Sie
   zeigt dasselbe wie der Messenger — **kompakter, mit weniger Einstellungen**, ggf. nur mit einem
   Antwortfeld. Wer mehr will, öffnet die App (ähnlich einem Widget auf dem Desktop).
3. **Ordner = Gruppe = E-Mail-Verteiler** (dasselbe Konzept). Schreibe ich im Helpdesk, werden die
   Nachrichten in einem Messenger-Ordner gesammelt: im Helpdesk sehe ich nur dieses eine Fenster, im
   Messenger alle Ordner.
4. **Status lokal speichern:** Anwesenheit, „zugestellt“, „gesehen“ usw. liegen in **unserer**
   Datenbank (`fs-store`), damit Vorschauen auch ohne Matrix- oder Mailserver dahinter möglich sind.
5. **App ≠ Composer:** Die Hauptelemente einer App sind Composer (Workbenches). Die App bringt
   zusätzlich Menüs, Gesten, Maus-Verhalten, Animationen. Der Composer weiß nicht, was er braucht
   oder hat. **Gesten (z. B. Wischen) kommen erst im Frontend dazu**, nicht vorher.
6. **Anrufe sind überall ein eigenes Programm** (Streaming, SIP, normaler Anruf am Smartphone);
   alles, was man davon sieht, sind wiederverwendbare Components.

## Folgen
- Jedes Programm liefert seine Workbench + eine kompakte Variante (Einstellungen reduziert).
- `messages`: Status-Daten (Presence, delivered, read) als eigene Objekte in `fs-store`.
