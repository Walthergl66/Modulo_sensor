import pytest
from app.repositorios import repositorio_sensores, repositorio_ubicaciones
from app.esquemas.esquema_sensor import SensorCrear
from app.esquemas.esquema_ubicacion import UbicacionCrear

def test_crear_ubicacion(db_session):
    sensor = repositorio_sensores.crear_sensor(db_session, SensorCrear(tipo="geo", modelo="G1"))
    ubicacion_data = UbicacionCrear(sensor_id=sensor.id, latitud="10.0", longitud="20.0", descripcion="Campo A")
    ubicacion = repositorio_ubicaciones.crear_ubicacion(db_session, ubicacion_data)
    assert ubicacion.id is not None
    assert ubicacion.descripcion == "Campo A"

def test_obtener_ubicaciones(db_session):
    sensor = repositorio_sensores.crear_sensor(db_session, SensorCrear(tipo="geo", modelo="G1"))
    ubicacion_data = UbicacionCrear(sensor_id=sensor.id, latitud="10.0", longitud="20.0", descripcion="Campo A")
    repositorio_ubicaciones.crear_ubicacion(db_session, ubicacion_data)
    ubicaciones = repositorio_ubicaciones.obtener_ubicaciones(db_session)
    assert len(ubicaciones) == 1
    assert ubicaciones[0].latitud == "10.0"