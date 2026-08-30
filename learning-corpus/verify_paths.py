#!/usr/bin/env python3
"""Verify PDFs exist and can be processed"""

import os
from pathlib import Path

base = Path(r'Path(__file__).resolve().parent.parent / 'learning-corpus'')
dir_path = base / 'diffusion-generative'

print(f"Base exists: {base.exists()}")
print(f"Dir path: {dir_path}")
print(f"Dir exists: {dir_path.exists()}")

if dir_path.exists():
    pdf_files = list(dir_path.glob('*.pdf'))
    print(f"PDF count: {len(pdf_files)}")
    if pdf_files:
        print(f"First PDF: {pdf_files[0]}")
        print(f"File exists: {pdf_files[0].exists()}")