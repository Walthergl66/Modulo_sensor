from pydantic import BaseModel
from datetime import datetime

class PrediccionCrear(BaseModel):
    probabilidad: float

class PrediccionRespuesta(PrediccionCrear):
    id: int
    fecha: datetime

    class Config:
        orm_mode = True
