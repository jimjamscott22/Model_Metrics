"""Benchmarks router: serves the data the dashboard fetches from BENCHMARK_API_URL."""

from fastapi import APIRouter

from app.data import SNAPSHOT_MODELS
from app.schemas import BenchmarkModel

router = APIRouter()


@router.get("/latest", response_model=list[BenchmarkModel])
async def get_latest_benchmarks() -> list[BenchmarkModel]:
    """Return the current benchmark scores for all tracked models.

    Response shape matches docs/API-Integration-Guide.md exactly, so pointing
    the dashboard's BENCHMARK_API_URL at this endpoint works with no changes
    to the dashboard's fetch logic.
    """
    return SNAPSHOT_MODELS
