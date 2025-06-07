from sqlalchemy.orm import Session
from dominio.lectura import Lectura
from app.esquemas.esquema_lectura import LecturaCrear

def crear_lectura(db: Session, datos: LecturaCrear) -> Lectura:
    nueva_lectura = Lectura(**datos.dict())
    db.add(nueva_lectura)
    db.commit()
    db.refresh(nueva_lectura)
    return nueva_lectura

def obtener_lecturas_por_sensor(db: Session, sensor_id: int):
    return db.query(Lectura).filter(Lectura.sensor_id == sensor_id).all()

def obtener_lectura_por_id(db: Session, lectura_id: int):
    return db.query(Lectura).filter(Lectura.id == lectura_id).first()
