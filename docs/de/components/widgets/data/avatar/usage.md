# Avatar - Verwendung

## Einfacher Avatar mit Initialen

```jsx
<Avatar name="John Doe" size="medium" />
```

## Avatar mit Bild

```jsx
<Avatar 
  name="John Doe" 
  src="/images/john-doe.jpg" 
  size="large"
/>
```

## Avatar mit Status

```jsx
<Avatar 
  name="Jane Smith" 
  status="online" 
  showStatus={true}
/>
```

## Interaktiver Avatar

```jsx
<Avatar 
  name="John Doe" 
  size="medium"
  interactive={true}
  onClick={() => navigate('/profile/john')}
  hoverEffect="zoom"
/>
```

## Avatar in einem Listeneintrag

```jsx
<ListItem>
  <Avatar name={user.name} src={user.avatarUrl} size="small" />
  <span>{user.name}</span>
</ListItem>
```

## Avatar im Chat

```jsx
<Message>
  <Avatar 
    name={message.sender} 
    size="small" 
    src={message.senderAvatar}
  />
  <div>{message.text}</div>
</Message>
```

## Avatar mit Dropdown

```jsx
<Dropdown>
  <Avatar 
    name={currentUser.name} 
    src={currentUser.avatarUrl}
    interactive={true}
  />
  <Dropdown.Menu>
    <Dropdown.Item onClick={logout}>Abmelden</Dropdown.Item>
  </Dropdown.Menu>
</Dropdown>
```

## Avatar-Raster

```jsx
<UserGrid>
  {users.map(user => (
    <Avatar 
      key={user.id}
      name={user.name}
      src={user.avatarUrl}
      status={user.status}
      showStatus={true}
      onClick={() => selectUser(user.id)}
    />
  ))}
</UserGrid>
```

## Beispiele

## Beispiel 1: Chat-Liste

```
┌────────────────────────────────────┐
│ 👤 John Doe     ✓                  │
│    Jane Smith   •                  │
│    Bob Müller   -                  │
│    Alice Winter ●                  │
└────────────────────────────────────┘
```

## Beispiel 2: Profilkarte

```
┌─────────────────────────────┐
│                             │
│     🖼️ John Doe            │
│                             │
│     Entwickler              │
│     john@example.com        │
│                             │
└─────────────────────────────┘
```

## Beispiel 3: Teamliste

```
┌────────────────────────────────────────────┐
│ 🧑‍💻 Teammitglieder                        │
├────────────────────────────────────────────┤
│ 👤 Alice    ✓  Entwicklerin               │
│ 👤 Bob      •  Designer                   │
│ 👤 Carol    -  Produktmanagerin           │
│ 👤 Dave     ✓  Entwickler                 │
└────────────────────────────────────────────┘
```

## Beispiel 4: Kommentarliste

```
┌────────────────────────────────────────────┐
│ 📝 Kommentare                              │
├────────────────────────────────────────────┤
│ 👤 John Doe: "Tolles Projekt!"            │
│    🖼️ Bild                                │
│                                            │
│ 👤 Jane Smith: "Danke für das Feedback"   │
└────────────────────────────────────────────┘
```

## Beispiel 5: Nutzerauswahl

```
┌──────────────────────────┐
│ Nutzer auswählen         │
├──────────────────────────┤
│ [👤 Alice] [👤 Bob]      │
│ [👤 Carol] [👤 Dave]     │
│ [👤 Eve]   [👤 Frank]    │
└──────────────────────────┘
```

## Beispiel 6: Avatar-Stapel

```
┌──────────────────────────┐
│ 📦 Team:                 │
│ 👤 👤 👤 👤              │
│ (+3 weitere)             │
└──────────────────────────┘
```

## Beispiel 7: Statusanzeige

```
Online:   🟢 John, Jane, Alice
Abwesend: 🟠 Bob
Offline:  ⚫ Carol, Dave
```

## Beispiel 8: Avatar mit Badge

```
┌──────────────────────────┐
│ 📩 Nachrichten           │
├──────────────────────────┤
│ 👤 John    🟢  3         │
│ 👤 Jane    🟢           │
│ 👤 Bob     🟠  1         │
└──────────────────────────┘
```
