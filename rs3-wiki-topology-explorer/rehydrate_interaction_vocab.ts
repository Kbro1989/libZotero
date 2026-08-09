import { createRequire } from 'module';
const require = createRequire(import.meta.url);

const { GameCacheLoader } = require("/c/Users/krist/Desktop/rsmv/src/cache/sqlite.js");
const { parse } = require("/c/Users/krist/Desktop/rsmv/src/opdecoder.js");
const { cacheMajors, cacheConfigPages } = require("/c/Users/krist/Desktop/rsmv/src/constants.js");
import * as fs from 'fs';
import * as path from 'path';

(global as any).__non_webpack_require__ = require;

const CACHE_DIR = "C:\\ProgramData\\Jagex\\RuneScape";
const OUTPUT_DIR = "C:\\Users\\krist\\Desktop\\zotero\\rs3-wiki-topology-explorer";

interface ActionEntry {
    action: string;
    entityId: number;
    entityType: 'item' | 'npc' | 'object';
    entityName: string;
    slot: number;
    isMembers: boolean;
}

async function extractAllActions() {
    console.log("🔍 Loading cache from:", CACHE_DIR);
    const cache = new GameCacheLoader(CACHE_DIR);
    (cache as any).buildnr = 940; // current build
    
    const allActions: ActionEntry[] = [];
    const actionFreq: Map<string, number> = new Map();
    
    // ── Extract ITEM actions (ground + widget) ──
    console.log("\n📦 Extracting ITEM actions (Major 19)...");
    try {
        const itemIndex = await cache.getCacheIndex(cacheMajors.items);
        console.log(`  Found ${itemIndex.length} item archives`);
        
        let itemCount = 0;
        for (const entry of itemIndex) {
            if (!entry) continue;
            try {
                const archive = await cache.getArchiveById(cacheMajors.items, entry.minor);
                for (const file of archive) {
                    try {
                        const item = parse.item.read(file.buffer, cache) as any;
                        if (!item.name) continue;
                        
                        const isMembers = item.members === true;
                        
                        // Ground actions (0x1E-0x22)
                        for (let slot = 0; slot < 5; slot++) {
                            const action = item[`ground_actions_${slot}`];
                            if (action && typeof action === 'string' && action.trim()) {
                                allActions.push({
                                    action: action.trim(),
                                    entityId: file.fileid,
                                    entityType: 'item',
                                    entityName: item.name,
                                    slot,
                                    isMembers
                                });
                                actionFreq.set(action.trim(), (actionFreq.get(action.trim()) || 0) + 1);
                            }
                        }
                        
                        // Widget actions (0x23-0x27)
                        for (let slot = 0; slot < 5; slot++) {
                            const action = item[`widget_actions_${slot}`];
                            if (action && typeof action === 'string' && action.trim()) {
                                allActions.push({
                                    action: action.trim(),
                                    entityId: file.fileid,
                                    entityType: 'item',
                                    entityName: item.name,
                                    slot: slot + 5, // offset for widget
                                    isMembers
                                });
                                actionFreq.set(action.trim(), (actionFreq.get(action.trim()) || 0) + 1);
                            }
                        }
                        
                        itemCount++;
                    } catch (_) {}
                }
            } catch (_) {}
        }
        console.log(`  ✅ Processed ${itemCount} items`);
    } catch (e) {
        console.error("  ❌ Item extraction failed:", e);
    }
    
    // ── Extract NPC actions ──
    console.log("\n👤 Extracting NPC actions (Major 18)...");
    try {
        const npcIndex = await cache.getCacheIndex(cacheMajors.npcs);
        console.log(`  Found ${npcIndex.length} NPC archives`);
        
        let npcCount = 0;
        for (const entry of npcIndex) {
            if (!entry) continue;
            try {
                const archive = await cache.getArchiveById(cacheMajors.npcs, entry.minor);
                for (const file of archive) {
                    try {
                        const npc = parse.npc.read(file.buffer, cache) as any;
                        if (!npc.name) continue;
                        
                        // Standard actions (0x1E-0x22)
                        for (let slot = 0; slot < 5; slot++) {
                            const action = npc[`actions_${slot}`];
                            if (action && typeof action === 'string' && action.trim()) {
                                allActions.push({
                                    action: action.trim(),
                                    entityId: file.fileid,
                                    entityType: 'npc',
                                    entityName: npc.name,
                                    slot,
                                    isMembers: false // NPC membership determined elsewhere
                                });
                                actionFreq.set(action.trim(), (actionFreq.get(action.trim()) || 0) + 1);
                            }
                        }
                        
                        // Members actions (0x96-0x9A)
                        for (let slot = 0; slot < 5; slot++) {
                            const action = npc[`members_actions_${slot}`];
                            if (action && typeof action === 'string' && action.trim()) {
                                allActions.push({
                                    action: action.trim(),
                                    entityId: file.fileid,
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
        console.log(`  ✅ Processed ${npcCount} NPCs`);
    } catch (e) {
        console.error("  ❌ NPC extraction failed:", e);
    }
    
    // ── Extract OBJECT actions ──
    console.log("\n🏗️ Extracting OBJECT actions (Major 17)...");
    try {
        const objIndex = await cache.getCacheIndex(cacheMajors.objects);
        console.log(`  Found ${objIndex.length} object archives`);
        
        let objCount = 0;
        for (const entry of objIndex) {
            if (!entry) continue;
            try {
                const archive = await cache.getArchiveById(cacheMajors.objects, entry.minor);
                for (const file of archive) {
                    try {
                        const obj = parse.object.read(file.buffer, cache) as any;
                        if (!obj.name) continue;
                        
                        const isMembers = obj.isMembers === true || obj.is_members === true;
                        
                        // Standard actions (0x1E-0x22)
                        for (let slot = 0; slot < 5; slot++) {
                            const action = obj[`actions_${slot}`];
                            if (action && typeof action === 'string' && action.trim()) {
                                allActions.push({
                                    action: action.trim(),
                                    entityId: file.fileid,
                                    entityType: 'object',
                                    entityName: obj.name,
                                    slot,
                                    isMembers
                                });
                                actionFreq.set(action.trim(), (actionFreq.get(action.trim()) || 0) + 1);
                            }
                        }
                        
                        // Members actions (0x96-0x9A)
                        for (let slot = 1; slot <= 5; slot++) {
                            const action = obj[`members_action_${slot}`];
                            if (action && typeof action === 'string' && action.trim()) {
                                allActions.push({
                                    action: action.trim(),
                                    entityId: file.fileid,
                                    entityType: 'object',
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
        console.log(`  ✅ Processed ${objCount} objects`);
    } catch (e) {
        console.error("  ❌ Object extraction failed:", e);
    }
    
    // ── Build frequency map ──
    console.log("\n📊 Building frequency map...");
    const freqArray: [string, number][] = Array.from(actionFreq.entries())
        .sort((a, b) => b[1] - a[1]);
    
    // ── Output ──
    const output = {
        meta: {
            timestamp: new Date().toISOString(),
            source: "RS3 Live Cache (build 940)",
            totals: {
                uniqueActions: freqArray.length,
                totalActionInstances: allActions.length,
                items: 0,
                npcs: 0,
                objects: 0
            }
        },
        actions: freqArray,
        byEntity: allActions
    };
    
    // Count by entity type
    for (const a of allActions) {
        if (a.entityType === 'item') output.meta.totals.items++;
        else if (a.entityType === 'npc') output.meta.totals.npcs++;
        else if (a.entityType === 'object') output.meta.totals.objects++;
    }
    
    const outPath = path.join(OUTPUT_DIR, "interaction_vocabulary_v2.json");
    fs.writeFileSync(outPath, JSON.stringify(output, null, 2));
    console.log(`\n✅ Wrote ${outPath}`);
    console.log(`   Unique actions: ${freqArray.length}`);
    console.log(`   Total instances: ${allActions.length}`);
    console.log(`   Items: ${output.meta.totals.items}, NPCs: ${output.meta.totals.npcs}, Objects: ${output.meta.totals.objects}`);
    
    // Also write the compact array format for compatibility
    const compactPath = path.join(OUTPUT_DIR, "interaction_vocabulary_compact.json");
    fs.writeFileSync(compactPath, JSON.stringify(freqArray, null, 2));
    console.log(`✅ Wrote ${compactPath}`);
    
    cache.close();
}

extractAllActions().catch(e => {
    console.error("❌ Fatal:", e);
    process.exit(1);
});