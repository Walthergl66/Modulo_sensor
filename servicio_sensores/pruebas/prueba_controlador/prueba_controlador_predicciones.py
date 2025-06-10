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

def crear_sensor(client):
    resp = client.post("/sensores/", json={
        "tipo": "temp",
        "modelo": "T100"
    })
    assert resp.status_code == 200, f"Error creando sensor: {resp.status_code}, {resp.text}"
    return resp.json()["id"]

def crear_ubicacion(client, sensor_id):
    resp = client.post("/ubicaciones/", json={
        "latitud": "10.0",
        "longitud": "20.0",
        "sensor_id": sensor_id,
        "descripcion": "test"
    })
    assert resp.status_code == 200, f"Error creando ubicación: {resp.status_code}, {resp.text}"
    return resp.json()["id"]

def test_crear_prediccion():
    limpiar_bd()
    client = TestClient(app)
    sensor_id = crear_sensor(client)
    ubicacion_id = crear_ubicacion(client, sensor_id)
    response = client.post("/predicciones/", json={
        "probabilidad": 0.85,
        "ubicacion_id": ubicacion_id
    })
    assert response.status_code == 200, f"Error creando predicción: {response.status_code}, {response.text}"
    data = response.json()
    assert "id" in data, f"Respuesta inesperada: {data}"
    assert 0 <= data["probabilidad"] <= 1, f"Probabilidad fuera de rango: {data['probabilidad']}"
    assert data["ubicacion_id"] == ubicacion_id, f"Ubicación incorrecta: {data['ubicacion_id']} != {ubicacion_id}"

def test_listar_predicciones():
    limpiar_bd()
    client = TestClient(app)
    sensor_id = crear_sensor(client)
    ubicacion_id = crear_ubicacion(client, sensor_id)
    # Crear una predicción primero
    resp_crear = client.post("/predicciones/", json={
        "probabilidad": 0.65,
        "ubicacion_id": ubicacion_id
    })
    assert resp_crear.status_code == 200, f"Error creando predicción: {resp_crear.status_code}, {resp_crear.text}"
    response = client.get("/predicciones/")
    assert response.status_code == 200, f"Error listando predicciones: {response.status_code}, {response.text}"
    data = response.json()
    assert isinstance(data, list), f"Respuesta no es lista: {data}"
    assert any(
        abs(pred["probabilidad"] - 0.65) < 1e-6 and pred["ubicacion_id"] == ubicacion_id
        for pred in data
    ), f"No se encontró la predicción esperada en: {data}"