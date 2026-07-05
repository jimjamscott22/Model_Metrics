"""FastAPI app serving benchmark data and the dashboard for the LLM Benchmark Dashboard."""

from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from app.routers import benchmarks

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DASHBOARD_PATH = REPO_ROOT / "LLM Benchmark Dashboard (standalone).html"

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


@app.get("/", include_in_schema=False)
async def dashboard() -> FileResponse:
    """Serve the dashboard so the whole app runs from one origin."""
    return FileResponse(DASHBOARD_PATH)
