from pathlib import Path
import json, re
from collections import Counter

corpus_root = Path(r'Path(__file__).resolve().parent.parent / 'learning-corpus' / '.text'')
output_path = Path(r'Path(__file__).resolve().parent.parent / 'learning-corpus'\paper_upgrade_notes.jsonl')

UPGRADE_PATTERNS = {
    'training_efficiency': ['pretraining', 'training speed', 'throughput', 'optimizer', 'mixed precision', 'gradient checkpointing', 'pipeline parallelism', 'tensor parallelism', 'ZeRO', 'DeepSpeed', 'Megatron', 'LAMB', 'LARS', 'learning rate schedule', 'batch size', 'gradient accumulation', 'data efficiency'],
    'inference_optimization': ['speculative decoding', 'kv cache', 'key-value cache', 'beam search', 'lookahead decoding', 'medusa', 'eagle', 'draft model', 'assistant decoding', 'token pruning', 'early exiting', 'inference latency', 'throughput'],
    'quantization_compression': ['quantization', 'quantize', 'int4', 'int8', 'int2', 'qat', 'ptq', 'gptq', 'awq', 'gguf', 'bitsandbytes', 'sparsity', 'pruning', 'weight sharing', 'low-rank', 'lora', 'qlora', 'adapter'],
    'long_context': ['long context', 'long-context', '128k', '256k', '1m', '1M', 'context window', 'rope', 'positional encoding', 'alibi', 'position interpolation', 'ntk-aware', 'yaRN', 'context extension', 'retrieval augmentation', 'memoria'],
    'multimodal_reasoning': ['multimodal', 'vision-language', 'vlm', 'clip', 'contrastive', 'alignment', 'grounding', 'visual reasoning', 'image-text', 'audio-text', 'video-text', 'perception', 'embodied'],
    'vision_generation': ['image generation', 'text-to-image', 'gan', 'latent diffusion', 'stable diffusion', 'dreambooth', 'lora', 'controlnet', 'inpainting', 'outpainting', 'super-resolution', 'style transfer'],
    'audio_speech': ['audio generation', 'speech synthesis', 'tts', 'text-to-speech', 'voice clone', 'prosody', 'pitch', 'duration', 'vocoder', 'waveform', 'mel spectrogram', 'music generation', 'sound generation'],
    'tool_use_function_calling': ['tool use', 'function calling', 'api call', 'code generation', 'program synthesis', 'agent', 'planning', 'reasoning', 'chain-of-thought', 'react', 'toolformer', 'code llama', 'code completion'],
    'memory_context': ['memory', 'retrieval', 'rag', 'context window', 'prompt', 'in-context learning', 'few-shot', 'zero-shot', 'icl', 'episodic memory', 'working memory', 'long-term memory'],
    'alignment_steering': ['alignment', 'rlhf', 'dpo', 'preference optimization', 'safety', 'red teaming', 'reward model', 'constitutional ai', 'steering', 'control', 'jailbreak', 'robustness'],
    'state_machine_agent': ['state machine', 'finite automaton', 'policy', 'reinforcement learning', 'decision making', 'planning', 'search', 'mcts', 'beam', 'agent architecture', 'tool use', 'action selection'],
    'diffusion_generative': ['diffusion', 'score matching', 'denoising', 'sde', 'sde', 'flow matching', 'ode', 'ddpm', 'ddim', 'latent diffusion', 'consistency model', 'distillation'],
    'retrieval_augmentation': ['retrieval', 'rag', 'retrieval-augmented', 'knowledge base', 'dense retrieval', 'sparse retrieval', 'bm25', 'vector search', 'embedding', 'reranking', 'augmented generation'],
    'world_model_simulation': ['world model', 'simulation', 'dynamics', 'video prediction', 'physics', 'embodied', 'navigation', 'environment', 'state prediction', 'transition model', 'planning', 'control'],
    'speech_voice_synthesis': ['voice synthesis', 'voice clone', 'voice style', 'voice transfer', 'prosody transfer', 'emotion', 'speaker adaptation', 'zero-shot tts', 'neural codec', 'audio token', 'speech token'],
    'video_generation': ['video generation', 'text-to-video', 'video diffusion', 'temporal', 'frame interpolation', 'video prediction', 'motion generation', 'temporal consistency', 'video transformer']
}

def detect_upgrades(text):
    text_lower = text.lower()
    upgrades = []
    for category, keywords in UPGRADE_PATTERNS.items():
        matches = [kw for kw in keywords if kw in text_lower]
        if matches:
            upgrades.append({
                'category': category,
                'matched_keywords': matches[:5],
                'confidence': min(1.0, len(matches) / 3.0)
            })
    return sorted(upgrades, key=lambda x: -x['confidence'])

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
    upgrades = detect_upgrades(text)
    is_relevant = len(upgrades) > 0
    
    record = {
        'file': str(path),
        'filename': path.name,
        'title': title,
        'category': 'learning-corpus',
        'char_count': len(text),
        'word_count_est': len(text) // 5,
        'reading_time_min': estimate_reading_time(len(text)),
        'upgrade_categories': [u['category'] for u in upgrades],
        'upgrade_details': upgrades,
        'is_relevant': is_relevant,
        'status': 'pending' if is_relevant else 'skipped',
        'study_notes': [],
        'kingwen_hexagram_ids': [],
        'kingwen_phase_suggestions': []
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
    for u in rec['upgrade_details']:
        cat_counter[u['category']] += 1
print('\nUpgrade category distribution:')
for k, v in cat_counter.most_common():
    print(f'  {k}: {v}')
