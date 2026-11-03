# Language Switcher - Usage

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

## With event handlers

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

## Examples

## Example 1: Header-Wechsel

```
┌─────────────────────────────────────────┐
│ 🏠 Home  📚 Wiki  📬 Nachrichten        │
│                                🇩🇪 🇬🇧  │
└─────────────────────────────────────────┘
```

## Example 2: Einstellungen

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

## Example 3: Dropdown

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

## Example 4: Flaggen-Buttons

```
┌─────────────────────────────────────────┐
│ [🇩🇪] [🇬🇧] [🇫🇷] [🇪🇸] [🇮🇹]              │
└─────────────────────────────────────────┘
```

## Example 5: Auto-Detect

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
