from pydantic import BaseModel, ConfigDict
from datetime import datetime

class AnomaliaBase(BaseModel):
    tipo: str
    valor: float

class AnomaliaCrear(AnomaliaBase):
    lectura_id: int

class AnomaliaRespuesta(AnomaliaBase):
    id: int
    lectura_id: int
    fecha: datetime
    
    model_config = ConfigDict(from_attributes=True)
