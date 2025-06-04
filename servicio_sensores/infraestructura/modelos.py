from sqlalchemy import Column, Integer, String, DateTime
from infraestructura.database import Base
from datetime import datetime

class SensorDB(Base):
    __tablename__ = "sensores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    ubicacion = Column(String, nullable=False)
    fecha_instalacion = Column(DateTime, default=datetime.utcnow)
