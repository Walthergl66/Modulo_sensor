from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from app.base_datos.conexion import Base  # Asumo que tienes un Base declarativo

class Anomalia(Base):
    __tablename__ = "anomalias"
    
    id = Column(Integer, primary_key=True, index=True)
    lectura_id = Column(Integer, ForeignKey("lecturas.id"), nullable=False)
    tipo = Column(String, nullable=False)        # Ejemplo: "temperatura_alta", "humedad_baja"
    descripcion = Column(String, nullable=True)
    valor_detectado = Column(Float, nullable=True)
    fecha_detectada = Column(DateTime, default=datetime.utcnow)
    
    lectura = relationship("Lectura", back_populates="anomalias")
