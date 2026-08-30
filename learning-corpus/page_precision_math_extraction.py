#!/usr/bin/env python3
"""
page_precision_math_extraction.py
Extracts math content with per-page precision from PDF text files
Output: JSONL with page-level math extraction preserving original structure
"""

import os
import re
import json
from pathlib import Path

# Math patterns
INLINE_MATH = re.compile(r'\$(?:[^$]|\$(?![^$]))*\$', re.DOTALL)
DISPLAY_MATH = re.compile(r'\$\$(?:[^$]|\\\$)*?\$\$', re.DOTALL)

def extract_page_math(txt_path: str) -> dict:
    """Extract math content with page-level precision from a text file."""
    
    # Read file with proper encoding handling
    with open(txt_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    # Split by form feeds and page markers (common PDF extraction markers)
    pages = re.split(r'\x0c|\f|PAGE\s+\d+|Page\s+\d+', content)
    
    results = {
        'file_path': txt_path,
        'file_name': os.path.basename(txt_path),
        'total_pages': len(pages),
        'pages': []
    }
    
    for page_num, page_content in enumerate(pages, 1):
        if not page_content.strip():
            continue
            
        # Extract inline math
        inline_matches = INLINE_MATH.findall(page_content)
        
        # Extract display math
        display_matches = DISPLAY_MATH.findall(page_content)
        
        # Get all math with positions
        all_math = []
        for match in INLINE_MATH.finditer(page_content):
            all_math.append({
                'type': 'inline',
                'content': match.group(),
                'start': match.start(),
                'end': match.end()
            })
        
        for match in DISPLAY_MATH.finditer(page_content):
            all_math.append({
                'type': 'display',
                'content': match.group(),
                'start': match.start(),
                'end': match.end()
            })
        
        page_data = {
            'page_number': page_num,
            'char_count': len(page_content),
            'word_count': len(page_content.split()),
            'inline_math_count': len(inline_matches),
            'display_math_count': len(display_matches),
            'total_math_count': len(inline_matches) + len(display_matches),
            'math_content': {
                'inline': inline_matches,
                'display': display_matches,
                'all_matches': all_math
            },
            'text_snippet': page_content[:500]  # First 500 chars for context
        }
        
        results['pages'].append(page_data)
    
    # Calculate total stats
    total_inline = sum(p['inline_math_count'] for p in results['pages'])
    total_display = sum(p['display_math_count'] for p in results['pages'])
    
    results['summary'] = {
        'total_inline_math': total_inline,
        'total_display_math': total_display,
        'total_math_expressions': total_inline + total_display,
        'pages_with_math': sum(1 for p in results['pages'] if p['total_math_count'] > 0)
    }
    
    return results

def process_all_txts(text_dir: str, output_path: str):
    """Process all txt files and output JSONL."""
    text_path = Path(text_dir)
    
    with open(output_path, 'w', encoding='utf-8') as out_f:
        for txt_file in sorted(text_path.glob('*.txt')):
            # Skip Python scripts in the directory
            if txt_file.suffix != '.txt':
                continue
            if 'extract' in txt_file.stem.lower() or 'build' in txt_file.stem.lower():
                continue
                
            try:
                result = extract_page_math(str(txt_file))
                # Write one JSONL line per source file
                out_f.write(json.dumps(result, ensure_ascii=False) + '\n')
                print(f"Processed: {txt_file.name} ({result['summary']['total_math_expressions']} math expressions)")
            except Exception as e:
                print(f"Error processing {txt_file.name}: {e}")

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 3:
        text_dir = sys.argv[1]
        output_path = sys.argv[2]
    else:
        text_dir = 'Path(__file__).resolve().parent.parent / 'learning-corpus' / '.text''
        output_path = 'Path(__file__).resolve().parent.parent / 'learning-corpus'/page_precision_math.jsonl'
    
    process_all_txts(text_dir, output_path)
    print(f"\nOutput written to: {output_path}")