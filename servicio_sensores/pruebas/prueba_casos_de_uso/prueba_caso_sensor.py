import pytest
from sqlalchemy.orm import Session
from app.esquemas.esquema_sensor import SensorCrear
import app.servicios.casos_de_uso.sensor_usecases as sensor_usecases

@pytest.fixture
def sensor_data():
    return SensorCrear(
        tipo="Temperatura",
        modelo="T1000"
    )

def test_crear_sensor(db_session: Session, sensor_data):
    sensor = sensor_usecases.crear_sensor(db_session, sensor_data)
    assert sensor.id is not None
    assert sensor.tipo == sensor_data.tipo  # <-- corregido

def test_obtener_sensores(db_session: Session, sensor_data):
    sensor_usecases.crear_sensor(db_session, sensor_data)
    sensores = sensor_usecases.obtener_sensores(db_session)
    assert len(sensores) > 0

def test_obtener_sensor_por_id(db_session: Session, sensor_data):
    sensor = sensor_usecases.crear_sensor(db_session, sensor_data)
    sensor_obtenido = sensor_usecases.obtener_sensor_por_id(db_session, sensor.id)
    assert sensor_obtenido is not None
    assert sensor_obtenido.id == sensor.id

def test_actualizar_sensor(db_session: Session, sensor_data):
    sensor = sensor_usecases.crear_sensor(db_session, sensor_data)
    nuevos_datos = SensorCrear(
        tipo="Humedad",           # <-- corregido
        modelo="H2000"            # <-- corregido
    )
    sensor_actualizado = sensor_usecases.actualizar_sensor(db_session, sensor.id, nuevos_datos)
    assert sensor_actualizado is not None
    assert sensor_actualizado.tipo == "Humedad"

def test_eliminar_sensor(db_session: Session, sensor_data):
    sensor = sensor_usecases.crear_sensor(db_session, sensor_data)
    resultado = sensor_usecases.eliminar_sensor(db_session, sensor.id)
    assert resultado is True
    sensor_eliminado = sensor_usecases.obtener_sensor_por_id(db_session, sensor.id)
    assert sensor_eliminado is None
