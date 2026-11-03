# OTP Input (Einmalpasswort) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Das Feld gehört in einen Anmelde- oder Bestätigungsdialog. Es meldet erst fertig,
wenn alle Zeichen gesetzt sind; die Prüfung übernimmt das Programm.

## Beispiele

### Zweitfaktor bei der Anmeldung

```jsx
<OtpInput length={6} autoComplete="one-time-code" onComplete={verify} />
```

### Bestätigung mit Neusenden

```jsx
<OtpInput length={6} value={code} error={failed} onResend={resend} />
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| TOTP-App | `length = 6`, `digits = 10` |
| E-Mail-Code | `length = 6`, `digits = 36`, Autofill behalten |
| Code abgelaufen | Fehlerzustand und Countdown für `onResend` |
