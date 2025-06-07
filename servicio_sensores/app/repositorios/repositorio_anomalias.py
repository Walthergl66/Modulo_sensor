from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from dominio.anomalia import Anomalia
from app.esquemas.esquema_anomalia import AnomaliaCrear

def crear_anomalia(db: Session, anomalia: AnomaliaCrear):
    try:
        nueva = Anomalia(**anomalia.dict())
        db.add(nueva)
        db.commit()
        db.refresh(nueva)
        return nueva
    except SQLAlchemyError:
        db.rollback()
        raise

def obtener_anomalias_por_lectura(db: Session, lectura_id: int):
    return db.query(Anomalia).filter(Anomalia.lectura_id == lectura_id).all()

def obtener_anomalia_por_id(db: Session, anomalia_id: int):
    return db.query(Anomalia).filter(Anomalia.id == anomalia_id).first()
