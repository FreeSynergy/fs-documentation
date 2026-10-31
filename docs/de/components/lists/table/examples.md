# Table (Tabelle) - Beispiele

## Beispiel 1: Benutzertabelle

```
┌─────────────────────────────────────────┐
│ ID │ Name │ Alter │ E-Mail                │
├─────────────────────────────────────────┤
│ 1  │ John │ 25    │ john@example.com      │
│ 2  │ Jane │ 30    │ jane@example.com      │
│ 3  │ Bob  │ 28    │ bob@example.com       │
└─────────────────────────────────────────┘
```

## Beispiel 2: mit Sortierung

```
┌─────────────────────────────────────────┐
│ ID │ Name ▲ │ Alter │ E-Mail              │
├─────────────────────────────────────────┤
│ 1  │ John   │ 25    │ john@example.com      │
│ 2  │ Jane   │ 30    │ jane@example.com      │
│ 3  │ Bob    │ 28    │ bob@example.com       │
└─────────────────────────────────────────┘
```

## Beispiel 3: mit Pagination

```
┌─────────────────────────────────────────┐
│ ID │ Name │ Alter │ E-Mail                │
├─────────────────────────────────────────┤
│ 1  │ John │ 25    │ john@example.com      │
│ 2  │ Jane │ 30    │ jane@example.com      │
├─────────────────────────────────────────┤
│ [1] [2] [3] [4] [5] [Nächste →]         │
│ 1-10 von 100                            │
└─────────────────────────────────────────┘
```

## Beispiel 4: mit Row Selection

```
┌─────────────────────────────────────────┐
│ [✓] ID │ Name │ Alter │ E-Mail             │
├─────────────────────────────────────────┤
│ [✓] 1  │ John │ 25    │ john@example.com     │
│ [✓] 2  │ Jane │ 30    │ jane@example.com     │
│ [ ] 3  │ Bob  │ 28    │ bob@example.com      │
└─────────────────────────────────────────┘
```

## Beispiel 5: mit Actions

```
┌─────────────────────────────────────────┐
│ ID │ Name │ Alter │ E-Mail │ Aktion       │
├─────────────────────────────────────────┤
│ 1  │ John │ 25    │ john@example.com │ [✏️] [🗑️] │
│ 2  │ Jane │ 30    │ jane@example.com │ [✏️] [🗑️] │
└─────────────────────────────────────────┘
```
