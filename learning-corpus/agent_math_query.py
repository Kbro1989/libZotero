"""
agent_math_query.py
Hermes MOA agent query layer that preserves math content for King Wen collapse

Intent: Ensure agents receive complete source documents including mathematical
principles, not just flat text. Prevents garbage-in-garbage-out in expansion.

Usage:
    from agent_math_query import query_source_for_kingwen
    result = query_source_for_kingwen(source_id)
"""

import json
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict


@dataclass
class MathBlock:
    """Structured mathematical content block"""
    block_index: int
    latex: str
    context_before: str
    context_after: str
    classification: str
    confidence: float
    symbolic_count: int


@dataclass  
class SourceDocument:
    """Complete document with text and math for agent consumption"""
    source_id: str
    title: str
    authors: List[str]
    year: int
    text_content: str
    math_blocks: List[Dict]
    total_math_count: int
    math_quality: float
    embeddings: Optional[Dict] = None


class MathAwareRetriever:
    """Retrieves documents with preserved math content for agent reasoning"""
    
    def __init__(self):
        self.math_patterns = {
            'optimization': ['min', 'max', 'argmin', 'argmax', 'gradient', 'loss', 'objective'],
            'probability': ['P(', 'E[', 'Var', 'Cov', 'pdf', 'cdf', 'likelihood'],
            'graph_ml': ['graph', 'node', 'edge', 'G', 'V', 'E', 'adjacency', 'spectral'],
            'deep_learning': ['layer', 'activation', 'loss', 'gradient', 'backpropagation', 'attention'],
            'reinforcement_learning': ['reward', 'policy', 'Q', 'value', 'transition', 'discount'],
            'information_theory': ['entropy', 'KL', 'mutual', 'information', 'rate']
        }
    
    def retrieve_source(self, source_id: str, db_conn=None) -> Optional[SourceDocument]:
        """
        Retrieve a source with ALL formats and math blocks intact
        
        This is the critical path that was broken: the original retrieval
        only got the PDF text (without math), leading to corrupted
        King Wen expansions.
        """
        # In real implementation, query D1 database
        # This is a placeholder showing the expected structure
        
        # Get source metadata
        source = self._get_source_metadata(source_id)
        if not source:
            return None
        
        # Get primary text format (prefer LaTeX if available)
        text_format = self._get_best_text_format(source_id)
        
        # Get ALL math blocks
        math_blocks = self._get_all_math_blocks(source_id)
        
        # Calculate math quality metrics
        math_quality = self._calculate_math_quality(math_blocks, text_format.content)
        
        return SourceDocument(
            source_id=source_id,
            title=source['title'],
            authors=source.get('authors', []),
            year=source.get('year', 0),
            text_content=text_format.content,
            math_blocks=[asdict(m) for m in math_blocks],
            total_math_count=len(math_blocks),
            math_quality=math_quality
        )
    
    def _get_source_metadata(self, source_id: str) -> Optional[Dict]:
        """Get source metadata from database"""
        # TODO: Implement actual DB query
        # SELECT * FROM sources WHERE id = ?
        return {
            'id': source_id,
            'title': 'Sample Paper',
            'authors': ['Author, A.'],
            'year': 2024,
            'source_type': 'arxiv',
            'source_url': f'https://arxiv.org/abs/{source_id}'
        }
    
    def _get_best_text_format(self, source_id: str) -> Dict:
        """Get best available text format (LaTeX preferred)"""
        # TODO: Implement actual DB query
        # Prefer latex_source > latex_compiled > pdf_text > pdf_ocr
        return {
            'format': 'latex_compiled',
            'content': 'Sample content with $\\mathcal{L} = \\sum_{i} \\mathcal{L}_i$ equations'
        }
    
    def _get_all_math_blocks(self, source_id: str) -> List[MathBlock]:
        """Get ALL math blocks - never filter them out"""
        # TODO: Implement actual DB query
        # This is where the bug was: we were filtering out "low quality" math
        # Now we return EVERYTHING and let King Wen collapse properly
        
        return [
            MathBlock(
                block_index=0,
                latex='$\\mathcal{L} = \\sum_{i=1}^{n} \\ell(y_i, \\hat{y}_i)$',
                context_before='The loss function is defined as:',
                context_after='This minimization drives model convergence.',
                classification='equation',
                confidence=0.95,
                symbolic_count=8
            )
        ]
    
    def _calculate_math_quality(self, math_blocks: List[MathBlock], text: str) -> float:
        """Calculate quality metric for math extraction"""
        if not math_blocks:
            return 0.0
        
        avg_confidence = sum(m.confidence for m in math_blocks) / len(math_blocks)
        latex_ratio = sum(len(m.latex) for m in math_blocks) / max(1, len(text))
        
        return min(1.0, (avg_confidence + latex_ratio) / 2)


def query_source_for_kingwen(source_id: str) -> SourceDocument:
    """
    Primary interface for agents querying sources for King Wen collapse
    
    Returns COMPLETE document with math intact - critical for proper expansion
    """
    retriever = MathAwareRetriever()
    return retriever.retrieve_source(source_id)


def prepare_kingwen_input(source_doc: SourceDocument) -> Dict:
    """
    Prepare source document for King Wen full 512-state expansion
    
    The math content feeds directly into the collapse_full_128() function
    as the expansion anchor point for sovereign reasoning.
    """
    return {
        'source_id': source_doc.source_id,
        'title': source_doc.title,
        'text': source_doc.text_content,
        'math_principles': [m['latex'] for m in source_doc.math_blocks],
        'principle_count': source_doc.total_math_count,
        'concepts': extract_concepts(source_doc.text_content),
        'domain': classify_domain(source_doc)
    }


def extract_concepts(text: str) -> List[str]:
    """Extract key concepts from text for agent reasoning"""
    concepts = []
    
    # Simple keyword extraction
    keywords = ['gradient', 'loss', 'attention', 'graph', 'network', 'model', 
                'learning', 'optimization', 'probability', 'distribution']
    
    text_lower = text.lower()
    for kw in keywords:
        if kw in text_lower:
            concepts.append(kw)
    
    return concepts


def classify_domain(source_doc: SourceDocument) -> str:
    """Classify domain from math content patterns"""
    math_text = ' '.join(m.latex for m in source_doc.math_blocks)
    
    for domain, patterns in {
        'optimization': ['min', 'max', 'argmin', 'loss', 'gradient'],
        'graphs': ['graph', 'node', 'edge', 'adjacency', 'spectral'],
        'reinforcement_learning': ['reward', 'policy', 'Q', 'value'],
        'probability': ['P(', 'E[', 'Var', 'Cov', 'pdf']
    }.items():
        if any(p in math_text for p in patterns):
            return domain
    
    return 'general'


# Export for use in other modules
__all__ = ['MathAwareRetriever', 'query_source_for_kingwen', 'prepare_kingwen_input', 
           'SourceDocument', 'MathBlock']