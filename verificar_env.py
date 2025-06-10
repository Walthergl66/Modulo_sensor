from dotenv import load_dotenv
import os

ruta_env = ".env.test"

if os.path.exists(ruta_env):
    print(f"Archivo encontrado: {ruta_env}")
else:
    print(f"Archivo NO encontrado: {ruta_env}")

load_dotenv(dotenv_path=ruta_env)

valor = os.getenv("TEST_DATABASE_URL")
print(f"Valor leído: {repr(valor)}")

if valor is None:
    print("No se pudo leer la variable de entorno TEST_DATABASE_URL")
else:
    print("La variable TEST_DATABASE_URL fue cargada correctamente")
