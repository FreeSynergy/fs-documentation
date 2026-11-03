# Language Switcher - Verwendung

## Einfacher Language Switcher

```jsx
<LanguageSwitcher 
  languages={[
    { code: 'de', label: 'Deutsch', flag: '🇩🇪' },
    { code: 'en', label: 'English', flag: '🇬🇧' },
    { code: 'fr', label: 'Français', flag: '🇫🇷' }
  ]}
  currentLanguage="de"
  onChange={(lang) => setLanguage(lang)}
/>
```

## Mit Dropdown

```jsx
<LanguageSwitcher 
  languages={languages}
  variant="dropdown"
  currentLanguage={currentLang}
  onChange={handleLanguageChange}
/>
```

## In Header

```jsx
<Header>
  <Logo />
  <Navigation />
  <LanguageSwitcher 
    languages={languages}
    variant="icons"
    currentLanguage={currentLang}
  />
</Header>
```

## Mit Event-Handlern

```jsx
<LanguageSwitcher 
  languages={languages}
  onChange={(lang) => {
    console.log('Language changed:', lang)
    setLanguage(lang)
  }}
  onOpen={() => console.log('Open')}
  onClose={() => console.log('Close')}
/>
```

## Beispiele

## Beispiel 1: Header-Wechsel

```
┌─────────────────────────────────────────┐
│ 🏠 Home  📚 Wiki  📬 Nachrichten        │
│                                🇩🇪 🇬🇧  │
└─────────────────────────────────────────┘
```

## Beispiel 2: Einstellungen

```
┌─────────────────────────────────────────┐
│ Sprache                                 │
├─────────────────────────────────────────┤
│ 🇩🇪 Deutsch                              │
│ 🇬🇧 English                              │
│ 🇫🇷 Français                             │
│ 🇪🇸 Español                              │
│ 🇮🇹 Italiano                             │
└─────────────────────────────────────────┘
```

## Beispiel 3: Dropdown

```
┌─────────────────────────────────────────┐
│ Sprache                                 │
├─────────────────────────────────────────┤
│ 🇩🇪 Deutsch ▼                            │
├─────────────────────────────────────────┤
│ 🇬🇧 English                              │
│ 🇫🇷 Français                             │
│ 🇪🇸 Español                              │
└─────────────────────────────────────────┘
```

## Beispiel 4: Flaggen-Buttons

```
┌─────────────────────────────────────────┐
│ [🇩🇪] [🇬🇧] [🇫🇷] [🇪🇸] [🇮🇹]              │
└─────────────────────────────────────────┘
```

## Beispiel 5: Auto-Detect

```
┌─────────────────────────────────────────┐
│ Sprache                                 │
├─────────────────────────────────────────┤
│ 🇩🇪 Deutsch (Standard)                   │
│ 🇬🇧 English                              │
│ 🇫🇷 Français                             │
├─────────────────────────────────────────┤
│ [✓] Sprache automatisch erkennen        │
└─────────────────────────────────────────┘
```
