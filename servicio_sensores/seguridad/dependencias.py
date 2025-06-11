from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .token import verificar_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")  # ← Nota el "/auth/login"

def obtener_usuario_actual(token: str = Depends(oauth2_scheme)):
    datos = verificar_token(token)
    if datos is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return datos["sub"]

