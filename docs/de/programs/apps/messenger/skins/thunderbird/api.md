# Thunderbird - API Dokumentation

## Übersicht
Thunderbird bietet eine umfangreiche Add-on API für die Erstellung von Erweiterungen und Themes. Die API ermöglicht den Zugriff auf E-Mails, Kontakte, Kalender, Filter und UI-Elemente.

## Authentifizierung
Thunderbird hat keine eingebaute Authentifizierungs-API für Add-ons:
- **Lokale Add-ons**: Keine Authentifizierung erforderlich
- **Remote APIs**: OAuth2 für externe Dienste (Gmail, Outlook, etc.)
- **Password Manager**: Speicherung von Anmeldedaten

## Endpunkte (Add-on API)

### Mail API (manifest v2/v3)
```json
{
  "manifest_version": 2,
  "permissions": [
    "accountsRead",
    "mail_modify",
    "addressesRead"
  ]
}
```

#### Accounts
```javascript
// Konten listen
await messenger.accounts.list();

// Konto abrufen
await messenger.accounts.getAccount(accountId);

// Konto aktualisieren
await messenger.accounts.update(accountId, updates);

// Abonnements listen
await messenger.accounts.listIdentities(accountId);
```

#### E-Mails
```javascript
// Nachrichten listen
await messenger.messages.list(filter);

// Nachricht abrufen
await messenger.messages.get(messageId);

// Nachricht lesen/als gelesen markieren
await messenger.messages.read(messageIds, true);

// Nachricht löschen
await messenger.messages.delete(messageIds);

// Nachricht verschieben
await messenger.messages.move(messageIds, destinationFolderId);
```

#### Folders
```javascript
// Ordner listen
await messenger.folders.getRootFolder();

// Unterordner
await messenger.folders.getChildren(folderId);

// Ordner erstellen
await messenger.folders.create(name, parentId);
```

#### Contacts
```javascript
// Adressbücher listen
await messenger.addressBooks.list();

// Kontakte listen
await messenger.addressBooks.getContacts(addressBookId);

// Kontakt erstellen
await messenger.addressBooks.createContact(contactData);
```

#### Search
```javascript
// Nachrichten suchen
await messenger.messages.search(searchParams);
```

#### Compose
```javascript
// Neue Nachricht erstellen
let composeDetails = {
    to: "empfaenger@example.com",
    subject: "Betreff",
    body: "Nachrichtentext"
};

await messenger.compose.beginNew(composeDetails);

// Senden
await messenger.compose.send(composeId);
```

### UI API

#### Tabs
```javascript
// Tab erstellen
await messenger.tabs.create({
    windowId: windowId,
    index: 0,
    active: true
});

// Tab schließen
await messenger.tabs.remove(tabId);
```

#### Windows
```javascript
// Fenster erstellen
await messenger.windows.create({
    width: 800,
    height: 600,
    type: "primary"
});

// Fenster listen
await messenger.windows.getAll();
```

#### Notifications
```javascript
// Benachrichtigung anzeigen
await messenger.notifications.showNotification({
    message: "Nachrichtentext",
    title: "Titel"
});
```

### Calendar API ( Lightning )

#### Events
```javascript
// Termine listen
await messenger.calendar.getEvents();

// Termin erstellen
await messenger.calendar.createEvent(eventData);

// Termin aktualisieren
await messenger.calendar.updateEvent(eventId, updates);

// Termin löschen
await messenger.calendar.deleteEvent(eventId);
```

#### Calendars
```javascript
// Kalender listen
await messenger.calendar.getCalendars();

// Kalender erstellen
await messenger.calendar.createCalendar(calendarData);
```

## Beispiele

### E-Mail senden
```javascript
// Neue Nachricht beginnen
let composeDetails = {
    to: "empfaenger@example.com",
    subject: "Test Nachricht",
    body: "Hallo,\n\nDies ist eine Test-Nachricht.\n\nMit freundlichen Grüßen"
};

let composeId = await messenger.compose.beginNew(composeDetails);

// Anhang hinzufügen
await messenger.compose.addAttachment(composeId, {
    data: "base64-data-here",
    name: "datei.txt",
    type: "text/plain"
});

// Senden
await messenger.compose.send(composeId);
```

### Nachrichten suchen
```javascript
// Suchparameter
let searchParams = {
    queryString: "Betrag: 100€",
    folder: folderId,  // Optional
    maxResults: 50
};

let results = await messenger.messages.search(searchParams);

// Ergebnisse verarbeiten
for (let message of results.messages) {
    console.log(message.subject, message.from);
}
```

### Contact management
```javascript
// Adressbuch abrufen
let addressBooks = await messenger.addressBooks.list();
let defaultBook = addressBooks[0];

// Kontakt erstellen
let contact = {
    displayName: "Max Mustermann",
    email: "max@example.com",
    firstName: "Max",
    lastName: "Mustermann",
    phoneNumbers: [{
        value: "+49 123 456789",
        type: "work"
    }]
};

await messenger.addressBooks.createContact(defaultBook.id, contact);
```

### Event listener
```javascript
// Neue Nachricht empfangen
messenger.messages.onCreated.addListener((message) => {
    console.log("Neue Nachricht:", message.subject);
    
    // Automatisch beantworten
    if (message.subject.includes("Frage")) {
        let reply = {
            to: message.from,
            subject: "Re: " + message.subject,
            body: "Danke für Ihre Nachricht!"
        };
        messenger.compose.beginNew(reply);
    }
});

// Nachrichten gelesen
messenger.messages.onReadStatusChanged.addListener((messageId, isRead) => {
    console.log("Nachricht gelesen:", messageId, isRead);
});
```

## Rate Limits
- Keine Rate Limits für lokale Add-on API Aufrufe
- Externe APIs unterliegen ihren eigenen Limites (Gmail, etc.)

## Webhooks
Thunderbird hat kein eingebautes Webhook-System. Alternativen:
- Event-Listener API für Echtzeit-Updates
- Periodisches Polling
- Native Messaging Host für externe Kommunikation

### Native Messaging
```json
// manifest.json für Native Messaging
{
  "name": "com.example.messaging",
  "description": "Nachrichten-System",
  "path": "./messaging.py",
  "type": "stdio",
  "allowed_extensions": ["extension-id@example.com"]
}
```

## SDKs und Client-Bibliotheken
- **JavaScript/TypeScript**: WebExtensions API
- **Python**: Thunderbird Native Messaging
- **C++**: Thunderbird Source Code

Development Setup:
```bash
# Add-on entwickeln
npm install webextension-polyfill

# Manifest erstellen
# manifest.json mit permissions
```

## API References
- **WebExtensions**: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions
- **Thunderbird Add-ons**: https://Thunderbird.addons.mozilla.org/
- **Mail API**: https://webextension-api.thunderbird.net/docs/

## Siehe auch
- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (diese Datei)
