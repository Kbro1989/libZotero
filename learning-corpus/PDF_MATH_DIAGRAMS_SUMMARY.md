# Mathematical Diagrams in Zotero Learning Corpus

## Executive Summary

**Yes, the corpus contains PDF files with mathematical diagrams, but the text extraction pipeline captured them as plain text without the visual/mathematical formatting.**

## PDF Availability

- **Total papers in corpus**: 490
- **Papers with PDF files**: 330
- **PDF location**: `C:/Users/krist/Desktop/zotero/learning-corpus/<domain>/`

## Mathematical Content Status

### What Was Captured:
- ✅ Paper titles and abstracts
- ✅ Paper IDs (arXiv identifiers)
- ✅ Domain classifications (generative models, GNNs, etc.)
- ✅ Metadata (year, categories)
- ✅ Mathematical **references** in text (GAN, loss functions, KL-divergence, etc.)

### What Was NOT Captured:
- ❌ Actual LaTeX mathematical formulas
- ❌ Mathematical diagrams/figures
- ❌ Equations in rendered image format (common in arXiv PDFs)
- ❌ Mathematical notation with proper formatting

### Why:
The PDFs are available but were extracted as plain text using `pdftotext`, which:
1. Converts mathematical notation to text (e.g., "KL divergence" instead of "KL-divergence")
2. Cannot extract mathematical diagrams/figures as visual content
3. Loses formatting that distinguishes mathematical symbols

## Papers with Explicit Mathematical Content

The following papers were flagged as containing mathematical content based on title/abstract analysis:

1. **Generative Adversarial Nets** (1406.2661) - GAN formulation equations
2. **Variational Inference with Normalizing Flows** (1505.05770) - variational bounds
3. **WaveNet** (1609.03499) - audio generation equations
4. **Photo-Realistic Super-Resolution** (1609.04802) - CNN/Loss equations
5. **Glow** (1807.03039) - flow-based models, Jacobian determinants
6. **ESRGAN** (1809.00219) - GAN loss functions
7. **Score-Based Generative Models** (2006.09011) - score matching, SDEs
8. **Denoising Diffusion Models** (2006.11239) - diffusion equations
9. **Graph Neural Networks** (various) - message passing, aggregation
10. **Attention Is All You Need** variants - transformer equations

## Recommendations for Capturing Mathematical Diagrams

To properly capture mathematical diagrams from these PDFs:

### Option 1: PDF-to-Image Conversion
```bash
# Convert PDF pages with equations to images
pdftoppm -png -f 10 -l 15 <pdf-file> output_prefix
```

### Option 2: Use MathOCR Tools
Tools like:
- **Mathpix**: Convert equation images to LaTeX
- **im2latex**: Deep learning model for formula recognition
- **CROHME**: Competition datasets for mathematical recognition

### Option 3: Download and Analyze Original PDFs
The PDFs (330 files, ~518KB average each) are available at their original arXiv locations. They contain:
- Mathematical equations in both LaTeX source (can extract with `pdftotext -raw`)
- Figures and diagrams showing architectural diagrams, loss curves, etc.
- Tables with quantitative results

## File Structure

```
C:/Users/krist/Desktop/zotero/learning-corpus/
├── .text/                     # Extracted text files (~8KB each)
├── diffusion-generative/      # Domain folder with PDFs
├── graph-neural-networks/     # Domain folder with PDFs
├── efficient-inference-quantization/
├── knowledge-graphs/
├── multimodal-learning/
├── llm-alignment/
└── video-generation/
```

## Next Steps

If you need to extract mathematical diagrams from these PDFs:
1. Use the PDF paths in `unified-knowledge-base.json`
2. Employ OCR tools designed for mathematical content
3. Consider using arXiv's source LaTeX files (available at `https://arxiv.org/src/<paper-id>`)
4. For figure extraction: use `pdftoppm` or similar PDF-to-image tools

## Knowledge Base File Updated

`unified-knowledge-base.json` now includes:
- Paper entries with `pdf_path` field
- Metadata indicating 330 PDFs are available
- Extraction status for each PDF