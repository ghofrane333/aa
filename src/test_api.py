from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_prediction():
    payload = {"input_data": [1, 2, 3, 4]}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "score" in response.json()
