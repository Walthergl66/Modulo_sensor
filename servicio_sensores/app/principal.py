from fastapi import FastAPI
from app.controladores.controlador_sensores import router as router_sensores
from app.controladores.controlador_lecturas import router as router_lecturas
from app.controladores.controlador_ubicaciones import router as router_ubicaciones
from app.controladores.controlador_anomalia import router as router_anomalias
from app.controladores.controlador_predicciones import router as router_predicciones

from app.base_datos.conexion import Base, engine
from dominio import sensor, lectura, ubicacion, anomalia, prediccion_sequia  # importa todas las entidades

app = FastAPI(title="Servicio de Sensores Agrotech")

# Crear tablas al arrancar la app (solo una vez)
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

# Registrar rutas con prefijos y tags únicos para cada recurso
app.include_router(router_sensores, prefix="/sensores", tags=["Sensores"])
app.include_router(router_lecturas, prefix="/lecturas", tags=["Lecturas"])
app.include_router(router_ubicaciones, prefix="/ubicaciones", tags=["Ubicaciones"])
app.include_router(router_anomalias, prefix="/anomalias", tags=["Anomalias"])
app.include_router(router_predicciones, prefix="/predicciones", tags=["Predicciones"])
