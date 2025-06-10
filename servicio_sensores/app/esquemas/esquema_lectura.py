from pydantic import BaseModel, ConfigDict
from datetime import datetime, UTC
datetime.now(UTC)

class LecturaBase(BaseModel):
    humedad: float
    temperatura: float

class LecturaCrear(LecturaBase):
    sensor_id: int

class LecturaRespuesta(LecturaBase):
    id: int
    fecha: datetime

    model_config = ConfigDict(from_attributes=True)
