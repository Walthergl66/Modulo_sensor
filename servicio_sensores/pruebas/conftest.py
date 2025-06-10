import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from app.base_datos.conexion import Base 
from dominio.sensor import Sensor
from dominio.lectura import Lectura
from dominio.anomalia import Anomalia
from dominio.prediccion_sequia import PrediccionSequia
from dominio.ubicacion import Ubicacion



# Cargar variables de entorno desde .env.test
dotenv_path = os.path.join(os.path.dirname(__file__), "..", "..", ".env.test")
print(f"[DEBUG] Cargando .env.test desde: {dotenv_path}")
load_dotenv(dotenv_path=dotenv_path)

TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")

if not TEST_DATABASE_URL:
    raise RuntimeError("La variable de entorno TEST_DATABASE_URL no está definida.")

# Crear la engine y session para pruebas
engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db_session():
    # Crear todas las tablas
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        # Eliminar las tablas después de cada prueba
        Base.metadata.drop_all(bind=engine)


@pytest.fixture
def sensor_ejemplo(db_session):
    sensor = Sensor(
        nombre="Sensor de prueba",
        descripcion="Sensor para pruebas",
        unidad_medida="Celsius",
        ubicacion="Laboratorio"
    )
    db_session.add(sensor)
    db_session.commit()
    return sensor
