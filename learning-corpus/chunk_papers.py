from pathlib import Path
import json, re
from collections import Counter

root = Path('.').resolve()
text_dir = root / '.text'
out_path = root / 'paper_chunks_solutions_issues.jsonl'

CHUNK_SIZE = 2500
OVERLAP = 300

issue_patterns = [
    (re.compile(r'problem|challenge|limitation|difficulty|obstacle|bottleneck|issue|drawback|shortcoming', re.I), 'problem'),
    (re.compile(r'propose|present|introduce|develop|design|novel|new method|our approach|we suggest', re.I), 'solution'),
    (re.compile(r'result|achieve|outperform|improve|state-of-the-art|sota|significant|effective|demonstrate', re.I), 'result'),
    (re.compile(r'fail|error|bias|toxicity|hallucination|drift|forgetting|adversar|jailbreak|attack', re.I), 'common_issue'),
    (re.compile(r'future work|future direction|open problem|remain to be', re.I), 'future_work'),
]

files = sorted(text_dir.glob('*.txt'))
print(f'found {len(files)} txt files')

# Deduplicate exact byte matches while preserving category-prefixed path as primary when present
seen = {}
for p in files:
    h = hash(p.read_bytes())
    seen.setdefault(h, []).append(p)

primary = {}
for h, paths in seen.items():
    primary[h] = sorted(paths, key=lambda p: (0 if p.parent == text_dir and '_' in p.stem and p.stem.split('_',1)[0].replace('-','').isalpha() else 1, p.name))[0]

unique = sorted(set(primary.values()))
print(f'unique files after exact-dedup: {len(unique)}')

records = []
chunk_id = 0
for path in unique:
    txt = path.read_text(encoding='utf-8', errors='ignore')
    txt = re.sub(r'\r\n?', '\n', txt)
    txt = re.sub(r'\n{3,}', '\n\n', txt)
    if len(txt.strip()) < 200:
        continue
    # page-ish chunks with overlap
    chunks = []
    start = 0
    while start < len(txt):
        end = min(start + CHUNK_SIZE, len(txt))
        chunk = txt[start:end]
        # try not to split mid-word
        if end < len(txt):
            nxt = txt.find('\n', end)
            if nxt != -1 and nxt - end < 120:
                end = nxt + 1
        chunk = txt[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start = max(end - OVERLAP, start + 1)

    for chunk in chunks:
        labels = []
        for pat, label in issue_patterns:
            if pat.search(chunk):
                labels.append(label)
        if labels:
            chunk_id += 1
            records.append({
                'chunk_id': chunk_id,
                'file': str(path.relative_to(root)),
                'category': path.stem.split('_')[0] if '_' in path.stem else 'unknown',
                'paper_id': path.stem.split('_', 1)[1] if '_' in path.stem else path.stem,
                'char_len': len(chunk),
                'labels': labels,
                'text': chunk,
            })

with out_path.open('w', encoding='utf-8') as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')

summary = {
    'input_files': len(unique),
    'total_chunks': len(records),
    'label_counts': dict(Counter(l for r in records for l in r['labels']).most_common()),
    'files_with_chunks': len({r['file'] for r in records}),
}
(root / 'paper_chunks_summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(summary, ensure_ascii=False, indent=2))
print('wrote', out_path)
