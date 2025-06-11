from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.base_datos.conexion import SessionLocal
from app.repositorios import repositorio_sensores
from app.esquemas.esquema_lectura import LecturaCrear, LecturaRespuesta
from seguridad.dependencias import obtener_usuario_actual  # ← Seguridad

router = APIRouter()

def obtener_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{sensor_id}/lecturas", response_model=LecturaRespuesta)
def crear_lectura(
    sensor_id: int,
    lectura: LecturaCrear,
    db: Session = Depends(obtener_db),
    usuario: str = Depends(obtener_usuario_actual)  # ← Protegido
):
    if lectura.sensor_id != sensor_id:
        raise HTTPException(status_code=400, detail="ID del sensor no coincide")
    return repositorio_sensores.crear_lectura(db, lectura)

@router.get("/{sensor_id}/lecturas", response_model=list[LecturaRespuesta])
def obtener_lecturas(
    sensor_id: int,
    db: Session = Depends(obtener_db),
    usuario: str = Depends(obtener_usuario_actual)  # ← Protegido
):
    return repositorio_sensores.obtener_lecturas_por_sensor(db, sensor_id)

