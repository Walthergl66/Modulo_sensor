from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SensorBase(BaseModel):
    tipo: str
    modelo: str

class SensorCrear(SensorBase):
    pass

class SensorRespuesta(SensorBase):
    id: int

    class Config:
        orm_mode = True


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


class AnomaliaRespuesta(BaseModel):
    id: int
    tipo: str
    valor: float
    fecha: datetime

    class Config:
        orm_mode = True


class PrediccionRespuesta(BaseModel):
    id: int
    probabilidad: float
    fecha: datetime

    class Config:
        orm_mode = True


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


class PrediccionCrear(BaseModel):
    probabilidad: float

class PrediccionRespuesta(PrediccionCrear):
    id: int
    fecha: datetime

    class Config:
        orm_mode = True
