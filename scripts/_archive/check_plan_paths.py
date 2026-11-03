import re, os

plan = open('temp/apps-plan.md', encoding='utf-8').read()
entries = re.findall(r'- \[( |x)\] (apps/\S+)', plan)

nowhere = []
for status, p in entries:
    tail = p[len('apps/'):] if p.startswith('apps/') else p
    candidates = [
        'docs/de/' + p,
        'docs/de/programs/' + p,
        'docs/de/programs/apps/' + tail,
        'docs/de/programs/suites/' + tail,
        'docs/de/programs/platform/' + tail,
    ]
    if not any(os.path.exists(c) for c in candidates):
        nowhere.append(p)

print('entries with no file anywhere:', len(nowhere))
for p in nowhere:
    print('   ', p)
