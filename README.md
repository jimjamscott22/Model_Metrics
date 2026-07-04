# LLM Benchmark Dashboard

A clean, single-file dashboard that ranks frontier and open-weight language models across the benchmarks that actually matter — overall Arena Elo, coding (SWE-bench Verified), long-context & agentic performance, and cost vs. speed.

Built as a self-contained HTML file: no build step, no dependencies to install, no framework to configure. Open it in a browser and it runs. Point it at an API and it goes live.

![Dashboard: horizontal bar leaderboard with per-lab colors, tab switcher, and a hover detail panel](img/Model-Metrics.png)

---

## Features

- **Four benchmark views** — Overall (Arena Elo), Coding (SWE-bench Verified %), Long-Context & Agentic (0–100 composite), and a combined Cost & Speed panel.
- **Bold per-lab colors** — every model gets a distinct hue that stays consistent across every view and the legend.
- **Hover for detail** — mousing over any row surfaces that model's full stat line in the side panel (release date, all metrics, cost, speed).
- **Sorted automatically** — each view ranks models by that metric; cost sorts cheapest-first, speed sorts fastest-first.
- **Live or offline** — ships with a curated snapshot as a built-in fallback; set one URL to switch to live daily data.
- **Zero dependencies** — a single HTML file. Works from `file://`, any static host, or a wall display.

---

## Quick start

**Just want to look at it?** Open `LLM Benchmark Dashboard (standalone).html` in any modern browser. Done.

**Want to edit it?** Edit `LLM Benchmark Dashboard.dc.html` — it holds the template and logic in a readable form. The `(standalone).html` file is the bundled, offline-ready build.

---

## Wiring in live data

The dashboard is designed to swap its built-in snapshot for live data from your own backend with a one-line change.

1. Open the logic section and set the endpoint:

   ```js
   const BENCHMARK_API_URL = 'https://api.yourapp.com/v1/benchmarks/latest';
   ```

2. Have your endpoint return a JSON array of model objects (`id`, `name`, `lab`, `open`, `hue`, `released`, `overall`, `coding`, `longctx`, `cost`, `speed`).

On load, the dashboard fetches the endpoint, shows a **Loading…** badge, then swaps in live data and flips to **Live**. If the fetch fails it falls back to the bundled snapshot and shows **Snapshot (API unreachable)**.

See **[API Integration Guide.md](API%20Integration%20Guide.md)** for the exact response shape, a field-by-field table, CORS notes, timestamp handling, and an optional daily auto-refresh snippet.

---

## Data & accuracy

The bundled numbers are a **curated snapshot** compiled from public leaderboard reporting (Arena, SWE-bench Verified, provider disclosures). They're directional, not exact — labs use different harnesses and self-reported numbers shift week to week. The live API refresh is the intended source of truth once connected.

---

## Project structure

```
LLM Benchmark Dashboard.dc.html        # Editable source (template + logic)
LLM Benchmark Dashboard (standalone).html  # Bundled, offline-ready build
API Integration Guide.md               # How to connect a live backend
```

---

## License

MIT — do what you like, no warranty.
