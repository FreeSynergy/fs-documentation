# Kontact - API documentation

## Overview
Kontact is part of the KDE PIM package and offers a unified access to contacts, appointments, notes and email. The API is available mainly over D-Bus and the Akonadi platform.

## Authentication
Kontact has no built-in authentication API:
- **Local use**: no authentication needed
- **D-Bus**: system-based access control
- **KWallet**: password storage for accounts

## Endpoints (D-Bus API)

### Kontact interface
```
Service: org.kde.kontact
Interface: org.kde.kontact.KontactInterface
Path: /Kontact
```

### Akonadi API (D-Bus)
Akonadi is the database and sync platform for KDE PIM:

#### PIM items
```
Service: org.freedesktop.Akonadi
Interface: org.freedesktop.Akonadi.Control
```

#### Contacts (KAB)
- D-Bus service: `org.kde.kaddressbook`
- Interface: `org.kde.kaddressbook.MainWidget`

#### Calendar (KOrganizer)
- D-Bus service: `org.kde.korganizer`
- Interface: `org.kde.korganizer.MainWidget`

#### Notes (KNotes)
- D-Bus service: `org.kde.knotes`
- Interface: `org.kde.knotes.MainWidget`

### D-Bus methods

#### Kontact
| Method | Parameter | Description |
|---------|-----------|--------------|
| `openUrl` | QUrl | Opens a URL in context |
| `showMainwindow` | void | Shows the main window |
| `activateModule` | QString | Activates a module |
| `viewCurrentUrl` | void | Shows the current view |

#### Akonadi
| Method | Parameter | Description |
|---------|-----------|--------------|
| `collections` | void | Lists collections |
| `fetchCollection` | Collection | Fetches a collection |
| `createCollection` | Collection | Creates a collection |
| `modifyCollection` | Collection | Changes a collection |
| `deleteCollection` | Collection | Deletes a collection |
| `items` | Collection | Lists items |
| `fetchItem` | Item | Fetches an item |
| `createItem` | Item | Creates an item |

## Examples

### Python with dbus
```python
import dbus

# Kontact connection
session_bus = dbus.SessionBus()
kontact = session_bus.get_object('org.kde.kontact', '/Kontact')
kontact_if = dbus.Interface(kontact, 'org.kde.kontact.KontactInterface')

# show the main window
kontact_if.showMainwindow()

# activate a module
kontact_if.activateModule('KAddressBook')

# Akonadi connection
akonadi = session_bus.get_object('org.freedesktop.Akonadi', '/')
control = dbus.Interface(akonadi, 'org.freedesktop.Akonadi.Control')

# list collections
collections = control.collections()
print(collections)
```

### C++ example
```cpp
#include <QApplication>
#include <KontactInterface/Core>
#include <Akonadi/CollectionFetchStrategy>

// Kontact Core
KontactInterface::Core *core = KontactInterface::Core::self();
core->init();

// activate a module
core->selectModule(QStringLiteral("KAddressBook"));

// Akonadi collection
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

### QML example
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
# call Kontact
qdbus org.kde.kontact /Kontact org.kde.kontact.KontactInterface.showMainwindow

# open KAddressBook
qdbus org.kde.kontact /Kontact org.kde.kontact.KontactInterface.activateModule KAddressBook

# list Akonadi collections
qdbus org.freedesktop.Akonadi / org.freedesktop.Akonadi.Control.collections
```

## Rate limits
- No rate limits for local D-Bus calls
- System resources limit the number of concurrent calls

## Webhooks
Kontact has no built-in webhook system. Options:
- Akonadi Monitor for changes
- D-Bus signal subscriptions
- Periodic polling over D-Bus

### Akonadi Monitor (C++)
```cpp
Akonadi::Monitor *monitor = new Akonadi::Monitor(this);
monitor->setAllCollectionsMonitored(true);
monitor->itemAdded.connect(this, &MyClass::itemAdded);

void MyClass::itemAdded(const Akonadi::Item &item, const Akonadi::Collection &collection) {
    qDebug() << "Item added:" << item.payload<Email>()->subject();
}
```

## SDKs and client libraries
- **C++/Qt**: Qt framework, KDE PIM libraries
- **Python**: PyKDE5, dbus-python
- **JavaScript**: QtQml, QML bindings
- **C**: libakonadi (low-level)

Installing:
```bash
# Qt/KDE development packages
sudo apt install libkf5akonadi-dev libkf5kontactinterface-dev
sudo apt install python3-pyqt5 python3-dbus

# Qt Creator project
# .pro file
QT += akonadi kontactinterface
```

## API references
- **Akonadi documentation**: https://api.kde.org/kdepimlibs/akonadi/
- **Kontact interface**: https://api.kde.org/kontactinterface/
- **D-Bus specification**: https://dbus.freedesktop.org/doc/api.html

## See also
- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (this file)
