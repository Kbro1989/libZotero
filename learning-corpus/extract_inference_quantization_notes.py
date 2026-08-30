from pathlib import Path
import re

corpus_root = Path(r'Path(__file__).resolve().parent.parent / 'learning-corpus' / '.text'')
output_path = Path(r'Path(__file__).resolve().parent.parent / 'learning-corpus'\extended_study_notes_inference_quantization.md')

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

TARGET_PAPERS = [
    "SpecInfer", "Medusa", "EAGLE", "Lookahead Decoding", "FlashAttention", "PagedAttention",
    "FlexGen", "DeepSeek-V2", "Switch Transformers", "Efficient Transformers Survey",
    "GPTQ", "AWQ", "QLoRA", "SmoothQuant", "ZeroQuant", "LLM-Pruner", "SpQR",
    "SqueezeLLM", "QuIP", "SpinQuant", "INT-FlashAttention", "LQ-LoRA", "LLM-QAT",
    "One-Shot Sparsity", "FLAP", "Staged Speculative", "LLM in a Flash",
    "Half-Quadratic Quantization", "BRECQ", "Up or Down Adaptive Rounding",
    "The Geometry of LLM Quantization"
]

FILENAME_ALIASES = {
    "The Geometry of LLM Quantization": ["geometry of llm quantization", "the geometry of llm quantization"],
    "Up or Down Adaptive Rounding": ["up or down adaptive rounding", "up_or_down_adaptive_rounding"],
    "LLM in a Flash": ["llm in a flash", "llm in a flash"],
    "Staged Speculative": ["staged speculative decoding", "accelerating llm inference with staged speculative decoding"],
    "Efficient Transformers Survey": ["efficient transformers_ a survey", "efficient transformers survey"],
    "One-Shot Sparsity": ["one-shot sensitivity-aware mixed sparsity pruning", "one-shot sparsity"],
    "INT-FlashAttention": ["int-flashattention", "int-flashattention_ enabling flash attention for int8 quantization"],
    "LQ-LoRA": ["lq-lora"],
    "Half-Quadratic Quantization": ["half-quadratic quantization"],
    "BRECQ": ["brecq_ pushing the limit of post-training quantization"],
    "FlexGen": ["flexgen"],
    "SpQR": ["spqr_ a sparse-quantized representation"],
    "QuIP": ["quip_ 2-bit quantization of large language models", "quip#_ even better llm quantization"],
    "LLM-Pruner": ["llm-pruner_ on the structural pruning"],
    "PagedAttention": ["efficient memory management for large language model serving with pagedattention", "pagedattention"],
    "EAGLE": ["eagle_ speculative sampling requires rethinking feature uncertainty"],
    "Medusa": ["medusa_ simple llm inference acceleration framework"],
    "Lookahead Decoding": ["lookahead decoding_ accelerating llm inference via parallel jacobi iteration"],
    "SpecInfer": ["specinfer_ accelerating generative llm serving"],
    "FlashAttention": ["flashattention_ fast and memory-efficient exact attention"],
    "DeepSeek-V2": ["deepseek-v2_ a strong, economical, and efficient"],
    "Switch Transformers": ["switch transformers_ scaling to trillion parameter models"],
    "GPTQ": ["gptq_ accurate post-training quantization"],
    "AWQ": ["awq_ activation-aware weight quantization"],
    "QLoRA": ["qlora_ efficient finetuning of quantized llms"],
    "SmoothQuant": ["smoothquant_ accurate and efficient post-training quantization"],
    "ZeroQuant": ["zeroquant_ efficient and affordable post-training quantization"],
    "SqueezeLLM": ["squeezellm_ dense-and-sparse quantization"],
    "SpinQuant": ["spinquant_ llm quantization with learned rotations"],
    "LLM-QAT": ["llm-qat_ data-free quantization aware training"],
    "FLAP": ["flap_ fluctuation-based adaptive structured pruning"],
    "Staged Speculative": ["accelerating llm inference with staged speculative decoding"],
    "LLM in a Flash": ["llm in a flash_ efficient large language model inference"],
}

def extract_equations(text):
    lines = text.splitlines()
    eqs = []
    for line in lines:
        s = line.strip()
        if not s:
            continue
        if ('=' in s or '∑' in s or '∫' in s or '∈' in s or '≈' in s or '≤' in s or '≥' in s) and len(s) < 220:
            if any(c.isdigit() for c in s) or any(k in s.lower() for k in ['softmax', 'argmax', 'q(w)', 'quant(', 'diag', 'norm', 'loss']):
                eqs.append(s)
    return list(dict.fromkeys(eqs))[:10]

def extract_claims(text):
    claims = []
    patterns = [
        r'(?:speedup|speed up|faster|throughput|tokens/sec)\b[^.\n]*\d+[^.\n]*[.!]',
        r'(?:perplexity|PPL)\b[^.\n]*\d+[^.\n]*[.!]',
        r'(?:INT2|INT3|INT4|INT8|2-bit|3-bit|4-bit|8-bit)\b[^.\n]{0,160}[.!]',
        r'(?:memory|GB|MB|VRAM)\b[^.\n]*\d+[^.\n]*[.!]',
        r'(?:accuracy|degradation|degrade)\b[^.\n]*\d+[^.\n]*[.!]',
        r'(?:compression|compress)\b[^.\n]*\d+[^.\n]*[.!]',
    ]
    seen = set()
    for pat in patterns:
        matches = re.findall(pat, text, re.IGNORECASE)
        for m in matches:
            m = m.strip()
            if m and m not in seen and 20 < len(m) < 320:
                seen.add(m)
                claims.append(m)
    return claims[:12]

def detect_categories(text):
    text_lower = text.lower()
    cats = []
    if any(k in text_lower for k in ["speculative decoding", "kv cache", "flashattention", "pagedattention", "inference latency", "throughput", "lookahead decoding", "medusa", "eagle", "specinfer", "draft model", "token tree", "jacobi"]):
        cats.append("inference_optimization")
    if any(k in text_lower for k in ["quantization", "quantize", "int4", "int8", "int2", "qat", "ptq", "gptq", "awq", "sparsity", "pruning", "lora", "qlora", "adapter", "bits", "rounding", "normalfloat", "nf4", "quip", "spinquant", "squeezellm", "spqr", "brecq", "half-quadratic", "zeroquant", "smoothquant", "lq-lora", "llm-qat"]):
        cats.append("quantization_compression")
    if any(k in text_lower for k in ["training", "pretraining", "throughput", "optimizer", "megatron", "deepspeed", "switch transformer", "mixture of experts"]):
        cats.append("training_efficiency")
    if not cats:
        cats.append("inference_optimization")
    return cats

def match_target_paper(filename):
    base = filename.lower()
    for canonical, aliases in FILENAME_ALIASES.items():
        for alias in aliases:
            if alias in base:
                return canonical
    for canonical in TARGET_PAPERS:
        if canonical.lower() in base:
            return canonical
    return None

def sovereign_relevance(categories):
    mapping = {
        "inference_optimization": "Direct upgrade path: speculative decoding, KV-cache management, and tiled attention can replace/upgrade sovereign stack token generation and memory subsystems.",
        "quantization_compression": "Direct upgrade path: weight-only and mixed-precision quantization reduce VRAM requirements, enabling larger sovereign models on constrained hardware.",
        "training_efficiency": "Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines."
    }
    return "\n".join(f"- {mapping.get(c, 'General relevance to sovereign stack efficiency.')}" for c in categories)

def hex_ids_for_categories(categories):
    ids = []
    seen = set()
    for cat in categories:
        if cat == "quantization_compression":
            for hid in [32, 41, 53, 62]:
                if hid not in seen:
                    ids.append(hid); seen.add(hid)
        else:
            for hid, mapped in HEXAGRAM_UPGRADE_MAP.items():
                if mapped == cat and hid not in seen:
                    ids.append(hid); seen.add(hid)
    return ids[:8]

# Dedupe: keep efficient-inference-quantization_ prefixed versions when duplicates exist
candidates = []
seen_canonical = {}
for path in sorted(corpus_root.glob('*.txt')):
    canonical = match_target_paper(path.name)
    if not canonical:
        continue
    if path.name.startswith('efficient-inference-quantization_'):
        seen_canonical[canonical] = path
    else:
        seen_canonical.setdefault(canonical, path)

matched = []
for canonical, path in seen_canonical.items():
    text = path.read_text(encoding='utf-8', errors='ignore')
    cats = detect_categories(text)
    methods = [canonical] + [m for m in TARGET_PAPERS if m != canonical and m.lower() in text.lower()]
    methods = list(dict.fromkeys(methods))
    equations = extract_equations(text)
    claims = extract_claims(text)
    hex_ids = hex_ids_for_categories(cats)
    arxiv_id = path.stem.split('_')[0] if '_' in path.stem else path.stem
    matched.append({
        "path": path,
        "canonical": canonical,
        "categories": cats,
        "methods": methods,
        "equations": equations,
        "claims": claims,
        "hex_ids": hex_ids,
        "arxiv_id": arxiv_id,
    })

matched.sort(key=lambda r: r['canonical'].lower())
print(f"Matched {len(matched)} unique target papers.")

md = []
md.append("# Extended Study Notes: Inference Optimization & Quantization Papers\n")
md.append("_Auto-extracted from local corpus first-two-page extracts. Focus: method descriptions, equations, quantitative claims, and King Wen hexagram mappings._\n")
md.append("---\n")

for rec in matched:
    md.append(f"## {rec['canonical']}\n")
    md.append(f"- **File:** `{rec['path'].name}`")
    md.append(f"- **arXiv ID:** {rec['arxiv_id']}")
    md.append(f"- **Categories:** {', '.join(rec['categories'])}")
    md.append(f"- **King Wen Hexagrams:** {', '.join(str(h) for h in rec['hex_ids'])}")
    md.append(f"- **Methods:** {', '.join(rec['methods'])}")
    md.append("")
    if rec['claims']:
        md.append("### Quantitative Claims")
        for c in rec['claims']:
            md.append(f"- {c}")
        md.append("")
    if rec['equations']:
        md.append("### Key Equations")
        for eq in rec['equations']:
            md.append(f"- `{eq}`")
        md.append("")
    md.append("### Sovereign Stack Upgrade Relevance")
    md.append(sovereign_relevance(rec['categories']))
    md.append("")
    md.append("---\n")

output_path.write_text("\n".join(md), encoding='utf-8')
print(f"Wrote {len(matched)} unique paper notes to {output_path}")
