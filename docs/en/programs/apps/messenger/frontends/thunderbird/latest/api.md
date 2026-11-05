# Thunderbird - API documentation

## Overview
Thunderbird offers an extensive add-on API for building extensions and themes. The API provides access to mail, contacts, calendars, filters and UI elements.

## Authentication
Thunderbird has no built-in authentication API for add-ons:
- **Local add-ons**: no authentication required
- **Remote APIs**: OAuth2 for external services (Gmail, Outlook, etc.)
- **Password manager**: storage of credentials

## Endpoints (add-on API)

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
// list accounts
await messenger.accounts.list();

// get account
await messenger.accounts.getAccount(accountId);

// update account
await messenger.accounts.update(accountId, updates);

// list identities
await messenger.accounts.listIdentities(accountId);
```

#### Messages
```javascript
// list messages
await messenger.messages.list(filter);

// get message
await messenger.messages.get(messageId);

// read message / mark as read
await messenger.messages.read(messageIds, true);

// delete message
await messenger.messages.delete(messageIds);

// move message
await messenger.messages.move(messageIds, destinationFolderId);
```

#### Folders
```javascript
// list folders
await messenger.folders.getRootFolder();

// subfolders
await messenger.folders.getChildren(folderId);

// create folder
await messenger.folders.create(name, parentId);
```

#### Contacts
```javascript
// list address books
await messenger.addressBooks.list();

// list contacts
await messenger.addressBooks.getContacts(addressBookId);

// create contact
await messenger.addressBooks.createContact(contactData);
```

#### Search
```javascript
// search messages
await messenger.messages.search(searchParams);
```

#### Compose
```javascript
// create new message
let composeDetails = {
    to: "recipient@example.com",
    subject: "Subject",
    body: "Message text"
};

await messenger.compose.beginNew(composeDetails);

// send
await messenger.compose.send(composeId);
```

### UI API

#### Tabs
```javascript
// create tab
await messenger.tabs.create({
    windowId: windowId,
    index: 0,
    active: true
});

// close tab
await messenger.tabs.remove(tabId);
```

#### Windows
```javascript
// create window
await messenger.windows.create({
    width: 800,
    height: 600,
    type: "primary"
});

// list windows
await messenger.windows.getAll();
```

#### Notifications
```javascript
// show notification
await messenger.notifications.showNotification({
    message: "Message text",
    title: "Title"
});
```

### Calendar API ( Lightning )

#### Events
```javascript
// list events
await messenger.calendar.getEvents();

// create event
await messenger.calendar.createEvent(eventData);

// update event
await messenger.calendar.updateEvent(eventId, updates);

// delete event
await messenger.calendar.deleteEvent(eventId);
```

#### Calendars
```javascript
// list calendars
await messenger.calendar.getCalendars();

// create calendar
await messenger.calendar.createCalendar(calendarData);
```

## Examples

### Sending mail
```javascript
// begin new message
let composeDetails = {
    to: "recipient@example.com",
    subject: "Test message",
    body: "Hello,\n\nThis is a test message.\n\nKind regards"
};

let composeId = await messenger.compose.beginNew(composeDetails);

// add attachment
await messenger.compose.addAttachment(composeId, {
    data: "base64-data-here",
    name: "file.txt",
    type: "text/plain"
});

// send
await messenger.compose.send(composeId);
```

### Searching messages
```javascript
// search parameters
let searchParams = {
    queryString: "Amount: 100€",
    folder: folderId,  // Optional
    maxResults: 50
};

let results = await messenger.messages.search(searchParams);

// process results
for (let message of results.messages) {
    console.log(message.subject, message.from);
}
```

### Contact management
```javascript
// get address book
let addressBooks = await messenger.addressBooks.list();
let defaultBook = addressBooks[0];

// create contact
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
// new message received
messenger.messages.onCreated.addListener((message) => {
    console.log("New message:", message.subject);
    
    // answer automatically
    if (message.subject.includes("Question")) {
        let reply = {
            to: message.from,
            subject: "Re: " + message.subject,
            body: "Thank you for your message!"
        };
        messenger.compose.beginNew(reply);
    }
});

// messages read
messenger.messages.onReadStatusChanged.addListener((messageId, isRead) => {
    console.log("Message read:", messageId, isRead);
});
```

## Rate limits
- No rate limits for local add-on API calls
- External APIs are subject to their own limits (Gmail, etc.)

## Webhooks
Thunderbird has no built-in webhook system. Alternatives:
- event listener API for real-time updates
- periodic polling
- native messaging host for external communication

### Native messaging
```json
// manifest.json for native messaging
{
  "name": "com.example.messaging",
  "description": "messaging system",
  "path": "./messaging.py",
  "type": "stdio",
  "allowed_extensions": ["extension-id@example.com"]
}
```

## SDKs and client libraries
- **JavaScript/TypeScript**: WebExtensions API
- **Python**: Thunderbird native messaging
- **C++**: Thunderbird source code

Development setup:
```bash
# develop an add-on
npm install webextension-polyfill

# create the manifest
# manifest.json with permissions
```

## API references
- **WebExtensions**: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions
- **Thunderbird add-ons**: https://Thunderbird.addons.mozilla.org/
- **Mail API**: https://webextension-api.thunderbird.net/docs/

## See also
- [menus.md](menus.md)
- [features.md](features.md)
- [description.md](description.md)
- [layout.md](layout.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (this file)
