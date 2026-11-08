# Install FreeSynergy

**Pre-release. Please read this first.** FreeSynergy is at the beginning. What you can install today is a first version meant for people who want to try things and tell us what is wrong. Expect rough edges, and do not put anything on it that you cannot lose.

## The idea: get the Store once, then everything from the Store

You install one program by hand, [FreeSynergy.Store](../programs/platform/store.md). After that you install, update and remove every other FreeSynergy program from there, with one click and with every file checked before it reaches your machine. You should not have to download things by hand over and over.

## Step 1: get the Store

The Store is published as a **pre-release** on GitHub: <https://github.com/FreeSynergy/fs-store/releases>.

Pick the newest release marked "Pre-release". A release carries these files (the exact set can change from release to release, so look at the list there):

| For | File |
|-----|------|
| Fedora and other rpm systems | `.rpm` |
| Debian and Ubuntu | `.deb` |
| Arch | `.pkg.tar.zst` |
| any Linux, no root needed | `.tar.gz` or `.AppImage` (x86_64 and aarch64) |
| macOS | `.dmg` |
| checking | `SHA256SUMS.txt`, one `.asc` signature next to every file, the release key `FreeSynergy-release-key.pgp` |

Windows is not in the release yet. The macOS build is not signed with a paid Apple certificate: on macOS open the app once, then System Settings > Privacy & Security > "Open Anyway". The OpenPGP signatures and checksums are the trust path.

!!! warning "State on 2026-11-08"
    The newest pre-release on 2026-11-08 is `v0.1.0-rc.9`. The first one (`v0.1.0-rc.1`) is marked "Do not use": it cannot verify packages signed by the release workflow. Always take the newest pre-release in the list.

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
- **Without root:** unpack the `.tar.gz` somewhere in your home folder, or make the `.AppImage` executable and start it.

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
