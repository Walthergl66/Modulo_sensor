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

def test_crear_ubicacion():
    limpiar_bd()
    client = TestClient(app)
    sensor_resp = client.post("/sensores/", json={"tipo": "geo", "modelo": "G1"})
    assert sensor_resp.status_code == 200
    sensor_id = sensor_resp.json()["id"]
    response = client.post("/ubicaciones/", json={
        "sensor_id": sensor_id,
        "latitud": "10.0",
        "longitud": "20.0",
        "descripcion": "Campo A"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["descripcion"] == "Campo A"

def test_listar_ubicaciones():
    limpiar_bd()
    client = TestClient(app)
    sensor_resp = client.post("/sensores/", json={"tipo": "geo", "modelo": "G2"})
    assert sensor_resp.status_code == 200
    sensor_id = sensor_resp.json()["id"]
    resp_ubic = client.post("/ubicaciones/", json={
        "sensor_id": sensor_id,
        "latitud": "11.0",
        "longitud": "21.0",
        "descripcion": "Campo B"
    })
    assert resp_ubic.status_code == 200
    response = client.get("/ubicaciones/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(ubic["descripcion"] == "Campo B" for ubic in data)