from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime, UTC
from app.base_datos.conexion import Base  # Asumo que tienes un Base declarativo

class Anomalia(Base):
    __tablename__ = "anomalias"
    
    id = Column(Integer, primary_key=True, index=True)
    lectura_id = Column(Integer, ForeignKey("lecturas.id"), nullable=False)
    tipo = Column(String, nullable=False)        # Ejemplo: "temperatura_alta", "humedad_baja"
    valor = Column(Float, nullable=False)        # Ahora se llama 'valor'
    fecha = Column(DateTime(timezone=True), default=lambda: datetime.now(UTC))  # Ahora se llama 'fecha'
    
    lectura = relationship("Lectura", back_populates="anomalias")