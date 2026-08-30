"""
Polished extractor for multimodal/vision/audio/video/world-model study notes.
Produces cleaner method descriptions, equations, quantitative claims, and
curated King Wen hexagram mappings from full-text .txt papers.
"""
from pathlib import Path
import re, json, hashlib, textwrap

CORPUS = Path(r"C:\Users\krist\Desktop\zotero\learning-corpus\.text")
OUT = Path(r"C:\Users\krist\Desktop\zotero\learning-corpus\.text\_extracted_notes_draft_v2.md")

# Curated topic-to-hex mapping for these paper families.
# Each entry: list of keyword tuples (substring, hexagram char, rationale note)
TOPIC_HEX = [
    ("clip", "䷌", "contrastive image-text pairing"),
    ("contrastive", "䷌", "shared representation via contrast"),
    ("language-image", "䷌", "fellowship across modalities"),
    ("blip", "䷐", "bootstrap captioner/filter loop"),
    ("caption", "䷐", "generating language from vision"),
    ("filter", "䷐", "bootstrapping denoising"),
    ("vlmo", "䷇", "mixture-of-modality experts"),
    ("unified", "䷇", "multimodal union"),
    ("visual instruction", "䷃", "instruction tuning"),
    ("instruction tuning", "䷃", "supervised behavioral shaping"),
    ("albef", "䷇", "align before fuse"),
    ("grounding", "䷁", "receptive spatial grounding"),
    ("localization", "䷋", "opposition/object localization"),
    ("object localization", "䷋", "locate target among distractors"),
    ("hallucination", "䷅", "conflict between vision and language"),
    ("fragility", "䷂", "obstruction under distribution shift"),
    ("adversarial", "䷂", "obstruction/attack"),
    ("bias", "䷎", "humility mitigation"),
    ("language bias", "䷎", "humility toward LM priors"),
    ("geometry", "䷁", "spatial receptive structure"),
    ("spatial", "䷁", "receptive geometry"),
    ("dual pathway", "䷕", "splitting into parallel routes"),
    ("dual-pathway", "䷕", "branching circuits"),
    ("world model", "䷒", "physical boundary simulation"),
    ("physics", "䷒", "world boundary/constraints"),
    ("video generation", "䷄", "waiting/time-ordered diffusion"),
    ("text-to-video", "䷄", "temporal generation"),
    ("imagen video", "䷄", "cascaded video diffusion"),
    ("make-a-video", "䷄", "unsupervised video synthesis"),
    ("latte", "䷄", "latent video transformer"),
    ("diffusion", "䷄", "iterative denoising process"),
    ("latent diffusion", "䷄", "compressed diffusion space"),
    ("dreamfusion", "䷔", "score distillation beauty"),
    ("3d", "䷒", "world geometry"),
    ("audio", "䷏", "sound enthusiasm"),
    ("music", "䷏", "generative audio enthusiasm"),
    ("speech", "䷏", "voice enthusiasm"),
    ("stable audio", "䷏", "latent audio diffusion"),
    ("avbench", "䷓", "observation/benchmark"),
    ("benchmark", "䷓", "assessment"),
    ("systematic post-train", "䷆", "organized post-training method"),
    ("post-train", "䷆", "methodical refinement"),
    ("sparse autoencoder", "䷗", "innocence/sparse foundation"),
    ("sae", "䷗", "sparse monome"),
    ("transcoder", "䷑", "mechanistic mapping"),
    ("mechanistic", "䷑", "work-on internals"),
    ("interpretability", "䷑", "analyze mechanism"),
    ("brain-llm", "䷖", "return to cortical alignment"),
    ("cortical", "䷖", "neural return"),
    ("drive", "䷉", "action in environment"),
    ("meta-action", "䷉", "discrete action stepping"),
    ("vla", "䷉", " embodied action"),
    ("reinforcement", "䷉", "active stepping"),
    ("ivgr", "䷃", "grounded reasoning training"),
    ("grounded reasoning", "䷃", "learned spatial thought"),
    ("pairwise", "䷇", "modality pairing"),
    ("alignment", "䷊", "peaceful correspondence"),
    ("mirage", "䷂", "illusory grounding"),
    ("circuit-to-verilog", "䷒", "formal world boundary"),
    ("graph world model", "䷒", "relational world"),
    ("phyworld", "䷒", "physics-faithful world"),
    ("wittgensteinian", "䷁", "language-attractor grounding"),
    ("language attractor", "䷁", "fixed point of meaning"),
    ("efficient", "䷈", "smallness/compression"),
    ("quantization", "䷈", "smallness/compression"),
    ("distillation", "䷐", "transfer by following"),
    ("knowledge distillation", "䷐", "student follows teacher"),
    ("autoregressive", "䷍", "greatness/scale"),
    ("scalable", "䷍", "expansive generation"),
]

TOPIC_HEX_ORDERED = TOPIC_HEX


def clean(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def extract_section(text: str, headers_pattern: str, max_chars: int = 1800):
    m = re.search(headers_pattern, text, re.I | re.S)
    if not m:
        return ""
    start = m.end()
    # stop at next major section or end
    tail = text[start:start + max_chars * 4]
    stop = re.search(r"\n\s*(?:References|Bibliography|Appendix|Acknowledge|Limitation|Discussion|Conclusion)\b", tail, re.I)
    if stop:
        tail = tail[:stop.start()]
    return clean(tail)[:max_chars]


def extract_equations(text: str, max_items: int = 25):
    eqs = []
    patterns = [
        r"(?:InfoNCE|NT-Xent|contrastive loss)[^\n]{0,160}",
        r"L\s*=\s*[^\n]{0,160}",
        r"mathcal\{?L\}?\s*=\s*[^\n]{0,160}",
        r"p[_\s]?θ\s*\([^\n]{0,160}",
        r"x_0\s*[^\n]{0,160}",
        r"x_t\s*[^\n]{0,160}",
        r"score\s*=\s*[^\n]{0,160}",
        r"∇[_\s]?x\s*log\s*p[^\n]{0,160}",
        r"KL\s*\([^\n]{0,160}",
        r"MSE\s*\([^\n]{0,160}",
        r"β[_\s]?t[^\n]{0,160}",
        r"α[_\s]?t[^\n]{0,160}",
        r"σ\s*=\s*[^\n]{0,160}",
        r"ϵ\s*\([^\n]{0,160}",
        r"ϵ_θ\s*\([^\n]{0,160}",
        r"z\s*=\s*E\([^\n]{0,160}",
        r"D\([^\n]{0,160}",
        r"Equation\s+\(\d+\)[^\n]{0,200}",
        r"Eq\.\s*\(\d+\)[^\n]{0,200}",
        r"(?:reparameterization|reparam)[^\n]{0,160}",
        r"(?:latent|score matching|SDE|ODE)[^\n]{0,160}",
        r"(?:classifier-free|guidance scale|CFG)[^\n]{0,160}",
        r"(?:Mixture of Experts|MoE|gate|router)[^\n]{0,160}",
        r"(?:transformer encoder|decoder|cross-attention)[^\n]{0,160}",
        r"(?:autoregressive|next-token|next-scale)[^\n]{0,160}",
        r"(?:masked generative|MUSE|masked)[^\n]{0,160}",
        r"(?:CLIP|BLIP|ALBEF|SAM|VLM)[^\n]{0,160}",
    ]
    seen = set()
    for pat in patterns:
        for m in re.finditer(pat, text, re.I):
            s = clean(m.group(0))
            if len(s) < 40:
                continue
            key = s[:80]
            if key in seen:
                continue
            seen.add(key)
            eqs.append(s)
            if len(eqs) >= max_items:
                return eqs
    return eqs


def extract_claims(text: str, max_items: int = 25):
    claims = []
    # sentences containing quantitative markers
    for m in re.finditer(r'[^.\n]{0,180}(?:outperform|state-of-the-art|SOTA|achieves|improvement|accuracy|top-1|top-5|F1|BLEU|CIDEr|mIoU|AUROC|AUPRC|AP@|gain|speedup|throughput|latency|p-value|±|×|%|parameters|FLOPs|score)[^.\n]{0,220}', text, re.I):
        s = clean(m.group(0))
        if 40 <= len(s) <= 800:
            claims.append(s)
    # dedupe by first 100 chars preserving order
    seen = set()
    out = []
    for s in claims:
        k = s[:100]
        if k not in seen:
            seen.add(k)
            out.append(s)
    return out[:max_items]


def hex_map_for(text: str):
    lower = text.lower()
    hits = []
    seen = set()
    for kw, hex_, note in TOPIC_HEX_ORDERED:
        if kw in lower and hex_ not in seen:
            seen.add(hex_)
            hits.append((hex_, note))
    return hits[:8]


def paper_notes(filepath: Path) -> dict:
    text = filepath.read_text(encoding="utf-8", errors="ignore")
    title = filepath.stem.split("_", 1)[-1] if "_" in filepath.stem else filepath.stem
    title = re.sub(r"^\d{4}\.\d{4,5}[^_]*_?", "", title).strip()
    abstract = extract_section(text, r"(?i)abstract[:\s]+(.*?)(?:\n1\s+Introduction|\nIntroduction|\nI\.\s+Introduction)", 1400) or clean(text[:1800])
    methods = extract_section(text, r"(?i)(method|approach|framework|architecture|model overview|pre-training|pretraining|algorithm)[^\n]{0,60}\n", 2200)
    equations = extract_equations(text)
    claims = extract_claims(text)
    hexes = hex_map_for(text)
    return {
        "file": filepath.name,
        "title": title,
        "abstract": abstract,
        "methods": methods,
        "equations": equations,
        "claims": claims,
        "hexagrams": hexes,
    }


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

# Resolve files, keeping only unique existing paths.
paths = []
seen = set()
for name in TARGETS:
    p = CORPUS / name
    if p.exists() and str(p) not in seen:
        seen.add(str(p))
        paths.append(p)
    else:
        # fallback by arxiv id prefix
        prefix = name.split("_")[0]
        for cand in CORPUS.glob(f"*{prefix}*"):
            if cand.is_file() and str(cand) not in seen:
                seen.add(str(cand))
                paths.append(cand)
                break

out_lines = []
out_lines.append("# Multimodal / Vision / Audio / Video / World-Model Study Notes\n")
out_lines.append(f"Generated from {len(paths)} full-text papers.\n\n")

for p in paths:
    try:
        notes = paper_notes(p)
    except Exception as e:
        out_lines.append(f"## {p.name}\n_Extraction error: {e}_\n\n")
        continue
    out_lines.append(f"## {notes['title']}\n")
    out_lines.append(f"**Source:** `{notes['file']}`\n\n")
    out_lines.append("### Abstract\n")
    out_lines.append(textwrap.fill(notes["abstract"], width=120) + "\n\n")
    out_lines.append("### Methods\n")
    out_lines.append(textwrap.fill(notes["methods"], width=120) + "\n\n")
    out_lines.append("### Equations / Objectives\n")
    if notes["equations"]:
        for eq in notes["equations"][:15]:
            out_lines.append(f"- {textwrap.fill(eq, width=120)}\n")
    else:
        out_lines.append("- _No explicit equations detected in extracted snippet._\n")
    out_lines.append("### Quantitative Claims\n")
    if notes["claims"]:
        for c in notes["claims"][:12]:
            out_lines.append(f"- {textwrap.fill(c, width=120)}\n")
    else:
        out_lines.append("- _No quantitative claims detected in extracted snippet._\n")
    out_lines.append("### King Wen Hexagram Mapping\n")
    if notes["hexagrams"]:
        for h, note in notes["hexagrams"]:
            out_lines.append(f"- {h}: {note}\n")
    else:
        out_lines.append("- _No heuristic hexagram matches; map manually._\n")
    out_lines.append("\n---\n\n")

OUT.write_text("".join(out_lines), encoding="utf-8")
print(f"Wrote polished notes to: {OUT}")
print(f"Lines: {len(out_lines)}")
