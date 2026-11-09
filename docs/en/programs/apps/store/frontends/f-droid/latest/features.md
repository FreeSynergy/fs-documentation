# F-Droid - Features

## Main features

- Browse and search apps by category; app page with description, versions, permissions and labels.
- **Anti-Features** shown per app. Documented labels: Ads, Disabled Algorithm (outdated signing algorithm), Known Vulnerability, Non-Free Addons, Non-Free Assets, Non-Free Dependencies, Non-Free Network Services, No Source Since, Tethered Network Services, Tracking.
- **Reproducibility**: the project rebuilds an app from source and compares it with the developer's signed APK by transplanting the signature; the result is shown on the app page.
- Two publishing modes: developer-signed only (published only if it matches the rebuild; the allowed signing key can be pinned), or signed by F-Droid.
- Extra repositories can be added by the user.
- Updates through the client app.

## What it does not do

- It is not a paid-app marketplace (Open: confirm wording in the documentation).

## Open

- Background update behaviour, privileged-extension installs, mirrors: not checked.
