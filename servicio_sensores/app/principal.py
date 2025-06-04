from fastapi import FastAPI
from app.controladores.controlador_sensores import router as router_sensores
from app.base_datos.conexion import Base, engine
from app.entidades import sensor, lectura, ubicacion, anomalia, prediccion_sequia  # importa todas las entidades

app = FastAPI(title="Servicio de Sensores Agrotech")

# Crear tablas al arrancar la app (solo una vez)
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

# Registrar rutas
app.include_router(router_sensores, prefix="/sensores", tags=["Sensores"])
