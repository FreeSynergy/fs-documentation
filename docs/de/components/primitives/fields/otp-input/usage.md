# OTP Input (Einmalcode) - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung auf Rust und Blinc
    wechselt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Das Feld gehört in einen Anmelde- oder Bestätigungsdialog. Es meldet erst „fertig“,
wenn alle Zeichen gesetzt sind. Die Prüfung übernimmt das Programm.

## Beispiele

### Zweiter Faktor bei der Anmeldung

```jsx
<OtpInput length={6} autoComplete="one-time-code" onComplete={verify} />
```

### Bestätigung mit erneutem Senden

```jsx
<OtpInput length={6} value={code} error={failed} onResend={resend} />
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| TOTP-App | `length = 6`, `digits = 10` |
| E-Mail-Code | `length = 6`, `digits = 36`, Autofill beibehalten |
| Code abgelaufen | Fehlerzustand und Countdown für `onResend` |
