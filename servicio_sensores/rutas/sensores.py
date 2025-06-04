from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from infraestructura.database import get_db
from dominio.entidades import Sensor, CrearSensor
import casos_de_uso.sensor_usecases as servicio

router = APIRouter(prefix="/sensores", tags=["sensores"])

@router.post("/", response_model=Sensor)
def crear(datos: CrearSensor, db: Session = Depends(get_db)):
    return servicio.crear_sensor(db, datos)

@router.get("/", response_model=list[Sensor])
def listar(db: Session = Depends(get_db)):
    return servicio.obtener_sensores(db)

@router.get("/{sensor_id}", response_model=Sensor)
def obtener(sensor_id: int, db: Session = Depends(get_db)):
    sensor = servicio.obtener_sensor_por_id(db, sensor_id)
    if sensor is None:
        raise HTTPException(status_code=404, detail="Sensor no encontrado")
    return sensor

@router.put("/{sensor_id}", response_model=Sensor)
def actualizar(sensor_id: int, datos: CrearSensor, db: Session = Depends(get_db)):
    sensor = servicio.actualizar_sensor(db, sensor_id, datos)
    if sensor is None:
        raise HTTPException(status_code=404, detail="Sensor no encontrado")
    return sensor

@router.delete("/{sensor_id}")
def eliminar(sensor_id: int, db: Session = Depends(get_db)):
    if not servicio.eliminar_sensor(db, sensor_id):
        raise HTTPException(status_code=404, detail="Sensor no encontrado")
    return {"ok": True}
