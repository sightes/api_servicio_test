📄 Propuesta Técnica - API de Beneficiarios


📆 Descripción General

Esta propuesta describe la arquitectura, mecanismos de seguridad y despliegue experimental de una API REST desarrollada con FastAPI para consultar información de beneficiarios desde una base de datos PostgreSQL.

El objetivo es disponibilizar datos relevantes mediante una API ligera, documentada, segura y con mecanismos modernos de acceso y control.

🚀 Despliegue Experimental

El script fue desplegado de forma experimental en una máquina virtual (VPS) de BlueHosting, con las siguientes características:

Sistema operativo: Ubuntu 22.04 LTS

Recursos: 1 vCPU y 2 GB de RAM

PostgreSQL 17 corriendo localmente

La API FastAPI se conecta a la base de datos por socket local dentro de la misma máquina. La exposición al exterior se realiza a través del puerto 8000, usando un dominio personalizado sght.cl configurado mediante Cloudflare (DNS gratuito).


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


🔐 Seguridad: API Key + Rate Limiting

La API requiere el uso de un header personalizado: X-API-Key

Solo se procesan solicitudes que incluyan una clave válida definida en .env

Se implementó rate limiting con slowapi: 10 solicitudes por minuto por IP

⚙️ Optimizaciones y buenas prácticas

✅ Uso de FastAPI + Uvicorn: asincronismo y eficiencia

✅ Compresión activada con GZipMiddleware

✅ Paginación de resultados (limit, skip)

✅ Variables de entorno gestionadas con python-dotenv

🌐 Endpoints disponibles

GET /beneficiaries
# Lista de beneficiarios (con paginación)
curl -H "X-API-Key: [API_KEY]" "http://sght.cl:8000/beneficiaries?skip=0&limit=10"

GET /beneficiaries/{id}
# Beneficiario por ID
curl -H "X-API-Key: [API_KEY]" "http://sght.cl:8000/beneficiaries/1"

GET /beneficiaries/program/{program_name}
# Beneficiarios por programa
curl -H "X-API-Key: [API_KEY]" "http://sght.cl:8000/beneficiaries/program/P3"


⚙️ Consideraciones de rendimiento, escalabilidad y eficiencia
	
  •	Rendimiento: la API fue desarrollada con FastAPI, un framework asincrónico que utiliza uvicorn como servidor ASGI, permitiendo tiempos de respuesta muy bajos y alta concurrencia. El acceso a datos se realiza mediante consultas SQL eficientes usando LIMIT y OFFSET, lo que facilita la paginación sin sobrecargar el servidor.

  •	Escalabilidad: la arquitectura es fácilmente escalable horizontalmente, permitiendo múltiples instancias detrás de un balanceador de carga. La conexión a la base de datos puede migrarse a servicios gestionados (como Cloud SQL o RDS) para separar preocupaciones.
	
  •	Eficiencia: se integró rate limiting con slowapi para mitigar abusos y bots, y compresión GZIP para reducir el tamaño de las respuestas. Además, la paginación evita el envío de grandes volúmenes de datos innecesarios.
  
  
💡 Reflexión: tecnologías modernas que podrían aportar valor
	
    •	GraphQL: permitiría a los clientes consumir solo los campos requeridos, optimizando tráfico y flexibilidad, especialmente útil para aplicaciones móviles o de frontend dinámico.

    •	Caching distribuido (Redis o CDN Edge Cache): para endpoints de alta demanda como /beneficiaries, aplicar cache por programa o por ID podría reducir significativamente la carga en la base de datos.

	•	Serverless (Cloud Run, AWS Lambda): permitiría una arquitectura autoscalable y de bajo costo para cargas variables, ideal para APIs eventuales o bajo demanda.

	•	Docker + CI/CD (GitHub Actions + Vercel/Render): para automatizar despliegues y facilitar entornos reproducibles con infraestructura como código.  