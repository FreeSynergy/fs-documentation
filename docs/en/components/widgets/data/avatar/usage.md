# Avatar - Usage

## Simple avatar with initials

```jsx
<Avatar name="John Doe" size="medium" />
```

## Avatar with an image

```jsx
<Avatar 
  name="John Doe" 
  src="/images/john-doe.jpg" 
  size="large"
/>
```

## Avatar with a status

```jsx
<Avatar 
  name="Jane Smith" 
  status="online" 
  showStatus={true}
/>
```

## Interactive avatar

```jsx
<Avatar 
  name="John Doe" 
  size="medium"
  interactive={true}
  onClick={() => navigate('/profile/john')}
  hoverEffect="zoom"
/>
```

## Avatar in a list item

```jsx
<ListItem>
  <Avatar name={user.name} src={user.avatarUrl} size="small" />
  <span>{user.name}</span>
</ListItem>
```

## Avatar in chat

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

## Avatar with a dropdown

```jsx
<Dropdown>
  <Avatar 
    name={currentUser.name} 
    src={currentUser.avatarUrl}
    interactive={true}
  />
  <Dropdown.Menu>
    <Dropdown.Item onClick={logout}>Sign out</Dropdown.Item>
  </Dropdown.Menu>
</Dropdown>
```

## Avatar grid

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

## Examples

## Example 1: chat list

```
┌────────────────────────────────────┐
│ 👤 John Doe     ✓                  │
│    Jane Smith   •                  │
│    Bob Müller   -                  │
│    Alice Winter ●                  │
└────────────────────────────────────┘
```

## Example 2: profile card

```
┌─────────────────────────────┐
│                             │
│     🖼️ John Doe            │
│                             │
│     Developer               │
│     john@example.com        │
│                             │
└─────────────────────────────┘
```

## Example 3: team list

```
┌────────────────────────────────────────────┐
│ 🧑‍💻 Team members                          │
├────────────────────────────────────────────┤
│ 👤 Alice    ✓  Developer                  │
│ 👤 Bob      •  Designer                   │
│ 👤 Carol    -  Product Manager            │
│ 👤 Dave     ✓  Developer                  │
└────────────────────────────────────────────┘
```

## Example 4: comment list

```
┌────────────────────────────────────────────┐
│ 📝 Comments                                │
├────────────────────────────────────────────┤
│ 👤 John Doe: "Great project!"             │
│    🖼️ Image                               │
│                                            │
│ 👤 Jane Smith: "Thanks for the feedback"  │
└────────────────────────────────────────────┘
```

## Example 5: user picker

```
┌──────────────────────────┐
│ Select user              │
├──────────────────────────┤
│ [👤 Alice] [👤 Bob]      │
│ [👤 Carol] [👤 Dave]     │
│ [👤 Eve]   [👤 Frank]    │
└──────────────────────────┘
```

## Example 6: avatar stack

```
┌──────────────────────────┐
│ 📦 Team:                 │
│ 👤 👤 👤 👤              │
│ (+3 more)                │
└──────────────────────────┘
```

## Example 7: status display

```
Online:   🟢 John, Jane, Alice
Away:     🟠 Bob
Offline:  ⚫ Carol, Dave
```

## Example 8: avatar with a badge

```
┌──────────────────────────┐
│ 📩 Messages              │
├──────────────────────────┤
│ 👤 John    🟢  3         │
│ 👤 Jane    🟢           │
│ 👤 Bob     🟠  1         │
└──────────────────────────┘
```
