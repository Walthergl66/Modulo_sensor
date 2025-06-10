from pydantic import BaseModel, ConfigDict
from typing import Optional

class UbicacionBase(BaseModel):
    latitud: str
    longitud: str
    descripcion: Optional[str] = None

class UbicacionCrear(UbicacionBase):
    sensor_id: int

class UbicacionRespuesta(UbicacionBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)
