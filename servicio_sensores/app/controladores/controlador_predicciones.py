from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.base_datos.conexion import SessionLocal
from app.repositorios import repositorio_sensores
from app.esquemas.esquema_prediccion import PrediccionCrear, PrediccionRespuesta

router = APIRouter()

def obtener_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=PrediccionRespuesta)
def crear_prediccion(prediccion: PrediccionCrear, db: Session = Depends(obtener_db)):
    return repositorio_sensores.crear_prediccion(db, prediccion)

@router.get("/", response_model=list[PrediccionRespuesta])
def listar_predicciones(db: Session = Depends(obtener_db)):
    return repositorio_sensores.obtener_predicciones(db)