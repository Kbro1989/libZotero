# Unified DB Math Preservation - New Assets

## Files Created for Math-Aware Ingestion

### 1. Database Schema
**File:** `schema/unified_corpus.sql`
**Purpose:** D1 schema with math block preservation
**Tables:**
- `sources` - Core paper metadata
- `source_formats` - Multiple format variants per source
- `math_blocks` - Structured equation storage
- `source_index` - Full-text and math-aware search
- `hash_verification` - Provenance tracking

### 2. Ingestion Pipeline
**File:** `ingest_with_math.py`
**Purpose:** Re-ingest Zotero corpus with proper math extraction
**Key Features:**
- Preserves LaTeX equations from pdftotext extraction
- Detects math blocks via pattern matching
- Stores multiple format variants
- Maintains hash provenance

### 3. Agent Query Layer
**File:** `agent_math_query.py`
**Purpose:** Ensure agents always receive math content for King Wen collapse
**Key Functions:**
- `query_source_for_kingwen()` - Complete document retrieval
- `prepare_kingwen_input()` - Prep for sovereign expansion
- `MathAwareRetriever` class - Database interface

## Architecture Fix

### The Problem (Already Documented)
```
Zotero PDF → PDFTOTEXT (math lost as flat text) → Agent reads text-only → 
Agent hallucinates math → King Wen expands hallucination → 
729 answers with no coherent paper trace
```

### The Solution (New Files)
```
Zotero PDF → Dual extraction (text + math) → 
Structured storage (text + math_blocks) → 
Agent queries with math intact → 
King Wen collapses actual principles → 
Coherent sovereign expansion
```

## Implementation Steps

### Step 1: Apply Database Schema
```bash
# Local SQLite (for development)
sqlite3 unified_corpus.db < schema/unified_corpus.sql

# D1 in Cloudflare
wrangler d1 execute unified-corpus --local < schema/unified_corpus.sql
```

### Step 2: Run Ingestion Pipeline
```bash
cd zotero/learning-corpus
python ingest_with_math.py --manifest arxiv-manifest.json --batch-size 50
```

### Step 3: Update Agent Queries
Replace existing `consult` calls with:
```python
from agent_math_query import query_source_for_kingwen

# OLD (broken)
result = simple_text_query(source_id)

# NEW (math-aware)  
doc = query_source_for_kingwen(source_id)
kingwen_input = prepare_kingwen_input(doc)
expansion = collapse_full_128(kingwen_input)
```

## Verification Criteria

After implementation, verify:

✅ **Math Preservation**: Sources have `math_blocks` with non-zero count
✅ **Hash Integrity**: SHA-256 includes math content in hash
✅ **Agent Queries**: Return `total_math_count > 0` for math papers  
✅ **King Wen Collapses**: Show actual equation principles, not hallucinated noise
✅ **Sovereign Alignment**: Downstream agent outputs correlate with source math

## Next Actions

1. **Run schema migration** on D1 database
2. **Execute batch ingestion** of 330 PDF+text pairs
3. **Update `/consult` endpoint** to use `agent_math_query.py`
4. **Add test harness** for math detection accuracy
5. **Monitor King Wen outputs** for principled coherence

## Risk Points

⚠️ **pdftotext math detection** - Some LaTeX may be lost in conversion
⚠️ **Manual fallback needed** for complex equations that don't extract cleanly
⚠️ **Agent prompting** must use `prepare_kingwen_input()` format
⚠️ **Hash collision risk** - SHA-256 truncated IDs; monitor for conflicts

## Integration with Existing Work

This ties together:
- **Color-by-numbers imageProcessor.ts** → `ingest_with_math.py` region detection
- **Vision analysis** → Math block classification and confidence
- **King Wen collapse** → Receives actual mathematical principles as anchor
- **Hermes MOA** → Never loses math in the query chain again

The chain is only as strong as its weakest link. We've fixed the ingestion link.