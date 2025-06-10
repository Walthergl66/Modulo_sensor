import pytest
from app.repositorios import repositorio_sensores, repositorio_lecturas
from app.esquemas.esquema_sensor import SensorCrear
from app.esquemas.esquema_lectura import LecturaCrear

def test_crear_lectura(db_session):
    sensor = repositorio_sensores.crear_sensor(db_session, SensorCrear(tipo="temp", modelo="T300"))
    lectura_data = LecturaCrear(sensor_id=sensor.id, humedad=50.0, temperatura=20.0)
    lectura = repositorio_lecturas.crear_lectura(db_session, lectura_data)
    assert lectura.id is not None
    assert lectura.humedad == 50.0

def test_obtener_lecturas_por_sensor(db_session):
    sensor = repositorio_sensores.crear_sensor(db_session, SensorCrear(tipo="temp", modelo="T300"))
    lectura_data = LecturaCrear(sensor_id=sensor.id, humedad=50.0, temperatura=20.0)
    repositorio_lecturas.crear_lectura(db_session, lectura_data)
    lecturas = repositorio_lecturas.obtener_lecturas_por_sensor(db_session, sensor.id)
    assert len(lecturas) == 1
    assert lecturas[0].temperatura == 20.0