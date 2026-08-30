"""
Test standpoint corpus builder against a single paper.
Uses: full_shotgun_expansion_all.jsonl + .text/1406.2661_Generative Adversarial Nets.txt
"""
from pathlib import Path
import json, re
from collections import Counter
from emotional_engine import collapse_full_128

corpus_root = Path(r'Path(__file__).resolve().parent.parent / 'learning-corpus'')
text_root = corpus_root / '.text'
shotgun_path = Path(r'C:\Users\krist\Desktop\KING-WEN-I-CHING-IMMUTABLE-TABLES\kingwen_train_data\full_shotgun_expansion_all.jsonl')

# Load single test paper
test_fname = 'diffusion-generative_1406.2661_Generative Adversarial Nets.txt'
txt_path = text_root / test_fname
paper_text = txt_path.read_text(encoding='utf-8', errors='ignore')
print(f'Test paper: {test_fname}')
print(f'Text length: {len(paper_text)} chars')

# Load shotgun stance pool
shotgun_index = {}
with shotgun_path.open(encoding='utf-8') as f:
    for line in f:
        rec = json.loads(line)
        lp = rec.get('label_payload', {})
        hid = lp.get('hexagram_id')
        phase = lp.get('phase_temporal')
        if hid and phase:
            key = (int(hid), phase)
            shotgun_index.setdefault(key, []).append(lp)
print(f'Shotgun pool: {len(shotgun_index)} (hex,phase) entries')

# Run live consult for comparison
consult = collapse_full_128(50)
resolved = consult.get('resolved', [])
print(f'Live consult: {len(resolved)} resolved')

STOP = {'a','an','the','for','of','on','and','in','to','with','from','by','into','via','using','based','towards','is','are','was','were','be','been','being','have','has','had','do','does','did','will','would','could','should','may','might','shall','can','this','that','these','those','it','its','we','our','they','them','their','he','she','his','her','i','me','my','at','as','but','or','nor','not','so','if','then','than','too','very','just','about','above','after','again','all','also','am','because','before','between','both','during','each','few','further','get','here','how','into','more','most','other','out','over','own','same','some','such','only','through','under','until','up','while','within','without','model','models','paper','method','methods','approach','results','show','shows','present','propose','proposed','training','trained','learn','learning','data','dataset','datasets','performance','state','art','task','tasks','experiment','experiments','figure','table','section','introduction','conclusion','references','appendix','arxiv','abs','et','al','using','used','use','new','propose','proposed','proposal','result','results','show','showed','shown','showing','found','find','found','one','two','first','second','third','also','well','like','even','much','many','make','made','way','may','might','must','shall','will','would','could','should','can','cannot','could','would','should','however','therefore','thus','hence','since','because','although','though','while','where','when','how','what','which','who','whom','whose','why'}

def tokenize(text):
    return set(re.findall(r'[a-z0-9]+', text.lower())) - STOP

def extract_key_phrases(text, max_k=30):
    words = re.findall(r'[a-z]{3,}', text.lower())
    from collections import Counter
    counts = Counter(w for w in words if w not in STOP and len(w) > 2)
    return [w for w, _ in counts.most_common(max_k)]

def extract_paper_claims(text, max_claims=5):
    claims = []
    sentences = re.split(r'(?<=[.!?])\s+', text)
    patterns = ['we propose','we present','we introduce','we show','we demonstrate','our method','our approach','our model','this paper','this work','contribution','novel','outperform','state-of-the-art','sota','achieve','results show','we achieve','we obtain','we find','key insight','central','framework','architecture','algorithm','objective function','loss function','training procedure','network','model','approach','method']
    for s in sentences:
        s_clean = s.strip()
        if len(s_clean) < 40 or len(s_clean) > 500:
            continue
        if re.match(r'^[\d\s\.\,\[\]\(\)]+\s*$', s_clean):
            continue
        if 'http' in s_clean or 'doi.org' in s_clean or 'arxiv:' in s_clean.lower():
            continue
        words = re.findall(r'[a-z]{3,}', s_clean.lower())
        if len(words) < 5:
            continue
        if any(p in s_clean.lower() for p in patterns):
            claims.append(s_clean)
        if len(claims) >= max_claims:
            break
    return claims[:max_claims]

def stance_signature(rec):
    sym = rec.get('hexagram_symbols', {})
    inj = rec.get('inject_site', {})
    intent = rec.get('intent', {})
    parts = [
        sym.get('name', ''), sym.get('category', ''), sym.get('action', ''),
        sym.get('upper_trigram', ''), sym.get('lower_trigram', ''),
        inj.get('primary_pool', ''), inj.get('secondary_pool', ''),
        ' '.join(intent.get('matched_intents', {}).keys()),
        rec.get('phase_temporal', ''),
    ]
    for sp in rec.get('sample_paths', [])[:3]:
        parts.append(sp.get('description', ''))
    return ' '.join(str(x) for x in parts if x)

# Build stance index from ALL 512 standpoints
stance_index = []
for key, recs in shotgun_index.items():
    lp = recs[0]
    sym = lp.get('hexagram_symbols', {})
    stance_index.append({
        'hexagram_id': lp.get('hexagram_id'),
        'hexagram_name': sym.get('name', ''),
        'phase_temporal': lp.get('phase_temporal', ''),
        'category': sym.get('category', ''),
        'action': sym.get('action', ''),
        'signature': stance_signature(lp),
        'primary_pool': lp.get('inject_site', {}).get('primary_pool', ''),
        'secondary_pool': lp.get('inject_site', {}).get('secondary_pool', ''),
    })

print(f'Stance index: {len(stance_index)} entries')

# Extract paper-specific content
paper_keywords = extract_key_phrases(paper_text)
paper_claims = extract_paper_claims(paper_text)
print(f'Paper keywords: {paper_keywords[:10]}')
print(f'Paper claims: {len(paper_claims)}')
for i, c in enumerate(paper_claims[:3]):
    print(f'  Claim {i+1}: {c[:150]}...')

# Score all 512 standpoints
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

scored.sort(key=lambda x: x['score'], reverse=True)
print(f'\nScored {len(scored)} standpoints')
print('Top 10 standpoints:')
for s in scored[:10]:
    print(f"  Hex {s['hexagram_id']:02d} {s['hexagram_name']} ({s['phase_temporal']}) score={s['score']} cat={s['category']} action={s['action']}")
    print(f"    primary_pool={s['primary_pool']}")
    print(f"    signature={s['signature'][:100]}...")

print('\nBottom 5 standpoints:')
for s in scored[-5:]:
    print(f"  Hex {s['hexagram_id']:02d} {s['hexagram_name']} ({s['phase_temporal']}) score={s['score']}")

# Build full output for this paper
output_records = []
for stance in scored:
    best_claim = paper_claims[0][:250] if paper_claims else ''
    action_verb = {'ASSERT': 'asserts', 'YIELD': 'yields to', 'ADAPT': 'adapts through', 'NAVIGATE': 'navigates', 'MEASURE': 'measures', 'CONNECT': 'connects', 'RECEIVE': 'receives', 'GENERATE': 'generates', 'TRANSFORM': 'transforms'}.get(stance['action'], stance['action'].lower())
    output_records.append({
        'paper_title': 'Generative Adversarial Nets',
        'paper_filename': test_fname,
        'standpoint_hexagram_id': stance['hexagram_id'],
        'standpoint_hexagram_name': stance['hexagram_name'],
        'standpoint_phase_temporal': stance['phase_temporal'],
        'standpoint_score': stance['score'],
        'standpoint_category': stance['category'],
        'standpoint_action': stance['action'],
        'why_this_standpoint': f"{stance['hexagram_name']} ({stance['action']}, {stance['category']}) {action_verb} this paper: '{best_claim}'" if best_claim else f"{stance['hexagram_name']} ({stance['action']}, {stance['category']}) {action_verb} this paper through {stance['category'].lower()} lens",
        'paper_keywords': paper_keywords[:15],
        'paper_claims': paper_claims[:3],
    })

# Write test output
out_path = corpus_root / 'test_standpoint_single_paper.jsonl'
with out_path.open('w', encoding='utf-8') as f:
    for rec in output_records:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')

print(f'\nWrote {len(output_records)} records to {out_path}')
print(f'File size: {out_path.stat().st_size:,} bytes')

# Verify coverage
hex_counter = Counter(r['standpoint_hexagram_id'] for r in output_records)
phase_counter = Counter(r['standpoint_phase_temporal'] for r in output_records)
print(f'Unique hexagrams: {len(hex_counter)}')
print(f'Unique phases: {len(phase_counter)}')
print(f'Score range: {min(r["standpoint_score"] for r in output_records)} - {max(r["standpoint_score"] for r in output_records)}')

# Show 3 sample records with full content
print('\n=== SAMPLE RECORDS ===')
for rec in output_records[:3]:
    print(f"\nHex {rec['standpoint_hexagram_id']:02d} {rec['standpoint_hexagram_name']} ({rec['standpoint_phase_temporal']}) score={rec['standpoint_score']}")
    print(f"  cat={rec['standpoint_category']} action={rec['standpoint_action']}")
    print(f"  why: {rec['why_this_standpoint'][:200]}")
    if rec['paper_claims']:
        print(f"  claim: {rec['paper_claims'][0][:120]}...")
