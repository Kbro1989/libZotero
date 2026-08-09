/**
 * Equilibrium League (Leagues II) — Sovereign Data Schema
 * Generated from Jagex official reveals + RuneScape Wiki corpus
 * Compatible with POG2 CacheLearningLimb / Pedagogy ingestion
 */

// ─── Core Enums ───────────────────────────────────────────────────────────────

export type LeagueTheme = 'Order' | 'Balance' | 'Chaos';
export type BlessingPath = 'Order' | 'Balance' | 'Chaos';
export type RegionId = 'misthalin' | 'havenhythe' | 'karamja' | 'anachronia' | 'asgarnia' | 'desert' | 'fremennik' | 'kandarin' | 'morytania' | 'tirannwn' | 'wilderness';
export type SkillName = 'Attack' | 'Strength' | 'Defence' | 'Ranged' | 'Magic' | 'Necromancy' | 'Prayer' | 'Summoning' | 'Melee' | 'Constitution' | 'Mining' | 'Agility' | 'Smithing' | 'Herblore' | 'Fishing' | 'Thieving' | 'Cooking' | 'Crafting' | 'Firemaking' | 'Fletching' | 'Woodcutting' | 'Runecrafting' | 'Slayer' | 'Farming' | 'Construction' | 'Hunter' | 'Dungeoneering' | 'Divination' | 'Invention' | 'Archaeology';
export type TaskDifficulty = 'Easy' | 'Medium' | 'Hard' | 'Elite' | 'Master';
export type TrophyTier = 'Bronze' | 'Iron' | 'Steel' | 'Mithril' | 'Adamant' | 'Rune' | 'Dragon';

// ─── Meta ─────────────────────────────────────────────────────────────────────

export interface LeagueMeta {
  name: string;
  start_date: string; // ISO 8601
  end_date: string;
  theme: string;
  total_tasks: number;
  total_points: number;
  max_regions: number;
}

// ─── XP Multipliers ───────────────────────────────────────────────────────────

export interface XpMultiplierMap {
  tier_1: number;
  tier_2: number;
  tier_3: number;
  tier_4: number;
  tier_5: number;
  tier_6: number;
  tier_7: number;
}

// ─── Relics ───────────────────────────────────────────────────────────────────

export interface RelicChoice {
  id: string;
  name: string;
  skills: SkillName[];
  description: string;
  icon: string; // wiki filename
}

export interface RelicTier {
  tier: number;
  points_required: number;
  choices: RelicChoice[];
  passives: string[];
}

// ─── Blessings ────────────────────────────────────────────────────────────────

export interface BlessingChoice {
  id: string;
  name: string;
  path: BlessingPath;
  description: string;
}

export interface BlessingTier {
  tier: number | string; // "God Tier 1" etc
  name: string;
  tasks_required: number;
  passives: string[];
  choices: BlessingChoice[];
}

// ─── Regions ──────────────────────────────────────────────────────────────────

export interface Region {
  id: RegionId;
  name: string;
  tasks_required: number | null; // null for choice regions
  points: number;
  tasks: number;
  blessing_tasks: number;
  starting: boolean;
  auto_quests: string[];
}

export interface RegionUnlock {
  region: string;
  tasks_required: number;
  type: 'automatic' | 'choice';
}

// ─── Tasks ────────────────────────────────────────────────────────────────────

export interface TaskDifficultyEntry {
  difficulty: TaskDifficulty;
  points_per_task: number | null;
}

// ─── Trophies ─────────────────────────────────────────────────────────────────

export interface Trophy {
  tier: TrophyTier;
  points_required: number;
}

// ─── Special Rules ────────────────────────────────────────────────────────────

export interface SpecialRules {
  ironman: boolean;
  trading_disabled: boolean;
  damage_cap_removed: boolean;
  life_points_cap_removed: boolean;
  shops_infinite_stock: boolean;
  boss_spawns_sped_up: boolean;
  xp_from_quests_multiplied: boolean;
  xp_from_dnds_multiplied: boolean;
  pets_obtainable: boolean;
  pets_persist_between_leagues: boolean;
  reaper_weekly_cap_removed: boolean;
  reaper_hard_cap: number;
  dungeoneering_tokens_multiplied: boolean;
  dungeoneering_xp_from_tokens_disabled: boolean;
  clue_scrolls_respect_regions: boolean;
  slayer_tasks_respect_regions: boolean;
  reaper_tasks_respect_regions: boolean;
  tetracompasses_respect_regions: boolean;
  masterwork_at_any_anvil: boolean;
  construction_workbench_lumbridge: boolean;
  invention_tutorial_auto: boolean;
  necromancy_kili_tasks_skipped: boolean;
  archaeology_qualification_associate: boolean;
  contract_claws_auto: boolean;
  area_tasks_multi_region_auto: boolean;
}

// ─── Root Document ────────────────────────────────────────────────────────────

export interface EquilibriumLeagueDocument {
  meta: LeagueMeta;
  xp_multipliers: XpMultiplierMap;
  relic_tiers: RelicTier[];
  blessing_tiers: BlessingTier[];
  regions: Region[];
  region_unlocks: RegionUnlock[];
  task_difficulties: TaskDifficultyEntry[];
  trophies: Trophy[];
  special_rules: SpecialRules;
}

// ─── Player Build / Theorycraft Types ─────────────────────────────────────────

export interface SelectedRelic {
  tier: number;
  choice_id: string;
}

export interface SelectedBlessing {
  tier: number | string;
  choice_id: string;
  path: BlessingPath;
}

export interface PlayerBuild {
  selected_regions: RegionId[]; // includes starting + karamja + 3 choices
  selected_relics: SelectedRelic[];
  selected_blessings: SelectedBlessing[];
  target_trophy: TrophyTier;
}

export interface BuildAnalysis {
  total_points_available: number;
  total_tasks_available: number;
  blessing_tasks_available: number;
  relics_unlocked: number;
  blessing_tiers_unlocked: number;
  xp_multiplier: number;
  rare_item_multiplier: number;
  combat_style_tags: string[];
  skilling_focus: SkillName[];
  estimated_completion_time_hours: number | null;
}

// ─── Pedagogy / Cache Ingest Types ────────────────────────────────────────────

export interface LeagueEntityPedagogy {
  entity_type: 'relic' | 'blessing' | 'region' | 'task' | 'trophy';
  entity_id: string;
  semantic_name: string;
  description_vector: string; // embedding target
  tags: string[];
  verified: boolean;
  source_urls: string[];
}
