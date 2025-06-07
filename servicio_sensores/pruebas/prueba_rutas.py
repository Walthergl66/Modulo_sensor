from fastapi.testclient import TestClient
from app.principal import app

client = TestClient(app)

def test_listar_sensores():
    response = client.get("/sensores/")
    assert response.status_code == 200
