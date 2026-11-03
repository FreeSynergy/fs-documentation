# Kontact - API Dokumentation

## Übersicht
Kontact ist Teil des KDE-PIM-Pakets und bietet einen einheitlichen Zugriff auf Kontakte, Termine, Notizen und E-Mails. Die API ist hauptsächlich über D-Bus und die Akonadi-Plattform verfügbar.

## Authentifizierung
Kontact hat keine eingebaute Authentifizierungs-API:
- **Lokale Nutzung**: Keine Authentifizierung erforderlich
- **D-Bus**: System-basierte Zugriffskontrolle
- **KWallet**: Passwort-Speicherung für Konten

## Endpunkte (D-Bus API)

### Kontact Interface
```
Service: org.kde.kontact
Interface: org.kde.kontact.KontactInterface
Path: /Kontact
```

### Akonadi API (D-Bus)
Akonadi ist die Datenbank- und Sync-Plattform für KDE-PIM:

#### PIM Items
```
Service: org.freedesktop.Akonadi
Interface: org.freedesktop.Akonadi.Control
```

#### Kontakte (KAB)
- D-Bus Service: `org.kde.kaddressbook`
- Interface: `org.kde.kaddressbook.MainWidget`

#### Kalender (KOrganizer)
- D-Bus Service: `org.kde.korganizer`
- Interface: `org.kde.korganizer.MainWidget`

#### Notizen (KNotes)
- D-Bus Service: `org.kde.knotes`
- Interface: `org.kde.knotes.MainWidget`

### D-Bus Methoden

#### Kontact
| Methode | Parameter | Beschreibung |
|---------|-----------|--------------|
| `openUrl` | QUrl | Öffnet URL im Kontext |
| `showMainwindow` | void | Zeigt Hauptfenster |
| `activateModule` | QString | Aktiviert Modul |
| `viewCurrentUrl` | void | Zeigt aktuelle Ansicht |

#### Akonadi
| Methode | Parameter | Beschreibung |
|---------|-----------|--------------|
| `collections` | void | Listet Sammlungen |
| `fetchCollection` | Collection | Holt Sammlung |
| `createCollection` | Collection | Erstellt Sammlung |
| `modifyCollection` | Collection | Ändert Sammlung |
| `deleteCollection` | Collection | Löscht Sammlung |
| `items` | Collection | Listet Items |
| `fetchItem` | Item | Holt Item |
| `createItem` | Item | Erstellt Item |

## Beispiele

### Python mit dbus
```python
import dbus

# Kontact Verbindung
session_bus = dbus.SessionBus()
kontact = session_bus.get_object('org.kde.kontact', '/Kontact')
kontact_if = dbus.Interface(kontact, 'org.kde.kontact.KontactInterface')

# Hauptfenster anzeigen
kontact_if.showMainwindow()

# Modul aktivieren
kontact_if.activateModule('KAddressBook')

# Akonadi Verbindung
akonadi = session_bus.get_object('org.freedesktop.Akonadi', '/')
control = dbus.Interface(akonadi, 'org.freedesktop.Akonadi.Control')

# Sammlungen listen
collections = control.collections()
print(collections)
```

### C++ Example
```cpp
#include <QApplication>
#include <KontactInterface/Core>
#include <Akonadi/CollectionFetchStrategy>

// Kontact Core
KontactInterface::Core *core = KontactInterface::Core::self();
core->init();

// Modul aktivieren
core->selectModule(QStringLiteral("KAddressBook"));

// Akonadi Collection
Akonadi::CollectionFetchStrategy fetchStrategy;
fetchStrategy.setRetriever(Akonadi::CollectionFetchStrategy::All);

Akonadi::CollectionFetchJob *fetchJob = 
    new Akonadi::CollectionFetchJob(Akonadi::Collection::root(), 
                                    Akonadi::CollectionFetchJob::FirstLevel);
fetchJob->fetchStrategy().setRetriever(Akonadi::CollectionFetchStrategy::All);

connect(fetchJob, &Akonadi::CollectionFetchJob::result, [](KJob *job) {
    if (job->error()) {
        qDebug() << "Error:" << job->errorString();
        return;
    }
    
    auto *fetchJob = static_cast<Akonadi::CollectionFetchJob*>(job);
    const Akonadi::Collection::List collections = fetchJob->collections();
    
    for (const Akonadi::Collection &collection : collections) {
        qDebug() << "Collection:" << collection.name();
    }
});
```

### QML Example
```qml
import QtQuick 2.15
import org.kde.kontact 1.0

ApplicationWindow {
    visible: true
    
    function showKontact() {
        var kontact = org.kde.kontact;
        kontact.showMainwindow();
    }
    
    function openAddressBook() {
        var kontact = org.kde.kontact;
        kontact.activateModule("KAddressBook");
    }
}
```

### bash with qdbus
```bash
# Kontact aufrufen
qdbus org.kde.kontact /Kontact org.kde.kontact.KontactInterface.showMainwindow

# KAddressBook öffnen
qdbus org.kde.kontact /Kontact org.kde.kontact.KontactInterface.activateModule KAddressBook

# Akonadi Collections listen
qdbus org.freedesktop.Akonadi / org.freedesktop.Akonadi.Control.collections
```

## Rate Limits
- Keine Rate Limits für lokale D-Bus Aufrufe
- System-Ressourcen begrenzen die Anzahl der gleichzeitigen Aufrufe

## Webhooks
Kontact hat kein eingebautes Webhook-System. Möglichkeiten:
- Akonadi Monitor für Änderungen
- D-Bus Signalabonnement
- Periodisches Polling über D-Bus

### Akonadi Monitor (C++)
```cpp
Akonadi::Monitor *monitor = new Akonadi::Monitor(this);
monitor->setAllCollectionsMonitored(true);
monitor->itemAdded.connect(this, &MyClass::itemAdded);

void MyClass::itemAdded(const Akonadi::Item &item, const Akonadi::Collection &collection) {
    qDebug() << "Item added:" << item.payload<Email>()->subject();
}
```

## SDKs und Client-Bibliotheken
- **C++/Qt**: Qt Framework, KDE PIM Libraries
- **Python**: PyKDE5, dbus-python
- **JavaScript**: QtQml, QML bindings
- **C**: libakonadi (low-level)

Installieren:
```bash
# Qt/KDE Entwicklungs-Pakete
sudo apt install libkf5akonadi-dev libkf5kontactinterface-dev
sudo apt install python3-pyqt5 python3-dbus

# Qt Creator Project
# .pro file
QT += akonadi kontactinterface
```

## API References
- **Akonadi Documentation**: https://api.kde.org/kdepimlibs/akonadi/
- **Kontact Interface**: https://api.kde.org/kontactinterface/
- **D-Bus Specification**: https://dbus.freedesktop.org/doc/api.html

## Siehe auch
- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (diese Datei)
