# 0046 – Speichern ist nicht Exportieren

Status: akzeptiert (2026-11-06) · Details: Vorschlag · ergänzt ADR 0042, 0030

## Entscheidung (Nutzer)
- Dateien und Texte können als Datei und in der Datenbank liegen; beides ist möglich.
- **Beim Bearbeiten wird immer eine Kopie gemacht, gearbeitet wird mit der Datenbank.** Die Dateien sind Backups und
  können gelagert werden.
- **Erst ein Export bringt sie heraus.** Damit gibt es einen echten Unterschied zwischen Speichern und Export.
- Sammlungen statt Kopien; git und RustFS sind dafür Optionen.

## Vorschlag (vom Nutzer auf später verschoben, nicht vergessen)
Frontends, die fremde Programme nachbilden, verhalten sich ohnehin wie diese.

- Große Dateien wie Videos passen nicht als ganze Kopie in die Datenbank: Bytes bleiben im Dateispeicher, Versionen
  teilen unveränderte Blöcke.
- Nicht bei jedem Verlassen nach dem Export fragen: Das Programm bietet ihn beim Weitergeben an und fragt nur nach,
  wenn eine Datei von außen geöffnet wurde („Original auch aktualisieren?“).
