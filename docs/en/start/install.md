# Install FreeSynergy

**Pre-release. Please read this first.** FreeSynergy is at the beginning. What you can install today is a first version meant for people who want to try things and tell us what is wrong. Expect rough edges, and do not put anything on it that you cannot lose.

## The idea: get the Store once, then everything from the Store

You install one program by hand, [FreeSynergy.Store](../programs/platform/store.md). After that you install, update and remove every other FreeSynergy program from there, with one click and with every file checked before it reaches your machine. You should not have to download things by hand over and over.

## Step 1: get the Store

The Store is published as a **pre-release** on GitHub: <https://github.com/FreeSynergy/fs-store/releases>.

Pick the newest release marked "Pre-release". On 2026-11-08 the releases (up to `v0.0.6`) carry these files (look at the list there, it can grow):

| For | File |
|-----|------|
| Fedora and other rpm systems | `.rpm` (x86_64 and aarch64) |
| any Linux, no root needed | `.tar.gz` (x86_64 and aarch64) |
| checking | `SHA256SUMS.txt`, one `.asc` signature next to every file, the release key `FreeSynergy-release-key.pgp`, an SBOM (`.spdx.json`) |

Packages for Debian and Ubuntu (`.deb`), Arch, AppImage and macOS (`.dmg`) are not in these releases; earlier builds had them. Windows is not built yet. If you use a macOS build later: it is not signed with a paid Apple certificate, so open the app once, then System Settings > Privacy & Security > "Open Anyway". The OpenPGP signatures and checksums are the trust path.

!!! warning "State on 2026-11-08"
    Always take the newest release in the list. Version numbers were reset to `0.0.N` ([ADR 0064](../decisions/0064-versionen-ab-0-0-1.md)): `0.0.N` means development, `0.1.0` means a person can use it, `1.0.0` means two independent users of its interface. The earlier builds (`0.1.0-rc.N`) were removed. If you installed one as an rpm, remove it once (`sudo dnf remove fs-store`) before installing the new one, because the new number is lower and would not count as an update.

## Step 2: check the signature

Every file is signed with OpenPGP. The project key is:

```text
16A4 A3EE 563A EF51 FCF0 C55D ED7B 57C4 A190 4342
```

Releases are signed by a signing subkey of this key: `372A 583D 05BF 8362 604C F25D E26A 2347 F2B1 C097`.

With `gpg`, in the folder with your downloads:

```bash
gpg --import FreeSynergy-release-key.pgp
gpg --fingerprint 16A4A3EE563AEF51FCF0C55DED7B57C4A1904342     # compare with the line above
gpg --verify SHA256SUMS.txt.asc SHA256SUMS.txt                 # must say "Good signature"
sha256sum --ignore-missing -c SHA256SUMS.txt                   # every file you downloaded: OK
```

The releases also carry a build provenance attestation (SLSA), which you can check with `gh attestation verify <file> --repo FreeSynergy/fs-store`, and an SBOM (`*.spdx.json`).

Do not trust the key file only because it came with the release. Compare the fingerprint with this page and with the key file in the [documentation repository](https://github.com/FreeSynergy/fs-documentation). If a check fails, do not install, and tell us.

## Step 3: install the Store

- **Fedora:** `sudo dnf install ./fs-store-*.rpm` (root is asked by your system, not by us).
- **Without root (no `sudo`):** the `.tar.gz` holds one folder with the program `fs-store`. Unpack it into your home folder and run it from there:

  ```bash
  tar xzf fs-store-*-linux-x86_64.tar.gz     # or ...-linux-aarch64.tar.gz
  mkdir -p ~/.local/bin
  cp fs-store-*/fs-store ~/.local/bin/
  fs-store                                    # opens the window; if "command not found", use ~/.local/bin/fs-store
  ```

  Programs you install from the Store this way also go to your home folder (`~/.local`), so nothing needs root.

The Store is one program, `fs-store`. Started without arguments it opens its window. On the command line it works like `git`: `fs-store sources`, `fs-store available`, `fs-store install <package>`, `fs-store installed`. See [the Store](../programs/platform/store.md) for what works today.

## Step 4: everything else from the Store

Install the programs you want from the Store, for example Tasks or People. The Store checks the catalog and every package against the project key, keeps the old version when it updates, rolls back if an update fails, and updates itself the same way.

In the window, or on the command line:

```bash
fs-store install fs-tasks
fs-store install fs-people
fs-store installed
```

## What is not there yet

- A finished app for ordinary users. The windows are provisional and say so.
- A small catalog: the repository [fs-catalog](https://github.com/FreeSynergy/fs-catalog) offers the Store, Tasks and People so far (2026-11-08).
- Windows, and sign-in. See the [overall plan](../programs/apps/roadmap.md) for what comes next.

Found something broken or unclear? See [How to help](help.md).
