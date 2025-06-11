from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from datetime import datetime, timedelta

from seguridad.token import SECRET_KEY, ALGORITHM, crear_token_acceso

router = APIRouter()

# Usuario de prueba (en producción consulta la base de datos)
usuario_demo = {
    "username": "admin",
    "password": "admin123"
}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != usuario_demo["username"] or form_data.password != usuario_demo["password"]:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    acceso_token = crear_token_acceso(data={"sub": form_data.username})
    return {"access_token": acceso_token, "token_type": "bearer"}
