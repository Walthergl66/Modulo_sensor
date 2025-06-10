from sqlalchemy.orm import Session
from dominio.sensor import Sensor
from app.esquemas.esquema_sensor import SensorCrear

def crear_sensor(db: Session, datos: SensorCrear) -> Sensor:
    nuevo_sensor = Sensor(**datos.model_dump())
    db.add(nuevo_sensor)
    db.commit()
    db.refresh(nuevo_sensor)
    return nuevo_sensor

def obtener_sensores(db: Session):
    return db.query(Sensor).all()

def obtener_sensor_por_id(db: Session, sensor_id: int):
    return db.query(Sensor).filter(Sensor.id == sensor_id).first()

def actualizar_sensor(db: Session, sensor_id: int, datos: SensorCrear):
    sensor = obtener_sensor_por_id(db, sensor_id)
    if not sensor:
        return None
    for key, value in datos.model_dump().items():
        setattr(sensor, key, value)
    db.commit()
    db.refresh(sensor)
    return sensor

def eliminar_sensor(db: Session, sensor_id: int) -> bool:
    sensor = obtener_sensor_por_id(db, sensor_id)
    if not sensor:
        return False
    db.delete(sensor)
    db.commit()
    return True
