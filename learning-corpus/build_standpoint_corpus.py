"""
Full expanded standpoint corpus: 245 papers × 512 standpoints = 125,440 records.
Uses:
  - full_shotgun_expansion_all.jsonl for hexagram standpoint definitions
  - .text/*.txt for actual paper content extraction
  - collapse_full_128() consult for live engine pool
"""
from pathlib import Path
import json, re
from collections import Counter
from emotional_engine import collapse_full_128

corpus_root = Path(r'C:\Users\krist\Desktop\zotero\learning-corpus')
text_root = corpus_root / '.text'
output_path = corpus_root / 'kingwen_standpoint_corpus.jsonl'
corpus_path = corpus_root / 'kingwen_paper_study_corpus.jsonl'
shotgun_path = Path(r'C:\Users\krist\Desktop\KING-WEN-I-CHING-IMMUTABLE-TABLES\kingwen_train_data\full_shotgun_expansion_all.jsonl')

# Load base corpus
base_records = []
with corpus_path.open('r', encoding='utf-8') as f:
    for line in f:
        if line.strip():
            base_records.append(json.loads(line))
print(f'Loaded {len(base_records)} base corpus records')

# Load full shotgun expansion for standpoint definitions
shotgun_index = {}
with shotgun_path.open('r', encoding='utf-8') as f:
    for line in f:
        rec = json.loads(line)
        lp = rec.get('label_payload', {})
        hid = lp.get('hexagram_id')
        phase = lp.get('phase_temporal')
        if hid and phase:
            key = (int(hid), phase)
            shotgun_index.setdefault(key, []).append(lp)
print(f'Shotgun index: {len(shotgun_index)} (hex,phase) entries')

# Also run live consult for fresh pool
consult = collapse_full_128(50)
resolved = consult.get('resolved', [])
print(f'Live consult: {len(resolved)} resolved standpoints')

# Merge: use shotgun if available, fallback to live consult
stance_pool = []
seen_keys = set()
for key, recs in shotgun_index.items():
    hid, phase = key
    lp = recs[0]
    stance_pool.append({
        'hexagram_id': hid,
        'phase_temporal': phase,
        'hexagram_symbols': lp.get('hexagram_symbols', {}),
        'inject_site': lp.get('inject_site', {}),
        'intent': lp.get('intent', {}),
        'sample_paths': lp.get('sample_paths', [])[:2],
        'source': 'shotgun'
    })
    seen_keys.add(key)

for rec in resolved:
    hid = rec.get('hexagram_id')
    phase = rec.get('phase_temporal')
    key = (hid, phase)
    if key not in seen_keys:
        stance_pool.append({
            'hexagram_id': hid,
            'phase_temporal': phase,
            'hexagram_symbols': rec.get('hexagram_symbols', {}),
            'inject_site': rec.get('inject_site', {}),
            'intent': rec.get('intent', {}),
            'sample_paths': rec.get('sample_paths', [])[:2],
            'source': 'live'
        })
        seen_keys.add(key)

print(f'Merged stance pool: {len(stance_pool)} entries')

STOP = {'a','an','the','for','of','on','and','in','to','with','from','by','into','via','using','based','towards','is','are','was','were','be','been','being','have','has','had','do','does','did','will','would','could','should','may','might','shall','can','this','that','these','those','it','its','we','our','they','them','their','he','she','his','her','i','me','my','at','as','but','or','nor','not','so','if','then','than','too','very','just','about','above','after','again','all','also','am','because','before','between','both','during','each','few','further','get','here','how','into','more','most','other','out','over','own','same','some','such','only','through','under','until','up','while','within','without','model','models','paper','method','methods','approach','results','show','shows','present','propose','proposed','training','trained','learn','learning','data','dataset','datasets','performance','state','art','task','tasks','experiment','experiments','figure','table','section','introduction','conclusion','references','appendix','arxiv','abs','et','al','using','used','use','new','propose','proposed','proposal','result','results','show','showed','shown','showing','found','find','found','one','two','first','second','third','also','well','like','even','much','many','make','made','way','may','might','must','shall','will','would','could','should','can','cannot','could','would','should','however','therefore','thus','hence','since','because','although','though','while','where','when','how','what','which','who','whom','whose','why'}

def tokenize(text):
    return set(re.findall(r'[a-z0-9]+', text.lower())) - STOP

def extract_paper_claims(text, max_claims=8):
    """Extract specific claims/methods from paper text."""
    claims = []
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    # Look for claim patterns
    patterns = [
        r'we propose',
        r'we present',
        r'we introduce',
        r'we show',
        r'we demonstrate',
        r'our method',
        r'our approach',
        r'our model',
        r'this paper',
        r'this work',
        r'contribution',
        r'novel',
        r'outperform',
        r'state-of-the-art',
        r'sota',
        r'achieve',
        r'results show',
        r'we achieve',
        r'we obtain',
        r'we find',
        r'key insight',
        r'central',
        r'framework',
        r'architecture',
        r'algorithm',
        r'objective function',
        r'loss function',
        r'training procedure',
        r'network',
        r'model',
        r'approach',
        r'method',
    ]
    
    for s in sentences:
        s_clean = s.strip()
        if len(s_clean) < 40 or len(s_clean) > 500:
            continue
        s_lower = s_clean.lower()
        if any(p in s_lower for p in patterns):
            # Skip references, author lines, etc.
            if re.match(r'^[\d\s\.\,\[\]\(\)]+\s*$', s_clean):
                continue
            if 'http' in s_clean or 'doi.org' in s_clean or 'arxiv:' in s_clean.lower():
                continue
            words = re.findall(r'[a-z]{3,}', s_lower)
            if len(words) < 5:
                continue
            claims.append(s_clean)
        if len(claims) >= max_claims:
            break
    
    return claims[:max_claims]

def extract_key_phrases(text, max_k=30):
    words = re.findall(r'[a-z]{3,}', text.lower())
    counts = Counter(w for w in words if w not in STOP and len(w) > 2)
    return [w for w, _ in counts.most_common(max_k)]

def stance_signature(rec):
    sym = rec.get('hexagram_symbols', {})
    inj = rec.get('inject_site', {})
    intent = rec.get('intent', {})
    parts = [
        sym.get('name', ''),
        sym.get('category', ''),
        sym.get('action', ''),
        sym.get('upper_trigram', ''),
        sym.get('lower_trigram', ''),
        inj.get('primary_pool', ''),
        inj.get('secondary_pool', ''),
        ' '.join(intent.get('matched_intents', {}).keys()),
        rec.get('phase_temporal', ''),
    ]
    for sp in rec.get('sample_paths', [])[:3]:
        parts.append(sp.get('description', ''))
    return ' '.join(str(x) for x in parts if x)

# Build stance index from ALL 512 standpoints
stance_index = []
for stance in stance_pool:
    stance_index.append({
        'hexagram_id': stance['hexagram_id'],
        'hexagram_name': stance['hexagram_symbols'].get('name', ''),
        'phase_bits': stance['hexagram_symbols'].get('phase_bits', 0),
        'phase_temporal': stance['phase_temporal'],
        'category': stance['hexagram_symbols'].get('category', ''),
        'action': stance['hexagram_symbols'].get('action', ''),
        'signature': stance_signature(stance),
        'primary_pool': stance['inject_site'].get('primary_pool', ''),
        'secondary_pool': stance['inject_site'].get('secondary_pool', ''),
        'sample_paths': [sp.get('description','') for sp in stance.get('sample_paths', [])[:2]],
        'training_notes': list(stance['intent'].get('matched_intents', {}).keys())[:5],
    })

print(f'Stance index: {len(stance_index)} entries')

# Build FULL expanded standpoint corpus: ALL 512 standpoints per paper
standpoint_records = []
skipped = 0
no_text = 0

for base in base_records:
    fname = base.get('filename', '')
    txt_path = text_root / fname
    if not txt_path.exists():
        no_text += 1
        skipped += 1
        continue

    paper_text = txt_path.read_text(encoding='utf-8', errors='ignore')
    paper_keywords = extract_key_phrases(paper_text)
    paper_claims = extract_paper_claims(paper_text)
    
    # Score ALL 512 standpoints
    scored = []
    for stance in stance_index:
        sig_tokens = tokenize(stance['signature'])
        kw_tokens = tokenize(' '.join(paper_keywords[:30]))
        overlap = len(sig_tokens & kw_tokens)
        score = overlap / max(len(kw_tokens), 1)
        action_bonus = sum(0.02 for kw in paper_keywords[:20] if kw in stance['action'].lower())
        cat_bonus = sum(0.02 for kw in paper_keywords[:20] if kw in stance['category'].lower())
        total = round(min(score + action_bonus + cat_bonus, 1.0), 4)
        scored.append({**stance, 'score': total})

    # ALL 512 standpoints per paper
    for stance in scored:
        # Build paper-specific why using actual claims
        best_claim = ''
        if paper_claims:
            best_claim = paper_claims[0][:250]
        else:
            # fallback to first substantial sentence
            sentences = re.split(r'(?<=[.!?])\s+', paper_text)
            for s in sentences:
                s = s.strip()
                if 40 < len(s) < 500:
                    best_claim = s[:250]
                    break
        
        action_verb = {
            'ASSERT': 'asserts', 'YIELD': 'yields to', 'ADAPT': 'adapts through',
            'NAVIGATE': 'navigates', 'MEASURE': 'measures', 'CONNECT': 'connects',
            'RECEIVE': 'receives', 'GENERATE': 'generates', 'TRANSFORM': 'transforms'
        }.get(stance['action'], stance['action'].lower())
        
        record = {
            'paper_title': base.get('title', ''),
            'paper_filename': fname,
            'paper_arxiv_id': base.get('file', '').split('_', 1)[0] if base.get('file') else '',
            'paper_upgrade_categories': base.get('upgrade_categories', []),
            'standpoint_hexagram_id': stance['hexagram_id'],
            'standpoint_hexagram_name': stance['hexagram_name'],
            'standpoint_phase_bits': stance['phase_bits'],
            'standpoint_phase_temporal': stance['phase_temporal'],
            'standpoint_score': stance['score'],
            'standpoint_category': stance['category'],
            'standpoint_action': stance['action'],
            'standpoint_primary_pool': stance['primary_pool'],
            'standpoint_secondary_pool': stance['secondary_pool'],
            'standpoint_training_intents': stance['training_notes'],
            'standpoint_sample_paths': stance['sample_paths'],
            'why_this_standpoint': f"{stance['hexagram_name']} ({stance['action']}, {stance['category']}) {action_verb} this paper: '{best_claim}'" if best_claim else f"{stance['hexagram_name']} ({stance['action']}, {stance['category']}) {action_verb} this paper through {stance['category'].lower()} lens",
            'paper_keywords': paper_keywords[:15],
            'paper_char_count': len(paper_text),
            'paper_claims': paper_claims[:3],
        }
        standpoint_records.append(record)

print(f'Skipped: {skipped} total, {no_text} missing text')
print(f'Standpoint records generated: {len(standpoint_records)}')
print(f'Expected: {len(base_records) * 512} = {len(base_records)} papers × 512 standpoints')

with output_path.open('w', encoding='utf-8') as f:
    for rec in standpoint_records:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')

print(f'Wrote to {output_path}')
hex_counter = Counter(r['standpoint_hexagram_id'] for r in standpoint_records)
phase_counter = Counter(r['standpoint_phase_temporal'] for r in standpoint_records)
print('Top hexagrams:')
for hid, cnt in hex_counter.most_common(12):
    print(f'  Hex {hid:02d}: {cnt}')
print('Phase distribution:', dict(phase_counter))
print('Avg standpoints per paper:', round(len(standpoint_records) / max(len(base_records), 1), 2))
