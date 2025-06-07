from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.base_datos.conexion import SessionLocal
from dominio.prediccion_sequia import Prediccion, CrearPrediccion
import app.servicios.casos_de_uso.prediccion_usecases as servicio

router = APIRouter(prefix="/predicciones", tags=["Predicciones"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Prediccion)
def crear_prediccion(datos: CrearPrediccion, db: Session = Depends(get_db)):
    return servicio.crear_prediccion(db, datos)

@router.get("/", response_model=list[Prediccion])
def listar_predicciones(db: Session = Depends(get_db)):
    return servicio.obtener_predicciones(db)

@router.get("/{prediccion_id}", response_model=Prediccion)
def obtener_prediccion(prediccion_id: int, db: Session = Depends(get_db)):
    prediccion = servicio.obtener_prediccion_por_id(db, prediccion_id)
    if prediccion is None:
        raise HTTPException(status_code=404, detail="Predicción no encontrada")
    return prediccion

@router.put("/{prediccion_id}", response_model=Prediccion)
def actualizar_prediccion(prediccion_id: int, datos: CrearPrediccion, db: Session = Depends(get_db)):
    prediccion = servicio.actualizar_prediccion(db, prediccion_id, datos)
    if prediccion is None:
        raise HTTPException(status_code=404, detail="Predicción no encontrada")
    return prediccion

@router.delete("/{prediccion_id}")
def eliminar_prediccion(prediccion_id: int, db: Session = Depends(get_db)):
    if not servicio.eliminar_prediccion(db, prediccion_id):
        raise HTTPException(status_code=404, detail="Predicción no encontrada")
    return {"ok": True}
