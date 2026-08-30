from pathlib import Path
import json, re
from collections import Counter

corpus_root = Path(r'Path(__file__).resolve().parent.parent / 'learning-corpus' / '.text'')
output_path = Path(r'Path(__file__).resolve().parent.parent / 'learning-corpus'\paper_study_notes.jsonl')

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

UPGRADE_PATTERNS = {
    "training_efficiency": ["pretraining", "training speed", "throughput", "optimizer", "mixed precision", "gradient checkpointing", "pipeline parallelism", "tensor parallelism", "ZeRO", "DeepSpeed", "Megatron", "LAMB", "LARS", "learning rate schedule", "batch size", "gradient accumulation", "data efficiency"],
    "inference_optimization": ["speculative decoding", "kv cache", "key-value cache", "beam search", "lookahead decoding", "medusa", "eagle", "draft model", "assistant decoding", "token pruning", "early exiting", "inference latency", "throughput"],
    "quantization_compression": ["quantization", "quantize", "int4", "int8", "int2", "qat", "ptq", "gptq", "awq", "gguf", "bitsandbytes", "sparsity", "pruning", "weight sharing", "low-rank", "lora", "qlora", "adapter"],
    "long_context": ["long context", "long-context", "128k", "256k", "1m", "1M", "context window", "rope", "positional encoding", "alibi", "position interpolation", "ntk-aware", "yaRN", "context extension", "retrieval augmentation", "memoria"],
    "multimodal_reasoning": ["multimodal", "vision-language", "vlm", "clip", "contrastive", "alignment", "grounding", "visual reasoning", "image-text", "audio-text", "video-text", "perception", "embodied"],
    "vision_generation": ["image generation", "text-to-image", "gan", "latent diffusion", "stable diffusion", "dreambooth", "lora", "controlnet", "inpainting", "outpainting", "super-resolution", "style transfer"],
    "audio_speech": ["audio generation", "speech synthesis", "tts", "text-to-speech", "voice clone", "prosody", "pitch", "duration", "vocoder", "waveform", "mel spectrogram", "music generation", "sound generation"],
    "tool_use_function_calling": ["tool use", "function calling", "api call", "code generation", "program synthesis", "agent", "planning", "reasoning", "chain-of-thought", "react", "toolformer", "code llama", "code completion"],
    "memory_context": ["memory", "retrieval", "rag", "context window", "prompt", "in-context learning", "few-shot", "zero-shot", "icl", "episodic memory", "working memory", "long-term memory"],
    "alignment_steering": ["alignment", "rlhf", "dpo", "preference optimization", "safety", "red teaming", "reward model", "constitutional ai", "steering", "control", "jailbreak", "robustness"],
    "state_machine_agent": ["state machine", "finite automaton", "policy", "reinforcement learning", "decision making", "planning", "search", "mcts", "beam", "agent architecture", "tool use", "action selection"],
    "diffusion_generative": ["diffusion", "score matching", "denoising", "sde", "flow matching", "ode", "ddpm", "ddim", "latent diffusion", "consistency model", "distillation"],
    "retrieval_augmentation": ["retrieval", "rag", "retrieval-augmented", "knowledge base", "dense retrieval", "sparse retrieval", "bm25", "vector search", "embedding", "reranking", "augmented generation"],
    "world_model_simulation": ["world model", "simulation", "dynamics", "video prediction", "physics", "embodied", "navigation", "environment", "state prediction", "transition model", "planning", "control"],
    "speech_voice_synthesis": ["voice synthesis", "voice clone", "voice style", "voice transfer", "prosody transfer", "emotion", "speaker adaptation", "zero-shot tts", "neural codec", "audio token", "speech token"],
    "video_generation": ["video generation", "text-to-video", "video diffusion", "temporal", "frame interpolation", "video prediction", "motion generation", "temporal consistency", "video transformer"]
}

def detect_upgrades(text):
    text_lower = text.lower()
    upgrades = []
    for category, keywords in UPGRADE_PATTERNS.items():
        matches = [kw for kw in keywords if kw in text_lower]
        if matches:
            upgrades.append({
                "category": category,
                "matched_keywords": matches[:5],
                "confidence": min(1.0, len(matches) / 3.0)
            })
    return sorted(upgrades, key=lambda x: -x["confidence"])

def chunk_pages(text, chunk_chars=3000):
    chunks = []
    start = 0
    page = 1
    while start < len(text):
        end = start + chunk_chars
        chunk = text[start:end]
        # try to break on double newline
        if end < len(text):
            brk = chunk.rfind('\n\n')
            if brk > 500:
                chunk = chunk[:brk+2]
                end = start + brk + 2
        chunks.append({"page_number": page, "text": chunk})
        start = end
        page += 1
    return chunks

def extract_title_from_filename(filename):
    base = filename.replace('.txt', '')
    if '_' in base:
        parts = base.split('_', 1)
        if len(parts) == 2:
            return parts[1].replace('_', ' ')
    return base.replace('_', ' ')

def estimate_reading_time(char_count):
    words = char_count / 5
    minutes = words / 200
    return max(1, int(minutes))

files = sorted(corpus_root.glob('*.txt'))
print(f'Found {len(files)} txt files')

results = []
for path in files:
    try:
        text = path.read_text(encoding='utf-8', errors='ignore')
    except Exception as e:
        print(f'Error reading {path}: {e}')
        continue
    
    title = extract_title_from_filename(path.name)
    chunks = chunk_pages(text)
    upgrade_categories_all = []
    per_page = []
    for chunk in chunks:
        upgrades = detect_upgrades(chunk['text'])
        upgrade_categories_all.extend([u['category'] for u in upgrades])
        page_note = {
            "page_number": chunk['page_number'],
            "char_count": len(chunk['text']),
            "upgrade_categories": [u['category'] for u in upgrades],
            "upgrade_details": upgrades,
            "study_notes": [],
            "quoted_findings": []
        }
        per_page.append(page_note)
    
    upgrade_categories = sorted(set(upgrade_categories_all))
    is_relevant = len(upgrade_categories) > 0
    
    record = {
        'file': str(path),
        'filename': path.name,
        'title': title,
        'category': 'learning-corpus',
        'char_count': len(text),
        'word_count_est': len(text) // 5,
        'reading_time_min': estimate_reading_time(len(text)),
        'upgrade_categories': upgrade_categories,
        'is_relevant': is_relevant,
        'status': 'pending' if is_relevant else 'skipped',
        'study_notes': [],
        'kingwen_hexagram_ids': [],
        'kingwen_phase_suggestions': [],
        'per_page_notes': per_page
    }
    results.append(record)

with output_path.open('w', encoding='utf-8') as f:
    for rec in results:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')

print(f'Wrote {len(results)} records to {output_path}')
print(f'Relevant papers: {sum(1 for r in results if r["is_relevant"])}')
print(f'Skipped papers: {sum(1 for r in results if not r["is_relevant"])}')

cat_counter = Counter()
for rec in results:
    for u in rec['upgrade_categories']:
        cat_counter[u] += 1
print('\nUpgrade category distribution:')
for k, v in cat_counter.most_common():
    print(f'  {k}: {v}')
