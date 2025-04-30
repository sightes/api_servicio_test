📘 Documentación de la API: Beneficiaries Service

🔧 Descripción general

Esta API REST permite acceder a información de beneficiarios almacenados en una base de datos PostgreSQL. La API fue desarrollada con FastAPI, y permite autenticación por API Key, paginación, filtrado por programa y protección básica contra abuso vía rate-limiting.

🚀 Endpoints disponibles

Todos los endpoints requieren autenticación con API Key en el header:

```html
X-API-Key: [API_KEY]
```

---

📄 GET /beneficiaries

Devuelve una lista paginada de beneficiarios.

🔸 Parámetros opcionales:
	•	skip: entero ≥ 0 (por defecto 0)
	•	limit: entero ≤ 1000 (por defecto 100)

✅ Ejemplo curl:

 ```curl
 curl -H "X-API-Key: [API_KEY]" "http://localhost:8000/beneficiaries?skip=0&limit=10"
 ```

---

  📄 GET /beneficiaries/{id}

Devuelve un beneficiario específico por su ID.

✅ Ejemplo curl:

```curl
curl -H "X-API-Key: [API_KEY]" "http://localhost:8000/beneficiaries/1"
```
---

📄 GET /beneficiaries/program/{program_name}

Filtra beneficiarios por el nombre del programa al que pertenecen.

✅ Ejemplo curl:
```curl
curl -H "X-API-Key: [API_KEY]" "http://localhost:8000/beneficiaries/program/P3"
```

⚙️ Rate Limiting

Para proteger el servicio contra abuso, los endpoints están limitados a 10 solicitudes por minuto si se supera el límite, se devuelve un error 429 Too Many Requests.


🛠 Instalación local
	1.	Clonar el repositorio
	2.	Crear entorno virtual
	3.	Instalar dependencias:
  
  ```bash
  pip install -r requirements.txt
  ````
  Crear un archivo .env con las siguientes variables:

DB_SERVER=
DB_PORT=
DB_DATABASE=
DB_USERNAME=
DB_PASSWORD=
API_KEY=


carga de datos en servidor psql 

psql -U sightes -d proempleo -f create_table.sql
\copy beneficiaries FROM 'beneficiaries_mock_updated.csv' WITH (FORMAT csv, HEADER true)

ejecucion de api 

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

📦 Dependencias principales

El script funciona con python 3.10 bajo las dependencias listadas en requirements.txt

```html
fastapi
uvicorn
psycopg2-binary
python-dotenv
slowapi
brotli
pandas
numpy
```


📁 Estructura del proyecto
```text
.
├── main.py                 ← Entrypoint de la API
├── database.py             ← Conexión a PostgreSQL
├── models.py               ← Modelos Pydantic
├── requirements.txt
├── .env                    ← Variables de entorno
├── beneficiaries_mock_updated.csv
├── create_table.sql
└── README.md
```

🧪 Comandos curl para probar la API

Importante: todos los endpoints requieren el header X-API-Key.


# Lista de beneficiarios (con paginación)
curl -H "X-API-Key: [API_KEY]" "http://sght.cl:8000/beneficiaries?skip=0&limit=10"

# Beneficiario por ID
curl -H "X-API-Key: [API_KEY]" "http://sght.cl:8000/beneficiaries/1"

# Beneficiarios por programa
curl -H "X-API-Key: [API_KEY]" "http://sght.cl:8000/beneficiaries/program/P3"
