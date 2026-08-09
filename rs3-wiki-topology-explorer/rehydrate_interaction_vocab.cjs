// Use the POG2 dist which has rsmv bundled (with upstream DBRows fix)
const POG2_DIST = '/c/Users/krist/.gemini/antigravity/scratch/pog2/dist';
const { EngineCache } = require(POG2_DIST + '/3d/modeltothree.js');
const { GameCacheLoader } = require(POG2_DIST + '/cache/sqlite.js');
const { cacheMajors, cacheConfigPages } = require(POG2_DIST + '/constants.js');
const { parse } = require(POG2_DIST + '/opdecoder.js');

const fs = require('fs');
const path = require('path');

const CACHE_DIR = "C:\\ProgramData\\Jagex\\RuneScape";
const OUTPUT_DIR = "C:\\Users\\krist\\Desktop\\zotero\\rs3-wiki-topology-explorer";

async function extractAllActions() {
    console.log("Loading cache from:", CACHE_DIR);
    const cache = new GameCacheLoader(CACHE_DIR);
    cache.buildnr = 940;
    
    const allActions = [];
    const actionFreq = new Map();
    const entityMeta = new Map();
    
    // ── Extract ITEM actions (ground + widget) ──
    console.log("\nExtracting ITEM actions (Major 19)...");
    try {
        const itemIndex = await cache.getCacheIndex(cacheMajors.items);
        console.log("  Found " + itemIndex.length + " item archives");
        
        let itemCount = 0;
        for (const entry of itemIndex) {
            if (!entry) continue;
            try {
                const archive = await cache.getArchiveById(cacheMajors.items, entry.minor);
                for (const file of archive) {
                    try {
                        const item = parse.item.read(file.buffer, cache);
                        if (!item.name) continue;
                        
                        const isMembers = item.members === true;
                        const eid = file.fileid;
                        entityMeta.set(eid, {name: item.name, type: 'item', isMembers: isMembers});
                        
                        // Ground actions (0x1E-0x22)
                        for (let slot = 0; slot < 5; slot++) {
                            const action = item['ground_actions_' + slot];
                            if (action && typeof action === 'string' && action.trim()) {
                                allActions.push({
                                    action: action.trim(),
                                    entityId: eid,
                                    entityType: 'item',
                                    entityName: item.name,
                                    slot: slot,
                                    isMembers: isMembers
                                });
                                actionFreq.set(action.trim(), (actionFreq.get(action.trim()) || 0) + 1);
                            }
                        }
                        
                        // Widget actions (0x23-0x27)
                        for (let slot = 0; slot < 5; slot++) {
                            const action = item['widget_actions_' + slot];
                            if (action && typeof action === 'string' && action.trim()) {
                                allActions.push({
                                    action: action.trim(),
                                    entityId: eid,
                                    entityType: 'item',
                                    entityName: item.name,
                                    slot: slot + 5,
                                    isMembers: isMembers
                                });
                                actionFreq.set(action.trim(), (actionFreq.get(action.trim()) || 0) + 1);
                            }
                        }
                        
                        itemCount++;
                    } catch (_) {}
                }
            } catch (_) {}
        }
        console.log("  Processed " + itemCount + " items");
    } catch (e) {
        console.error("  Item extraction failed:", e);
    }
    
    // ── Extract NPC actions ──
    console.log("\nExtracting NPC actions (Major 18)...");
    try {
        const npcIndex = await cache.getCacheIndex(cacheMajors.npcs);
        console.log("  Found " + npcIndex.length + " NPC archives");
        
        let npcCount = 0;
        for (const entry of npcIndex) {
            if (!entry) continue;
            try {
                const archive = await cache.getArchiveById(cacheMajors.npcs, entry.minor);
                for (const file of archive) {
                    try {
                        const npc = parse.npc.read(file.buffer, cache);
                        if (!npc.name) continue;
                        
                        const eid = file.fileid;
                        entityMeta.set(eid, {name: npc.name, type: 'npc', isMembers: false});
                        
                        // Standard actions (0x1E-0x22)
                        for (let slot = 0; slot < 5; slot++) {
                            const action = npc['actions_' + slot];
                            if (action && typeof action === 'string' && action.trim()) {
                                allActions.push({
                                    action: action.trim(),
                                    entityId: eid,
                                    entityType: 'npc',
                                    entityName: npc.name,
                                    slot: slot,
                                    isMembers: false
                                });
                                actionFreq.set(action.trim(), (actionFreq.get(action.trim()) || 0) + 1);
                            }
                        }
                        
                        // Members actions (0x96-0x9A)
                        for (let slot = 0; slot < 5; slot++) {
                            const action = npc['members_actions_' + slot];
                            if (action && typeof action === 'string' && action.trim()) {
                                allActions.push({
                                    action: action.trim(),
                                    entityId: eid,
                                    entityType: 'npc',
                                    entityName: npc.name,
                                    slot: slot + 5,
                                    isMembers: true
                                });
                                actionFreq.set(action.trim(), (actionFreq.get(action.trim()) || 0) + 1);
                            }
                        }
                        
                        npcCount++;
                    } catch (_) {}
                }
            } catch (_) {}
        }
        console.log("  Processed " + npcCount + " NPCs");
    } catch (e) {
        console.error("  NPC extraction failed:", e);
    }
    
    // ── Extract LOC actions ──
    console.log("\nExtracting LOC actions (Major 17)...");
    try {
        const objIndex = await cache.getCacheIndex(cacheMajors.objects);
        console.log("  Found " + objIndex.length + " loc archives");
        
        let objCount = 0;
        for (const entry of objIndex) {
            if (!entry) continue;
            try {
                const archive = await cache.getArchiveById(cacheMajors.objects, entry.minor);
                for (const file of archive) {
                    try {
                        const obj = parse.object.read(file.buffer, cache);
                        if (!obj.name) continue;
                        
                        const isMembers = obj.isMembers === true || obj.is_members === true;
                        const eid = file.fileid;
                        entityMeta.set(eid, {name: obj.name, type: 'loc', isMembers: isMembers});
                        
                        // Standard actions (0x1E-0x22)
                        for (let slot = 0; slot < 5; slot++) {
                            const action = obj['actions_' + slot];
                            if (action && typeof action === 'string' && action.trim()) {
                                allActions.push({
                                    action: action.trim(),
                                    entityId: eid,
                                    entityType: 'loc',
                                    entityName: obj.name,
                                    slot: slot,
                                    isMembers: isMembers
                                });
                                actionFreq.set(action.trim(), (actionFreq.get(action.trim()) || 0) + 1);
                            }
                        }
                        
                        // Members actions (0x96-0x9A)
                        for (let slot = 1; slot <= 5; slot++) {
                            const action = obj['members_action_' + slot];
                            if (action && typeof action === 'string' && action.trim()) {
                                allActions.push({
                                    action: action.trim(),
                                    entityId: eid,
                                    entityType: 'loc',
                                    entityName: obj.name,
                                    slot: slot + 4,
                                    isMembers: true
                                });
                                actionFreq.set(action.trim(), (actionFreq.get(action.trim()) || 0) + 1);
                            }
                        }
                        
                        objCount++;
                    } catch (_) {}
                }
            } catch (_) {}
        }
        console.log("  Processed " + objCount + " locs");
    } catch (e) {
        console.error("  Loc extraction failed:", e);
    }
    
    // ── Build frequency map ──
    console.log("\nBuilding frequency map...");
    const freqArray = Array.from(actionFreq.entries())
        .sort(function(a, b) { return b[1] - a[1]; });
    
    // ── Build entity lookup ──
    const entityLookup = {};
    for (const [eid, meta] of entityMeta.entries()) {
        entityLookup[eid] = meta;
    }
    
    // ── Output ──
    const outputData = {
        meta: {
            timestamp: new Date().toISOString(),
            source: "RS3 Live Cache (build 940) + upstream DBRows fix",
            upstream_commits: ["6a4eafc", "a7bd504", "e842db0", "d570844", "9148034"],
            totals: {
                uniqueActions: freqArray.length,
                totalActionInstances: allActions.length,
                items: 0,
                npcs: 0,
                locs: 0
            }
        },
        actions: freqArray,
        byEntity: allActions,
        entityLookup: entityLookup
    };
    
    for (const a of allActions) {
        if (a.entityType === 'item') outputData.meta.totals.items++;
        else if (a.entityType === 'npc') outputData.meta.totals.npcs++;
        else if (a.entityType === 'loc') outputData.meta.totals.locs++;
    }
    
    const outPath = path.join(OUTPUT_DIR, "interaction_vocabulary_v2.json");
    fs.writeFileSync(outPath, JSON.stringify(outputData, null, 2));
    console.log("\nWrote " + outPath);
    console.log("   Unique actions: " + freqArray.length);
    console.log("   Total instances: " + allActions.length);
    console.log("   Items: " + outputData.meta.totals.items + ", NPCs: " + outputData.meta.totals.npcs + ", Locs: " + outputData.meta.totals.locs);
    
    const compactPath = path.join(OUTPUT_DIR, "interaction_vocabulary_compact.json");
    fs.writeFileSync(compactPath, JSON.stringify(freqArray, null, 2));
    console.log("Wrote " + compactPath);
    
    cache.close();
}

extractAllActions().catch(function(e) {
    console.error("Fatal:", e);
    process.exit(1);
});