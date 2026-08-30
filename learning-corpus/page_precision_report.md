# Zotero PDF Math Extraction - Page Precision Report
# Generated: 2026-08-03
# Format: Machine-readable (per-page metrics)

## Summary Statistics
total_pdfs: 27
total_pages: 644
pdfs_with_math: 5
high_quality: 2
medium_quality: 3
low_quality: 3

## Page-by-Page Analysis

### PDF: 1412.6575_Embedding_Entities_and_Relations_for_Learning_and_Inference_in_Knowledge_Bases.pdf
- Total pages: 1
- Math expressions (high quality): 2
  - Page 1, Line 26: $$6y-9x=-\frac{3}{2}a.$$
  - Page 1, Line 27: $$\frac{a}{b}=\boxed{-\frac{2}{3}}$$
- Status: HIGH QUALITY - Clean LaTeX extraction

### PDF: 2405.04434_DeepSeek-V2.pdf
- Total pages: 4
- Math expressions (high quality): 46
  - Display math blocks across pages 1-4
  - Contains proper \frac, \boxed, \Rightarrow LaTeX
- Status: HIGH QUALITY

### PDF: 2009.09761_DiffWave_A_Versatile_Diffusion_Model_for_Audio_Synthesis.pdf
- Total pages: 17
- Math expressions: 6 (medium quality)
  - Page 4: $ = Bi-directional Dilated Conv (dilation = 2$ [garbled]
  - Page 16: Architecture convolution parameters with control chars
- Issues: Layout corruption, form feed characters embedded
- Status: MEDIUM QUALITY - Recoverable with cleanup

### PDF: 2106.05931_Score-based_Generative_Modeling_in_Latent_Space.pdf
- Total pages: 46
- Math expressions: 2 (low quality)
  - Page 31: $E $ and $T H$$ [garbled unicode]
- Issues: Unicode replacement chars, context corruption
- Status: LOW QUALITY - Requires regex cleanup

### PDF: 2106.12423_Alias-Free_Generative_Adversarial_Networks.pdf
- Total pages: 31
- Math expressions: 8 (low quality)
  - Page 20: Multiple $...$ with form feeds and control codes
  - Contains $1\u0015 sequences (raw ASCII control chars)
- Issues: Heavy layout corruption from original extraction
- Status: LOW QUALITY

### PDF: 2106.10934_Graph_Neural_Diffusion.pdf (and GRAND variant)
- Total pages: 15 each
- Math expressions: 3 (medium quality)
  - Page 3: Graph operators with edge field notation
- Notes: Duplicate detection - GRAND and Graph Neural Diffusion are same PDF
- Status: MEDIUM QUALITY

## Files WITHOUT Detectable Math
- 1406.2661_Generative_Adversarial_Nets.pdf: 9 pages, 0 math
- 1511.06434_Unsupervised_Representation_Learning.pdf: 16 pages, 0 math
- 1609.03499_WaveNet.pdf: 15 pages, 0 math
- 1712.04948_Style-Based_Generator.pdf: 12 pages, 0 math
- ... (22 more PDFs with no detectable LaTeX patterns)

## Quality Assessment Legend
HIGH: Clean LaTeX with proper delimiters, readable by humans
MEDIUM: Present but with unicode/layout corruption, recoverable
LOW: Garbled with control characters, requires processing
NONE: No $...$ patterns detected (ISBN prices not counted)

## Recommendations
1. For King Wen integration: Use ONLY high-quality files (1412.6575, 2405.04434)
2. For training data: Filter out low-quality extractions
3. Re-extract problem PDFs with: pdftotext -bbox -layout -enc UTF-8
4. Post-process with regex to remove control characters: [\u0015-\u001f]