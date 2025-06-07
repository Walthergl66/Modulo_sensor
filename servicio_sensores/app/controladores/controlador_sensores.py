from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.base_datos.conexion import SessionLocal
from app.repositorios import repositorio_sensores
from app.esquemas.esquema_sensor import SensorCrear, SensorRespuesta

router = APIRouter()

def obtener_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=SensorRespuesta)
def crear_sensor(sensor: SensorCrear, db: Session = Depends(obtener_db)):
    return repositorio_sensores.crear_sensor(db, sensor)

@router.get("/", response_model=list[SensorRespuesta])
def listar_sensores(db: Session = Depends(obtener_db)):
    return repositorio_sensores.obtener_sensores(db)
