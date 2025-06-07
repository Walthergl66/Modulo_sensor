# 🌱 Servicio de Sensores - Agrotech

Este microservicio desarrollado con **FastAPI** forma parte del sistema Agrotech. Su función principal es gestionar sensores agrícolas y registrar sus lecturas (como temperatura y humedad), facilitando el monitoreo eficiente de cultivos.

---

## 📦 Tecnologías utilizadas

- 🐍 **Python 3.11+**
- ⚡ **FastAPI**
- 🐘 **PostgreSQL**
- 🔁 **Uvicorn** (para el servidor ASGI)
- 🧪 **SQLAlchemy** (ORM)

---

## ✅ Requisitos previos

- Python 3.11 o superior
- PostgreSQL instalado y corriendo
- Git (opcional, para clonar el repositorio)

---

## ⚙️ Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/EmilioSle/Modulo_sensor.git
cd Modulo_sensor
```

### 2. Crear y activar entorno virtual

**Windows (PowerShell):**

```powershell
python -m venv venv
.env\Scripts\Activate.ps1
```

**Linux/macOS (bash):**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 🛠️ Configuración de la base de datos

Abre el archivo `app/base_datos/conexion.py` y modifica la URL de conexión con tus credenciales:

```python
SQLALCHEMY_DATABASE_URL = "postgresql://usuario:contraseña@localhost:5433/agrotech_db"
```

📌 **Ejemplo funcional:**

```python
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:hola12345@localhost:5433/agrotech_db"
```

🔔 Asegúrate de que:

- La base de datos `agrotech_db` existe.
- PostgreSQL esté ejecutándose en el puerto `5433`. sino cambia el puertos

---

## 🚀 Ejecución del servidor

Levanta el microservicio localmente con:

```bash
uvicorn app.principal:app --reload
```

El servidor estará disponible en:

```
http://127.0.0.1:8000
```

---

## 🔍 Exploración de Endpoints

Puedes probar todos los endpoints desde la interfaz Swagger:

👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

También está disponible la documentación ReDoc:

👉 [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📝 Notas importantes

- Las tablas se crean automáticamente si no existen.
- Si modificas los modelos, reinicia el servidor.
- Verifica que el puerto de PostgreSQL no esté bloqueado por firewall o antivirus.
- El servicio es modular y fácilmente escalable.

---

## ✅ Recomendaciones

- Utiliza un entorno virtual para evitar conflictos de dependencias.
- Maneja tus credenciales de manera segura mediante variables de entorno o un archivo `.env`.
- Protege los endpoints sensibles antes de desplegar en producción.
- Realiza pruebas unitarias y de integración para mantener la calidad del servicio.

---

## 📬 Contacto

Para consultas, sugerencias o colaboración, puedes contactarme a:

📧 **emiliosleimen555@gmail.com**
 **0962720681**

---