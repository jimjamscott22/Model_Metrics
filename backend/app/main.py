"""FastAPI app serving benchmark data for the LLM Benchmark Dashboard."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import benchmarks

app = FastAPI(
    title="Model Metrics Benchmarks API",
    description="Serves live benchmark scores for the LLM Benchmark Dashboard.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(benchmarks.router, prefix="/v1/benchmarks", tags=["Benchmarks"])


@app.get("/health", tags=["Health"])
async def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}
