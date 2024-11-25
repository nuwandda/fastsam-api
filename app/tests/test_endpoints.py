from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_fastsam_endpoint():
    response = client.post("/fastsam/", json={"data": "https://huggingface.co/spaces/An-619/FastSAM/resolve/main/examples/dogs.jpg"})
    assert response.status_code == 200
    assert "result" in response.json()
