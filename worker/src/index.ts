export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);

    if (url.pathname === '/ai/index' && request.method === 'POST') {
      try {
        const body = (await request.json()) as IndexRequest;
        const text = typeof body.text === 'string' ? body.text.slice(0, 12000) : '';
        const images = Array.isArray(body.images) ? body.images.slice(0, 8) : [];

        if (!text && images.length === 0) {
          return json({ error: 'text or images is required' }, 400);
        }

        const pages: IndexedPage[] = [];
        for (const image of images) {
          const bytes = await readImage(image);
          const visionResponse = await env.AI.run(VISION_MODEL, {
            prompt: [
              'Read this academic paper page or figure for indexing.',
              'Transcribe visible text and formal math exactly where possible.',
              'Describe diagrams, charts, axes, legends, tables, symbols, and relationships.',
              'Return concise plain text with these headings: TEXT, MATH, FIGURE.',
            ].join('\n'),
            image: Array.from(bytes),
            max_tokens: 1200,
            temperature: 0.1,
          });

          pages.push({
            page: image.page,
            source: image.url ? 'url' : 'upload',
            extraction: visionResponse.response ?? '',
          });
        }

        const visualText = pages
          .map((page) => `[Page ${page.page ?? 'unknown'}]\n${page.extraction}`)
          .join('\n\n');
        const indexText = [text && `TEXT\n${text}`, visualText && `VISUAL\n${visualText}`]
          .filter(Boolean)
          .join('\n\n');

        return json({
          model: VISION_MODEL,
          indexText,
          searchText: indexText,
          pages,
        });
      } catch (err) {
        return json({ error: String(err) }, 500);
      }
    }

    if (url.pathname === '/ai/summarize' && request.method === 'POST') {
      try {
        const { text } = (await request.json()) as { text: string };
        if (!text || text.length === 0) {
          return new Response(JSON.stringify({ error: 'text is required' }), {
            status: 400,
            headers: { 'content-type': 'application/json' },
          });
        }

        const prompt = `Summarize the following academic text concisely:\n\n${text.slice(0, 4000)}`;
        const models = ['@cf/meta/llama-3-8b-instruct', '@cf/mistral/mistral-7b-instruct-v0.1', '@cf/google/gemma-7b-it'];
        let lastError: unknown;
        for (const model of models) {
          try {
            const aiResponse = await env.AI.run(model, {
              prompt,
              max_tokens: 512,
              temperature: 0.2,
            });
            return new Response(JSON.stringify({ summary: aiResponse.response, model }), {
              headers: { 'content-type': 'application/json' },
            });
          } catch (err) {
            lastError = err;
          }
        }

        return new Response(JSON.stringify({ error: `AI models unavailable: ${String(lastError)}` }), {
          status: 502,
          headers: { 'content-type': 'application/json' },
        });
      } catch (err) {
        return new Response(JSON.stringify({ error: String(err) }), {
          status: 500,
          headers: { 'content-type': 'application/json' },
        });
      }
    }

    const assetPath = url.pathname === '/' ? '/index.html' : url.pathname;
    const assetRequest = new Request(`${url.origin}${assetPath}`, request);
    const asset = await env.ASSETS.fetch(assetRequest);
    if (asset.status !== 404) {
      return asset;
    }

    const fallbackRequest = new Request(`${url.origin}/index.html`, request);
    const index = await env.ASSETS.fetch(fallbackRequest);
    return new Response(index.body, {
      status: 200,
      headers: { 'content-type': 'text/html' },
    });
  },
};

const VISION_MODEL = '@cf/meta/llama-3.2-11b-vision-instruct';

type IndexImage = {
  data?: string;
  url?: string;
  page?: number;
};

type IndexRequest = {
  text?: string;
  images?: IndexImage[];
};

type IndexedPage = {
  page?: number;
  source: 'url' | 'upload';
  extraction: string;
};

async function readImage(image: IndexImage): Promise<Uint8Array> {
  if (image.url) {
    const parsedUrl = new URL(image.url);
    if (parsedUrl.protocol !== 'http:' && parsedUrl.protocol !== 'https:') {
      throw new Error('image url must use http or https');
    }

    const response = await fetch(parsedUrl);
    if (!response.ok) {
      throw new Error(`image fetch failed with status ${response.status}`);
    }
    const bytes = new Uint8Array(await response.arrayBuffer());
    if (bytes.byteLength > 6 * 1024 * 1024) {
      throw new Error('image is larger than 6 MB');
    }
    return bytes;
  }

  if (image.data?.startsWith('data:')) {
    const comma = image.data.indexOf(',');
    if (comma < 0) {
      throw new Error('invalid image data URL');
    }
    const encoded = image.data.slice(comma + 1);
    const binary = atob(encoded);
    if (binary.length > 6 * 1024 * 1024) {
      throw new Error('image is larger than 6 MB');
    }
    return Uint8Array.from(binary, (character) => character.charCodeAt(0));
  }

  throw new Error('each image needs a data URL or http(s) url');
}

function json(value: unknown, status = 200): Response {
  return new Response(JSON.stringify(value), {
    status,
    headers: { 'content-type': 'application/json' },
  });
}

export interface Env {
  ASSETS: Fetcher;
  AI: Ai;
}
