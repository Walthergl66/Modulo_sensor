from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from app.base_datos.conexion import Base  # Importa la base declarativa
from datetime import datetime, timezone

class PrediccionSequia(Base):
    __tablename__ = "predicciones_sequia"

    id = Column(Integer, primary_key=True, index=True)
    ubicacion_id = Column(Integer, ForeignKey("ubicaciones.id"), nullable=False)
    fecha = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    probabilidad = Column(Float, nullable=False)
    comentario = Column(String, nullable=True)

    ubicacion = relationship("Ubicacion")
