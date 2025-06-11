from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.base_datos.conexion import SessionLocal
from app.repositorios import repositorio_sensores
from app.esquemas.esquema_sensor import SensorCrear, SensorRespuesta

# 👇 Importar la función de seguridad
from seguridad.dependencias import obtener_usuario_actual

router = APIRouter()

def obtener_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=SensorRespuesta)
def crear_sensor(
    sensor: SensorCrear,
    db: Session = Depends(obtener_db),
    usuario: str = Depends(obtener_usuario_actual)  # 👈 Se requiere token
):
    return repositorio_sensores.crear_sensor(db, sensor)

@router.get("/", response_model=list[SensorRespuesta])
def listar_sensores(
    db: Session = Depends(obtener_db),
    usuario: str = Depends(obtener_usuario_actual)  # 👈 Se requiere token
):
    return repositorio_sensores.obtener_sensores(db)

