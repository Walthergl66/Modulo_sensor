from datetime import datetime
from pydantic import BaseModel

class Sensor(BaseModel):
    id: int
    nombre: str
    tipo: str
    ubicacion: str
    fecha_instalacion: datetime

    class Config:
        orm_mode = True

class CrearSensor(BaseModel):
    nombre: str
    tipo: str
    ubicacion: str
