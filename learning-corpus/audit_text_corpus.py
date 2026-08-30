from pathlib import Path
import json, re
from collections import Counter, defaultdict

root = Path('.').resolve()
text_dir = root / '.text'
out_path = root / 'text_corpus_audit.jsonl'

files = sorted(text_dir.glob('*.txt'))
print(f'found {len(files)} txt files')

issue_regexes = [
    (re.compile(r'catastrophic forgetting', re.I), 'catastrophic_forgetting'),
    (re.compile(r'drift|distribution shift|domain shift', re.I), 'distribution_drift'),
    (re.compile(r'hallucination|faithful|factuality', re.I), 'hallucination_factuality'),
    (re.compile(r'robust|adversar', re.I), 'robustness_adversarial'),
    (re.compile(r'bias|fairness|toxicity', re.I), 'bias_fairness'),
    (re.compile(r'quantiz|prun|spars|distill|compress', re.I), 'efficiency_compression'),
    (re.compile(r'multi[- ]?modal|vision[- ]?language', re.I), 'multimodal'),
    (re.compile(r'graph neural|GNN|node embedding|link prediction', re.I), 'graph_learning'),
    (re.compile(r'diffusion|score[- ]?based|flow|latent', re.I), 'generative_diffusion'),
    (re.compile(r'RLHF|preference|alignment|DPO|reward model', re.I), 'alignment_preference'),
    (re.compile(r'speculative decoding|KV cache|inference speed|latency', re.I), 'inference_optimization'),
    (re.compile(r'watermark|detectability|traceability', re.I), 'watermark_traceability'),
    (re.compile(r'privacy|differential privacy|membership inference', re.I), 'privacy'),
    (re.compile(r'safety|red team|jailbreak', re.I), 'safety'),
    (re.compile(r'benchmark|evaluation metric|leaderboard', re.I), 'benchmark_eval'),
]

# heuristic section split on blank-line double newlines
def split_pages(text):
    parts = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
    return parts

records = []
category_counter = Counter()
size_bucket_counter = Counter()
issue_counter = Counter()
per_category_issues = defaultdict(Counter)

for path in files:
    txt = path.read_text(encoding='utf-8', errors='ignore')
    chars = len(txt)
    words = len(txt.split())
    pages = max(1, round(chars / 3000))
    size_bucket = 'stub' if chars < 2000 else 'medium' if chars < 8000 else 'full'
    size_bucket_counter[size_bucket] += 1

    name = path.stem
    category = name.split('_')[0] if '_' in name else 'unknown'
    if category not in {'graph-neural-networks','diffusion-generative','llm-alignment','efficient-inference-quantization','multimodal-learning'}:
        category = 'unknown'
    category_counter[category] += 1

    parts = split_pages(txt)
    page_snippets = parts[:20]
    page_text = '\n'.join(page_snippets)

    found_issues = []
    seen = set()
    for pat, issue in issue_regexes:
        if pat.search(page_text):
            if issue not in seen:
                found_issues.append(issue)
                seen.add(issue)
                issue_counter[issue] += 1
                per_category_issues[category][issue] += 1

    records.append({
        'file': str(path.relative_to(root)),
        'category': category,
        'chars': chars,
        'words': words,
        'pages_approx': pages,
        'size_bucket': size_bucket,
        'issues': found_issues,
        'issue_count': len(found_issues),
        'page_snippets': page_snippets[:6],
    })

with out_path.open('w', encoding='utf-8') as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')

summary = {
    'total_files': len(records),
    'categories': dict(category_counter),
    'size_buckets': dict(size_bucket_counter),
    'issues_total': dict(issue_counter.most_common()),
    'per_category_issues': {k: dict(v.most_common()) for k,v in per_category_issues.items()},
    'top_issue_papers': [
        {'file': r['file'], 'issues': r['issues']}
        for r in sorted(records, key=lambda x: x['issue_count'], reverse=True)[:25]
    ],
}
(root / 'text_corpus_audit_summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')

print('wrote', out_path)
print(json.dumps(summary, ensure_ascii=False, indent=2))
