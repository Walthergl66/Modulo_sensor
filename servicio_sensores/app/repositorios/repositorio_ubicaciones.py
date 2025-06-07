from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from dominio.ubicacion import Ubicacion
from app.esquemas.esquema_ubicacion import UbicacionCrear

def crear_ubicacion(db: Session, ubicacion: UbicacionCrear):
    try:
        nueva = Ubicacion(**ubicacion.dict())
        db.add(nueva)
        db.commit()
        db.refresh(nueva)
        return nueva
    except SQLAlchemyError:
        db.rollback()
        raise

def obtener_ubicaciones(db: Session):
    return db.query(Ubicacion).all()

def obtener_ubicacion_por_id(db: Session, ubicacion_id: int):
    return db.query(Ubicacion).filter(Ubicacion.id == ubicacion_id).first()
