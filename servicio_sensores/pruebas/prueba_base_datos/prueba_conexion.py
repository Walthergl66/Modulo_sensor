from dotenv import load_dotenv
load_dotenv(dotenv_path=".env.test")

import pytest
from sqlalchemy import create_engine
import os

from app.base_datos.conexion import Base

DATABASE_URL = os.getenv("TEST_DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("La variable de entorno TEST_DATABASE_URL no está definida.")

def test_conexion_base_datos():
    """
    Test básico para verificar la conexión y la creación de tablas en la base de datos de pruebas.
    """
    engine = create_engine(DATABASE_URL)
    try:
        Base.metadata.create_all(engine)
        with engine.connect() as connection:
            pass  # La conexión fue exitosa
    except Exception as e:
        pytest.fail(f"No se pudo conectar a la base de datos: {e}")