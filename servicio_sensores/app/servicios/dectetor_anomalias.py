from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from app.base_datos.conexion import Base
from datetime import datetime

class Anomalia(Base):
    __tablename__ = "anomalias"

    id = Column(Integer, primary_key=True, index=True)
    lectura_id = Column(Integer, ForeignKey("lecturas.id"))
    tipo = Column(String)
    valor = Column(Float)
    fecha = Column(DateTime, default=datetime.utcnow)
