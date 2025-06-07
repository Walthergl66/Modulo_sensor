from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.base_datos.conexion import SessionLocal
from dominio.anomalia import Anomalia, CrearAnomalia
import app.servicios.casos_de_uso.anomalia_usecases as servicio

router = APIRouter(prefix="/anomalias", tags=["Anomalias"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Anomalia)
def crear_anomalia(datos: CrearAnomalia, db: Session = Depends(get_db)):
    return servicio.crear_anomalia(db, datos)

@router.get("/", response_model=list[Anomalia])
def listar_anomalias(db: Session = Depends(get_db)):
    return servicio.obtener_anomalias(db)

@router.get("/{anomalia_id}", response_model=Anomalia)
def obtener_anomalia(anomalia_id: int, db: Session = Depends(get_db)):
    anomalia = servicio.obtener_anomalia_por_id(db, anomalia_id)
    if anomalia is None:
        raise HTTPException(status_code=404, detail="Anomalía no encontrada")
    return anomalia

@router.put("/{anomalia_id}", response_model=Anomalia)
def actualizar_anomalia(anomalia_id: int, datos: CrearAnomalia, db: Session = Depends(get_db)):
    anomalia = servicio.actualizar_anomalia(db, anomalia_id, datos)
    if anomalia is None:
        raise HTTPException(status_code=404, detail="Anomalía no encontrada")
    return anomalia

@router.delete("/{anomalia_id}")
def eliminar_anomalia(anomalia_id: int, db: Session = Depends(get_db)):
    if not servicio.eliminar_anomalia(db, anomalia_id):
        raise HTTPException(status_code=404, detail="Anomalía no encontrada")
    return {"ok": True}
