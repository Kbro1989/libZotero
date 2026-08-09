/**
 * Furniture Wiki Link Sources — TypeScript Schema
 * Source: RS3 Wiki Furniture page HTML dump
 * Sovereign Stack — POG2/POG3 ingestor limb
 */

export interface WikiLinkEntry {
  /** Relative or absolute href */
  href: string;
  /** Title attributes collected from all occurrences */
  titles: string[];
  /** Number of times this href appears in the document */
  occurrences: number;
}

export interface WikiLinkCategories {
  /** /w/Article_Name links — primary content graph */
  wiki_articles: WikiLinkEntry[];
  /** /w/File:... links — media assets */
  wiki_files: WikiLinkEntry[];
  /** /w/Special:... links — wiki infrastructure */
  special_pages: WikiLinkEntry[];
  /** /images/... links — raw image assets */
  images: WikiLinkEntry[];
  /** /load.php?... links — ResourceLoader bundles */
  load_php: WikiLinkEntry[];
  /** External http/https/... links */
  external: WikiLinkEntry[];
  /** ?action=... / ?veaction=... query links */
  action_links: WikiLinkEntry[];
  /** Uncategorised */
  other: WikiLinkEntry[];
}

export interface FurnitureWikiLinkSources {
  source: string;
  parsed_at: string;
  statistics: {
    total_raw_links: number;
    unique_hrefs: number;
    category_breakdown: Record<string, number>;
  };
  categories: WikiLinkCategories;
}

/** Resolve a relative wiki href to canonical URL */
export function resolveWikiHref(href: string, base = "https://runescape.wiki"): string {
  if (href.startsWith("http")) return href;
  if (href.startsWith("//")) return `https:${href}`;
  return `${base}${href}`;
}

/** Extract article name from /w/Article_Name href */
export function extractArticleName(href: string): string | null {
  const m = href.match(/^/w/([^#?]+)/);
  return m ? decodeURIComponent(m[1].replace(/_/g, " ")) : null;
}

/** Filter articles by category keyword in title */
export function filterByKeyword(
  entries: WikiLinkEntry[],
  keyword: string
): WikiLinkEntry[] {
  const lower = keyword.toLowerCase();
  return entries.filter((e) =>
    e.titles.some((t) => t.toLowerCase().includes(lower)) ||
    e.href.toLowerCase().includes(lower)
  );
}
