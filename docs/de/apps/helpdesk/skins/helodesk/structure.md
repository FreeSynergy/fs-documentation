# Helodesk - Struktur und UI/UX

## Seitenstruktur

```
┌────────────────────────────────────────────────────────────────┐
│ Helodesk   [Contact Center][Cases][Contacts][Reports][⚙]       │
│ ┌ Softphone ──────────┐                                        │
│ │ 01 23 45 67 89  ☎   │  Case #4821 „Reklamation“             │
│ │ Queues: Support (3) │  Kanal: Anruf · Queue: Support         │
│ └─────────────────────┘  [Status ▾][Owner ▾][Tags]             │
│                          ┌ Kommunikation ────────────────────┐ │
│                          │ ☎ 09:12 Anruf 2:31 (Anna)         │ │
│                          │ ✉ 09:40 Antwort an Kunde          │ │
│                          │ [Neue Nachricht / Callback]        │ │
│                          └───────────────────────────────────┘ │
│                          Rechts: Kontakt + Historie + KB       │
└────────────────────────────────────────────────────────────────┘
```

- Softphone-Panel ist immer präsent (links oben), Case-Maske mittig, Kontakt rechts

## UI/UX

- modernes SaaS-Design (Violett-Akzent), enge Anruf-/Case-Verzahnung
- Screen-Pop öffnet bei Wähltem/Eingehendem automatisch den Kontext

## Interaktionen

- **Klick-wählen** aus jeder Nummer (Kontakt/Case/Telefonbuch)
- **Transfer** per Drag des aktiven Anrufs auf Agentenliste
- Chat/Callback-Widgets eingebettet auf Kunden-Websites (eigene Skins dort)

## Responsive Design

- Web-App Desktop-optimiert; Agenten-App (iOS/Android) mit Softphone-Funktion; Admin voll im Web

## Accessibility

- Formularlandschaft normaler SaaS-Qualität; Anrufsteuerung zusätzlich per Tastatur im Softphone-Panel (Ziffernblock)
- Screenreader: Case-Details barrierefrei lesbar; Live-Telefonie-Status textlich

## Performance

- WebRTC-Softphone braucht stabiles Netz; QoS-Hinweise im Admin-Bereich
