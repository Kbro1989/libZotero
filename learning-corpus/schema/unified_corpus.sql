-- unified_corpus_schema.sql
-- D1 Database Schema for Unified Research Corpus with Math Preservation
-- Version: 2026-08-03
-- Purpose: Store research sources with structured math content for agent reasoning

-- Enable essential extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Sources table: Core metadata for each research paper
CREATE TABLE sources (
    id TEXT PRIMARY KEY,                    -- SHA-256(content_hash) for determinism
    title TEXT NOT NULL,
    authors TEXT[],
    year INTEGER,
    source_type TEXT CHECK (source_type IN ('arxiv', 'zotero', 'html', 'pdf', 'bibtex')),
    source_url TEXT,                        -- Original location
    canonical_url TEXT,                     -- Internet Archive/Stable copy
    added_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    metadata JSONB                          -- Flexible schema for extra fields
);

-- Source formats table: Multiple representations of same source
CREATE TABLE source_formats (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    source_id TEXT REFERENCES sources(id) ON DELETE CASCADE,
    format TEXT NOT NULL CHECK (format IN ('latex_source', 'latex_compiled', 'pdf_text', 'pdf_ocr', 'html', 'markdown', 'json')),
    content TEXT,                           -- Full content in this format
    content_hash TEXT NOT NULL,             -- SHA-256 for deduplication
    math_count INTEGER DEFAULT 0,
    math_quality REAL CHECK (math_quality BETWEEN 0 AND 1),  -- Extraction confidence
    extraction_method TEXT CHECK (extraction_method IN ('pdftotext', 'latexml', 'pix2tex', 'manual', 'native')),
    extracted_at TIMESTAMP DEFAULT NOW(),
    file_size INTEGER,                      -- For PDFs/images
    dpi REAL,                               -- For image-based extracts
    UNIQUE(source_id, format, content_hash)
);

-- Math blocks table: Extracted equations/formulas as structured objects
CREATE TABLE math_blocks (
    id TEXT PRIMARY KEY DEFAULT encode(gen_random_bytes(16), 'hex'),
    source_id TEXT REFERENCES sources(id) ON DELETE CASCADE,
    block_index INTEGER,                    -- Order in document
    latex TEXT,                             -- Latin Modern Math compatible LaTeX
    mathml TEXT,                            -- MathML for rendering
    svg_path TEXT,                          -- Rendered SVG coordinate path (for visualization)
    context_before TEXT,                    -- Text immediately before equation
    context_after TEXT,                     -- Text immediately after equation
    position JSONB,                         -- {page: n, x: m, y: n, width: m, height: n}
    classification TEXT CHECK (classification IN ('equation', 'theorem', 'proof', 'definition', 'lemma', 'corollary', 'figure', 'table', 'algorithm')),
    primary_subject TEXT,                   -- High-level topic: 'optimization', 'graphs', 'probability', etc.
    secondary_subjects TEXT[],              -- Additional subject tags
    tags TEXT[],                            -- Auto-generated tags from content
    complexity_score REAL CHECK (complexity_score BETWEEN 0 AND 1),  -- AI-assessed complexity
    symbolic_count INTEGER,                 -- Number of symbols
    CONSTRAINT valid_latex CHECK (latex IS NULL OR LENGTH(latex) > 0)
);

-- Full-text search and semantic indexing
CREATE TABLE source_index (
    source_id TEXT PRIMARY KEY REFERENCES sources(id) ON DELETE CASCADE,
    text_vector TSVECTOR,                   -- Full-text search
    math_vector TSVECTOR,                   -- Math-aware search (symbols as tokens)
    embedding VECTOR(1536),                 -- OpenAI text-embedding-3-large
    last_indexed TIMESTAMP DEFAULT NOW()
);

-- Hash verification table for provenance tracking
CREATE TABLE hash_verification (
    source_id TEXT REFERENCES sources(id) ON DELETE CASCADE,
    component TEXT CHECK (component IN ('text', 'math', 'figures', 'metadata')),
    original_hash TEXT NOT NULL,            -- SHA-256 of original component
    current_hash TEXT NOT NULL,             -- Current stored component hash
    verified_at TIMESTAMP DEFAULT NOW(),
    is_valid BOOLEAN DEFAULT TRUE,
    PRIMARY KEY (source_id, component)
);

-- Indexes for performance
CREATE INDEX idx_sources_year ON sources(year);
CREATE INDEX idx_sources_url ON sources(source_url);
CREATE INDEX idx_sources_authors ON sources USING GIN(authors);
CREATE INDEX idx_source_formats_format ON source_formats(format);
CREATE INDEX idx_source_formats_math_count ON source_formats(math_count);
CREATE INDEX idx_math_blocks_source ON math_blocks(source_id);
CREATE INDEX idx_math_blocks_classification ON math_blocks(classification);
CREATE INDEX idx_math_blocks_position ON math_blocks USING GIN(position);
CREATE INDEX idx_text_vector ON source_index USING GIN(text_vector);
CREATE INDEX idx_math_vector ON source_index USING GIN(math_vector);

-- Trigger to update timestamps
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_sources_updated_at BEFORE UPDATE ON sources
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();