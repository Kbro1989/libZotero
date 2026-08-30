from pathlib import Path
import json, re
from collections import Counter

corpus_root = Path(r'C:\Users\krist\Desktop\zotero\learning-corpus')
base_manifest = corpus_root / 'paper_study_notes.jsonl'
corpus_path = corpus_root / 'kingwen_paper_study_corpus.jsonl'

# Step 1: Restore full 245-record baseline from manifest
records = []
with base_manifest.open('r', encoding='utf-8') as f:
    for line in f:
        records.append(json.loads(line))

print(f'Restored {len(records)} records from manifest')

# Ensure every record has the required fields
for rec in records:
    rec.setdefault('study_notes', [])
    rec.setdefault('kingwen_hexagram_ids', [])
    rec.setdefault('kingwen_phase_suggestions', [])
    rec.setdefault('per_page_notes', [])
    rec.setdefault('extended_study_notes', [])
    rec.setdefault('upgrade_matrix', {})

# Step 2: Parse inference/quantization sidecar if present
inference_md = corpus_root / 'extended_study_notes_inference_quantization.md'
if inference_md.exists():
    text = inference_md.read_text(encoding='utf-8', errors='ignore')
    # Split by paper headings
    papers = re.split(r'^##\s+', text, flags=re.MULTILINE)
    for paper_block in papers[1:]:
        lines = paper_block.splitlines()
        title = lines[0].strip().rstrip('#').strip() if lines else ''
        if not title:
            continue
        # Find matching record by title substring
        for rec in records:
            if title.lower() in rec.get('title', '').lower() or rec.get('title', '').lower() in title.lower():
                rec['extended_study_notes'].append({
                    'source': 'inference_quantization_sidecar',
                    'title': title,
                    'raw_block': paper_block.strip()[:2000]
                })
                break

# Step 3: Rebuild per-page notes from full text if missing
corpus_text_root = corpus_root / '.text'
for rec in records:
    if not rec.get('per_page_notes'):
        txt_path = corpus_text_root / rec['filename']
        if txt_path.exists():
            text = txt_path.read_text(encoding='utf-8', errors='ignore')
            chunk_size = 2200
            page = 1
            per_page = []
            start = 0
            while start < len(text):
                end = start + chunk_size
                chunk = text[start:end]
                if end < len(text):
                    brk = chunk.rfind('\n\n')
                    if brk > 350:
                        chunk = chunk[:brk+2]
                        end = start + brk + 2
                per_page.append({
                    'page_number': page,
                    'char_count': len(chunk),
                    'upgrade_categories': rec.get('upgrade_categories', [])[:3],
                    'findings': [],
                    'kingwen_hexagram_ids': rec.get('kingwen_hexagram_ids', [])[:6],
                    'kingwen_phase_suggestions': rec.get('kingwen_phase_suggestions', [])[:6]
                })
                start = end
                page += 1
            rec['per_page_notes'] = per_page

# Step 4: Build upgrade matrix
upgrade_matrix = {}
for rec in records:
    for cat in rec.get('upgrade_categories', []):
        upgrade_matrix.setdefault(cat, [])
        if rec['title'] not in upgrade_matrix[cat]:
            upgrade_matrix[cat].append(rec['title'])

# Attach upgrade_matrix to every record
for rec in records:
    rec['upgrade_matrix'] = upgrade_matrix

# Step 5: Write final corpus
with corpus_path.open('w', encoding='utf-8') as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')

print(f'Wrote {len(records)} records to {corpus_path}')
print(f'Records with extended_study_notes: {sum(1 for r in records if r.get("extended_study_notes"))}')
print(f'Records with upgrade_matrix: {sum(1 for r in records if r.get("upgrade_matrix"))}')
print(f'Records with per_page_notes: {sum(1 for r in records if r.get("per_page_notes"))}')
print(f'Upgrade matrix categories: {len(upgrade_matrix)}')
for k, v in sorted(upgrade_matrix.items(), key=lambda x: -len(x[1]))[:8]:
    print(f'  {k}: {len(v)} papers')
