from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from dominio.prediccion_sequia import PrediccionSequia
from app.esquemas.esquema_prediccion import PrediccionCrear

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

def obtener_prediccion_por_id(db: Session, prediccion_id: int):
    return db.query(PrediccionSequia).filter(PrediccionSequia.id == prediccion_id).first()

def obtener_predicciones_por_ubicacion(db: Session, ubicacion_id: int):
    return db.query(PrediccionSequia).filter(PrediccionSequia.ubicacion_id == ubicacion_id).all()

