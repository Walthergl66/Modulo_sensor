from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.base_datos.conexion import SessionLocal
from app.repositorios import repositorio_sensores
from app.esquemas.esquema_ubicacion import UbicacionCrear, UbicacionRespuesta

router = APIRouter()

def obtener_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/ubicaciones", response_model=UbicacionRespuesta)
def crear_ubicacion(ubicacion: UbicacionCrear, db: Session = Depends(obtener_db)):
    return repositorio_sensores.crear_ubicacion(db, ubicacion)

@router.get("/ubicaciones", response_model=list[UbicacionRespuesta])
def listar_ubicaciones(db: Session = Depends(obtener_db)):
    return repositorio_sensores.obtener_ubicaciones(db)
