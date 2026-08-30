#!/usr/bin/env python3
"""
page_precision_reextract.py
Machine-readable page-level math extraction from PDFs for King Wen quantum state expansion.
Each PDF can output 1-N pages, each page can contain 0-N math expressions.
No reduction - full preservation per King Wen superposition principle.
"""

import os
import re
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Any, Iterator

# Patterns for LaTeX math detection (King Wen phase encoding)
INLINE_MATH = re.compile(r'\$(?:[^$]|\\\$)*(?:\$(?![^$]))*\$', re.DOTALL)
DISPLAY_MATH = re.compile(r'\$\$(?:[^$]|\\\$)*?\$\$', re.DOTALL)

# Count pages in PDF using pdfinfo
def get_pdf_page_count(pdf_path: str) -> int:
    """Get exact page count from PDF."""
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

def extract_page_by_page(pdf_path: str) -> Iterator[Dict[str, Any]]:
    """Extract each page individually - King Wen per-page state preservation."""
    page_count = get_pdf_page_count(pdf_path)
    
    for page_num in range(1, page_count + 1):
        try:
            # Extract single page
            result = subprocess.run(
                ['pdftotext', '-layout', '-enc', 'UTF-8', 
                 '-f', str(page_num), '-l', str(page_num),
                 pdf_path, '-'],
                capture_output=True, text=True, timeout=30,
                errors='replace'  # Replace invalid UTF-8 with replacement char
            )
            
            page_text = result.stdout
            unicode_quality = '\ufffd' not in page_text
            
            # Extract math per page
            inline_matches = list(INLINE_MATH.finditer(page_text))
            display_matches = list(DISPLAY_MATH.finditer(page_text))
            
            all_math = []
            for m in inline_matches:
                all_math.append({
                    'type': 'inline',
                    'content': m.group(),
                    'start': m.start(),
                    'end': m.end(),
                    'length': m.end() - m.start()
                })
            for m in display_matches:
                all_math.append({
                    'type': 'display',
                    'content': m.group(),
                    'start': m.start(),
                    'end': m.end(),
                    'length': m.end() - m.start()
                })
            
            page_data = {
                'pdf_path': pdf_path,
                'pdf_name': os.path.basename(pdf_path),
                'page_number': page_num,
                'page_count_total': page_count,
                'char_count': len(page_text),
                'word_count': len(page_text.split()),
                'unicode_quality': unicode_quality,
                'encoding_errors': page_text.count('\ufffd'),
                'math_count': len(all_math),
                'math_inline': len(inline_matches),
                'math_display': len(display_matches),
                'math_expressions': all_math,
                'raw_text': page_text
            }
            
            yield page_data
            
        except Exception as e:
            yield {
                'pdf_path': pdf_path,
                'pdf_name': os.path.basename(pdf_path),
                'page_number': page_num,
                'error': str(e)
            }

def main():
    output_file = 'C:/Users/krist/Desktop/zotero/learning-corpus/pdf_page_math_extraction.jsonl'
    
    # Find all subdirectories with PDFs
    base = 'C:/Users/krist/Desktop/zotero/learning-corpus'
    subdirs = ['diffusion-generative', 'efficient-inference-quantization', 
               'graph-neural-networks', 'llm-alignment', 
               'multimodal-learning', 'video-generation']
    
    pdfs = []
    for sd in subdirs:
        spath = os.path.join(base, sd)
        if os.path.exists(spath):
            pdfs.extend(Path(spath).glob('*.pdf'))
    
    print(f"Found {len(pdfs)} PDFs to process")
    
    with open(output_file, 'w', encoding='utf-8') as out_f:
        pdf_count = 0
        pages_with_math = 0
        total_math = 0
        
        for pdf_path in sorted(pdfs):
            pdf_count += 1
            print(f"[{pdf_count}/{len(pdfs)}] {pdf_path.name}")
            
            for page_data in extract_page_by_page(str(pdf_path)):
                if 'error' in page_data:
                    print(f"  Page {page_data['page_number']}: ERROR - {page_data['error']}")
                    continue
                    
                out_f.write(json.dumps(page_data, ensure_ascii=False) + '\n')
                
                if page_data['math_count'] > 0:
                    pages_with_math += 1
                    total_math += page_data['math_count']
                    print(f"  Page {page_data['page_number']}: {page_data['math_count']} math exprs")
                else:
                    print(f"  Page {page_data['page_number']}: 0 math")
    
    print(f"\n{'='*60}")
    print(f"COMPLETE: {pdf_count} PDFs, {pages_with_math} pages with math, {total_math} total expressions")
    print(f"Output: {output_file}")

if __name__ == '__main__':
    main()