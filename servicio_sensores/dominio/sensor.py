from sqlalchemy import Column, Integer, String
from app.base_datos.conexion import Base

class Sensor(Base):
    __tablename__ = "sensores"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String)
    modelo = Column(String)
