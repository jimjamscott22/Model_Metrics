"""Bundled snapshot data, mirrored from the dashboard's built-in MODELS array."""

from app.schemas import BenchmarkModel

SNAPSHOT_MODELS: list[BenchmarkModel] = [
    BenchmarkModel(id="gpt55", name="GPT-5.5", lab="OpenAI", open=False, hue=150, released="Apr 2026", overall=1522, coding=90.4, longctx=88, cost=8.50, speed=95),
    BenchmarkModel(id="opus48", name="Claude Opus 4.8", lab="Anthropic", open=False, hue=35, released="May 2026", overall=1541, coding=93.8, longctx=91, cost=12.00, speed=78),
    BenchmarkModel(id="gem31", name="Gemini 3.1 Pro", lab="Google", open=False, hue=220, released="Feb 2026", overall=1498, coding=87.2, longctx=95, cost=7.00, speed=130),
    BenchmarkModel(id="grok41", name="Grok 4.1", lab="xAI", open=False, hue=0, released="Mar 2026", overall=1472, coding=82.5, longctx=80, cost=6.50, speed=145),
    BenchmarkModel(id="llama4", name="Llama 4 Scout", lab="Meta", open=True, hue=255, released="Jan 2026", overall=1410, coding=61.3, longctx=72, cost=0.35, speed=260),
    BenchmarkModel(id="deepseek", name="DeepSeek V4", lab="DeepSeek", open=True, hue=190, released="Feb 2026", overall=1449, coding=78.6, longctx=76, cost=0.55, speed=110),
    BenchmarkModel(id="qwen37", name="Qwen 3.7 Max", lab="Alibaba", open=True, hue=290, released="Apr 2026", overall=1438, coding=74.1, longctx=74, cost=0.60, speed=120),
    BenchmarkModel(id="glm52", name="GLM-5.2", lab="Zhipu", open=True, hue=95, released="May 2026", overall=1421, coding=70.8, longctx=70, cost=0.50, speed=115),
    BenchmarkModel(id="minimax", name="MiniMax M2.5", lab="MiniMax", open=True, hue=325, released="Mar 2026", overall=1405, coding=68.2, longctx=68, cost=0.45, speed=135),
    BenchmarkModel(id="mistral3", name="Mistral Large 3", lab="Mistral AI", open=True, hue=60, released="Jan 2026", overall=1415, coding=65.7, longctx=71, cost=2.20, speed=100),
]
