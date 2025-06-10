from dotenv import load_dotenv
load_dotenv(dotenv_path=".env.test")

import os
from sqlalchemy import create_engine
from app.base_datos.conexion import Base
from app.principal import app
from fastapi.testclient import TestClient

DATABASE_URL = os.getenv("TEST_DATABASE_URL", "postgresql://postgres:hola12345@localhost:5433/sensores_test")

def limpiar_bd():
    engine = create_engine(DATABASE_URL)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def test_crear_lectura():
    limpiar_bd()
    client = TestClient(app)
    sensor_resp = client.post("/sensores/", json={"tipo": "temp", "modelo": "T400"})
    assert sensor_resp.status_code == 200
    sensor_id = sensor_resp.json()["id"]
    response = client.post(f"/lecturas/{sensor_id}/lecturas", json={
        "sensor_id": sensor_id,
        "humedad": 55.0,
        "temperatura": 23.0
    })
    assert response.status_code == 200
    data = response.json()
    assert data["humedad"] == 55.0

def test_listar_lecturas_por_sensor():
    limpiar_bd()
    client = TestClient(app)
    sensor_resp = client.post("/sensores/", json={"tipo": "temp", "modelo": "T401"})
    assert sensor_resp.status_code == 200
    sensor_id = sensor_resp.json()["id"]
    post_resp = client.post(f"/lecturas/{sensor_id}/lecturas", json={
        "sensor_id": sensor_id,
        "humedad": 60.0,
        "temperatura": 24.0
    })
    assert post_resp.status_code == 200
    response = client.get(f"/lecturas/{sensor_id}/lecturas")
    assert response.status_code == 200
    data = response.json()
    # Ajusta esta validación según la estructura de tu endpoint
    if isinstance(data, list):
        assert any(lectura["humedad"] == 60.0 for lectura in data)
    elif isinstance(data, dict):
        assert data.get("humedad") == 60.0