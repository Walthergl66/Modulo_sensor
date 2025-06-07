from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from app.base_datos.conexion import Base
from datetime import datetime

class PrediccionSequia(Base):
    __tablename__ = "predicciones_sequia"

    id = Column(Integer, primary_key=True, index=True)
    ubicacion_id = Column(Integer, ForeignKey("ubicaciones.id"), nullable=False)
    fecha_prediccion = Column(DateTime, default=datetime.utcnow)
    probabilidad = Column(Float, nullable=False)  # Valor entre 0 y 1
    comentario = Column(String, nullable=True)

    ubicacion = relationship("Ubicacion")
