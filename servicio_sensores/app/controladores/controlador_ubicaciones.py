from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.base_datos.conexion import SessionLocal
from app.repositorios import repositorio_ubicaciones
from app.esquemas.esquema_ubicacion import UbicacionCrear, UbicacionRespuesta
from seguridad.dependencias import obtener_usuario_actual  # ← Importar autenticación

router = APIRouter()

def obtener_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UbicacionRespuesta)
def crear_ubicacion(
    ubicacion: UbicacionCrear,
    db: Session = Depends(obtener_db),
    usuario: str = Depends(obtener_usuario_actual)  # ← Protegido con token
):
    return repositorio_ubicaciones.crear_ubicacion(db, ubicacion)

@router.get("/", response_model=list[UbicacionRespuesta])
def listar_ubicaciones(
    db: Session = Depends(obtener_db),
    usuario: str = Depends(obtener_usuario_actual)  # ← Protegido con token
):
    return repositorio_ubicaciones.obtener_ubicaciones(db)

