from sqlalchemy import Column, Integer, Float, DateTime
from app.base_datos.conexion import Base
from datetime import datetime

class PrediccionSequía(Base):
    __tablename__ = "predicciones_sequia"

    id = Column(Integer, primary_key=True, index=True)
    probabilidad = Column(Float)
    fecha = Column(DateTime, default=datetime.utcnow)
