from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from dominio.lectura import Lectura
from dominio.sensor import Sensor
from app.esquemas.esquema_sensor import LecturaCrear

def crear_lectura(db: Session, lectura: LecturaCrear):
    sensor = db.query(Sensor).get(lectura.sensor_id)
    if not sensor:
        raise ValueError("Sensor no encontrado")
    try:
        lectura_nueva = Lectura(**lectura.dict())
        db.add(lectura_nueva)
        db.commit()
        db.refresh(lectura_nueva)
        return lectura_nueva
    except SQLAlchemyError:
        db.rollback()
        raise

def obtener_lecturas_por_sensor(db: Session, sensor_id: int):
    return db.query(Lectura).filter(Lectura.sensor_id == sensor_id).all()

def obtener_lectura_por_id(db: Session, lectura_id: int):
    return db.query(Lectura).filter(Lectura.id == lectura_id).first()
