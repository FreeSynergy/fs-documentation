#!/usr/bin/env python3
"""delete.py [--run] repo...: delete the old tags/releases listed in delete-list.md for repos that already have v0.0.1."""
import re, subprocess, sys
run = '--run' in sys.argv
rel_only = '--releases-only' in sys.argv
repos = [a for a in sys.argv[1:] if not a.startswith('--')]
text = open('/srv/FreeSynergy/.scratch/tr/delete-list.md').read()
sections = re.split(r'\n## ', text)[1:]
keep_tags = {'v0.0.1', 'v0.0.2'}
def sh(*a): return subprocess.run(a, capture_output=True, text=True)
for sec in sections:
    name = sec.split('\n', 1)[0].strip()
    if name not in repos: continue
    tags = re.search(r'^tags: (.*)$', sec, re.M).group(1).split()
    rel = re.findall(r'^\s+\S.*?\t(?:Draft|Pre-release|Latest)?\t?(v[^\t\s]+)\t', sec, re.M)
    tags = [t for t in tags if t not in keep_tags]
    # releases listed in the snapshot with tag != v0.0.x kept ones
    rtags = []
    for l in sec.split('\n'):
        parts = l.strip().split('\t')
        if len(parts) >= 3 and parts[-2].startswith('v'):
            rtags.append(parts[-2])
    rtags = [t for t in rtags if t not in keep_tags]
    print(f'{name}: releases {rtags} tags {tags}')
    if not run: continue
    have = sh('git', 'ls-remote', '--tags', f'git@github.com:FreeSynergy/{name}.git').stdout
    assert 'refs/tags/v0.0.1' in have, f'{name} has no v0.0.1: refusing'
    for t in rtags:
        r = sh('gh', 'release', 'delete', t, '-R', f'FreeSynergy/{name}', '-y')
        print('  release', t, 'rc', r.returncode, r.stderr.strip()[:100])
    if rel_only: continue
    for t in tags:
        if f'refs/tags/{t}\n' in have or have.endswith(f'refs/tags/{t}'):
            if t in rtags: continue
            r = subprocess.run(['git', 'push', f'git@github.com:FreeSynergy/{name}.git', f':refs/tags/{t}'], capture_output=True, text=True, cwd='/srv/FreeSynergy/fs-objects')
            print('  tag', t, 'rc', r.returncode, r.stderr.strip()[:100])
