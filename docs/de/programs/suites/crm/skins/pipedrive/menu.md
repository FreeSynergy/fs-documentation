# Pipedrive - Menüpunkte

## Übersicht

Pipedrive bedient über eine linke Navigationsleiste mit den Hauptmodulen, eine Aktionsschaltfläche oben rechts, ein persönliches Menü und das Company-Setup für Administratoren. Welche Punkte sichtbar sind, hängt von Lizenz und Rechten ab (Admin, Regular, Restricted). Die genauen Beschriftungen ändern sich mit den Releases; Abweichungen sind versionsabhängig.

## Hauptmenüpunkte

### 1. Home / Start
- **Funktion**: Tagesübersicht mit fälligen Aktivitäten und persönlichen Kennzahlen
- **Details**:
  - Liste "Heute fällig" und "Überfällig"

### 2. Aktivitäten (Activities)
- **Funktion**: Aufgaben, Anrufe und Termine über alle Objekte hinweg verwalten
- **Details**:
  - Zeitplan-Ansicht nach Tag und Woche
  - Filter nach Bearbeiter, Typ, Zeitraum, Objekt

### 3. Deals
- **Funktion**: Verkaufschancen in Pipeline- oder Listenansicht führen
- **Details**:
  - **Pipeline-Ansicht**: Kanban mit Stage-Spalten, Drag & Drop zwischen Stages
  - **Listenansicht (Grid)**: Tabelle mit Spaltenauswahl und Sortierung
  - Filterleiste: Pipeline, Stage, Bearbeiter, Betragsspanne, Abschlusszeitraum

### 4. Mailbox / Sales Inbox
- **Funktion**: gemeinsame E-Mail-Adresse des Teams bearbeiten
- **Details**:
  - Eingehende Anfragen zuweisen, beantworten, abschließen
  - Verknüpfung mit Kontakt, Organisation und Deal

### 5. Produkte (Products)
- **Funktion**: Produktkatalog pflegen und Preisübersicht sehen
- **Details**:
  - Produktliste mit Standardpreis und Währung

### 6. Marketing
- **Funktion**: einfache Marketing-Funktionen des Abos
- **Details**:
  - E-Mail-Kampagnen an Kontaktlisten (planabhängig)
  - Web-Besucher-Verfolgung (Add-on, versionsabhängig)

### 7. Berichte (Reports)
- **Funktion**: Pipeline-, Aktivitäts- und Leistungsberichte öffnen
- **Details**:
  - Berichtsbibliothek nach Kategorien
  - Eigene Berichte mit Achse, Metrik und Filter

### 8. More / Zusatzmodule
- **Funktion**: weitere Module und Add-ons bündeln
- **Details**:
  - Leads (Lead-Verwaltung), Workflows/Automatisierungen
  - Team-Leistung bzw. Insights, wiederkehrende Umsätze (ARR)
  - Marketplace-Integrationen und Webhooks-Verwaltung (planabhängig)

### 9. Aktionsschaltfläche "Add" (oben)
- **Funktion**: Datensatztyp direkt anlegen
- **Details**:
  - Aktivität, Deal, Person, Organisation, Produkt, Lead

### 10. Persönliches Menü (Avatar oben rechts)
- **Funktion**: eigenes Konto und Benachrichtigungen
- **Details**:
  - Persönliche Einstellungen, Passwort, Zwei-Faktor-Sicherung
  - Persönliche API-Token verwalten (Reiter "Personal access tokens")

### 11. Company-Setup (nur Administratoren)
- **Funktion**: Instanz konfigurieren
- **Details** (Auswahl):
  - **Pipelines & Stages**: Pipelines anlegen, Stages und Reihenfolge pflegen
  - **Custom Fields**: eigene Felder je Objekttyp
  - **Workflows**: Automatisierungsregeln
  - **Nutzer und Berechtigungen**: Lizenzen, Rollen, Sichtbarkeitsgruppen
  - **E-Mail-Einstellungen**: Sync, Signaturen, Sales-Inbox-Postfächer
  - **Firmendaten, Abrechnung und Speicher**: planabhängig

## Kontext-Menüs

### Deal-Kachel im Pipeline-Board
- Deal öffnen, Bearbeiten, Duplizieren, Löschen
- Stage wechseln (auch per Drag & Drop)
- Bearbeiter und Team öffnen
- Abschluss "Won" oder "Lost" mit Grundabfrage

### Deal-Detailbereich
- Reiter: Übersicht, Aktivitäten, Dateien, Produkte/Angebote, Team & Zugriff
- Aktionen: Bearbeiten, Duplizieren, Löschen, Aktivität hinzufügen

### Aktivität
- Als erledigt markieren, verschieben, bearbeiten, löschen
- Bearbeiter wechseln, Erinnerung einstellen

### Filter und Listen
- Filter anlegen, speichern, teilen
- Spalten auswählen, sortieren, Gruppenbildung je Stage

### Rechtsklick
- **Nicht vorhanden**: Pipedrive bietet keine Rechtsklick-Menüs; Aktionen liegen in Symbol-Buttons der Kachel und im Detailbereich

## Menüs nach Rolle

### Administrator
- Company-Setup vollständig: Pipelines, Custom Fields, Workflows, Nutzer, Lizenzen, Abrechnung
- Alle Objekte und alle Nutzer-Datensätze sichtbar und bearbeitbar
- Integrationen, Webhooks und API-Zugriffe verwalten

### Bearbeiter (Regular-Nutzer mit Lizenz)
- Module: Leads, Aktivitäten, Deals, Kontakte, Organisationen, Produkte, Berichte
- Eigene und freigegebene Datensätze bearbeiten, Deals im eigenen Team anlegen
- Kein Company-Setup, keine Nutzerverwaltung

### Leser (Restricted- bzw. Read-only-Nutzer)
- Zugewiesene Objekte einsehen, keine Anlage neuer Kerndatensätze
- Eigene Aktivitäten und Notizen je nach Berechtigung
- Keine Berichte-Verwaltung, keine Konfiguration, kein API-Zugriff über Account-Token (versionsabhängig)

## Shortcuts

Pipedrive veroeffentlicht keine umfassende Shortcut-Liste. Die real nutzbare Tastatursteuerung und die als fehlend markierten Kurzzeichen stehen in [shortcuts.md](shortcuts.md).
