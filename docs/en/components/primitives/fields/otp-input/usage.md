# OTP Input (one-time password) - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

The field belongs in a sign-in or confirmation dialog. It only reports finished
once all characters are set; the program does the verification.

## Examples

### Second factor at sign-in

```jsx
<OtpInput length={6} autoComplete="one-time-code" onComplete={verify} />
```

### Confirmation with resend

```jsx
<OtpInput length={6} value={code} error={failed} onResend={resend} />
```

## Scenarios

| Scenario | Recommendation |
|----------|----------------|
| TOTP app | `length = 6`, `digits = 10` |
| Email code | `length = 6`, `digits = 36`, keep the autofill |
| Code expired | error state and a countdown for `onResend` |
