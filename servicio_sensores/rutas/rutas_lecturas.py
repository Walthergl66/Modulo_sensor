from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.base_datos.conexion import SessionLocal
from app.esquemas.esquema_lectura import Lectura, CrearLectura
import app.servicios.casos_de_uso.lectura_usecases as servicio

router = APIRouter(prefix="/lecturas", tags=["Lecturas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Lectura)
def crear_lectura(datos: CrearLectura, db: Session = Depends(get_db)):
    return servicio.crear_lectura(db, datos)

@router.get("/", response_model=list[Lectura])
def listar_lecturas(db: Session = Depends(get_db)):
    return servicio.obtener_lecturas(db)

@router.get("/{lectura_id}", response_model=Lectura)
def obtener_lectura(lectura_id: int, db: Session = Depends(get_db)):
    lectura = servicio.obtener_lectura_por_id(db, lectura_id)
    if lectura is None:
        raise HTTPException(status_code=404, detail="Lectura no encontrada")
    return lectura

@router.put("/{lectura_id}", response_model=Lectura)
def actualizar_lectura(lectura_id: int, datos: CrearLectura, db: Session = Depends(get_db)):
    lectura = servicio.actualizar_lectura(db, lectura_id, datos)
    if lectura is None:
        raise HTTPException(status_code=404, detail="Lectura no encontrada")
    return lectura

@router.delete("/{lectura_id}")
def eliminar_lectura(lectura_id: int, db: Session = Depends(get_db)):
    if not servicio.eliminar_lectura(db, lectura_id):
        raise HTTPException(status_code=404, detail="Lectura no encontrada")
    return {"ok": True}
