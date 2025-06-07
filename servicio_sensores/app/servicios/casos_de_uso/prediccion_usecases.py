from sqlalchemy.orm import Session
from dominio.prediccion_sequia import PrediccionSequia
from app.esquemas.esquema_prediccion import PrediccionCrear

def crear_prediccion(db: Session, datos: PrediccionCrear) -> PrediccionSequia:
    nueva_prediccion = PrediccionSequia(**datos.dict())
    db.add(nueva_prediccion)
    db.commit()
    db.refresh(nueva_prediccion)
    return nueva_prediccion

def obtener_predicciones(db: Session):
    return db.query(PrediccionSequia).all()

def obtener_prediccion_por_id(db: Session, prediccion_id: int):
    return db.query(PrediccionSequia).filter(PrediccionSequia.id == prediccion_id).first()
