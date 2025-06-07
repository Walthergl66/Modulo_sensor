from sqlalchemy.orm import Session
from dominio.ubicacion import Ubicacion
from app.esquemas.esquema_ubicacion import UbicacionCrear

def crear_ubicacion(db: Session, datos: UbicacionCrear) -> Ubicacion:
    nueva_ubicacion = Ubicacion(**datos.dict())
    db.add(nueva_ubicacion)
    db.commit()
    db.refresh(nueva_ubicacion)
    return nueva_ubicacion

def obtener_ubicaciones(db: Session):
    return db.query(Ubicacion).all()

def obtener_ubicacion_por_id(db: Session, ubicacion_id: int):
    return db.query(Ubicacion).filter(Ubicacion.id == ubicacion_id).first()
