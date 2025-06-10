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

def test_crear_sensor():
    limpiar_bd()
    client = TestClient(app)
    response = client.post("/sensores/", json={"tipo": "humedad", "modelo": "X100"})
    assert response.status_code == 200
    data = response.json()
    assert data["tipo"] == "humedad"
    assert data["modelo"] == "X100"

def test_listar_sensores():
    limpiar_bd()
    client = TestClient(app)
    resp = client.post("/sensores/", json={"tipo": "temp", "modelo": "T200"})
    assert resp.status_code == 200
    response = client.get("/sensores/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(sensor["modelo"] == "T200" for sensor in data)


#$env:PYTHONPATH = "$PWD\servicio_sensores"       
#>> pytest servicio_sensores/pruebas/prueba_controlador/prueba_controlador_sensores.py 