import os, re, json, glob
root = r'Path(__file__).resolve().parent.parent / 'learning-corpus''
text_dir = os.path.join(root, '.text')
out_path = os.path.join(root, 'kingwen_paper_study_corpus.jsonl')

patterns = {
    'DDPM': '2006.11239',
    'DDIM': '2010.02502',
    'IDDPM': '2102.09672',
    'LDM': '2112.10752',
    'DiT': '2212.09748',
    'VideoDiffusion': '2204.03458',
    'Make-A-Video': '2209.14792',
    'DreamFusion': '2209.14988',
    'Latte': '2401.03048',
    'StableAudio': '2404.10351',
    'AudioLDM': '2301.12503',
    'Jukebox': '2005.00341',
    'WaveNet': '1609.03499',
    'ScoreBased': '2011.13456',
    'SDE': '2011.13456',
    'FlowMatching': '2210.02747',
    'ImprovedDDPM': '2102.09672',
    'DiffusionBeatGANs': '2105.05233',
    'ElucidatingDesignSpace': '2206.00364',
    'ClassifierFreeGuidance': '2207.12598',
    'ProgressiveDistillation': '2202.00512',
    'RePaint': '2201.09865',
    'Palette': '2111.05826',
    'GLIDE': '2112.10741',
    'DPMSolver': '2206.00927',
    'DPMSolverpp': '2211.01095',
    'ConsistencyModels': '2210.01350',
    'SchrodingerBridge': '2106.01357',
    'AliasFreeGAN': '2106.12423',
    'StyleGAN2': '1812.04948',
    'ESRGAN': '1809.00219',
    'SinGAN': '1905.01164',
    'Glow': '1807.03039',
    'UGATIT': '1907.10830',
    'ArbitraryStyleTransfer': '1703.06868',
    'PhotoRealisticSR': '1609.04802',
}

arxiv_files = {}
for path in glob.glob(text_dir + '/*.txt'):
    base = os.path.basename(path)
    for key, aid in patterns.items():
        if aid in base:
            arxiv_files[key] = path
print('matched files:', len(arxiv_files))

def clean(s):
    return ' '.join(s.split())

def extract_equations(text):
    eqs = []
    for m in re.finditer(r'(?i)(eq(?:uation)?\.?\s*\(\d+\)|\\\[.*?\\\]|\\\(.*?\\\)|\b(?:log\s+)?p\b.*?=|p\(.*?\).*?=|L\b.*?=)', text):
        s = m.group(0)
        if 8 <= len(s) <= 200:
            eqs.append(clean(s))
    if not eqs:
        for pat in [r'L\s*=\s*E', r'p\s*\(', r'x\s*\|\s*y', r'q\s*\(', r'\(\s*1\s*-\s*sigma\s*\)', r'L\s*=\s*-\s*log', r'alpha\s*=', r'sigma\s*=']:
            ms = re.findall(pat, text)
            if ms:
                eqs.extend([clean(m) for m in ms[:10]])
                break
    uniq = []
    seen = set()
    for e in eqs:
        if e not in seen:
            seen.add(e)
            uniq.append(e)
    return uniq[:20]

def extract_quantitative(text):
    patterns_q = [
        r'(?i)(FID\s*[:=]\s*[0-9]+\.[0-9]+)',
        r'(?i)(IS\s*[:=]\s*[0-9]+\.[0-9]+)',
        r'(?i)(accuracy\s+of\s+[0-9]+\.[0-9]+%)',
        r'(?i)(state-of-the-art\s+[A-Za-z0-9\-]+)',
        r'(?i)(outperform[s]?\s+[A-Za-z0-9\-]+)',
        r'(?i)([0-9]+\s*\+\s*steps?)',
        r'(?i)(\d+\s*fps\b)',
        r'(?i)(\d+\s*gpus?)',
        r'(?i)(\d+[\.\d]*\s*(?:ms|samples|bits|channels|layers|heads|m\^2|dB|KL|NLL|BPD)?)',
    ]
    hits=[]
    for pat in patterns_q:
        hits.extend(re.findall(pat, text))
    hits = [clean(h) for h in hits if isinstance(h, str)]
    uniq=[]
    seen=set()
    for h in hits:
        if h not in seen:
            seen.add(h)
            uniq.append(h)
    return uniq[:30]

def extract_claims(text):
    claim_starts = [
        r'(?i)(we\s+show\s+that\s+.{20,120})',
        r'(?i)(our\s+method\s+.{10,120})',
        r'(?i)(we\s+propose\s+.{10,120})',
        r'(?i)(our\s+results\s+.{10,120})',
        r'(?i)(state-of-the-art[^\.]{0,200})',
        r'(?i)(outperform[^\.]{0,200})',
    ]
    claims=[]
    for pat in claim_starts:
        claims.extend(re.findall(pat, text))
    claims = [clean(c) for c in claims]
    uniq=[]
    seen=set()
    for c in claims:
        if c not in seen:
            seen.add(c)
            uniq.append(c)
    return uniq[:12]

topic_hex = {
    'DDPM': [3,4],
    'DDIM': [3,4,18],
    'IDDPM': [3,4,18],
    'LDM': [29,55,21],
    'DiT': [29,55,21],
    'VideoDiffusion': [29,55,21,2],
    'Make-A-Video': [29,55,21,2],
    'DreamFusion': [29,55,51],
    'Latte': [29,55,21],
    'StableAudio': [29,51,55],
    'AudioLDM': [29,51,55],
    'Jukebox': [29,51,55],
    'WaveNet': [51,55,29],
    'ScoreBased': [3,4,17],
    'SDE': [3,4,17],
    'FlowMatching': [3,4,17,55],
    'ImprovedDDPM': [3,4,18],
    'DiffusionBeatGANs': [3,4,18],
    'ElucidatingDesignSpace': [3,4,18],
    'ClassifierFreeGuidance': [3,4,18,13],
    'ProgressiveDistillation': [3,4,18,20],
    'RePaint': [3,4,18,29],
    'Palette': [3,4,18,29],
    'GLIDE': [3,4,18,13],
    'DPMSolver': [3,4,18,20],
    'DPMSolverpp': [3,4,18,20],
    'ConsistencyModels': [3,4,18,20],
    'SchrodingerBridge': [3,4,17,55],
    'AliasFreeGAN': [3,4,12],
    'StyleGAN2': [3,4,12],
    'ESRGAN': [3,4,12,40],
    'SinGAN': [3,4,12,40],
    'Glow': [3,4,17,40],
    'UGATIT': [3,4,12,29],
    'ArbitraryStyleTransfer': [3,4,12,29],
    'PhotoRealisticSR': [3,4,12,40],
}

upgrade_templates = {
    'DDPM': 'Foundation for sovereign diffusion pretraining; latent/spectral noise schedules',
    'DDIM': 'Deterministic sampler reduces sovereign inference latency',
    'IDDPM': 'Improved noise schedule for stronger sovereign generation quality',
    'LDM': 'Latent compression enables sovereign diffusion on limited hardware',
    'DiT': 'Transformer backbone scalable to sovereign model sizes',
    'VideoDiffusion': 'Spatio-temporal foundation for sovereign video generation',
    'Make-A-Video': 'Decoupled temporal priors reduce sovereign video data needs',
    'DreamFusion': '2D lifted to 3D for sovereign embodied generation',
    'Latte': 'Latent transformer video generation for sovereign streaming',
    'StableAudio': 'Timing-conditioned latent audio diffusion for sovereign speech/music',
    'AudioLDM': 'Text-to-audio with frozen CLAP/LDM for sovereign voice models',
    'Jukebox': 'Hierarchical VQ-VAE + transformer for sovereign long-form audio',
    'WaveNet': 'Autoregressive raw audio baseline for sovereign speech synthesis',
    'ScoreBased': 'Score-matching unifies generative pipelines for sovereign training',
    'SDE': 'Continuous-time generative flow for sovereign diffusion SDE solvers',
    'FlowMatching': 'Optimal transport path for sovereign efficient generative training',
    'ImprovedDDPM': 'Better schedules/hyperparams for sovereign stable diffusion',
    'DiffusionBeatGANs': 'Demonstrates sovereign diffusion superiority over GANs',
    'ElucidatingDesignSpace': 'Design space taxonomy improves sovereign model tuning',
    'ClassifierFreeGuidance': 'Training-free guidance scales sovereign text-to-media quality',
    'ProgressiveDistillation': 'Knowledge distillation reduces sovereign sampling cost',
    'RePaint': 'Inpainting via reverse diffusion for sovereign image repair',
    'Palette': 'Unified I2I diffusion for sovereign translation tasks',
    'GLIDE': 'CLIP-guided diffusion for sovereign text-guided editing',
    'DPMSolver': 'ODE-based fast sampler for sovereign inference acceleration',
    'DPMSolverpp': 'Second-order fast sampler for sovereign guided sampling',
    'ConsistencyModels': 'One-step model distillation for sovereign real-time inference',
    'SchrodingerBridge': 'SB provides interpretable interpolation for sovereign editing',
    'AliasFreeGAN': 'Alias-free architecture improves sovereign GAN stability',
    'StyleGAN2': 'Style latent space for sovereign controlled generation',
    'ESRGAN': 'Residual dense network for sovereign super-resolution',
    'SinGAN': 'Single-image generative prior for sovereign restoration',
    'Glow': 'Exact likelihood via invertible flow for sovereign density estimation',
    'UGATIT': 'Attention normalization for sovereign unsupervised translation',
    'ArbitraryStyleTransfer': 'AdaIN for sovereign fast style transfer',
    'PhotoRealisticSR': 'GAN SR baseline for sovereign high-fidelity upscaling',
}

# Load existing corpus to preserve any current fields
existing = {}
if os.path.exists(out_path):
    with open(out_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except Exception:
                continue
            key = obj.get('file') or obj.get('filename')
            if key:
                existing[key] = obj

corpus_out = []
updated = 0
for key, path in arxiv_files.items():
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    base = os.path.basename(path)
    title_match = re.search(r'^(.*?)_\d{4}\.\d{4,5}', base)
    title = title_match.group(1).replace('_', ' ').strip() if title_match else base
    aid = patterns[key]
    method_names = list(dict.fromkeys([
        title,
        'Diffusion Generative Models',
        'Score-Based Generative Modeling',
        'Training Efficiency',
        'King Wen Corpus'
    ]))
    extra = {
        'DDPM': ['Denoising Diffusion Probabilistic Model','DDPM','noise schedule','Markov noising process'],
        'DDIM': ['Denoising Diffusion Implicit Model','DDIM','deterministic sampling','tau','reparameterization'],
        'IDDPM': ['Improved DDPM','IDDPM','cosine noise schedule','contiguous noise schedule','log SNR','FID 3.17'],
        'LDM': ['Latent Diffusion','LDM','KL-regularized VAE','downsampling factor 8','cross-attention conditioning'],
        'DiT': ['Scalable Diffusion with Transformers','DiT','DiT-XL','patchify','adaln-zero','CFG scale'],
        'VideoDiffusion': ['Video Diffusion','factorized attention','spatial-temporal diffusion','VDM'],
        'Make-A-Video': ['Make-A-Video','temporal prior','text-to-video without text-video data','upsampler','temporal attention'],
        'DreamFusion': ['DreamFusion','text-to-3D','score distillation sampling','SDS','NeRF','CLIP'],
        'Latte': ['Latent Diffusion Transformer','Latte','video generation','DiT backbone','temporal attention'],
        'StableAudio': ['Stable Audio','timing-conditioned latent audio diffusion','latent diffusion','VAE for audio','CLAP conditioning'],
        'AudioLDM': ['AudioLDM','latent diffusion models','text-to-audio','CLAP','HiFi-GAN vocoder'],
        'Jukebox': ['Jukebox','VQ-VAE','top prior','downsample/upsample','long-context music generation'],
        'WaveNet': ['WaveNet','autoregressive model','dilated causal convolution','softmax output','raw audio waveform'],
        'ScoreBased': ['Score-Based Generative Modeling','score matching','SDE','VP-SDE','VE-SDE','ODE probability flow'],
        'SDE': ['Score-Based SDE','VP-SDE','VE-SDE','PC sampling','reverse diffusion SDE'],
        'FlowMatching': ['Flow Matching','optimal transport path','simplified flow','Conditional Flow Matching','rectified flow'],
        'ImprovedDDPM': ['Improved DDPM','cosine noise schedule','contiguous noise schedule','FID 3.17','KL-weighted loss'],
        'DiffusionBeatGANs': ['Diffusion Models Beat GANs','classifier guidance','FID','IS','upsampling'],
        'ElucidatingDesignSpace': ['Elucidating Design Space','EDM','preconditioning','noise conditioning','Heun sampler','loss weighting'],
        'ClassifierFreeGuidance': ['Classifier-Free Guidance','CFG','guidance scale w','unconditional score','classifier-free training'],
        'ProgressiveDistillation': ['Progressive Distillation','student-teacher distillation','half-step distillation','FID','sampling speedup'],
        'RePaint': ['RePaint','inpainting','known-region resampling','reverse diffusion','hole filling'],
        'Palette': ['Palette','image-to-image translation','DDPM','FID','LPIPS','color consistency'],
        'GLIDE': ['GLIDE','text-guided diffusion','CLIP','upsampling classifier','classifier-free guidance','inpainting'],
        'DPMSolver': ['DPM-Solver','ODE solver','DPM','k-step sampling','log-signal SNR','half-step'],
        'DPMSolverpp': ['DPM-Solver++','second-order solver','analytic SNR','guided sampling','exponential integrator'],
        'ConsistencyModels': ['Consistency Models','consistency function','one-step generation','consistency distillation','consistency training'],
        'SchrodingerBridge': ['Schrodinger Bridge','SB','iterative refinement','interpolation','score function','SDE path'],
        'AliasFreeGAN': ['Alias-Free GAN','alias-free generator','equalized learning rate','style mapping','truncation trick'],
        'StyleGAN2': ['StyleGAN2','style-based generator','mapping network','adaptive instance normalization','truncation psi'],
        'ESRGAN': ['ESRGAN','residual dense block','relu in discriminator','activations without BN','perceptual loss'],
        'SinGAN': ['SinGAN','single-image GAN','pyramid of GANs','multi-scale training','inpainting super-resolution'],
        'Glow': ['Glow','invertible 1x1 convolution','actnorm','flow-based model','exact likelihood'],
        'UGATIT': ['U-GAT-IT','adversarial attention normalization','class activation map','unsupervised image translation'],
        'ArbitraryStyleTransfer': ['AdaIN','arbitrary style transfer','adaptive instance normalization','feature transformation','real-time transfer'],
        'PhotoRealisticSR': ['SRGAN','photo-realistic super-resolution','perceptual loss','VGG feature loss','adversarial loss','PSNR/SSIM'],
    }
    for mk in extra.get(key, []):
        if mk not in method_names:
            method_names.append(mk)

    equations = extract_equations(text)
    quantitative = extract_quantitative(text)
    claims = extract_claims(text)
    sovereign = upgrade_templates.get(key, '')
    hex_ids = topic_hex.get(key, [3,4])
    phase_suggestions = [{'hexagram_id': h, 'phase_bits': 0, 'phase_temporal': 'past'} for h in hex_ids]
    old = existing.get(os.path.join(text_dir, base))
    study_notes = old.get('study_notes', []) if old else [{'category':'diffusion_generative','sentence': clean(text[:500]), 'keyword': title.split()[0]}]
    if not study_notes:
        study_notes = [{'category':'diffusion_generative','sentence': clean(text[:500]), 'keyword': title.split()[0]}]
    obj = {
        'file': os.path.join(text_dir, base),
        'filename': base,
        'title': title,
        'category': 'diffusion_generative',
        'char_count': len(text),
        'upgrade_categories': ['diffusion_generative', 'training_efficiency'],
        'is_relevant': True,
        'status': 'pending',
        'method_names': method_names,
        'equations': equations,
        'quantitative_results': quantitative,
        'claims': claims,
        'sovereign_stack_upgrade': sovereign,
        'study_notes': study_notes,
        'kingwen_hexagram_ids': hex_ids,
        'kingwen_phase_suggestions': phase_suggestions,
        'per_page_notes': old.get('per_page_notes', []) if old else [],
    }
    corpus_out.append(obj)
    updated += 1

with open(out_path, 'w', encoding='utf-8') as f:
    for obj in corpus_out:
        f.write(json.dumps(obj, ensure_ascii=False) + '\n')
print('updated entries:', updated)
print('wrote to', out_path)
