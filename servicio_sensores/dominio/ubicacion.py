from sqlalchemy import Column, Integer, String, ForeignKey
from app.base_datos.conexion import Base

class Ubicacion(Base):
    __tablename__ = "ubicaciones"

    id = Column(Integer, primary_key=True, index=True)
    sensor_id = Column(Integer, ForeignKey("sensores.id"))
    latitud = Column(String)
    longitud = Column(String)
    descripcion = Column(String)
