from pydantic import BaseModel

class SensorBase(BaseModel):
    tipo: str
    modelo: str

class SensorCrear(SensorBase):
    pass

class SensorRespuesta(SensorBase):
    id: int

    class Config:
        orm_mode = True
