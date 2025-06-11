from pydantic import BaseModel

class LoginDatos(BaseModel):
    username: str
    password: str