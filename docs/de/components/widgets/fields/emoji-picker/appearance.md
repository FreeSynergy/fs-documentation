# Emoji Picker - Aussehen

## Grundlayout
Ein Emoji Picker ist eine Emoji-Auswahl für Chat/Kommentare.

```
┌─────────────────────────────────────────┐
│ [Smileys] [Gesichter] [Hände] ...       │  ← Tabs
├─────────────────────────────────────────┤
│  😀  😃  😄  😁  😆  😅  🤣  😂          │
│  😊  😇  🙃  😁  😋  😛  😜  😝          │
│  🤪  😘  🤗  🤭  🫦  😙  🤤  😚          │
│  🥰  😗  😖  😞  😟  😬  😣  😪           │
│  🥱  😴  😷  🤒  🤕  🤢  🤮  🤧           │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **inline** | fest unter dem Eingabefeld, Höhe begrenzt, Liste scrollt |
| **overlay** | Klappe mit Schatten über dem Text, Reiter oben |
| **reaktion** | einzeilige Leiste mit 6–8 Emojis und „mehr…“-Button |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| Small | 200px | Inline |
| Medium | 300px | Standard |
| Large | 400px | Featured |
| Full | 100% | Volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Default** | Hell | Standard |
| **Active** | Primärfarbe | Aktiver Tab |
| **Hover** | Heller | Hover-Zustand |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `scale` | Vergrößerung |
| `shadow` | Schatten stärker |

## Reaktiv

- Die Emoji-Raster skaliert mit: 8 Spalten ab 300 px, auf schmalen Geräten 6 Spalten.
- Kategorienwechsel per `swipe`; die Liste behält ihre Scroll-Position je Kategorie.
- Unter `small` Bildschirmbreite wird der Picker zur bodenbündigen Vollfläche mit
  festem Reiter oben; die Kacheln bleiben mindestens 40 px groß.

## Tabs

| Tab | Emojis |
|-----|--------|
| **Smileys** | 😀  😃  😄  ... |
| **Gesichter** | 🤪  😘  🤗  ... |
| **Hände** | ✌️  🤘  🙌  ... |
| **Tiere** | 🐱  🐶  🐼  ... |
| **Essen** | 🍔  🍕  🍫  ... |
| **Sport** | ⚽  🏀  🏈  ... |
| **Reisen** | 🚗  🚀  ✈️  ... |

## Search

```
┌─────────────────────────────────────────┐
│ 🔍 Suche...                             │
├─────────────────────────────────────────┤
│  😀  😃  😄  😁  😆  😅  🤣  😂          │
└─────────────────────────────────────────┘
```
