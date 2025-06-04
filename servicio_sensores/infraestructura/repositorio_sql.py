from sqlalchemy.orm import Session
from infraestructura.modelos import SensorDB
from dominio.entidades import Sensor

class SensorRepositorio:

    def __init__(self, db: Session):
        self.db = db

    def crear(self, sensor: Sensor):
        sensor_db = SensorDB(**sensor.dict())
        self.db.add(sensor_db)
        self.db.commit()
        self.db.refresh(sensor_db)
        return sensor_db

    def listar_todos(self):
        return self.db.query(SensorDB).all()

    def obtener_por_id(self, id: int):
        return self.db.query(SensorDB).filter(SensorDB.id == id).first()

    def actualizar(self, id: int, sensor: Sensor):
        sensor_db = self.obtener_por_id(id)
        if not sensor_db:
            return None
        for key, value in sensor.dict().items():
            setattr(sensor_db, key, value)
        self.db.commit()
        return sensor_db

    def eliminar(self, id: int):
        sensor_db = self.obtener_por_id(id)
        if not sensor_db:
            return None
        self.db.delete(sensor_db)
        self.db.commit()
        return True
