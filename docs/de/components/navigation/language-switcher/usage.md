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
