from pydantic import BaseModel
from typing import Optional

class UbicacionBase(BaseModel):
    latitud: str
    longitud: str
    descripcion: Optional[str]

class UbicacionCrear(UbicacionBase):
    sensor_id: int

class UbicacionRespuesta(UbicacionBase):
    id: int

    class Config:
        orm_mode = True
