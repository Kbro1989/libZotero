"""
Fast extractor for study notes. Minimal per-file processing to avoid timeout.
"""
from pathlib import Path
import re

CORPUS = Path(r"Path(__file__).resolve().parent.parent / 'learning-corpus' / '.text'")
OUT = Path(r"Path(__file__).resolve().parent.parent / 'learning-corpus' / '.text'\_extracted_notes_draft_v3.md")

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
    ("vla", "䷉", "embodied action"),
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


def clean(s):
    return re.sub(r"\s+", " ", s).strip()


def fast_abstract(text):
    m = re.search(r"(?i)abstract[:\s]+(.*?)(?:\n1\s+Introduction|\nIntroduction|\nI\.\s+Introduction)", text, re.S)
    if m:
        return clean(m.group(1))[:1200]
    return clean(text[:1500])[:1200]


def fast_methods(text):
    lines = []
    for line in text.splitlines():
        s = clean(line)
        if any(k in s.lower() for k in ["we propose", "we introduce", "our method", "framework", "architecture", "model", "objective", "loss function", "pretraining", "contrastive", "diffusion", "transformer", "autoencoder", "clip", "blip", "sam", "vlm", "mllm", "post-train", "instruction tuning"]):
            if 60 <= len(s) <= 900:
                lines.append(s)
    out = []
    seen = set()
    for s in lines:
        k = s[:80]
        if k not in seen:
            seen.add(k)
            out.append(s)
    return out[:12]


def fast_equations(text):
    out = []
    patterns = [r"L\s*=\s*[^\n]{0,150}", r"InfoNCE[^\n]{0,150}", r"KL\s*\([^\n]{0,150}", r"MSE[^\n]{0,150}", r"x_t\s*[^\n]{0,150}", r"p_theta[^\n]{0,150}", r"epsilon_theta[^\n]{0,150}", r"alpha_t[^\n]{0,150}", r"beta_t[^\n]{0,150}", r"score[^\n]{0,150}", r"guidance[^\n]{0,150}", r"Equation\s+\(\d+\)[^\n]{0,180}", r"Eq\.\s*\(\d+\)[^\n]{0,180}"]
    seen = set()
    for pat in patterns:
        for m in re.finditer(pat, text, re.I):
            s = clean(m.group(0))
            if 30 <= len(s) <= 500:
                k = s[:80]
                if k not in seen:
                    seen.add(k)
                    out.append(s)
    return out[:15]


def fast_claims(text):
    out = []
    for m in re.finditer(r'.{0,160}(?:outperform|state-of-the-art|achieves|improvement|accuracy|top-1|top-5|F1|BLEU|CIDEr|mIoU|AUROC|AUPRC|AP@|gain|speedup|throughput|p-value|±|×|[0-9]+(\.[0-9]+)?%|parameters|FLOPs).{0,200}', text, re.I):
        s = clean(m.group(0))
        if 40 <= len(s) <= 700:
            out.append(s)
    seen = set()
    final = []
    for s in out:
        k = s[:100]
        if k not in seen:
            seen.add(k)
            final.append(s)
    return final[:12]


def hex_map(text):
    lower = text.lower()
    hits = []
    seen = set()
    for kw, hex_, note in TOPIC_HEX:
        if kw in lower and hex_ not in seen:
            seen.add(hex_)
            hits.append((hex_, note))
    return hits[:7]


def notes_for(path):
    text = path.read_text(encoding="utf-8", errors="ignore")
    title = path.stem.split("_", 1)[-1] if "_" in path.stem else path.stem
    title = re.sub(r"^\d{4}\.\d{4,5}[^_]*_?", "", title).strip()
    return {
        "file": path.name,
        "title": title,
        "abstract": fast_abstract(text),
        "methods": "; ".join(fast_methods(text)),
        "equations": fast_equations(text),
        "claims": fast_claims(text),
        "hexagrams": hex_map(text),
    }


paths = []
seen = set()
for name in TARGETS:
    p = CORPUS / name
    if p.exists() and str(p) not in seen:
        seen.add(str(p))
        paths.append(p)
    else:
        prefix = name.split("_")[0]
        for cand in CORPUS.glob(f"*{prefix}*"):
            if cand.is_file() and str(cand) not in seen:
                seen.add(str(cand))
                paths.append(cand)
                break

out = ["# Multimodal / Vision / Audio / Video / World-Model Study Notes\n", f"Papers: {len(paths)}\n\n"]
for p in paths:
    try:
        n = notes_for(p)
    except Exception as e:
        out.append(f"## {p.name}\n_Error: {e}_\n\n")
        continue
    out.append(f"## {n['title']}\n**Source:** `{n['file']}`\n\n")
    out.append("### Abstract\n" + n["abstract"] + "\n\n")
    out.append("### Methods\n" + n["methods"] + "\n\n")
    out.append("### Equations\n")
    if n["equations"]:
        for eq in n["equations"]:
            out.append(f"- {eq}\n")
    else:
        out.append("- _None detected_\n")
    out.append("### Quantitative Claims\n")
    if n["claims"]:
        for c in n["claims"]:
            out.append(f"- {c}\n")
    else:
        out.append("- _None detected_\n")
    out.append("### King Wen Hexagram Mapping\n")
    if n["hexagrams"]:
        for h, note in n["hexagrams"]:
            out.append(f"- {h}: {note}\n")
    else:
        out.append("- _Manual curation needed_\n")
    out.append("\n---\n\n")

OUT.write_text("".join(out), encoding="utf-8")
print(f"Done. Wrote {len(paths)} papers to {OUT}")
