# Google Drive

> Kategorie: [Dateien](../../index.md) · [Frontends](../index.md)

## Was es ist

Cloud-Speicher von Google: Web, Apps und ein Desktop-Client. Proprietär. ⚠️

## Bemerkenswerte Ideen

- **Streamen oder Spiegeln** in Drive für den Desktop: Streamen lädt Dateien bei Bedarf und braucht fast keinen Festplattenplatz; Spiegeln hält eine vollständige Kopie. Offline-Nutzung ist für ausgewählte Dateien möglich ✅.
- **Drei Rollen:** Betrachter, Kommentator, Bearbeiter ✅. Bearbeiter dürfen standardmäßig Berechtigungen ändern ✅.
- **Linkzugriff:** eingeschränkt, jeder mit dem Link (nur Ansicht) oder deine Organisation ✅.
- **Ablaufdatum für den Zugriff einer Person** bis zu einem Jahr (Arbeits- oder Schulkonten) ✅. **Herunterladen, Kopieren, Drucken einschränken** pro Rolle ✅.
- **Eigentumsübertragung** ✅; wenn du eine geteilte Datei löschst, die dir gehört, endet der Zugriff für alle ✅.
- **Verknüpfungen:** eine Datei nur mit Metadaten, die auf eine andere zeigt; Ordner sind Dateien eines Ordnertyps; in „Meine Ablage“ kann eine Datei mehrere übergeordnete Ordner haben, auf einem freigegebenen Laufwerk nur einen ✅ (API-Leitfaden).
- **Liste „Mit mir geteilt“** und **Aus Ansicht entfernen** ✅.
- **Papierkorb:** 30 Tage; zählt zum Speicher, bis er geleert wird; Nicht-Eigentümer können nur entfernen ✅.

## Gesehene Fähigkeiten

| Fähigkeit | Gesehen | Hinweis |
|-----------|---------|---------|
| Rollen und Link-Freigabe | ✅ | |
| Streamen, Spiegeln, Offline | ✅ | |
| Papierkorb | ✅ | |
| Verknüpfungen, mehrere übergeordnete Ordner | ✅ | |
| Stabile undurchsichtige Datei-ID, Name kann sich ändern | ✅ | |
| Versionsverlauf | ⚠️ | Die abgerufene Seite deckte das nicht ab |
| Doppelte Namen in einem Ordner | ⚠️ | Die API-Seite sagt es nicht |

## Namensregeln

⚠️ Nicht geprüft.

## Was wir übernehmen

Rollen als Grundlage für die Freigabe-Spezifikation. Ablaufdatum bei einer Freigabe. Download-Einschränkung pro Rolle. Eine Datei in mehreren Ordnern ohne Kopie (passt zu „Sammlungen, nicht Kopien“). „Aus Ansicht entfernen“ gegenüber Löschen für Personen, die nicht Eigentümer sind.

## Quellen (gelesen 2026-11-06)

- https://support.google.com/drive/answer/2494822 (Freigabe)
- https://support.google.com/drive/answer/2375057 (Mit mir geteilt)
- https://support.google.com/drive/answer/2375102 (Löschen und Papierkorb)
- https://support.google.com/drive/answer/10838124 (Drive für den Desktop)
- https://developers.google.com/workspace/drive/api/guides/about-files
