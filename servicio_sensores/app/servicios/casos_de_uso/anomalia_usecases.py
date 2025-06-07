from sqlalchemy.orm import Session
from dominio.anomalia import Anomalia
from app.esquemas.esquema_anomalia import AnomaliaCrear

def crear_anomalia(db: Session, datos: AnomaliaCrear) -> Anomalia:
    nueva_anomalia = Anomalia(**datos.dict())
    db.add(nueva_anomalia)
    db.commit()
    db.refresh(nueva_anomalia)
    return nueva_anomalia

def obtener_anomalias_por_lectura(db: Session, lectura_id: int):
    return db.query(Anomalia).filter(Anomalia.lectura_id == lectura_id).all()

def obtener_anomalia_por_id(db: Session, anomalia_id: int):
    return db.query(Anomalia).filter(Anomalia.id == anomalia_id).first()
