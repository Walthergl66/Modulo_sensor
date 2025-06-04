from sqlalchemy.orm import Session
from infraestructura.modelos import SensorDB
from dominio.entidades import Sensor, CrearSensor
from datetime import datetime

def crear_sensor(db: Session, datos: CrearSensor) -> Sensor:
    nuevo_sensor = SensorDB(
        nombre=datos.nombre,
        tipo=datos.tipo,
        ubicacion=datos.ubicacion,
        fecha_instalacion=datetime.utcnow()
    )
    db.add(nuevo_sensor)
    db.commit()
    db.refresh(nuevo_sensor)
    return nuevo_sensor

def obtener_sensores(db: Session) -> list[Sensor]:
    return db.query(SensorDB).all()

def obtener_sensor_por_id(db: Session, sensor_id: int) -> SensorDB | None:
    return db.query(SensorDB).filter(SensorDB.id == sensor_id).first()

def actualizar_sensor(db: Session, sensor_id: int, datos: CrearSensor) -> SensorDB | None:
    sensor = db.query(SensorDB).filter(SensorDB.id == sensor_id).first()
    if sensor:
        sensor.nombre = datos.nombre
        sensor.tipo = datos.tipo
        sensor.ubicacion = datos.ubicacion
        db.commit()
        db.refresh(sensor)
    return sensor

def eliminar_sensor(db: Session, sensor_id: int) -> bool:
    sensor = db.query(SensorDB).filter(SensorDB.id == sensor_id).first()
    if sensor:
        db.delete(sensor)
        db.commit()
        return True
    return False

