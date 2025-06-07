from pydantic import BaseModel
from datetime import datetime

class AnomaliaBase(BaseModel):
    tipo: str
    valor: float

class AnomaliaCrear(AnomaliaBase):
    lectura_id: int

class AnomaliaRespuesta(AnomaliaBase):
    id: int
    fecha: datetime

    class Config:
        orm_mode = True
