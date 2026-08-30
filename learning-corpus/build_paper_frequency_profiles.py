from pathlib import Path
import json, re
from collections import Counter

root = Path('Path(__file__).resolve().parent.parent / 'learning-corpus' / '.text'')
out_path = root.parent / 'paper_frequency_profiles.jsonl'

STOP = {'the','and','for','with','from','that','this','they','have','been','were','their','would','could','should','which','where','when','what','than','then','them','also','more','most','some','into','over','such','only','other','many','much','each','about','because','through','during','before','after','above','below','between','same','different','often','however','although','while','since','until','because','both','few','most','own','same','than','too','very','just','still','already','ever','never','always','usually','sometimes','really','perhaps','certainly','definitely','probably','possible','likely','clear','known','given','shown','found','used','using','based','proposed','presented','introduced','developed','designed','implemented','evaluated','compared','analyzed','discussed','reported','demonstrated','shown','observed','results','method','approach','model','models','paper','propose','present','introduce','show','result','performance','accuracy','improvement','state','art','using','based','et','al','fig','figure','table','equation','section','appendix','references','abstract','introduction','conclusion','future','work'}

files = sorted(root.glob('*.txt'))
print(f'found {len(files)} files')

def profile_paper(path):
    txt = path.read_text(encoding='utf-8', errors='ignore')
    txt = re.sub(r'\r\n?', '\n', txt)
    
    words = re.findall(r"[A-Za-z']+", txt.lower())
    word_freq = Counter(w for w in words if w not in STOP and len(w) > 2)
    
    numbers = re.findall(r'\b\d+\.?\d*\b', txt)
    number_freq = Counter(numbers)
    
    symbols = re.findall(r'[^A-Za-z0-9\s]', txt)
    symbol_freq = Counter(symbols)
    
    top_words = [{'w': w, 'c': c, 'pct': round(c/max(len(words),1), 6)} for w, c in word_freq.most_common(80)]
    top_numbers = [{'n': n, 'c': c} for n, c in number_freq.most_common(30)]
    top_symbols = [{'s': s, 'c': c} for s, c in symbol_freq.most_common(20)]
    
    categories = {
        'diffusion': len(re.findall(r'diffusion|ddpm|score[- ]based|denoise', txt, re.I)),
        'gan': len(re.findall(r'generative adversarial|gan\b|dcgan|stylegan', txt, re.I)),
        'transformer': len(re.findall(r'transformer|self[- ]attention|multi[- ]head', txt, re.I)),
        'graph': len(re.findall(r'graph neural|gnn|node embedding|link prediction', txt, re.I)),
        'rlhf_alignment': len(re.findall(r'rlhf|preference|alignment|dpo|reward model', txt, re.I)),
        'quant_efficiency': len(re.findall(r'quantiz|prun|spars|distill|compress|speculative|kv cache', txt, re.I)),
        'multimodal': len(re.findall(r'multimodal|vision[- ]?language|vqa|clip', txt, re.I)),
        'audio': len(re.findall(r'audio|speech|tts|music generation', txt, re.I)),
        'video': len(re.findall(r'video generation|temporal|frame', txt, re.I)),
        'reasoning': len(re.findall(r'reasoning|chain[- ]of[- ]thought|cot\b', txt, re.I)),
        'safety': len(re.findall(r'safety|jailbreak|red team|adversarial attack', txt, re.I)),
    }
    total_signal = max(sum(categories.values()), 1)
    category_signals = {k: round(v/total_signal, 4) for k, v in categories.items() if v > 0}
    dominant_signal = max(categories, key=categories.get) if max(categories.values()) > 0 else 'general'
    
    latex_density = round(len(re.findall(r'\\[A-Za-z]+\{', txt)) / max(len(txt), 1), 6)
    
    return {
        'file': str(path.relative_to(root)),
        'paper_id': path.stem.split('_', 1)[1] if '_' in path.stem else path.stem,
        'category': path.stem.split('_')[0] if '_' in path.stem else 'unknown',
        'chars': len(txt),
        'words_total': len(words),
        'unique_words': len(word_freq),
        'lexical_density': round(len(word_freq) / max(len(words), 1), 4),
        'top_words': top_words[:50],
        'top_numbers': top_numbers[:20],
        'top_symbols': top_symbols[:15],
        'category_signals': category_signals,
        'dominant_signal': dominant_signal,
        'latex_density': latex_density,
        'number_density': round(len(numbers) / max(len(txt), 1), 6),
        'symbol_density': round(len(symbols) / max(len(txt), 1), 6),
    }

profiles = []
errors = 0
for path in files:
    try:
        profiles.append(profile_paper(path))
    except Exception as e:
        errors += 1
        if errors <= 5:
            print(f'error {path.name}: {e}')

with out_path.open('w', encoding='utf-8') as f:
    for rec in profiles:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')

print(f'profiles: {len(profiles)}')
print('dominant signals:', Counter(p['dominant_signal'] for p in profiles).most_common(10))
print('avg lexical density:', round(sum(p['lexical_density'] for p in profiles)/max(len(profiles),1), 4))
print('avg latex density:', round(sum(p['latex_density'] for p in profiles)/max(len(profiles),1), 6))
print('avg number density:', round(sum(p['number_density'] for p in profiles)/max(len(profiles),1), 6))
print('wrote', out_path)
