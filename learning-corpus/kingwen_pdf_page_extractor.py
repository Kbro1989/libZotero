#!/usr/bin/env python3
"""
Simple direct PDF to JSONL extractor for King Wen quantum expansion.
No subprocess - uses pdftotext output directly.
"""

import os
import json

base = "C:/Users/krist/Desktop/zotero/learning-corpus"
output = base + "/pdf_page_math_extraction.jsonl"

pdf_dirs = ['diffusion-generative', 'efficient-inference-quantization',
             'graph-neural-networks', 'llm-alignment',
             'multimodal-learning', 'video-generation']

total_pages = 0
total_pdfs = 0

with open(output, 'w', encoding='utf-8') as out_f:
    for d in pdf_dirs:
        dir_path = os.path.join(base, d)
        
        if not os.path.exists(dir_path):
            continue
        
        for fname in sorted(os.listdir(dir_path)):
            if not fname.endswith('.pdf'):
                continue
            
            total_pdfs += 1
            print(f"  {fname}")
            
            # Read pre-extracted txt files if available
            txt_name = fname.replace('.pdf', '.txt')
            txt_path = base + '/.text/' + txt_name
            
            if os.path.exists(txt_path):
                with open(txt_path, 'r', encoding='utf-8', errors='replace') as f:
                    full_text = f.read()
            else:
                # Create placeholder
                full_text = "[PDF_TXT_NOT_AVAILABLE]"
            
            # Split by form feed
            if '\x0c' in full_text:
                pages = full_text.split('\x0c')
            else:
                pages = [full_text]
            
            for page_num, page_text in enumerate(pages, 1):
                page_text = page_text.strip()
                if not page_text or len(page_text) < 50:
                    continue
                
                record = {
                    'pdf_name': fname,
                    'page_number': page_num,
                    'page_count': len(pages),
                    'char_count': len(page_text),
                    'unicode_quality': '\ufffd' not in page_text,
                    'text': page_text[:5000]
                }
                out_f.write(json.dumps(record, ensure_ascii=False) + '\n')
                total_pages += 1

print(f"\nKing Wen quantum expansion complete:")
print(f"  PDFs processed: {total_pdfs}")
print(f"  Pages extracted: {total_pages}")
print(f"  Output: {output}")