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

## With a dropdown

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

## Example 1: header switcher

```
┌─────────────────────────────────────────┐
│ 🏠 Home  📚 Wiki  📬 Messages           │
│                                🇩🇪 🇬🇧  │
└─────────────────────────────────────────┘
```

## Example 2: settings

```
┌─────────────────────────────────────────┐
│ Language                                │
├─────────────────────────────────────────┤
│ 🇩🇪 Deutsch                              │
│ 🇬🇧 English                              │
│ 🇫🇷 Français                             │
│ 🇪🇸 Español                              │
│ 🇮🇹 Italiano                             │
└─────────────────────────────────────────┘
```

## Example 3: dropdown

```
┌─────────────────────────────────────────┐
│ Language                                │
├─────────────────────────────────────────┤
│ 🇩🇪 Deutsch ▼                            │
├─────────────────────────────────────────┤
│ 🇬🇧 English                              │
│ 🇫🇷 Français                             │
│ 🇪🇸 Español                              │
└─────────────────────────────────────────┘
```

## Example 4: flag buttons

```
┌─────────────────────────────────────────┐
│ [🇩🇪] [🇬🇧] [🇫🇷] [🇪🇸] [🇮🇹]              │
└─────────────────────────────────────────┘
```

## Example 5: auto-detect

```
┌─────────────────────────────────────────┐
│ Language                                │
├─────────────────────────────────────────┤
│ 🇩🇪 Deutsch (default)                    │
│ 🇬🇧 English                              │
│ 🇫🇷 Français                             │
├─────────────────────────────────────────┤
│ [✓] Detect language automatically       │
└─────────────────────────────────────────┘
```
