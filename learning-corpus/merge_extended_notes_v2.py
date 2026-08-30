from pathlib import Path
import json, re

corpus_root = Path(r'Path(__file__).resolve().parent.parent / 'learning-corpus'')
corpus_path = corpus_root / 'kingwen_paper_study_corpus.jsonl'
md_inference = corpus_root / 'extended_study_notes_inference_quantization.md'
md_multimodal = corpus_root / '_extracted_notes_draft_v3.md'

HEXAGRAM_UPGRADE_MAP = {
    1: "training_efficiency", 2: "state_machine_agent", 3: "diffusion_generative",
    4: "state_machine_agent", 5: "diffusion_generative", 6: "state_machine_agent",
    7: "inference_optimization", 8: "state_machine_agent", 9: "diffusion_generative",
    10: "state_machine_agent", 11: "training_efficiency", 12: "inference_optimization",
    13: "multimodal_reasoning", 14: "multimodal_reasoning", 15: "diffusion_generative",
    16: "training_efficiency", 17: "state_machine_agent", 18: "state_machine_agent",
    19: "multimodal_reasoning", 20: "inference_optimization", 21: "state_machine_agent",
    22: "multimodal_reasoning", 23: "diffusion_generative", 24: "diffusion_generative",
    25: "state_machine_agent", 26: "training_efficiency", 27: "state_machine_agent",
    28: "state_machine_agent", 29: "state_machine_agent", 30: "diffusion_generative",
    31: "multimodal_reasoning", 32: "training_efficiency", 33: "training_efficiency",
    34: "state_machine_agent", 35: "diffusion_generative", 36: "state_machine_agent",
    37: "multimodal_reasoning", 38: "state_machine_agent", 39: "state_machine_agent",
    40: "inference_optimization", 41: "training_efficiency", 42: "inference_optimization",
    43: "diffusion_generative", 44: "state_machine_agent", 45: "multimodal_reasoning",
    46: "diffusion_generative", 47: "state_machine_agent", 48: "state_machine_agent",
    49: "multimodal_reasoning", 50: "multimodal_reasoning", 51: "state_machine_agent",
    52: "state_machine_agent", 53: "training_efficiency", 54: "state_machine_agent",
    55: "multimodal_reasoning", 56: "inference_optimization", 57: "state_machine_agent",
    58: "state_machine_agent", 59: "inference_optimization", 60: "multimodal_reasoning",
    61: "state_machine_agent", 62: "training_efficiency", 63: "training_efficiency",
    64: "state_machine_agent"
}

def parse_markdown_blocks(text):
    blocks = []
    current_title = None
    current_body = []
    for line in text.splitlines():
        if line.startswith('## '):
            if current_title is not None:
                blocks.append({'title': current_title, 'body': '\n'.join(current_body).strip()})
            current_title = line[3:].strip()
            current_body = []
        else:
            current_body.append(line)
    if current_title is not None:
        blocks.append({'title': current_title, 'body': '\n'.join(current_body).strip()})
    return blocks

def extract_structured(block):
    body = block.get('body', '')
    lines = body.splitlines()
    methods = []
    equations = []
    claims = []
    upgrades = []
    hex_ids = []
    current_section = 'general'
    for line in lines:
        line_stripped = line.strip()
        if not line_stripped:
            continue
        if re.match(r'\*\*King Wen Hexagrams', line_stripped, re.I) or re.match(r'\*\*Hexagram', line_stripped, re.I) or line_stripped.lower().startswith('king wen hexagrams') or line_stripped.lower().startswith('hexagram'):
            hex_str = line_stripped.split(':', 1)[-1].strip() if ':' in line_stripped else line_stripped
            hex_ids = [int(h.strip()) for h in re.findall(r'\d+', hex_str) if 1 <= int(h.strip()) <= 64]
            continue
        if line_stripped.startswith('**Method') or line_stripped.startswith('Method:'):
            current_section = 'method'
            methods.append(line_stripped.split(':', 1)[-1].strip() if ':' in line_stripped else line_stripped)
        elif line_stripped.startswith('**Equation') or line_stripped.startswith('Equation'):
            current_section = 'equation'
            equations.append(line_stripped.split(':', 1)[-1].strip() if ':' in line_stripped else line_stripped)
        elif line_stripped.startswith('**Claim') or line_stripped.startswith('Claim'):
            current_section = 'claim'
            claims.append(line_stripped.split(':', 1)[-1].strip() if ':' in line_stripped else line_stripped)
        elif line_stripped.startswith('**Upgrade') or line_stripped.startswith('Upgrade'):
            current_section = 'upgrade'
            upgrades.append(line_stripped.split(':', 1)[-1].strip() if ':' in line_stripped else line_stripped)
        elif line_stripped.startswith('- '):
            item = line_stripped[2:].strip()
            if current_section == 'method':
                methods.append(item)
            elif current_section == 'equation':
                equations.append(item)
            elif current_section == 'claim':
                claims.append(item)
            elif current_section == 'upgrade':
                upgrades.append(item)
    return {
        'method': methods[:5],
        'equation': equations[:5],
        'claim': claims[:5],
        'upgrade_potential': upgrades[:5],
        'hexagram_ids': hex_ids[:6]
    }

records = []
with corpus_path.open('r', encoding='utf-8') as f:
    for line in f:
        records.append(json.loads(line))

print(f'Loaded {len(records)} records')

index_by_prefix = {}
index_by_title = {}
for idx, rec in enumerate(records):
    fname = rec.get('filename', '').lower()
    parts = fname.split('_', 1)
    if len(parts) >= 1:
        index_by_prefix[parts[0]] = idx
    title = rec.get('title', '').lower()
    index_by_title[title] = idx

sidecar_blocks = []
for md_path in [md_inference, md_multimodal]:
    if md_path.exists():
        text = md_path.read_text(encoding='utf-8', errors='ignore')
        blocks = parse_markdown_blocks(text)
        for block in blocks:
            block['source'] = md_path.name
            sidecar_blocks.append(block)
        print(f'Parsed {len(blocks)} blocks from {md_path.name}')

print(f'Total sidecar blocks: {len(sidecar_blocks)}')

def keyword_overlap_score(sidecar_title, corpus_title):
    stop = {'a','an','the','for','of','on','and','in','to','with','from','by','into','via','using','based','towards'}
    s_tokens = set(re.findall(r'[a-z0-9]+', sidecar_title.lower())) - stop
    c_tokens = set(re.findall(r'[a-z0-9]+', corpus_title.lower())) - stop
    if not s_tokens:
        return 0
    return len(s_tokens & c_tokens) / len(s_tokens)

matched = 0
unmatched = []
for block in sidecar_blocks:
    title = block.get('title', '')
    structured = extract_structured(block)
    body = block.get('body', '')
    file_match = re.search(r'`[^`]*?(\d{4}\.\d{4,5})[^`]*?\.txt`', body)
    arxiv_id = file_match.group(1) if file_match else None
    match_idx = None
    if arxiv_id and arxiv_id in index_by_prefix:
        match_idx = index_by_prefix[arxiv_id]
    else:
        best_score = 0
        best_idx = None
        for t, idx in index_by_title.items():
            score = keyword_overlap_score(title, t)
            if score > best_score and score >= 0.5:
                best_score = score
                best_idx = idx
        match_idx = best_idx
    if match_idx is not None:
        rec = records[match_idx]
        year_match = re.search(r'20\d{2}', rec.get('filename', ''))
        year = int(year_match.group()) if year_match else 2020
        if year >= 2024:
            phase_temporal = 'future'
            phase_bits = 2
        elif year >= 2022:
            phase_temporal = 'present'
            phase_bits = 1
        else:
            phase_temporal = 'past'
            phase_bits = 0
        if not structured['hexagram_ids']:
            hex_ids = []
            for cat in rec.get('upgrade_categories', []):
                for hid, mapped in HEXAGRAM_UPGRADE_MAP.items():
                    if mapped == cat and hid not in hex_ids:
                        hex_ids.append(hid)
                        break
            structured['hexagram_ids'] = hex_ids[:6]
        note = {
            'source': block.get('source', 'sidecar'),
            'title': title,
            'method': structured['method'],
            'equation': structured['equation'],
            'claim': structured['claim'],
            'upgrade_potential': structured['upgrade_potential'],
            'hexagram_ids': structured['hexagram_ids'],
            'phase_suggestion': {
                'phase_bits': phase_bits,
                'phase_temporal': phase_temporal
            }
        }
        existing_titles = [n.get('title') for n in rec.get('extended_study_notes', [])]
        if title not in existing_titles:
            rec.setdefault('extended_study_notes', []).append(note)
            matched += 1
    else:
        unmatched.append(title)

print(f'Matched and appended {matched} extended notes')
if unmatched:
    print(f'Unmatched ({len(unmatched)}):')
    for t in unmatched:
        print(f'  {t}')

upgrade_matrix = {}
for rec in records:
    for cat in rec.get('upgrade_categories', []):
        upgrade_matrix.setdefault(cat, [])
        if rec['title'] not in upgrade_matrix[cat]:
            upgrade_matrix[cat].append(rec['title'])

for rec in records:
    rec['upgrade_matrix'] = upgrade_matrix

with corpus_path.open('w', encoding='utf-8') as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')

print(f'Wrote {len(records)} records to {corpus_path}')
print(f'Records with extended_study_notes: {sum(1 for r in records if r.get("extended_study_notes"))}')
print(f'Records with upgrade_matrix: {sum(1 for r in records if r.get("upgrade_matrix"))}')
print(f'Upgrade matrix categories: {len(upgrade_matrix)}')
for k, v in sorted(upgrade_matrix.items(), key=lambda x: -len(x[1]))[:8]:
    print(f'  {k}: {len(v)} papers')
