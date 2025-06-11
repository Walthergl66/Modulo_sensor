from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.base_datos.conexion import SessionLocal
from app.repositorios import repositorio_sensores
from app.esquemas.esquema_anomalia import AnomaliaCrear, AnomaliaRespuesta
from seguridad.dependencias import obtener_usuario_actual  # ← Seguridad

router = APIRouter()

def obtener_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AnomaliaRespuesta)
def crear_anomalia(
    anomalia: AnomaliaCrear,
    db: Session = Depends(obtener_db),
    usuario: str = Depends(obtener_usuario_actual)  # ← Protegido
):
    return repositorio_sensores.crear_anomalia(db, anomalia)

@router.get("/lecturas/{lectura_id}/anomalias", response_model=list[AnomaliaRespuesta])
def obtener_anomalias(
    lectura_id: int,
    db: Session = Depends(obtener_db),
    usuario: str = Depends(obtener_usuario_actual)  # ← Protegido
):
    return repositorio_sensores.obtener_anomalias_por_lectura(db, lectura_id)
