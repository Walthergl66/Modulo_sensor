from pydantic import BaseModel
from datetime import datetime

class LecturaBase(BaseModel):
    humedad: float
    temperatura: float

class LecturaCrear(LecturaBase):
    sensor_id: int

class LecturaRespuesta(LecturaBase):
    id: int
    fecha: datetime

    class Config:
        orm_mode = True
