from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.base_datos.conexion import Base
from datetime import datetime

class Lectura(Base):
    __tablename__ = "lecturas"

    id = Column(Integer, primary_key=True, index=True)
    sensor_id = Column(Integer, ForeignKey("sensores.id"), nullable=False)
    humedad = Column(Float)
    temperatura = Column(Float)
    fecha = Column(DateTime, default=datetime.utcnow)

    anomalias = relationship("Anomalia", back_populates="lectura", cascade="all, delete-orphan")
