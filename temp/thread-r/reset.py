#!/usr/bin/env python3
"""reset.py <repo dir>: versions -> 0.0.1 (package/workspace.package only), FreeSynergy git tags -> v0.0.1, path+version -> 0.0.1."""
import re, sys, glob, os
root = sys.argv[1]
deps_only = '--deps-only' in sys.argv
names = {os.path.basename(p.rstrip('/')) for p in glob.glob('/srv/FreeSynergy/fs-*/')}
files = [os.path.join(root, 'Cargo.toml')] + glob.glob(os.path.join(root, 'crates', '*', 'Cargo.toml'))
changed = 0
for f in files:
    if not os.path.exists(f): continue
    out, sect = [], ''
    for line in open(f).read().split('\n'):
        m = re.match(r'^\[(.+)\]\s*$', line)
        if m: sect = m.group(1)
        if not deps_only and sect in ('package', 'workspace.package') and re.match(r'^version = "', line):
            line = 'version = "0.0.1"'
        # git deps on our repos
        line = re.sub(r'(github\.com/FreeSynergy/(fs-[a-z0-9-]+)(?:\.git)?",\s*tag = ")v[0-9][^"]*"',
                      lambda m: m.group(1) + 'v0.0.1"' if m.group(2) in names else m.group(0), line)
        line = re.sub(r'(github\.com/FreeSynergy/(fs-[a-z0-9-]+)(?:\.git)?",\s*)rev = "[^"]*"',
                      lambda m: m.group(1) + 'tag = "v0.0.1"' if m.group(2) in names else m.group(0), line)
        # path deps with a version requirement on our own crates
        if re.match(r'^fs-[a-z0-9-]+\s*=\s*\{.*path\s*=', line):
            if not deps_only: line = re.sub(r'version = "[^"]*"', 'version = "0.0.1"', line)
        out.append(line)
    new = '\n'.join(out)
    if new != open(f).read():
        open(f, 'w').write(new); changed += 1
print('changed', changed, 'files')
