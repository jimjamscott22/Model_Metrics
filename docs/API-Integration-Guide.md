# Wiring the LLM Benchmark Dashboard to a Live API

This guide explains exactly how to swap the built-in snapshot data for live data
from your own backend. No build step is required — the dashboard is a single
HTML file with an inline logic class.

---

## 1. What the dashboard already does

The logic class already contains all the wiring. You only need to:

1. Set one URL constant.
2. Make sure your API returns data in the expected shape.

On page load, if a URL is configured, the dashboard fetches it, shows a
**Loading…** badge, and on success swaps in the live data and flips the badge to
**Live**. If the fetch fails it falls back to the bundled snapshot and shows
**Snapshot (API unreachable)**.

Look for this block near the top of the `<script>` logic:

```js
// ---- API wiring ----------------------------------------------------------
const BENCHMARK_API_URL = ''; // e.g. 'https://api.yourapp.com/v1/benchmarks/latest'
```

---

## 2. Step one: point it at your endpoint

Change the empty string to your endpoint URL:

```js
const BENCHMARK_API_URL = 'https://api.yourapp.com/v1/benchmarks/latest';
```

That's the only required change. Everything else (tabs, sorting, bars,
tooltips, the detail panel, the legend, the "last updated" date) reacts
automatically to whatever data comes back.

---

## 3. Step two: match the response shape

Your endpoint must return a **JSON array** of model objects. Each object should
have these fields:

| Field      | Type    | Meaning                                             | Example              |
|------------|---------|-----------------------------------------------------|----------------------|
| `id`       | string  | Unique, stable identifier                            | `"opus48"`           |
| `name`     | string  | Display name                                         | `"Claude Opus 4.8"`  |
| `lab`      | string  | Provider / lab name (drives the legend grouping)    | `"Anthropic"`        |
| `open`     | boolean | `true` for open-weight models (shows an "open" tag) | `false`              |
| `hue`      | number  | Color hue, 0–360 — sets the model's bar/dot color   | `35`                 |
| `released` | string  | Release label shown in the detail panel             | `"May 2026"`         |
| `overall`  | number  | Overall score (Arena Elo in the current design)     | `1541`               |
| `coding`   | number  | Coding score, e.g. SWE-bench Verified %             | `93.8`               |
| `reasoning`| number  | Reasoning & logic score (MATH/GPQA composite), %    | `93.5`               |
| `vision`   | number  | Vision & multimodal score (MMMU/VQAv2 composite), % | `90.5`               |
| `longctx`  | number  | Long-context & agentic composite (0–100)            | `91`                 |
| `context`  | number  | Maximum supported context window size in tokens     | `1000000`            |
| `cost`     | number  | Blended cost, $ per 1M tokens                        | `12.0`               |
| `speed`    | number  | Output speed, tokens/sec                             | `78`                 |

### Minimal example response

```json
[
  {
    "id": "opus48",
    "name": "Claude Opus 4.8",
    "lab": "Anthropic",
    "open": false,
    "hue": 35,
    "released": "May 2026",
    "overall": 1541,
    "coding": 93.8,
    "longctx": 91,
    "reasoning": 93.5,
    "vision": 90.5,
    "context": 1000000,
    "cost": 12.0,
    "speed": 78
  },
  {
    "id": "gpt55",
    "name": "GPT-5.5",
    "lab": "OpenAI",
    "open": false,
    "hue": 150,
    "released": "Apr 2026",
    "overall": 1522,
    "coding": 90.4,
    "longctx": 88,
    "reasoning": 92.8,
    "vision": 91.0,
    "context": 1000000,
    "cost": 8.5,
    "speed": 95
  }
]
```

### Notes on fields

- **`hue`** is the only "styling" field. It's an OKLCH hue (0–360); the
  dashboard renders the color as `oklch(0.62 0.17 <hue>)` so every model stays
  the same lightness/saturation and only the hue varies. Space your labs' hues
  apart (e.g. 30–40° gaps) so colors stay distinguishable.
- **`open`** only controls the small "open" label in the Labs legend.
- Numeric fields are used directly for sorting and bar lengths. If a model is
  missing a metric, the row will still render but that value shows blank/`NaN`;
  prefer sending `0` or omitting the model if you don't have a score.
- **`id`** must be unique — it's used as the React key and for hover tracking.

---

## 4. How "last updated" works

On a successful fetch, the badge date is set to **today** automatically:

```js
lastUpdated: new Date().toLocaleDateString('en-US',
  { month: 'short', day: 'numeric', year: 'numeric' })
```

If you'd rather show the timestamp of when your data was actually scraped (not
when the page loaded), return a wrapper object and read it. For example, change
your API to return:

```json
{ "updatedAt": "2026-07-03", "models": [ ... ] }
```

Then adjust the fetch helper and the `.then(...)` in `componentDidMount`:

```js
async function fetchModelsFromApi(url) {
  const res = await fetch(url, { headers: { Accept: 'application/json' } });
  if (!res.ok) throw new Error('Benchmark API returned ' + res.status);
  const data = await res.json();
  const models = Array.isArray(data) ? data : data.models;
  if (!models || !models.length) throw new Error('Benchmark API returned no models');
  return { models, updatedAt: data.updatedAt };
}
```

```js
fetchModelsFromApi(BENCHMARK_API_URL)
  .then(({ models, updatedAt }) => this.setState({
    models,
    dataSource: 'live',
    lastUpdated: updatedAt || new Date().toLocaleDateString('en-US',
      { month: 'short', day: 'numeric', year: 'numeric' })
  }))
  .catch(err => {
    console.warn('Falling back to snapshot data:', err);
    this.setState({ models: MODELS, dataSource: 'error' });
  });
```

---

## 5. CORS (important if your API is on another domain)

The dashboard runs entirely in the browser, so the fetch is subject to CORS.
If your API is served from a different origin than the page, your backend must
send:

```
Access-Control-Allow-Origin: *
```

(or the specific origin the page is served from). If you can't enable CORS on
the benchmark API, proxy the request through your own backend on the same
origin as the page.

---

## 6. Optional: refresh on a schedule

The dashboard fetches once on load. If you keep the page open on a wall display
and want it to re-pull once a day, add a timer in `componentDidMount` after the
initial fetch:

```js
componentDidMount() {
  if (!BENCHMARK_API_URL) return;
  const load = () => {
    this.setState({ dataSource: 'loading' });
    fetchModelsFromApi(BENCHMARK_API_URL)
      .then(models => this.setState({
        models,
        dataSource: 'live',
        lastUpdated: new Date().toLocaleDateString('en-US',
          { month: 'short', day: 'numeric', year: 'numeric' })
      }))
      .catch(err => {
        console.warn('Falling back to snapshot data:', err);
        this.setState({ dataSource: 'error' });
      });
  };
  load();
  // re-fetch every 24h
  this._timer = setInterval(load, 24 * 60 * 60 * 1000);
}

componentWillUnmount() {
  clearInterval(this._timer);
}
```

---

## 7. Testing checklist

- [ ] `BENCHMARK_API_URL` set to your endpoint.
- [ ] Endpoint returns a JSON array (or `{ models: [...] }`) with the fields above.
- [ ] CORS headers present if cross-origin.
- [ ] Open the page → badge shows **Loading…** then **Live** with today's date.
- [ ] Bars, tabs, hover detail panel, and the Labs legend all populate.
- [ ] Kill the endpoint / go offline → badge falls back to **Snapshot (API unreachable)** and the built-in data still renders.

---

*The bundled snapshot in the file stays as the offline fallback — you can leave
it as-is, or replace the `MODELS` array with your own default set.*
