from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from dominio.sensor import Sensor
from dominio.lectura import Lectura
from dominio.ubicacion import Ubicacion
from dominio.anomalia import Anomalia
from dominio.prediccion_sequia import PrediccionSequia

from app.esquemas.esquema_sensor import (
    SensorCrear) 
from app.esquemas.esquema_lectura import (LecturaCrear) 
from app.esquemas.esquema_ubicacion import (UbicacionCrear) 
from app.esquemas.esquema_anomalia import (AnomaliaCrear)
from app.esquemas.esquema_prediccion import (PrediccionCrear)


def crear_sensor(db: Session, sensor: SensorCrear):
    try:
        sensor_nuevo = Sensor(**sensor.model_dump())
        db.add(sensor_nuevo)
        db.commit()
        db.refresh(sensor_nuevo)
        return sensor_nuevo
    except SQLAlchemyError:
        db.rollback()
        raise

def obtener_sensores(db: Session):
    return db.query(Sensor).all()

def crear_lectura(db: Session, lectura: LecturaCrear):
    sensor = db.get(Sensor, lectura.sensor_id)
    if not sensor:
        raise ValueError("Sensor no encontrado")
    try:
        lectura_nueva = Lectura(**lectura.model_dump())
        db.add(lectura_nueva)
        db.commit()
        db.refresh(lectura_nueva)
        return lectura_nueva
    except SQLAlchemyError:
        db.rollback()
        raise

def obtener_lecturas_por_sensor(db: Session, sensor_id: int):
    return db.query(Lectura).filter(Lectura.sensor_id == sensor_id).all()

def crear_ubicacion(db: Session, ubicacion: UbicacionCrear):
    try:
        nueva = Ubicacion(**ubicacion.model_dump())
        db.add(nueva)
        db.commit()
        db.refresh(nueva)
        return nueva
    except SQLAlchemyError:
        db.rollback()
        raise

def obtener_ubicaciones(db: Session):
    return db.query(Ubicacion).all()

def crear_anomalia(db: Session, anomalia: AnomaliaCrear):
    try:
        nueva = Anomalia(**anomalia.model_dump())
        db.add(nueva)
        db.commit()
        db.refresh(nueva)
        return nueva
    except SQLAlchemyError:
        db.rollback()
        raise

def obtener_anomalias_por_lectura(db: Session, lectura_id: int):
    return db.query(Anomalia).filter(Anomalia.lectura_id == lectura_id).all()

def crear_prediccion(db: Session, prediccion: PrediccionCrear):
    try:
        nueva = PrediccionSequia(**prediccion.model_dump())
        db.add(nueva)
        db.commit()
        db.refresh(nueva)
        return nueva
    except SQLAlchemyError:
        db.rollback()
        raise

def obtener_predicciones(db: Session):
    return db.query(PrediccionSequia).all()
