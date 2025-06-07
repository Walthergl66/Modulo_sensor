from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.base_datos.conexion import SessionLocal
from dominio.ubicacion import Ubicacion, CrearUbicacion  
import app.servicios.casos_de_uso.ubicacion_usecases as servicio

router = APIRouter(prefix="/ubicaciones", tags=["Ubicaciones"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Ubicacion)
def crear_ubicacion(datos: CrearUbicacion, db: Session = Depends(get_db)):
    return servicio.crear_ubicacion(db, datos)

@router.get("/", response_model=list[Ubicacion])
def listar_ubicaciones(db: Session = Depends(get_db)):
    return servicio.obtener_ubicaciones(db)

@router.get("/{ubicacion_id}", response_model=Ubicacion)
def obtener_ubicacion(ubicacion_id: int, db: Session = Depends(get_db)):
    ubicacion = servicio.obtener_ubicacion_por_id(db, ubicacion_id)
    if ubicacion is None:
        raise HTTPException(status_code=404, detail="Ubicación no encontrada")
    return ubicacion

@router.put("/{ubicacion_id}", response_model=Ubicacion)
def actualizar_ubicacion(ubicacion_id: int, datos: CrearUbicacion, db: Session = Depends(get_db)):
    ubicacion = servicio.actualizar_ubicacion(db, ubicacion_id, datos)
    if ubicacion is None:
        raise HTTPException(status_code=404, detail="Ubicación no encontrada")
    return ubicacion

@router.delete("/{ubicacion_id}")
def eliminar_ubicacion(ubicacion_id: int, db: Session = Depends(get_db)):
    if not servicio.eliminar_ubicacion(db, ubicacion_id):
        raise HTTPException(status_code=404, detail="Ubicación no encontrada")
    return {"ok": True}
