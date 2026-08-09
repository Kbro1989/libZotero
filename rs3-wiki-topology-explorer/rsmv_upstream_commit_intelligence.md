# RSMV Upstream Commit Intelligence — skillbert/rsmv (master)
**Mined:** 2026-08-07 19:37 CDT  
**Range:** Jul 8, 2026 → Aug 6, 2026  
**Total Commits:** 35  
**Head:** `a73a0510dc26e615b1e32fb9063403e0d70d3242`  

## Full Chronological Log

| Date | SHA | Author | Message |
|------|-----|--------|---------|
| 2026-08-06 | `a73a051` | skillbert | add slideshow style cutscene exporter |
| 2026-08-06 | `f7dd87d` | skillbert | add dbrow renderer |
| 2026-08-05 | `cdd3856` | skillbert | fix sqlite wasm imports failing with new webpack version |
| 2026-08-05 | `e2ca22c` | skillbert | update dependencies |
| 2026-08-05 | `9148034` | skillbert | central coordgrid implementation |
| 2026-08-05 | `94f5962` | skillbert | missed rename |
| 2026-08-05 | `0fffe34` | skillbert | rename some props |
| 2026-08-05 | `4bbc851` | skillbert | improve loc typings |
| 2026-08-04 | `58e530e` | skillbert | add source.getObject helper and use it where relevant |
| 2026-08-04 | `ed89125` | skillbert | refactor json decoding files and make file structure more logical |
| 2026-08-04 | `f21d4f8` | skillbert | mapzone testing |
| 2026-08-04 | `0aacf4a` | skillbert | fix npc animations |
| 2026-08-04 | `1a9f47d` | skillbert | further improve json typings and parsing |
| 2026-08-03 | `d8e3f2f` | skillbert | add json type annotations low hanging fruit |
| 2026-08-03 | `d39825a` | skillbert | enum and varbit improvements |
| 2026-08-02 | `97e21c0` | skillbert | rename and move subtypes to vartypes |
| 2026-08-02 | `d626a22` | skillbert | further json typing and displays |
| 2026-08-02 | `d570844` | skillbert | add decoders for mapzones and maplabels (credit to gaz) |
| 2026-08-01 | `29953f0` | skillbert | add maplabel internal names |
| 2026-08-01 | `a5b2433` | skillbert | found the color blending flag on new materials! |
| 2026-08-01 | `ce479f0` | skillbert | improve typed json |
| 2026-07-31 | `3a39692` | skillbert | implement more typed json views |
| 2026-07-31 | `bbf5141` | skillbert | improve json viewer |
| 2026-07-31 | `c0237c6` | skillbert | add known var names to clientscript decompilation (no round-trip support yet) |
| 2026-07-31 | `cb0aa58` | skillbert | update opcodes |
| 2026-07-31 | `f48aaf2` | skillbert | begin working on typed/interactive json displays |
| 2026-07-30 | `688f512` | skillbert | refactor: properly use react contexts for ui/renderer context |
| 2026-07-30 | `e842db0` | skillbert | refactor: finally rename objects to locs |
| 2026-07-29 | `5db0e3d` | skillbert | bzip2 wasm implementation ~3x as fast |
| 2026-07-25 | `6a4eafc` | skillbert | fix dbrows parser |
| 2026-07-15 | `d94e608` | skillbert | add internal names to json dumps and make it searchable |
| 2026-07-15 | `570afbc` | 1bakedpotato | new object opcodes for POH rework |
| 2026-07-14 | `7c198c4` | skillbert | support new item icons with con update |
| 2026-07-10 | `d58e752` | skillbert | show internal filenames in various model viewer modes |
| 2026-07-09 | `a7bd504` | 1bakedpotato | new 949 item opcodes - item ID is now treated as a tribyte rather than a short - added "_old" to field names for opcodes that were duplicated with newer ones that use the new byte length |

---

## Category Breakdown with Sovereign Relevance

### 🔧 OPCODE & CACHE FORMAT (7 commits)
*Relevance: CacheForensicsLimb, versioned opcode rules, TernaryRouter, decoder drift mitigation*

- **`f7dd87d`** — add dbrow renderer
  - Author: Skillbert (skillbert)
  - Date: 2026-08-06
  - URL: https://github.com/skillbert/rsmv/commit/f7dd87dee8b81e16fbc45cce3b25f18e7c086b16

- **`d39825a`** — enum and varbit improvements
  - Author: Skillbert (skillbert)
  - Date: 2026-08-03
  - URL: https://github.com/skillbert/rsmv/commit/d39825a96d4238456bd64896b219abd343bbf230

- **`c0237c6`** — add known var names to clientscript decompilation (no round-trip support yet)
  - Author: Skillbert (skillbert)
  - Date: 2026-07-31
  - URL: https://github.com/skillbert/rsmv/commit/c0237c624c86694e7e7853ee36cdf21d63f53017

- **`cb0aa58`** — update opcodes
  - Author: Skillbert (skillbert)
  - Date: 2026-07-31
  - URL: https://github.com/skillbert/rsmv/commit/cb0aa5809f9e9062eb52a5c9882d29a889026931

- **`6a4eafc`** — fix dbrows parser
  - Author: Skillbert (skillbert)
  - Date: 2026-07-25
  - URL: https://github.com/skillbert/rsmv/commit/6a4eafcbfc8a22d73e4535c84f52019655fb9b70

- **`570afbc`** — new object opcodes for POH rework
  - Author: MrDew (1bakedpotato)
  - Date: 2026-07-15
  - URL: https://github.com/skillbert/rsmv/commit/570afbc8348c799222f8668ba40b1bbeba335ab6

- **`a7bd504`** — new 949 item opcodes - item ID is now treated as a tribyte rather than a short - added "_old" to field names for opcodes that were duplicated with newer ones that use the new byte length
  - Author: MrDew (1bakedpotato)
  - Date: 2026-07-09
  - URL: https://github.com/skillbert/rsmv/commit/a7bd504a3f6371d4489d0c763efa470ea0b42055

### 🎨 RENDERER & VIEWER (7 commits)
*Relevance: RSMV fork temporal modes, AvatarCompositionEngine, PBR materials, model-viewer.ts*

- **`a73a051`** — add slideshow style cutscene exporter
  - Author: Skillbert (skillbert)
  - Date: 2026-08-06
  - URL: https://github.com/skillbert/rsmv/commit/a73a0510dc26e615b1e32fb9063403e0d70d3242

- **`0aacf4a`** — fix npc animations
  - Author: Skillbert (skillbert)
  - Date: 2026-08-04
  - URL: https://github.com/skillbert/rsmv/commit/0aacf4a050c85e5ea3cbbb03c785f145a1b60fb3

- **`a5b2433`** — found the color blending flag on new materials!
  - Author: Skillbert (skillbert)
  - Date: 2026-08-01
  - URL: https://github.com/skillbert/rsmv/commit/a5b2433e58a57efb2ed4faa98d9b42f936ea304a

- **`bbf5141`** — improve json viewer
  - Author: Skillbert (skillbert)
  - Date: 2026-07-31
  - URL: https://github.com/skillbert/rsmv/commit/bbf51415f91f62dbda1bc37f5f1955577f07e16e

- **`688f512`** — refactor: properly use react contexts for ui/renderer context
  - Author: Skillbert (skillbert)
  - Date: 2026-07-30
  - URL: https://github.com/skillbert/rsmv/commit/688f5121b6e635d113a40808c8ead1ff436a27c7

- **`7c198c4`** — support new item icons with con update
  - Author: Skillbert (skillbert)
  - Date: 2026-07-14
  - URL: https://github.com/skillbert/rsmv/commit/7c198c44092ef7133eadb1845b7697b37bc58449

- **`d58e752`** — show internal filenames in various model viewer modes
  - Author: Skillbert (skillbert)
  - Date: 2026-07-10
  - URL: https://github.com/skillbert/rsmv/commit/d58e75273bfeffbc037c7046e4ae2904e06dff61

### 📋 JSON / TYPING / PEDAGOGY (10 commits)
*Relevance: Cache pedagogy corpus, typed cache introspection, internal name resolution*

- **`4bbc851`** — improve loc typings
  - Author: Skillbert (skillbert)
  - Date: 2026-08-05
  - URL: https://github.com/skillbert/rsmv/commit/4bbc851ac6c0c96fa0bbdf9760d7c19cb1d83952

- **`ed89125`** — refactor json decoding files and make file structure more logical
  - Author: Skillbert (skillbert)
  - Date: 2026-08-04
  - URL: https://github.com/skillbert/rsmv/commit/ed891256a6320b37c98af7b63e3ce3cf4a020ffb

- **`1a9f47d`** — further improve json typings and parsing
  - Author: Skillbert (skillbert)
  - Date: 2026-08-04
  - URL: https://github.com/skillbert/rsmv/commit/1a9f47dbea3bd28d9fc3f9612bbd040f8cead2e1

- **`d8e3f2f`** — add json type annotations low hanging fruit
  - Author: Skillbert (skillbert)
  - Date: 2026-08-03
  - URL: https://github.com/skillbert/rsmv/commit/d8e3f2fe379e8e7891c7413bb9da94a2a12ffdf4

- **`97e21c0`** — rename and move subtypes to vartypes
  - Author: Skillbert (skillbert)
  - Date: 2026-08-02
  - URL: https://github.com/skillbert/rsmv/commit/97e21c0d87ef1f7977042448d86f29fbed8c60bd

- **`d626a22`** — further json typing and displays
  - Author: Skillbert (skillbert)
  - Date: 2026-08-02
  - URL: https://github.com/skillbert/rsmv/commit/d626a22a2afbbd707cee0a0ee32c2a99a78b8126

- **`ce479f0`** — improve typed json
  - Author: Skillbert (skillbert)
  - Date: 2026-08-01
  - URL: https://github.com/skillbert/rsmv/commit/ce479f028587fa564e9d68d9d2d1acb9ddfd12a4

- **`3a39692`** — implement more typed json views
  - Author: Skillbert (skillbert)
  - Date: 2026-07-31
  - URL: https://github.com/skillbert/rsmv/commit/3a396922df4da1a75bf21c7782bc6da5abee08ed

- **`f48aaf2`** — begin working on typed/interactive json displays
  - Author: Skillbert (skillbert)
  - Date: 2026-07-31
  - URL: https://github.com/skillbert/rsmv/commit/f48aaf293e369dfff3922da38f4b621e11484332

- **`d94e608`** — add internal names to json dumps and make it searchable
  - Author: Skillbert (skillbert)
  - Date: 2026-07-15
  - URL: https://github.com/skillbert/rsmv/commit/d94e6089285340f066925cc6692431259ef2ef42

### 🏗️ INFRASTRUCTURE & BUILD (4 commits)
*Relevance: Ghost Limb WASM stack, coordgrid alignment, dependency hygiene*

- **`cdd3856`** — fix sqlite wasm imports failing with new webpack version
  - Author: Skillbert (skillbert)
  - Date: 2026-08-05
  - URL: https://github.com/skillbert/rsmv/commit/cdd38569fb9b0ae3c2b7f77c6f95c96fcfb3a3a4

- **`e2ca22c`** — update dependencies
  - Author: Skillbert (skillbert)
  - Date: 2026-08-05
  - URL: https://github.com/skillbert/rsmv/commit/e2ca22c9fd2a6c23b16f1ec5ec376e478d30d112

- **`9148034`** — central coordgrid implementation
  - Author: Skillbert (skillbert)
  - Date: 2026-08-05
  - URL: https://github.com/skillbert/rsmv/commit/9148034302f1799eff679b21215ccbb0413d8d2d

- **`5db0e3d`** — bzip2 wasm implementation ~3x as fast
  - Author: Skillbert (skillbert)
  - Date: 2026-07-29
  - URL: https://github.com/skillbert/rsmv/commit/5db0e3d5df00c9e8b0efa103aaa2ad8c37f2d5eb

### 🔄 REFACTOR / RENAME (3 commits)
*Relevance: API surface changes — 'objects→locs' rename affects POG2 spatial substrate*

- **`94f5962`** — missed rename
  - Author: Skillbert (skillbert)
  - Date: 2026-08-05
  - URL: https://github.com/skillbert/rsmv/commit/94f596285d833a085073d1921a46870c7afa1221

- **`0fffe34`** — rename some props
  - Author: Skillbert (skillbert)
  - Date: 2026-08-05
  - URL: https://github.com/skillbert/rsmv/commit/0fffe3402c5b2786b620ff081484ae1c47889331

- **`e842db0`** — refactor: finally rename objects to locs
  - Author: Skillbert (skillbert)
  - Date: 2026-07-30
  - URL: https://github.com/skillbert/rsmv/commit/e842db0caf6d9984e0f89b79e04ca78caae591f3

### 🗺️ SPATIAL / MAP (4 commits)
*Relevance: Havenhythe collision bake, mapzone decoding, SovereignCollisionEngine*

- **`58e530e`** — add source.getObject helper and use it where relevant
  - Author: Skillbert (skillbert)
  - Date: 2026-08-04
  - URL: https://github.com/skillbert/rsmv/commit/58e530e6538d675eacfab15a12df345d7bf05182

- **`f21d4f8`** — mapzone testing
  - Author: Skillbert (skillbert)
  - Date: 2026-08-04
  - URL: https://github.com/skillbert/rsmv/commit/f21d4f8d952d3d2d80d13ebe44fe8b6f0a6514b6

- **`d570844`** — add decoders for mapzones and maplabels (credit to gaz)
  - Author: Skillbert (skillbert)
  - Date: 2026-08-02
  - URL: https://github.com/skillbert/rsmv/commit/d57084469b16d363d9223614fee68a75d430ecba

- **`29953f0`** — add maplabel internal names
  - Author: Skillbert (skillbert)
  - Date: 2026-08-01
  - URL: https://github.com/skillbert/rsmv/commit/29953f05ffe4553810995084056463ef769d71ee

---

## High-Priority Integration Targets for POG2

1. **`a7bd504` — new 949 item opcodes (tribyte item IDs)**
   - *Action:* Update CacheForensicsLimb item decoder. Old short→new tribyte. `_old` suffix pattern for duplicated opcodes.

2. **`570afbc` — new object opcodes for POH rework**
   - *Action:* Sync loc/object decoder with new POH opcodes.

3. **`9148034` — central coordgrid implementation**
   - *Action:* Evaluate against POG2 SovereignCollisionEngine coordgrid. Potential unification or divergence audit.

4. **`a5b2433` — color blending flag on new materials**
   - *Action:* PBR pipeline update. First photon / draconic point-cloud material system may need flag support.

5. **`e842db0` — rename objects to locs**
   - *Action:* Breaking API change. POG2 uses 'objects' in spatial substrate. Migrate to 'locs' nomenclature or maintain alias layer.

6. **`d570844` / `29953f0` — mapzone + maplabel decoders**
   - *Action:* Spatial substrate enrichment. Maplabels feed into SovereignEye / Edge Radar.

7. **`5db0e3d` — bzip2 wasm ~3x faster**
   - *Action:* Ghost Limb cache decompression performance. Evaluate for R2 asset streaming.

8. **`cdd3856` — sqlite wasm imports fix (webpack)**
   - *Action:* If POG2 uses sqlite WASM for cache indexing, apply same import fix.
