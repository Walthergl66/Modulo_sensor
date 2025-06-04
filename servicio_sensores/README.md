# Servicio de Sensores Agrotech

Este proyecto es un microservicio desarrollado con **FastAPI** que gestiona sensores y sus datos como parte del sistema Agrotech.

---

## 🚀 Requisitos

- Python 3.11 o superior
- PostgreSQL (en ejecución)
- Git (opcional)

---

## ⚙️ Instalación y Ejecución

### 1. Clonar el repositorio (opcional)

```bash
git clone https://tu-repositorio-url.git
cd nombre-del-repositorio
```

### 2. Crear y activar entorno virtual

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
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

### 4. Configurar conexión a PostgreSQL

Edita el archivo `app/base_datos/conexion.py` y asegúrate de que la variable `SQLALCHEMY_DATABASE_URL` tenga los valores correctos:

```python
SQLALCHEMY_DATABASE_URL = "postgresql://usuario:contraseña@localhost:5433/agrotech_db"

ejemplo:
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:hola12345@localhost:5433/agrotech_db"
```

Asegúrate de que la base de datos `agrotech_db` exista y que PostgreSQL esté corriendo.

### 5. Ejecutar la aplicación

```bash
uvicorn app.principal:app --reload
```

Esto levantará el servidor en:

```
http://127.0.0.1:8000
```

---

## 🧪 Probar los Endpoints

Abre tu navegador en:

```
http://127.0.0.1:8000/docs
```

Allí encontrarás la interfaz Swagger para probar los endpoints.

---

## 📄 Notas

- El sistema crea automáticamente las tablas en la base de datos al arrancar si no existen.
- Si haces cambios en los modelos, reinicia la app para aplicar los cambios.
- Asegúrate de que el puerto `5433` de PostgreSQL esté disponible en la otra máquina.

---

## ✅ Recomendaciones

- Usar un entorno virtual para evitar conflictos de dependencias.
- Añadir variables de entorno para mayor seguridad (usuario/contraseña de DB).
- Proteger los endpoints sensibles en producción.

---

## 📬 Contacto

Para dudas o mejoras, puedes escribir a emiliosleimen555@gmail.com
