from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.base_datos.conexion import SessionLocal
from app.repositorios import repositorio_sensores
from app.esquemas.esquema_sensor import (
    SensorCrear, SensorRespuesta,
    LecturaCrear, LecturaRespuesta
)
from app.esquemas.esquema_sensor import (
    UbicacionCrear, UbicacionRespuesta,
    AnomaliaCrear, AnomaliaRespuesta,
    PrediccionCrear, PrediccionRespuesta
)
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

@router.post("/{sensor_id}/lecturas", response_model=LecturaRespuesta)
def crear_lectura(sensor_id: int, lectura: LecturaCrear, db: Session = Depends(obtener_db)):
    if lectura.sensor_id != sensor_id:
        raise HTTPException(status_code=400, detail="ID del sensor no coincide")
    return repositorio_sensores.crear_lectura(db, lectura)

@router.get("/{sensor_id}/lecturas", response_model=list[LecturaRespuesta])
def obtener_lecturas(sensor_id: int, db: Session = Depends(obtener_db)):
    return repositorio_sensores.obtener_lecturas_por_sensor(db, sensor_id)

@router.post("/ubicaciones", response_model=UbicacionRespuesta)
def crear_ubicacion(ubicacion: UbicacionCrear, db: Session = Depends(obtener_db)):
    return repositorio_sensores.crear_ubicacion(db, ubicacion)

@router.get("/ubicaciones", response_model=list[UbicacionRespuesta])
def listar_ubicaciones(db: Session = Depends(obtener_db)):
    return repositorio_sensores.obtener_ubicaciones(db)


@router.post("/anomalias", response_model=AnomaliaRespuesta)
def crear_anomalia(anomalia: AnomaliaCrear, db: Session = Depends(obtener_db)):
    return repositorio_sensores.crear_anomalia(db, anomalia)

@router.get("/lecturas/{lectura_id}/anomalias", response_model=list[AnomaliaRespuesta])
def obtener_anomalias(lectura_id: int, db: Session = Depends(obtener_db)):
    return repositorio_sensores.obtener_anomalias_por_lectura(db, lectura_id)


@router.post("/predicciones", response_model=PrediccionRespuesta)
def crear_prediccion(prediccion: PrediccionCrear, db: Session = Depends(obtener_db)):
    return repositorio_sensores.crear_prediccion(db, prediccion)

@router.get("/predicciones", response_model=list[PrediccionRespuesta])
def listar_predicciones(db: Session = Depends(obtener_db)):
    return repositorio_sensores.obtener_predicciones(db)