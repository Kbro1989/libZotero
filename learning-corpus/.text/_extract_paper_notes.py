"""
Extract structured study notes from multimodal/vision/audio/video/world-model papers.
Reads actual .txt full texts from the learning corpus and writes draft study notes.
"""
from pathlib import Path
import re, json, textwrap

CORPUS = Path(r"Path(__file__).resolve().parent.parent / 'learning-corpus' / '.text'")
OUT = Path(r"Path(__file__).resolve().parent.parent / 'learning-corpus' / '.text'\_extracted_notes_draft.md")

TARGETS = [
    "2103.00020_Learning Transferable Visual Models From Natural Language Supervision.txt",
    "2201.12086_BLIP_ Bootstrapping Language-Image Pre-training for Unified Vision-Language Unde.txt",
    "2111.02358_VLMO_ Unified Vision-Language Pre-Training with Mixture-of-Modality-Experts.txt",
    "2304.08485_Visual Instruction Tuning.txt",
    "2605.24807_CLIP-Guided SAM_ Parameter-Efficient Semantic Conditioning for Promptable Segmen.txt",
    "2605.22902_Transcoders Trace Visual Grounding and Hallucinations in Vision-Language Models.txt",
    "2605.19792_Mechanisms of Object Localization in Vision-Language Models.txt",
    "2605.13156_Dual-Pathway Circuits of Object Hallucination in Vision-Language Models.txt",
    "2605.25334_Dual-Pathway Geometry-Aware MLLM for Spatial Intelligence.txt",
    "2605.25036_Language Bias in LVLMs_ From In-Depth Analysis to Simple and Effective Mitigatio.txt",
    "2605.26501_Unveiling the Fragility of Vision-Language Models_ Multi-Modal Adversarial Syner.txt",
    "2605.27315_Real Images, Worse Judgments_ Evaluating Vision-Language Models on Concreteness .txt",
    "2605.30912_Attend to Evidence_ Evidence-Anchored Spatial Attention Supervision for Multimod.txt",
    "2605.31096_iVGR_ Internalizing Visually Grounded Reasoning for MLLMs with Reinforcement Lea.txt",
    "2605.31271_DriveMA_ Driving Vision-Language-Action Models with verifiable Meta-Actions.txt",
    "2605.17204_Event-Grounded Sparse Autoencoders for Vision-Language-Action Policies.txt",
    "2605.23035_Sparse Autoencoders Map Brain-LLM Alignment onto Cortical Semantic Topography.txt",
    "2605.09352_The Wittgensteinian Representation Hypothesis_ Is Language the Attractor of Mult.txt",
    "2605.16468_Mechanistically Interpretable Neural Encoding Reveals Fine-Grained Functional Se.txt",
    "2604.27969_From Mirage to Grounding_ Towards Reliable Multimodal Circuit-to-Verilog Code Ge.txt",
    "2605.21059_Multimodal LLMs under Pairwise Modalities.txt",
    "2604.25427_A Systematic Post-Train Framework for Video Generation.txt",
    "2401.03048_Latte_ Latent Diffusion Transformer for Video Generation.txt",
    "2209.14792_Make-A-Video_ Text-to-Video Generation without Text-Video Data.txt",
    "2210.02303_Imagen Video_ High Definition Video Generation with Diffusion Models.txt",
    "2209.14988_DreamFusion_ Text-to-3D using 2D Diffusion.txt",
    "2204.03458_Video Diffusion Models.txt",
    "2605.24652_AVBench_ Human-Aligned and Automated Evaluation Benchmark for Audio-Video Genera.txt",
    "2404.10351_Stable Audio_ Fast Timing-Conditioned Latent Audio Diffusion.txt",
    "2605.19242_PhyWorld_ Physics-Faithful World Model for Video Generation.txt",
    "2106.08389_Graph World Models.txt",
]

# Additional duplicates also available, map to unique paths.
paths = []
seen = set()
for name in TARGETS:
    p = CORPUS / name
    if p.exists() and str(p) not in seen:
        seen.add(str(p))
        paths.append(p)

# Also scan root corpus for exact filenames without category prefix if any were missing.
if len(paths) < len(TARGETS):
    for name in TARGETS:
        p = CORPUS / name
        if not p.exists():
            for candidate in CORPUS.glob("*" + Path(name).stem.split("_")[0] + "*"):
                if candidate.exists() and str(candidate) not in seen:
                    seen.add(str(candidate))
                    paths.append(candidate)

# Fallback: search for partial matches.
root_hits = {p.name: p for p in CORPUS.glob("*.txt")}
for name in TARGETS:
    stem = Path(name).stem
    prefix = stem.split("_")[0] if "_" in stem else stem
    if prefix not in [Path(x).name for x in paths]:
        matches = [p for p in CORPUS.glob("*.txt") if prefix in p.name]
        if matches:
            m = matches[0]
            if str(m) not in seen:
                seen.add(str(m))
                paths.append(m)

paths = list(dict.fromkeys(paths))


def clean(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def extract_paper_notes(text: str, filename: str) -> dict:
    title = Path(filename).stem.replace("_", " ")
    title = re.sub(r"^\d{4}\.\d{4,5}[^_]*_?", "", title).strip()
    abstract = ""
    m = re.search(r"(?i)abstract[:\s]+(.*?)(?:\n1\s+Introduction|\nIntroduction|\nI\.\s+Introduction)", text, re.S)
    if m:
        abstract = clean(m.group(1))[:1800]
    else:
        # grab first 1200 chars after title-ish line
        abstract = clean(text[:2200])[:1800]

    methods = []
    # heuristic: lines mentioning model/method names
    for line in text.splitlines():
        s = clean(line)
        if not s:
            continue
        if any(k in s.lower() for k in ["we propose", "we introduce", "we present", "our method", "approach", "framework", "model:", "method:", "algorithm", "architecture", "module", "objective", "loss function", "training", "fine-tuning", "pretraining", "contrastive", "diffusion", "transformer", "autoencoder", "sparse autoencoder", "knowledge distillation", "reinforcement learning", "clip", "blip", "sam", "vlm", "mllm"]):
            if len(s) > 60 and len(s) < 1200:
                methods.append(s)
    methods = list(dict.fromkeys(methods))[:20]

    equations = re.findall(r"(?:Equation|Eq\.?|formula|loss\s*=|objective\s*=|L\s*=|mathcalL\s*=|score|gradient|x_t\s*=|p_theta|p\(x|x0|log\s+likelihood|mse|kl|kl divergence|contrastive|infonce|nt-xent).{0,180}", text, re.I)
    equations = [clean(e) for e in equations][:20]

    claims = []
    for line in text.splitlines():
        s = clean(line)
        if not s:
            continue
        if any(k in s.lower() for k in ["outperforms", "state-of-the-art", "sota", "achieves", "improvement", "accuracy", "f1", "bleu", "rouge", "mIoU", "AP ", "AUPRC", "gain", "results show", "we observe", "significantly"]):
            if len(s) > 40 and len(s) < 1000:
                claims.append(s)
    claims = list(dict.fromkeys(claims))[:20]

    # heuristic hexagram mapping via keyword tags
    domain_tags = []
    lower = text.lower()
    tags = {
        "䷀": ["creation", "generation", "origin", "world model", "foundational"],
        "䷁": ["receptive", "grounding", "spatial", "geometry", "localization", "segmentation"],
        "䷂": ["obstruction", "adversarial", "fragility", "bias", "difficulty"],
        "䷃": ["youthful", "learning", "instruction tuning", "pretraining", "supervision"],
        "䷄": ["waiting", "video generation", "timing", "diffusion", "progressive"],
        "䷅": ["conflict", "contradiction", "hallucination", "disagreement", "oppose"],
        "䷆": ["army", "systematic", "framework", "post-train", "methodology"],
        "䷇": ["union", "multimodal", "fusion", "alignment", "pairwise"],
        "䷈": ["smallness", "efficiency", "quantization", "small", "incremental"],
        "䷉": ["treading", "action", "driving", "meta-action", "robotics"],
        "䷊": ["peace", "alignment", "grounding", "reliable", "robust"],
        "䷋": ["opposition", "object localization", "localize", "detect"],
        "䷌": ["fellowship", "clip", "contrastive", "language-image", "shared"],
        "䷍": ["greatness", "visual autoregressive", "scalable", "generation"],
        "䷎": ["humility", "mitigation", "bias", "safety", "mitigating"],
        "䷏": ["enthusiasm", "audio", "music", "speech", "sound"],
        "䷐": ["following", "distillation", "bootstrapping", "follow", "transfer"],
        "䷑": ["work on", "interpretability", "mechanism", "circuit", "analysis"],
        "䷒": ["boundary", "world model", "simulation", "physics", "boundary"],
        "䷓": ["observation", "evaluation", "benchmark", "observing", "assessment"],
        "䷔": ["grace", "beauty", "image", "visual", "rendering"],
        "䷕": ["splitting apart", "split", "pathway", "dual", "branching"],
        "䷖": ["return", "brain-llm", "alignment", "cortical", "neuroscience"],
        "䷗": ["innocence", "event-grounded", "sparse", "autoencoder", "foundation"],
        "䷘": "error",
    }
    matched = []
    for hex_, keywords in tags.items():
        if hex_ == "䷘":
            continue
        if any(k in lower for k in keywords):
            matched.append((hex_, keywords))
    # dedupe keeping order
    seen_hex = set()
    hex_mappings = []
    for h, ks in matched:
        if h not in seen_hex:
            seen_hex.add(h)
            hex_mappings.append((h, ks[:3]))

    return {
        "filename": filename,
        "title": title,
        "abstract": abstract,
        "methods": methods,
        "equations": equations,
        "claims": claims,
        "hexagram_mappings": hex_mappings,
    }


lines = []
lines.append("# Multimodal / Vision / Audio / Video / World-Model Study Notes (Draft)\n")
lines.append(f"Papers extracted: {len(paths)}\n")
lines.append("---\n")

for p in paths:
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        lines.append(f"## {p.name}\n_Read error: {e}_\n\n")
        continue
    notes = extract_paper_notes(text, p.name)
    lines.append(f"## {notes['title']}\n")
    lines.append(f"**File:** `{p.name}`\n")
    lines.append("### Abstract\n")
    lines.append(notes["abstract"] + "\n")
    lines.append("### Methods / Architecture\n")
    for m in notes["methods"]:
        lines.append(f"- {m}\n")
    lines.append("### Equations / Objectives\n")
    for e in notes["equations"]:
        lines.append(f"- {e}\n")
    lines.append("### Quantitative Claims\n")
    for c in notes["claims"]:
        lines.append(f"- {c}\n")
    lines.append("### King Wen Hexagram Mapping\n")
    if notes["hexagram_mappings"]:
        for h, ks in notes["hexagram_mappings"]:
            lines.append(f"- {h}: {', '.join(ks)}\n")
    else:
        lines.append("- _None detected by heuristic; needs manual curation._\n")
    lines.append("---\n")

OUT.write_text("".join(lines), encoding="utf-8")
print(f"Wrote draft notes for {len(paths)} papers to:\n{OUT}")
