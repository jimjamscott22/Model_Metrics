"""Bundled snapshot data, mirrored from the dashboard's built-in MODELS array."""

from app.schemas import BenchmarkModel

SNAPSHOT_MODELS: list[BenchmarkModel] = [
    BenchmarkModel(id="gpt55", name="GPT-5.5", lab="OpenAI", open=False, hue=150, released="Apr 2026", overall=1522, coding=90.4, longctx=88, reasoning=92.8, vision=91.0, context=1000000, cost=8.50, speed=95),
    BenchmarkModel(id="opus48", name="Claude Opus 4.8", lab="Anthropic", open=False, hue=35, released="May 2026", overall=1541, coding=93.8, longctx=91, reasoning=93.5, vision=90.5, context=1000000, cost=12.00, speed=78),
    BenchmarkModel(id="gem31", name="Gemini 3.1 Pro", lab="Google", open=False, hue=220, released="Feb 2026", overall=1498, coding=87.2, longctx=95, reasoning=88.4, vision=93.8, context=2000000, cost=7.00, speed=130),
    BenchmarkModel(id="grok41", name="Grok 4.1", lab="xAI", open=False, hue=0, released="Mar 2026", overall=1472, coding=82.5, longctx=80, reasoning=86.0, vision=85.2, context=256000, cost=6.50, speed=145),
    BenchmarkModel(id="llama4", name="Llama 4 Scout", lab="Meta", open=True, hue=255, released="Jan 2026", overall=1410, coding=61.3, longctx=72, reasoning=76.5, vision=78.0, context=256000, cost=0.35, speed=260),
    BenchmarkModel(id="deepseek", name="DeepSeek V4", lab="DeepSeek", open=True, hue=190, released="Feb 2026", overall=1449, coding=78.6, longctx=76, reasoning=85.2, vision=80.4, context=128000, cost=0.55, speed=110),
    BenchmarkModel(id="qwen37", name="Qwen 3.7 Max", lab="Alibaba", open=True, hue=290, released="Apr 2026", overall=1438, coding=74.1, longctx=74, reasoning=83.1, vision=84.6, context=256000, cost=0.60, speed=120),
    BenchmarkModel(id="glm52", name="GLM-5.2", lab="Zhipu", open=True, hue=95, released="May 2026", overall=1421, coding=70.8, longctx=70, reasoning=80.5, vision=81.2, context=128000, cost=0.50, speed=115),
    BenchmarkModel(id="minimax", name="MiniMax M2.5", lab="MiniMax", open=True, hue=325, released="Mar 2026", overall=1405, coding=68.2, longctx=68, reasoning=78.2, vision=77.5, context=200000, cost=0.45, speed=135),
    BenchmarkModel(id="mistral3", name="Mistral Large 3", lab="Mistral AI", open=True, hue=60, released="Jan 2026", overall=1415, coding=65.7, longctx=71, reasoning=79.0, vision=79.8, context=256000, cost=2.20, speed=100),
    BenchmarkModel(id="sonnet5", name="Claude Sonnet 5.0", lab="Anthropic", open=False, hue=45, released="Jun 2026", overall=1530, coding=92.1, longctx=94, reasoning=91.5, vision=89.2, context=500000, cost=3.50, speed=140),
    BenchmarkModel(id="deepseekr2", name="DeepSeek R2", lab="DeepSeek", open=True, hue=180, released="May 2026", overall=1515, coding=89.5, longctx=92, reasoning=94.8, vision=84.0, context=256000, cost=1.20, speed=85),
    BenchmarkModel(id="gem3flash", name="Gemini 3.0 Flash", lab="Google", open=False, hue=210, released="Mar 2026", overall=1485, coding=84.0, longctx=96, reasoning=85.3, vision=92.4, context=2000000, cost=0.80, speed=220),
    BenchmarkModel(id="llama4mav", name="Llama 4 Maverick", lab="Meta", open=True, hue=265, released="Apr 2026", overall=1460, coding=81.2, longctx=85, reasoning=86.1, vision=82.5, context=512000, cost=0.65, speed=180),
    BenchmarkModel(id="o4", name="OpenAI o4", lab="OpenAI", open=False, hue=160, released="Jun 2026", overall=1538, coding=94.2, longctx=93, reasoning=96.0, vision=88.7, context=200000, cost=10.00, speed=65),
]
