from pydantic import BaseModel, ConfigDict

class SensorBase(BaseModel):
    tipo: str
    modelo: str

class SensorCrear(SensorBase):
    pass

class SensorRespuesta(SensorBase):
    id: int

    model_config = ConfigDict(from_attributes=True)