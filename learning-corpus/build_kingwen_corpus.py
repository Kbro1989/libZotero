from pathlib import Path
import json
from collections import Counter

manifest_path = Path(r'Path(__file__).resolve().parent.parent / 'learning-corpus'\paper_study_notes.jsonl')
output_path = Path(r'Path(__file__).resolve().parent.parent / 'learning-corpus'\kingwen_paper_study_corpus.jsonl')

HEXAGRAM_UPGRADE_MAP = {
    1: "training_efficiency",
    2: "state_machine_agent",
    3: "diffusion_generative",
    4: "state_machine_agent",
    5: "diffusion_generative",
    6: "state_machine_agent",
    7: "inference_optimization",
    8: "state_machine_agent",
    9: "diffusion_generative",
    10: "state_machine_agent",
    11: "training_efficiency",
    12: "inference_optimization",
    13: "multimodal_reasoning",
    14: "multimodal_reasoning",
    15: "diffusion_generative",
    16: "training_efficiency",
    17: "state_machine_agent",
    18: "state_machine_agent",
    19: "multimodal_reasoning",
    20: "inference_optimization",
    21: "state_machine_agent",
    22: "multimodal_reasoning",
    23: "diffusion_generative",
    24: "diffusion_generative",
    25: "state_machine_agent",
    26: "training_efficiency",
    27: "state_machine_agent",
    28: "state_machine_agent",
    29: "state_machine_agent",
    30: "diffusion_generative",
    31: "multimodal_reasoning",
    32: "training_efficiency",
    33: "training_efficiency",
    34: "state_machine_agent",
    35: "diffusion_generative",
    36: "state_machine_agent",
    37: "multimodal_reasoning",
    38: "state_machine_agent",
    39: "state_machine_agent",
    40: "inference_optimization",
    41: "training_efficiency",
    42: "inference_optimization",
    43: "diffusion_generative",
    44: "state_machine_agent",
    45: "multimodal_reasoning",
    46: "diffusion_generative",
    47: "state_machine_agent",
    48: "state_machine_agent",
    49: "multimodal_reasoning",
    50: "multimodal_reasoning",
    51: "state_machine_agent",
    52: "state_machine_agent",
    53: "training_efficiency",
    54: "state_machine_agent",
    55: "multimodal_reasoning",
    56: "inference_optimization",
    57: "state_machine_agent",
    58: "state_machine_agent",
    59: "inference_optimization",
    60: "multimodal_reasoning",
    61: "state_machine_agent",
    62: "training_efficiency",
    63: "training_efficiency",
    64: "state_machine_agent"
}

def map_categories_to_hex(categories):
    hex_ids = []
    for category in categories:
        for hid, mapped in HEXAGRAM_UPGRADE_MAP.items():
            if mapped == category and hid not in hex_ids:
                hex_ids.append(hid)
                break
    return hex_ids[:12]

records = []
with manifest_path.open('r', encoding='utf-8') as f:
    for line in f:
        records.append(json.loads(line))

print(f'Loaded {len(records)} records')

updated = []
for rec in records:
    upgrade_categories = rec.get('upgrade_categories', [])
    hex_ids = map_categories_to_hex(upgrade_categories)
    phase_suggestions = [
        {"hexagram_id": hid, "phase_bits": 0, "phase_temporal": "past"}
        for hid in hex_ids
    ]
    rec['kingwen_hexagram_ids'] = hex_ids
    rec['kingwen_phase_suggestions'] = phase_suggestions
    
    per_page = rec.get('per_page_notes', [])
    for page in per_page:
        page_cats = page.get('upgrade_categories', [])
        page_hex = map_categories_to_hex(page_cats)
        page['kingwen_hexagram_ids'] = page_hex
        page['kingwen_phase_suggestions'] = [
            {"hexagram_id": hid, "phase_bits": 0, "phase_temporal": "past"}
            for hid in page_hex
        ]
    updated.append(rec)

with output_path.open('w', encoding='utf-8') as f:
    for rec in updated:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')

print(f'Wrote {len(updated)} records to {output_path}')
cat_counter = Counter()
for rec in updated:
    for cat in rec['upgrade_categories']:
        cat_counter[cat] += 1
print('\nPaper-level upgrade categories:')
for k, v in cat_counter.most_common(10):
    print(f'  {k}: {v}')
