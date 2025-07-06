🌱 Servicio de Sensores - Mundo Verde
Este microservicio desarrollado con FastAPI forma parte del sistema de Mundo verde, Su función principal es gestionar sensores agrícolas y registrar sus lecturas (como temperatura y humedad), facilitando el monitoreo eficiente de cultivos.

📦 Tecnologías utilizadas:
    🐍 Python 3.11+
    ⚡ FastAPI
    🐘 PostgreSQL
    🔁 Uvicorn
    🧪 SQLAlchemy
    🔐 Autenticación JWT (python-jose, passlib, OAuth2PasswordBearer)
    📦 python-dotenv
    🧪 pytest

✅ Requisitos previos
    Python 3.11 o superior
    PostgreSQL instalado y corriendo
    Git (opcional)

⚙️ Instalación y ejecución
1. Clonar el repositorio
git clone https://github.com/EmilioSle/Modulo_sensor.git
cd Modulo_sensor

2. Crear y activar entorno virtual
Windows (PowerShell):
    python -m venv venv
    .\venv\Scripts\Activate.ps1

Linux/macOS (bash):
    python3 -m venv venv
    source venv/bin/activate

3. Instalar dependencias
pip install -r requirements.txt

🛠️ Configuración de la base de datos
Crea el archivo .env en la raíz del proyecto:

DATABASE_URL=
Asegúrate de que la base de datos agrotech_db existe y PostgreSQL corre en el puerto correcto.

🚀 Ejecutar el servidor

uvicorn app.principal:app --reload
Accede a la app en:
👉 http://127.0.0.1:8000/docs

🔐 Uso del sistema de autenticación
Visita /auth/login en Swagger.
Ingresa usuario y contraseña (ej. admin, admin123).
Obtendrás un access_token.
Haz clic en el botón Authorize en Swagger y pega: Bearer TU_TOKEN

🧪 Pruebas
Ejecuta las pruebas con:
pytest

📬 Contacto
📧 emiliosleimen555@gmail.com
📞 0962720681