servicios_content = '''\
from app.repositorios.repositorio_lecturas import crear_lectura
from app.base_datos.conexion import SessionLocal
from app.esquemas.esquema_lectura import LecturaCrear

def test_crear_lectura():
    db = SessionLocal()
    lectura = LecturaCrear(valor=23.5, sensor_id=1)
    nueva = crear_lectura(db, lectura)
    assert nueva.valor == 23.5
    assert nueva.sensor_id == 1
    db.close()
'''