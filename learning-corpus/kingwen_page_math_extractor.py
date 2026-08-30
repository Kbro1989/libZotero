#!/usr/bin/env python3
"""
kingwen_page_math_extractor.py
Page-precision math extraction for King Wen quantum state expansion.
Handles multiple math formats: LaTeX $...$ $$...$$ AND embedded text equations.
No reduction - full preservation of every line as quantum state.
"""

import os
import re
import json
import subprocess
from pathlib import Path
from typing import Dict, Any

# Patterns for LaTeX math detection
INLINE_MATH = re.compile(r'\$(?:[^$]|\\\$)*(?:\$(?![^$]))*\$')
DISPLAY_MATH = re.compile(r'\$\$(?:[^$]|\\\$)*?\$\$')

# Patterns for embedded math expressions (GAN training equations, etc.)
# Looks for equations like: V(D,G) = Exp[log...]
EMBEDDED_EQUATION = re.compile(
    r'(?:min|max|log|D\(|G\(|p_data|p_g|KL|exp|exp\[|Ez|expected)[^.\n]{10,100}[=+\-][^.\n]{0,50}',
    re.IGNORECASE
)

# Pattern for equation numbers like "(1)", "(2)", etc.
EQUATION_REF = re.compile(r'\(\d+\)')

def get_pdf_page_count(pdf_path: str) -> int:
    """Get page count from PDF metadata."""
    try:
        result = subprocess.run(
            ['pdfinfo', pdf_path],
            capture_output=True, text=True, timeout=10
        )
        for line in result.stdout.split('\n'):
            if line.startswith('Pages:'):
                return int(line.split(':')[1].strip())
    except:
        pass
    return 0

def extract_page_text(pdf_path: str, page_num: int) -> str:
    """Extract text for a single page."""
    try:
        result = subprocess.run(
            ['pdftotext', '-layout', '-enc', 'UTF-8',
             '-f', str(page_num), '-l', str(page_num),
             pdf_path, '-'],
            capture_output=True, text=True, timeout=30,
            errors='replace'
        )
        return result.stdout
    except Exception as e:
        return f"EXTRACTION_ERROR: {e}"

def detect_math_forms(page_text: str) -> Dict[str, Any]:
    """Detect all math forms in text - King Wen expansion requires full capture."""
    
    # 1. LaTeX inline math
    latex_inline = [
        {'type': 'latex_inline', 'content': m.group(), 'span': m.span()}
        for m in INLINE_MATH.finditer(page_text)
    ]
    
    # 2. LaTeX display math
    latex_display = [
        {'type': 'latex_display', 'content': m.group(), 'span': m.span()}
        for m in DISPLAY_MATH.finditer(page_text)
    ]
    
    # 3. Embedded mathematical expressions (text-form equations)
    embedded = [
        {'type': 'embedded_equation', 'content': m.group().strip(), 'span': m.span()}
        for m in EMBEDDED_EQUATION.finditer(page_text)
    ]
    
    # 4. Equation reference markers (these indicate math presence)
    equation_refs = list(EQUATION_REF.finditer(page_text))
    
    return {
        'latex_inline_count': len(latex_inline),
        'latex_display_count': len(latex_display),
        'embedded_equation_count': len(embedded),
        'equation_ref_count': len(equation_refs),
        'latex_inline': latex_inline,
        'latex_display': latex_display,
        'embedded_equations': embedded,
        'equation_references': [m.group() for m in equation_refs],
        'total_math_indicators': len(latex_inline) + len(latex_display) + len(embedded) + len(equation_refs)
    }

def process_pdf_to_pages(pdf_path: str) -> list:
    """Process single PDF to page-level JSON records - King Wen superposition."""
    page_count = get_pdf_page_count(pdf_path)
    pages = []
    
    for page_num in range(1, page_count + 1):
        text = extract_page_text(pdf_path, page_num)
        
        if text.startswith("EXTRACTION_ERROR"):
            page_data = {
                'pdf_path': pdf_path,
                'pdf_name': os.path.basename(pdf_path),
                'page_number': page_num,
                'extraction_error': text
            }
        else:
            math_data = detect_math_forms(text)
            
            page_data = {
                'pdf_path': pdf_path,
                'pdf_name': os.path.basename(pdf_path),
                'page_number': page_num,
                'page_count': page_count,
                'char_count': len(text),
                'word_count': len(text.split()),
                'unicode_quality': '\ufffd' not in text,
                'encoding_replacement_chars': text.count('\ufffd'),
                'math': math_data,
                'raw_text': text[:10000],  # First 10k chars for inspection
                'text_hash': hash(text[:1000])  # For deduplication
            }
        pages.append(page_data)
    
    return pages

def main():
    output_file = 'Path(__file__).resolve().parent.parent / 'learning-corpus'/pdf_page_math_extraction.jsonl'
    base = 'Path(__file__).resolve().parent.parent / 'learning-corpus''
    
    # Find all PDFs
    subdirs = ['diffusion-generative', 'efficient-inference-quantization',
               'graph-neural-networks', 'llm-alignment',
               'multimodal-learning', 'video-generation']
    
    pdfs = []
    for sd in subdirs:
        spath = os.path.join(base, sd)
        if os.path.exists(spath):
            pdfs.extend(Path(spath).glob('*.pdf'))
    
    print(f"King Wen quantum expansion: Processing {len(pdfs)} PDFs to page-level states...")
    
    with open(output_file, 'w', encoding='utf-8') as out_f:
        total_pages = 0
        pages_with_math = 0
        
        for pdf_path in sorted(pdfs):
            pdf_str = str(pdf_path)
            pdf_name = pdf_path.name
            
            print(f"  {pdf_name}")
            
            for page_record in process_pdf_to_pages(pdf_str):
                total_pages += 1
                
                # Emit record (King Wen: every page is a quantum state)
                out_f.write(json.dumps(page_record, ensure_ascii=False) + '\n')
                
                if page_record.get('math', {}).get('total_math_indicators', 0) > 0:
                    pages_with_math += 1
    
    print(f"\n{'='*60}")
    print(f"King Wen quantum expansion complete")
    print(f"  Total pages (quantum states): {total_pages}")
    print(f"  Pages with math indicators: {pages_with_math}")
    print(f"  Output file: {output_file}")

if __name__ == '__main__':
    main()