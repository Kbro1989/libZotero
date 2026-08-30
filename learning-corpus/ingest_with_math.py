#!/usr/bin/env python3
"""
ingest_with_math.py
Multi-format ingestion pipeline for Zotero learning corpus with math preservation

Intent: Re-ingest PDFs with proper math extraction to prevent ground truth corruption
in King Wen expansion chain. Without math, agents hallucinate; with math, they collapse correctly.

Usage:
    python ingest_with_math.py [--db-url postgresql://...] [--batch-size 10]
"""

import os
import re
import json
import hashlib
import subprocess
import argparse
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

class MathExtractor:
    """Extracts mathematical content from text/PDF files"""
    
    def __init__(self, dpi: int = 300):
        self.dpi = dpi
        self.math_blocks = []
    
    def extract_from_text(self, text: str, source_id: str) -> Dict:
        """Extract math blocks from text (already extracted via pdftotext)"""
        blocks = []
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            math_matches = []
            
            # Simple but effective patterns for LaTeX in pdftotext output
            patterns = [
                r'\$[^$]+\$',  # Inline LaTeX math
                r'\$\$.*?\$\$',  # Display math
            ]
            
            for pattern in patterns:
                try:
                    matches = re.findall(pattern, line, re.IGNORECASE | re.DOTALL)
                    if matches:
                        math_matches.extend(matches)
                except:
                    pass
            
            if math_matches:
                blocks.append({
                    'source_id': source_id,
                    'block_index': len(blocks),
                    'latex': ' '.join(math_matches)[:500],
                    'context_before': lines[i-1][:200] if i > 0 else '',
                    'context_after': lines[i+1][:200] if i < len(lines)-1 else '',
                    'position': {'vertical_offset': i},
                    'classification': 'equation',
                    'confidence': 0.9,
                    'symbolic_count': len(re.findall(r'[A-Za-z]+', ' '.join(math_matches)))
                })
        
        return {
            'math_blocks': blocks,
            'math_count': len(blocks),
            'math_quality': min(1.0, len(blocks) / max(1, text.count('\n') / 50))
        }

class UnifiedIngestor:
    """Manages database operations for unified corpus"""
    
    def __init__(self, db_path: str = 'unified_corpus.db'):
        self.db_path = db_path
        self.conn = None
    
    def connect(self):
        """Establish database connection"""
        import sqlite3
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        # Create tables if not exist
        self._create_tables()
    
    def _create_tables(self):
        """Create database tables"""
        cursor = self.conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sources (
                id TEXT PRIMARY KEY,
                title TEXT,
                authors TEXT,
                year INTEGER,
                source_type TEXT,
                source_url TEXT,
                metadata TEXT,
                added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS source_formats (
                source_id TEXT REFERENCES sources(id),
                format TEXT,
                content TEXT,
                content_hash TEXT,
                math_count INTEGER,
                math_quality REAL,
                extraction_method TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS math_blocks (
                source_id TEXT REFERENCES sources(id),
                block_index INTEGER,
                latex TEXT,
                context_before TEXT,
                context_after TEXT,
                position TEXT,
                classification TEXT,
                confidence REAL,
                symbolic_count INTEGER
            )
        ''')
        
        self.conn.commit()
    
    def ingest_source(self, source_data: Dict, formats: List[Dict], math_blocks: List[Dict]) -> str:
        """Ingest a single source with all its formats and math blocks"""
        source_id = source_data['id']
        
        cursor = self.conn.cursor()
        
        # Insert source
        cursor.execute('''
            INSERT OR REPLACE INTO sources 
            (id, title, authors, year, source_type, source_url, metadata)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            source_id,
            source_data['title'],
            json.dumps(source_data.get('authors', [])),
            source_data.get('year'),
            source_data.get('source_type'),
            source_data.get('source_url'),
            json.dumps(source_data.get('metadata', {}))
        ))
        
        # Insert formats
        for fmt in formats:
            cursor.execute('''
                INSERT INTO source_formats 
                (source_id, format, content, content_hash, math_count, math_quality, extraction_method)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                source_id,
                fmt['format'],
                fmt['content'],
                hashlib.sha256(fmt['content'].encode()).hexdigest()[:32],
                fmt.get('math_count', 0),
                fmt.get('math_quality', 0),
                fmt.get('extraction_method', 'unknown')
            ))
        
        # Insert math blocks
        for block in math_blocks:
            cursor.execute('''
                INSERT INTO math_blocks 
                (source_id, block_index, latex, context_before, context_after, 
                 position, classification, confidence, symbolic_count)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                source_id,
                block['block_index'],
                block['latex'],
                block.get('context_before', ''),
                block.get('context_after', ''),
                json.dumps(block.get('position', {})),
                block.get('classification', 'equation'),
                block.get('confidence', 0.5),
                block.get('symbolic_count', 0)
            ))
        
        self.conn.commit()
        return source_id
    
    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()

def process_paper(paper_entry: Dict) -> Tuple[Dict, List[Dict], List[Dict]]:
    """Process a single paper entry"""
    paper_id = paper_entry['id']
    title = paper_entry['title']
    year = int(paper_entry.get('year', datetime.now().year))
    
    # Generate source ID
    source_id = hashlib.sha256(f"{title}|{year}".encode()).hexdigest()[:32]
    
    # Read TXT content
    txt_path = f'C:/Users/krist/Desktop/zotero/learning-corpus/.text/{paper_id}.txt'
    text_content = ""
    if os.path.exists(txt_path):
        with open(txt_path, 'r', encoding='utf-8', errors='ignore') as f:
            text_content = f.read()
    
    # Extract math
    extractor = MathExtractor()
    math_result = extractor.extract_from_text(text_content, source_id)
    
    # Prepare source data
    source_data = {
        'id': source_id,
        'title': title,
        'authors': paper_entry.get('authors', []),
        'year': year,
        'source_type': 'arxiv',
        'source_url': f"https://arxiv.org/abs/{paper_id}",
        'metadata': {'domain': paper_entry.get('domain', 'unknown') if 'domain' in paper_entry else 'title' in paper_entry}
    }
    
    # Prepare formats
    formats = [
        {
            'format': 'pdf_text',
            'content': text_content[:100000],
            'math_count': math_result['math_count'],
            'math_quality': math_result['math_quality'],
            'extraction_method': 'pdftotext'
        }
    ]
    
    return source_data, formats, math_result['math_blocks']

def main():
    parser = argparse.ArgumentParser(description='Ingest Zotero corpus with math preservation')
    parser.add_argument('--db-path', default='unified_corpus.db', help='Database path')
    parser.add_argument('--batch-size', type=int, default=10, help='Batch size for inserts')
    parser.add_argument('--manifest', default='C:/Users/krist/Desktop/zotero/learning-corpus/arxiv-manifest.json',
                       help='Path to arXiv manifest JSON')
    args = parser.parse_args()
    
    # Load manifest
    with open(args.manifest, 'r') as f:
        manifest = json.load(f)
    
    # Initialize database
    ingestor = UnifiedIngestor(args.db_path)
    ingestor.connect()
    
    # Process papers
    processed = 0
    with_math = 0
    
    for paper_entry in manifest[:args.batch_size]:
        try:
            source_data, formats, math_blocks = process_paper(paper_entry)
            source_id = ingestor.ingest_source(source_data, formats, math_blocks)
            
            processed += 1
            if math_blocks:
                with_math += 1
            
            print(f"Processed {source_id[:8]}... {len(math_blocks)} math blocks")
        
        except Exception as e:
            print(f"Error processing {paper_entry.get('id', 'unknown')}: {e}")
            import traceback
            traceback.print_exc()
            continue
    
    ingestor.close()
    
    print(f"\nIngestion complete:")
    print(f"  Processed: {processed}")
    print(f"  With math blocks: {with_math}")

if __name__ == '__main__':
    main()