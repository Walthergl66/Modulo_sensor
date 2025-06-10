from dotenv import load_dotenv
load_dotenv(dotenv_path=".env.test")

import os
from sqlalchemy import create_engine, inspect
from app.base_datos.conexion import Base
from app.principal import app
from fastapi.testclient import TestClient

DATABASE_URL = os.getenv("TEST_DATABASE_URL", "postgresql://postgres:hola12345@localhost:5433/sensores_test")

def limpiar_bd():
    engine = create_engine(DATABASE_URL)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def verificar_columnas_anomalias():
    """
    Verifica que la tabla 'anomalias' tenga las columnas esperadas.
    """
    engine = create_engine(DATABASE_URL)
    inspector = inspect(engine)
    columnas = {col["name"] for col in inspector.get_columns("anomalias")}
    columnas_esperadas = {"id", "lectura_id", "tipo", "valor", "fecha"}
    assert columnas_esperadas.issubset(columnas), (
        f"La tabla 'anomalias' no tiene las columnas esperadas: {columnas_esperadas}. "
        f"Columnas actuales: {columnas}"
    )

def test_crear_anomalia():
    limpiar_bd()
    verificar_columnas_anomalias()
    client = TestClient(app)
    sensor_resp = client.post("/sensores/", json={"tipo": "temp", "modelo": "T300"})
    assert sensor_resp.status_code == 200
    sensor_id = sensor_resp.json()["id"]

    lectura_resp = client.post(f"/lecturas/{sensor_id}/lecturas", json={
        "sensor_id": sensor_id,
        "humedad": 30.0,
        "temperatura": 50.0
    })
    assert lectura_resp.status_code == 200
    lectura_id = lectura_resp.json()["id"]

    # Solo los campos que espera el modelo AnomaliaCrear
    anomalia_resp = client.post("/anomalias", json={
        "lectura_id": lectura_id,
        "tipo": "temperatura_alta",
        "valor": 50.0
    })
    assert anomalia_resp.status_code == 200
    data = anomalia_resp.json()
    assert data["lectura_id"] == lectura_id
    assert data["tipo"] == "temperatura_alta"

def test_obtener_anomalias():
    limpiar_bd()
    verificar_columnas_anomalias()
    client = TestClient(app)
    sensor_resp = client.post("/sensores/", json={"tipo": "temp", "modelo": "T301"})
    assert sensor_resp.status_code == 200
    sensor_id = sensor_resp.json()["id"]

    lectura_resp = client.post(f"/lecturas/{sensor_id}/lecturas", json={
        "sensor_id": sensor_id,
        "humedad": 31.0,
        "temperatura": 51.0
    })
    assert lectura_resp.status_code == 200
    lectura_id = lectura_resp.json()["id"]

    anomalia_resp = client.post("/anomalias", json={
        "lectura_id": lectura_id,
        "tipo": "temperatura_alta",
        "valor": 51.0
    })
    assert anomalia_resp.status_code == 200

    response = client.get(f"/anomalias/lecturas/{lectura_id}/anomalias")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(a["valor"] == 51.0 for a in data)