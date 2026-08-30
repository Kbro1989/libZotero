#!/usr/bin/env python3
"""
Build a unified knowledge base from the Zotero learning corpus.
Extracts key concepts, methodologies, and findings from academic papers.
"""

import os
import json
from pathlib import Path
from collections import defaultdict
import re

TEXT_DIR = Path("/c/Users/krist/Desktop/zotero/learning-corpus/.text")
OUTPUT_FILE = Path("/c/Users/krist/Desktop/zotero/knowledge-base.json")

# Domain classification patterns
DOMAIN_KEYWORDS = {
    "generative_models": ["adversarial", "gan", "generative", "flow", "normalizing", "variational"],
    "representation_learning": ["embedding", "representation", "feature learning", "unsupervised", "self-supervised"],
    "graph_neural_networks": ["graph", "gcn", "gnn", "node2vec", "graph attention", "gae", "pool"],
    "knowledge_graphs": ["knowledge graph", "embedding entities", "rotatio", "transE", "ComplEx"],
    "computer_vision": ["super-resolution", "vqa", "style transfer", "image", "vision"],
    "audio_processing": ["waveform", "waveNet", "audio"],
    "reinforcement_learning": ["reinforcement", "human preferences", "policy"],
    "explainability": ["explainer", "intermediate", "attention", "explanation"],
}

def extract_core_concepts(text, title):
    """Extract core concepts from a paper's text."""
    concepts = {
        "key_problems": [],
        "proposed_methods": [],
        "key_findings": [],
        "datasets_used": [],
        "metrics_reported": [],
    }
    
    # Simple heuristics for concept extraction
    lines = text.split('\n')
    
    # Look for problem statements
    problem_patterns = [
        r'we (propose|introduce|develop) ([^\n]+?)\.',
        r'the (key|main|primary) (challenge|problem) is ([^\n]+?)\.',
    ]
    
    # Look for method contributions
    method_patterns = [
        r'our (approach|method|framework) (uses|employs|applies) ([^\n]+?)\.',
        r'we (designed|built|created) ([^\n]+?)\.',
    ]
    
    # Look for results
    result_patterns = [
        r'we (achieve|obtain|report) ([^\n]+?)\.',
        r'experimental results show ([^\n]+?)\.',
    ]
    
    return concepts

def classify_domain(title, text):
    """Classify paper into domain categories."""
    text_lower = (title + " " + text[:1000]).lower()
    domains = []
    
    for domain, keywords in DOMAIN_KEYWORDS.items():
        if any(kw in text_lower for kw in keywords):
            domains.append(domain)
    
    return domains if domains else ["other"]

def extract_paper_metadata(filepath):
    """Extract metadata from a paper file."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
        
        title = filepath.stem
        # Clean up title from filename
        title = re.sub(r'^\d+\.\d+_', '', title)
        title = title.replace('_', ' ').strip()
        
        domains = classify_domain(title, text)
        concepts = extract_core_concepts(text, title)
        
        return {
            "id": filepath.stem,
            "title": title,
            "arxiv_id": re.match(r'^(\d+\.\d+)', filepath.name),
            "domains": domains,
            "concepts": concepts,
            "snippet": text[:500].replace('\n', ' ')[:500],
        }
    except Exception as e:
        return {"id": filepath.name, "title": "error", "error": str(e)}

def build_knowledge_base():
    """Build the unified knowledge base from all papers."""
    papers = []
    domain_map = defaultdict(list)
    
    txt_files = list(TEXT_DIR.glob("*.txt"))
    print(f"Found {len(txt_files)} papers to process")
    
    for i, filepath in enumerate(txt_files[:50]):  # Process first 50 as sample
        if i % 10 == 0:
            print(f"Processing paper {i+1}/{min(50, len(txt_files))}...")
        
        paper = extract_paper_metadata(filepath)
        papers.append(paper)
        
        for domain in paper.get("domains", []):
            domain_map[domain].append(paper["id"])
    
    knowledge_base = {
        "metadata": {
            "total_papers_processed": len(papers),
            "total_domains": len(domain_map),
            "source_path": str(TEXT_DIR),
        },
        "by_domain": dict(domain_map),
        "papers": papers,
        "domains": list(DOMAIN_KEYWORDS.keys()) + ["other"],
    }
    
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(knowledge_base, f, indent=2)
    
    print(f"\nKnowledge base saved to {OUTPUT_FILE}")
    print(f"Total papers: {len(papers)}")
    print(f"Domains: {list(domain_map.keys())}")
    
    return knowledge_base

if __name__ == "__main__":
    build_knowledge_base()