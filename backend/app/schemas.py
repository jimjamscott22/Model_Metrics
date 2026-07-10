"""Pydantic schemas for the benchmarks API."""

from pydantic import BaseModel, Field


class BenchmarkModel(BaseModel):
    """A single model's benchmark scores, matching docs/API-Integration-Guide.md."""

    id: str = Field(..., description="Unique, stable identifier")
    name: str = Field(..., description="Display name")
    lab: str = Field(..., description="Provider / lab name")
    open: bool = Field(..., description="True for open-weight models")
    hue: int = Field(..., ge=0, le=360, description="OKLCH color hue")
    released: str = Field(..., description="Release label, e.g. 'May 2026'")
    overall: float = Field(..., description="Overall score (Arena Elo)")
    coding: float = Field(..., description="SWE-bench Verified resolve rate, %")
    longctx: float = Field(..., description="Long-context & agentic composite, 0-100")
    reasoning: float = Field(..., description="Reasoning & logic resolve rate (MATH/GPQA composite), %")
    vision: float = Field(..., description="Vision & multimodal benchmark score (MMMU/VQAv2 composite), %")
    context: int = Field(..., description="Maximum supported context window size, in tokens")
    cost: float = Field(..., description="Blended cost, $ per 1M tokens")
    speed: float = Field(..., description="Output speed, tokens/sec")
