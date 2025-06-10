from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class PrediccionCrear(BaseModel):
    probabilidad: float
    ubicacion_id: int
    comentario: Optional[str] = None  # <- Agregado, opcional

class PrediccionRespuesta(PrediccionCrear):
    id: int
    fecha: datetime

    model_config = ConfigDict(from_attributes=True)
