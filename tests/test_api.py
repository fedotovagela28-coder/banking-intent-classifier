from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)

def test_health() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_predict() -> None:
    response = client.post("/predict", json={"text": "hello world"})

    assert response.status_code == 200
    assert "prediction" in response.json()