# RS3 Wiki Topology Explorer

Self-contained interactive dashboard for exploring the RuneScape 3 wiki link topology graph.

## Files

| File | Description |
|------|-------------|
| `index.html` | Full interactive explorer (245 KB). Open in any browser. |
| `topology_data.json` | Raw graph data: 84 source pages, 17,946 unique articles, 42,517 link instances. |

## Run Locally

### Option 1: Direct open
Double-click `index.html`. Works in Chrome, Firefox, Edge, Safari.

### Option 2: Local server (recommended)
```bash
cd /path/to/this/folder
python3 -m http.server 8080
# Then open http://localhost:8080
```

### Option 3: Node
```bash
npx serve .
```

## Features

- **Article List**: Search, filter by category, sort by in-degree or name. Click any article to see which pages link to it.
- **Network Graph**: Force-directed canvas visualization of cross-page links. Drag nodes, zoom with scroll, hover for labels.
- **Category Distribution**: Horizontal bar chart of all 20 article categories.
- **Clickable Wiki Links**: Every article name links directly to `runescape.wiki`.

## Data Source

MediaWiki API (`action=query&prop=links`) against `runescape.wiki`.
84 core pages queried including: Furniture, Construction, Player-owned_house, Money_making_guide, Bestiary, List_of_quests, all 29 skills, all major bosses, PvM abilities, perks, relics, locations, and more.

## Sovereign Stack Integration

The `topology_data.json` can be ingested by:
- `WikiTopologyGraph.ts` — TypeScript schema with `getBacklinks()`, `pageDistance()`, `toPedagogyCorpus()`
- `SovereignFurnitureOntologyLimb.ts` — Construction material graph builder
- `CacheLearningLimb` — Resolve article names to cache item IDs
- `HexagramManager` — Map category hub scores to 512-state oracle indices
