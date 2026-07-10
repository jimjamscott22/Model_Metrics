from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_latest_benchmarks_returns_expected_shape():
    response = client.get("/v1/benchmarks/latest")
    assert response.status_code == 200

    models = response.json()
    assert isinstance(models, list)
    assert len(models) == 15

    expected_fields = {
        "id", "name", "lab", "open", "hue", "released",
        "overall", "coding", "longctx", "reasoning", "vision", "context", "cost", "speed",
    }
    assert expected_fields.issubset(models[0].keys())

    ids = [m["id"] for m in models]
    assert len(ids) == len(set(ids))


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
