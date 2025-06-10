import pytest
from sqlalchemy.orm import Session
from app.esquemas.esquema_sensor import SensorCrear
from app.repositorios.repositorio_sensores import crear_sensor, obtener_sensores

@pytest.fixture
def sensor_ejemplo():
    return SensorCrear(tipo="temperatura", modelo="T-1000")

def test_crear_sensor(db_session: Session, sensor_ejemplo):
    nuevo_sensor = crear_sensor(db_session, sensor_ejemplo)
    assert nuevo_sensor.id is not None
    assert nuevo_sensor.tipo == sensor_ejemplo.tipo
    assert nuevo_sensor.modelo == sensor_ejemplo.modelo

def test_obtener_sensores(db_session: Session, sensor_ejemplo):
    crear_sensor(db_session, sensor_ejemplo)
    sensores = obtener_sensores(db_session)
    assert len(sensores) > 0
