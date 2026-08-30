from pathlib import Path
import json, re
from collections import Counter

corpus_root = Path(r'C:\Users\krist\Desktop\zotero\learning-corpus\.text')
manifest_path = Path(r'C:\Users\krist\Desktop\zotero\learning-corpus\paper_study_notes.jsonl')
output_path = Path(r'C:\Users\krist\Desktop\zotero\learning-corpus\kingwen_paper_study_corpus.jsonl')

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

FIND_PATTERNS = {
    "training_efficiency": ["pretraining", "training speed", "throughput", "optimizer", "mixed precision", "gradient checkpointing", "pipeline parallel", "tensor parallel", "DeepSpeed", "Megatron", "LAMB", "LARS", "batch size", "gradient accum"],
    "inference_optimization": ["speculative decoding", "kv cache", "beam search", "lookahead decoding", "medusa", "eagle", "draft model", "assistant decoding", "token pruning", "early exiting", "inference latency", "throughput"],
    "quantization_compression": ["quantization", "quantize", "int4", "int8", "int2", "qat", "ptq", "gptq", "awq", "gguf", "sparsity", "pruning", "low-rank", "lora", "qlora", "adapter"],
    "long_context": ["long context", "long-context", "128k", "256k", "1m", "context window", "rope", "positional encoding", "alibi", "position interpolation", "ntk-aware", "yaRN", "context extension"],
    "multimodal_reasoning": ["multimodal", "vision-language", "vlm", "clip", "contrastive", "alignment", "grounding", "visual reasoning", "image-text", "audio-text", "video-text", "perception", "embodied"],
    "vision_generation": ["image generation", "text-to-image", "gan", "latent diffusion", "stable diffusion", "dreambooth", "controlnet", "inpainting", "outpainting", "super-resolution", "style transfer"],
    "audio_speech": ["audio generation", "speech synthesis", "text-to-speech", "voice clone", "prosody", "pitch", "duration", "vocoder", "waveform", "mel spectrogram", "music generation", "sound generation"],
    "tool_use_function_calling": ["tool use", "function calling", "api call", "code generation", "program synthesis", "agent", "planning", "reasoning", "chain-of-thought", "toolformer", "code llama", "code completion"],
    "memory_context": ["memory", "retrieval", "rag", "context window", "prompt", "in-context learning", "few-shot", "zero-shot", "episodic memory", "working memory", "long-term memory"],
    "alignment_steering": ["alignment", "rlhf", "dpo", "preference optimization", "safety", "red teaming", "reward model", "constitutional ai", "steering", "control", "jailbreak", "robustness"],
    "state_machine_agent": ["state machine", "finite automaton", "policy", "reinforcement learning", "decision making", "planning", "search", "mcts", "agent architecture", "tool use", "action selection"],
    "diffusion_generative": ["diffusion", "score matching", "denoising", "sde", "flow matching", "ode", "ddpm", "ddim", "latent diffusion", "consistency model", "distillation"],
    "retrieval_augmentation": ["retrieval", "rag", "retrieval-augmented", "knowledge base", "dense retrieval", "sparse retrieval", "bm25", "vector search", "embedding", "reranking", "augmented generation"],
    "world_model_simulation": ["world model", "simulation", "dynamics", "video prediction", "physics", "embodied", "navigation", "environment", "state prediction", "transition model", "planning", "control"],
    "speech_voice_synthesis": ["voice synthesis", "voice clone", "voice style", "prosody transfer", "speaker adaptation", "zero-shot tts", "neural codec", "audio token", "speech token"],
    "video_generation": ["video generation", "text-to-video", "video diffusion", "frame interpolation", "video prediction", "motion generation", "temporal consistency", "video transformer"]
}

def detect_upgrades(text):
    text_lower = text.lower()
    upgrades = []
    for category, keywords in FIND_PATTERNS.items():
        matches = [kw for kw in keywords if kw in text_lower]
        if matches:
            upgrades.append({
                "category": category,
                "matched_keywords": matches[:5],
                "confidence": min(1.0, len(matches) / 3.0)
            })
    return sorted(upgrades, key=lambda x: -x["confidence"])

def chunk_pages(text, chunk_chars=2200):
    chunks = []
    start = 0
    page = 1
    while start < len(text):
        end = start + chunk_chars
        chunk = text[start:end]
        if end < len(text):
            brk = chunk.rfind('\n\n')
            if brk > 350:
                chunk = chunk[:brk+2]
                end = start + brk + 2
        chunks.append({"page_number": page, "text": chunk})
        start = end
        page += 1
    return chunks

def extract_findings(text, categories):
    text_lower = text.lower()
    findings = []
    seen = set()
    for category in categories:
        keywords = FIND_PATTERNS.get(category, [])[:4]
        for kw in keywords:
            if kw in text_lower:
                idx = text_lower.find(kw)
                start = max(0, idx - 110)
                end = min(len(text), idx + 170)
                sentence = text[start:end].replace('\n', ' ').strip()
                if sentence and sentence not in seen:
                    seen.add(sentence)
                    findings.append({"category": category, "sentence": sentence, "keyword": kw})
                if len(findings) >= 8:
                    break
        if len(findings) >= 8:
            break
    return findings[:8]

def extract_title_from_filename(filename):
    base = filename.replace('.txt', '')
    if '_' in base:
        parts = base.split('_', 1)
        if len(parts) == 2:
            return parts[1].replace('_', ' ')
    return base.replace('_', ' ')

def map_categories_to_hex(categories):
    hex_ids = []
    for category in categories:
        for hid, mapped in HEXAGRAM_UPGRADE_MAP.items():
            if mapped == category and hid not in hex_ids:
                hex_ids.append(hid)
                break
    return hex_ids[:12]

manifest = []
with manifest_path.open('r', encoding='utf-8') as f:
    for line in f:
        manifest.append(json.loads(line))

print(f'Loaded {len(manifest)} papers from manifest')

results = []
for idx, paper in enumerate(manifest, 1):
    path = corpus_root / paper['filename']
    if not path.exists():
        continue

    text = path.read_text(encoding='utf-8', errors='ignore')
    title = paper.get('title', extract_title_from_filename(path.name))
    upgrade_categories = paper.get('upgrade_categories', [])

    chunks = chunk_pages(text)
    per_page = []
    all_findings = []
    for chunk in chunks:
        findings = extract_findings(chunk['text'], upgrade_categories)
        all_findings.extend(findings)
        page_cats = list(set(f['category'] for f in findings))
        page_hex = map_categories_to_hex(page_cats)
        per_page.append({
            "page_number": chunk['page_number'],
            "char_count": len(chunk['text']),
            "upgrade_categories": page_cats,
            "findings": findings,
            "kingwen_hexagram_ids": page_hex,
            "kingwen_phase_suggestions": [
                {"hexagram_id": hid, "phase_bits": 0, "phase_temporal": "past"}
                for hid in page_hex
            ]
        })

    hex_ids = map_categories_to_hex(upgrade_categories)
    phase_suggestions = [
        {"hexagram_id": hid, "phase_bits": 0, "phase_temporal": "past"}
        for hid in hex_ids
    ]

    record = {
        "file": str(path),
        "filename": path.name,
        "title": title,
        "category": "learning-corpus",
        "char_count": len(text),
        "upgrade_categories": upgrade_categories,
        "is_relevant": paper.get('is_relevant', True),
        "status": paper.get('status', 'pending'),
        "study_notes": all_findings[:20],
        "kingwen_hexagram_ids": hex_ids,
        "kingwen_phase_suggestions": phase_suggestions,
        "per_page_notes": per_page
    }
    results.append(record)
    if idx % 50 == 0:
        print(f'Processed {idx}/{len(manifest)}...')

with output_path.open('w', encoding='utf-8') as f:
    for rec in results:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')

print(f'Wrote {len(results)} records to {output_path}')
from collections import Counter
cat_counter = Counter()
for rec in results:
    for cat in rec['upgrade_categories']:
        cat_counter[cat] += 1
print('\nPaper-level upgrade categories:')
for k, v in cat_counter.most_common(10):
    print(f'  {k}: {v}')
