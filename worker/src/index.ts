export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);

    if (url.pathname === '/ai/summarize' && request.method === 'POST') {
      try {
        const { text } = await request.json<{ text: string }>();
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

export interface Env {
  ASSETS: Fetcher;
  AI: Ai;
}
