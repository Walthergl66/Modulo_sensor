from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.controladores.controlador_sensores import router as router_sensores
from app.controladores.controlador_lecturas import router as router_lecturas
from app.controladores.controlador_ubicaciones import router as router_ubicaciones
from app.controladores.controlador_anomalia import router as router_anomalias
from app.controladores.controlador_predicciones import router as router_predicciones
from seguridad.login import router as router_login  # Ruta para autenticación

from app.base_datos.conexion import Base, engine
from dominio import sensor, lectura, ubicacion, anomalia, prediccion_sequia

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(title="Servicio de Sensores Mundo Verde", lifespan=lifespan)

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambiar en producción a orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas protegidas
app.include_router(router_sensores, prefix="/sensores", tags=["Sensores"])
app.include_router(router_lecturas, prefix="/lecturas", tags=["Lecturas"])
app.include_router(router_ubicaciones, prefix="/ubicaciones", tags=["Ubicaciones"])
app.include_router(router_anomalias, prefix="/anomalias", tags=["Anomalias"])
app.include_router(router_predicciones, prefix="/predicciones", tags=["Predicciones"])

# Ruta pública para autenticación
app.include_router(router_login, prefix="/auth", tags=["Autenticación"])
