#!/usr/bin/env python3
"""
reextract_pdfs_page_precision.py
Re-extracts PDFs with proper Unicode handling and page-level precision
Output: JSONL with per-page math extraction from original PDFs
"""

import os
import re
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Optional

# Math patterns for LaTeX detection
INLINE_MATH = re.compile(r'\$(?:[^$]|\\\$)*(?:\$(?![^$]))*\$', re.DOTALL)
DISPLAY_MATH = re.compile(r'\$\$(?:[^$]|\\\$)*?\$\$', re.DOTALL)

def extract_pdf_with_pdftotext(pdf_path: str) -> Dict:
    """Extract text from PDF using pdftotext with page separation."""
    result = {
        'file_path': pdf_path,
        'file_name': os.path.basename(pdf_path),
        'pages': [],
        'extraction_status': 'pending'
    }
    
    try:
        # Use pdftotext with layout preservation and page separation
        cmd = [
            'pdftotext',
            '-layout',      # Preserve layout
            '-enc', 'UTF-8', # UTF-8 encoding
            '-f', '1',       # Start page
            '-l', '999',     # End page (all)
            pdf_path,
            '-'            # Output to stdout
        ]
        
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        
        if proc.returncode != 0:
            result['extraction_status'] = f'error: {proc.stderr}'
            return result
        
        # Split into pages (pdftotext uses form feed characters between pages)
        text = proc.stdout
        
        # Try to detect actual page breaks
        # Method 1: Form feed characters
        if '\x0c' in text:
            pages_raw = text.split('\x0c')
        else:
            # Method 2: Try page markers
            pages_raw = re.split(r'(?=Page\s+\d+|^\d+\s*Page)', text, flags=re.MULTILINE)
        
        # Clean up pages
        clean_pages = []
        for page_text in pages_raw:
            page_text = page_text.strip()
            if page_text and len(page_text) > 20:  # Skip empty/tiny pages
                clean_pages.append(page_text)
        
        result['extraction_status'] = 'success'
        
        # Process each page
        for page_num, page_content in enumerate(clean_pages, 1):
            # Find all math expressions
            inline_matches = INLINE_MATH.findall(page_content)
            display_matches = DISPLAY_MATH.findall(page_content)
            
            # Build positions
            all_math = []
            for match in INLINE_MATH.finditer(page_content):
                all_math.append({
                    'type': 'inline',
                    'content': match.group(),
                    'start': match.start(),
                    'end': match.end(),
                    'length': match.end() - match.start()
                })
            
            for match in DISPLAY_MATH.finditer(page_content):
                all_math.append({
                    'type': 'display',
                    'content': match.group(),
                    'start': match.start(),
                    'end': match.end(),
                    'length': match.end() - match.start()
                })
            
            # Extract surrounding context for each math expression
            math_with_context = []
            for m in all_math:
                start = max(0, m['start'] - 100)
                end = min(len(page_content), m['end'] + 100)
                math_with_context.append({
                    'type': m['type'],
                    'content': m['content'],
                    'position': {'page_line': page_num, 'char_offset': m['start']},
                    'context_before': page_content[start:m['start']],
                    'context_after': page_content[m['end']:end]
                })
            
            page_data = {
                'page_number': page_num,
                'char_count': len(page_content),
                'word_count': len(page_content.split()),
                'inline_math_count': len(inline_matches),
                'display_math_count': len(display_matches),
                'total_math_count': len(inline_matches) + len(display_matches),
                'math_expressions': math_with_context,
                'raw_text_length': len(page_content),
                'unicode_quality': page_content.count('\ufffd') == 0  # No replacement chars
            }
            
            result['pages'].append(page_data)
        
        # Summary
        total_inline = sum(p['inline_math_count'] for p in result['pages'])
        total_display = sum(p['display_math_count'] for p in result['pages'])
        
        result['summary'] = {
            'total_pages': len(result['pages']),
            'total_inline_math': total_inline,
            'total_display_math': total_display,
            'total_math_expressions': total_inline + total_display,
            'pages_with_math': sum(1 for p in result['pages'] if p['total_math_count'] > 0),
            'any_math_found': (total_inline + total_display) > 0
        }
        
    except Exception as e:
        result['extraction_status'] = f'exception: {str(e)}'
    
    return result

def reextract_all_pdfs(pdf_dir: str, output_jsonl: str):
    """Re-extract all PDFs and output page-precision JSONL."""
    pdf_path = Path(pdf_dir)
    
    with open(output_jsonl, 'w', encoding='utf-8') as out_f:
        pdf_count = 0
        math_found = 0
        
        for pdf_file in sorted(pdf_path.glob('*.pdf')):
            pdf_count += 1
            print(f"Processing [{pdf_count}]: {pdf_file.name}")
            
            result = extract_pdf_with_pdftotext(str(pdf_file))
            
            if result['extraction_status'] == 'success':
                if result['summary']['any_math_found']:
                    math_found += 1
                
                out_f.write(json.dumps(result, ensure_ascii=False) + '\n')
                print(f"  -> {result['summary']['total_math_expressions']} math in {result['summary']['total_pages']} pages")
            else:
                print(f"  -> ERROR: {result['extraction_status']}")
    
    print(f"\n{'='*60}")
    print(f"EXTRACTION COMPLETE")
    print(f"  PDFs processed: {pdf_count}")
    print(f"  PDFs with math: {math_found}")
    print(f"  Output: {output_jsonl}")

if __name__ == '__main__':
    import sys
    
    pdf_dir = sys.argv[1] if len(sys.argv) > 1 else 'Path(__file__).resolve().parent.parent / 'learning-corpus''
    output = sys.argv[2] if len(sys.argv) > 2 else 'Path(__file__).resolve().parent.parent / 'learning-corpus'/pdf_page_math_extraction.jsonl'
    
    # Find pdf subdirectories
    subdirs = [
        'diffusion-generative',
        'efficient-inference-quantization', 
        'graph-neural-networks',
        'llm-alignment',
        'multimodal-learning',
        'video-generation'
    ]
    
    # Use the first directory that has PDFs
    for subdir in subdirs:
        test_path = os.path.join(pdf_dir, subdir)
        if os.path.exists(test_path) and os.listdir(test_path):
            pdf_dir = test_path
            break
    
    reextract_all_pdfs(pdf_dir, output)