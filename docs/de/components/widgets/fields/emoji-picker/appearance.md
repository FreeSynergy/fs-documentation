# Emoji Picker - Erscheinungsbild

## Grundlayout
Ein Emoji Picker ist eine Emoji-Auswahl für Chat und Kommentare.

```
┌─────────────────────────────────────────┐
│ [Smileys] [Gesichter] [Hände] ...       │  ← Reiter
├─────────────────────────────────────────┤
│  😀  😃  😄  😁  😆  😅  🤣  😂          │
│  😊  😇  🙃  😁  😋  😛  😜  😝          │
│  🤪  😘  🤗  🤭  🫦  😙  🤤  😚          │
│  🥰  😗  😖  😞  😟  😬  😣  😪           │
│  🥱  😴  😷  🤒  🤕  🤢  🤮  🤧           │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **inline** | fest unter dem Eingabefeld, Höhe begrenzt, die Liste scrollt |
| **overlay** | Klappe mit Schatten über dem Text, Reiter oben |
| **reaktion** | einzeilige Leiste mit 6–8 Emojis und einer Schaltfläche „Mehr…“ |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| small | 200px | im Text |
| medium | 300px | Standard |
| large | 400px | hervorgehoben |
| full | 100% | volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Standard** | hell | Standard |
| **Aktiv** | Primärfarbe | aktiver Reiter |
| **Hover** | heller | Zustand beim Überfahren |

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
|--------|--------------|
| `scale` | Vergrößerung |
| `shadow` | der Schatten wird stärker |

## Responsiv

- Die Emoji-Raster skalieren mit: 8 Spalten ab 300 px, 6 Spalten auf schmalen Geräten.
- Der Kategoriewechsel erfolgt per `swipe`; die Liste behält ihre Scrollposition pro Kategorie.
- Unterhalb der Bildschirmbreite `small` wird der Picker zu einer am unteren Rand verankerten
  Vollfläche mit fester Reiterleiste oben; die Kacheln bleiben mindestens 40 px groß.

## Reiter

| Reiter | Emojis |
|--------|--------|
| **Smileys** | 😀  😃  😄  ... |
| **Gesichter** | 🤪  😘  🤗  ... |
| **Hände** | ✌️  🤘  🙌  ... |
| **Tiere** | 🐱  🐶  🐼  ... |
| **Essen** | 🍔  🍕  🍫  ... |
| **Sport** | ⚽  🏀  🏈  ... |
| **Reisen** | 🚗  🚀  ✈️  ... |

## Suche

```
┌─────────────────────────────────────────┐
│ 🔍 Suchen...                            │
├─────────────────────────────────────────┤
│  😀  😃  😄  😁  😆  😅  🤣  😂          │
└─────────────────────────────────────────┘
```
