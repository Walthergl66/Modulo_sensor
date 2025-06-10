import pytest
from app.repositorios import repositorio_sensores, repositorio_lecturas, repositorio_anomalias
from app.esquemas.esquema_sensor import SensorCrear
from app.esquemas.esquema_lectura import LecturaCrear
from app.esquemas.esquema_anomalia import AnomaliaCrear

def test_crear_anomalia(db_session):
    sensor = repositorio_sensores.crear_sensor(db_session, SensorCrear(tipo="temp", modelo="T300"))
    lectura = repositorio_lecturas.crear_lectura(db_session, LecturaCrear(sensor_id=sensor.id, humedad=30.0, temperatura=50.0))
    anomalia_data = AnomaliaCrear(
        lectura_id=lectura.id,
        tipo="temperatura_alta",
        descripcion="Muy alta",
        valor=50.0  # Cambio aquí
    )
    anomalia = repositorio_anomalias.crear_anomalia(db_session, anomalia_data)
    assert anomalia.id is not None
    assert anomalia.tipo == "temperatura_alta"

def test_obtener_anomalias_por_lectura(db_session):
    sensor = repositorio_sensores.crear_sensor(db_session, SensorCrear(tipo="temp", modelo="T300"))
    lectura = repositorio_lecturas.crear_lectura(db_session, LecturaCrear(sensor_id=sensor.id, humedad=30.0, temperatura=50.0))
    anomalia_data = AnomaliaCrear(
        lectura_id=lectura.id,
        tipo="temperatura_alta",
        valor=50.0
    )
    repositorio_anomalias.crear_anomalia(db_session, anomalia_data)
    anomalias = repositorio_anomalias.obtener_anomalias_por_lectura(db_session, lectura.id)
    assert len(anomalias) == 1
    assert anomalias[0].tipo == "temperatura_alta"
    assert anomalias[0].valor == 50.0