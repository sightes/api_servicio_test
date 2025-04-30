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

.
├── main.py                 ← Entrypoint de la API
├── database.py             ← Conexión a PostgreSQL
├── models.py               ← Modelos Pydantic
├── requirements.txt
├── .env                    ← Variables de entorno
├── beneficiaries_mock_updated.csv
├── create_table.sql
└── README.md


⚙️ Consideraciones de rendimiento, escalabilidad y eficiencia
	
  •	Rendimiento: la API fue desarrollada con FastAPI, un framework asincrónico que utiliza uvicorn como servidor ASGI, permitiendo tiempos de respuesta muy bajos y alta concurrencia. El acceso a datos se realiza mediante consultas SQL eficientes usando LIMIT y OFFSET, lo que facilita la paginación sin sobrecargar el servidor.

  •	Escalabilidad: la arquitectura es fácilmente escalable horizontalmente, permitiendo múltiples instancias detrás de un balanceador de carga. La conexión a la base de datos puede migrarse a servicios gestionados (como Cloud SQL o RDS) para separar preocupaciones.
	
  •	Eficiencia: se integró rate limiting con slowapi para mitigar abusos y bots, y compresión GZIP para reducir el tamaño de las respuestas. Además, la paginación evita el envío de grandes volúmenes de datos innecesarios.

💡 Reflexión: tecnologías modernas que podrían aportar valor
	
  •	GraphQL: permitiría a los clientes consumir solo los campos requeridos, optimizando tráfico y flexibilidad, especialmente útil para aplicaciones móviles o de frontend dinámico.

	•	Caching distribuido (Redis o CDN Edge Cache): para endpoints de alta demanda como /beneficiaries, aplicar cache por programa o por ID podría reducir significativamente la carga en la base de datos.

	•	Serverless (Cloud Run, AWS Lambda): permitiría una arquitectura autoscalable y de bajo costo para cargas variables, ideal para APIs eventuales o bajo demanda.

	•	Docker + CI/CD (GitHub Actions + Vercel/Render): para automatizar despliegues y facilitar entornos reproducibles con infraestructura como código.  


🚀 Despliegue Experimental

El script de esta API fue desplegado de forma experimental en una máquina virtual (VPS) hospedada en BlueHosting, corriendo Ubuntu 22.04 LTS, equipada con 1 CPU virtual y 2 GB de RAM.
Dentro de esta misma instancia corre un servidor de base de datos PostgreSQL 17 en modo local, al cual la API accede directamente mediante conexión interna.
La API desarrollada en FastAPI expone sus servicios al exterior a través del puerto 8000, utilizando un nombre de dominio personalizado (sght.cl) gestionado gratuitamente mediante Cloudflare, lo que permite acceso público y seguro sin necesidad de exponer directamente la IP del servidor.

```text

                    Internet
                        │
                ┌──────▼──────┐
                │  Cloudflare │
                │ (DNS Proxy) │
                └──────┬──────┘
                       │
          sght.cl → 45.7.xxx.xxx:8000
                       │
        ┌──────────────▼──────────────┐
        │ VPS (BlueHosting - Ubuntu) │
        │  CPU: 1 vCore / RAM: 2 GB   │
        │  - FastAPI app (puerto 8000)│
        │  - PostgreSQL 17 (localhost)│
        └─────────────────────────────┘

```

🧪 Comandos curl para probar la API

Importante: todos los endpoints requieren el header X-API-Key.


# Lista de beneficiarios (con paginación)
curl -H "X-API-Key: [API_KEY]" "http://sght.cl:8000/beneficiaries?skip=0&limit=10"

# Beneficiario por ID
curl -H "X-API-Key: [API_KEY]" "http://sght.cl:8000/beneficiaries/1"

# Beneficiarios por programa
curl -H "X-API-Key: [API_KEY]" "http://sght.cl:8000/beneficiaries/program/P3"
