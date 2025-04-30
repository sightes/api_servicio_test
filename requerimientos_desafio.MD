# Prueba Técnica - Encargado de Bases de Datos

## 📝 Contexto y Objetivo General

En ProEmpleo, necesitamos disponibilizar datos almacenados en una base SQL Server ubicada en una máquina virtual (IaaS) Windows, mediante una API REST, para ser consumidos fácilmente desde plataformas web, aplicaciones móviles u otros sistemas mediante mecanismos modernos y eficientes de consulta.

Esta prueba busca evaluar tu capacidad para plantear y desarrollar una solución técnica viable, segura y escalable, usando las tecnologías que prefieras entre las listadas.

## 📂 Archivos entregados

Recibes estos archivos en el paquete ZIP:

- `beneficiaries_mock_updated.csv`: datos anonimizados para utilizar.
- `create_table.sql`: script para crear la tabla en SQL Server localmente.

## 🚩 Desafío Técnico

### 1. Importar los datos

Utiliza el archivo CSV entregado para crear la tabla en una base de datos local SQL Server. Puedes usar herramientas gratuitas como SQL Server Express, Docker o cualquier otra que te facilite el desarrollo local.

### 2. Crear una API REST

Desarrolla una API REST sencilla que permita, al menos:

- **GET `/beneficiaries`**: Obtener lista de beneficiarios (con paginación opcional).
- **GET `/beneficiaries/{id}`**: Obtener información de un beneficiario específico.
- **GET `/beneficiaries/program/{program}`**: Obtener beneficiarios filtrados por programa.

### 🛠 Tecnologías permitidas (elige una):

- **Node.js**, **Deno**, **Bun**
- **Python** (FastAPI, Flask, Django REST Framework, etc.)
- **Otra**

Se evaluará la claridad del código, seguridad básica, organización del proyecto y buenas prácticas (estructura, comentarios, manejo de errores, etc.).

### 3. Propuesta técnica escrita

Redacta un breve documento (`PROPUESTA_TECNICA.md` o `.pdf`) donde expliques claramente:

- **Cómo simularías o configurarías una conexión segura desde una API alojada en una VM Windows hacia una base de datos SQL Server**, considerando aspectos como firewall, puertos, seguridad, rendimiento y mejores prácticas de la industria.
- **Si no tienes cómo desplegar realmente una VM**, describe conceptualmente cómo configurarías esta infraestructura y qué herramientas utilizarías (ej. VPN, SSH Tunnel, Cloud SQL Proxy, etc.).

### 4. Reflexión final (muy breve)

En tu propuesta técnica, añade un apartado al final respondiendo:

- ¿Propondrías una solución diferente para este problema? ¿Cuál sería y por qué?
- ¿Qué mecanismos adicionales o más actuales (por ejemplo GraphQL, caching, serverless functions, etc.) recomendarías utilizar para mejorar la eficiencia y rendimiento en consultas desde aplicaciones web o móviles?

### 🔄 Reproducibilidad del proyecto

Es muy importante que la solución que desarrolles pueda ser replicada fácilmente en otras máquinas utilizando únicamente el repositorio público de GitHub donde subirás tu proyecto. Asegúrate de incluir instrucciones claras y detalladas sobre cómo configurar y ejecutar tu proyecto localmente en el `README.md` del repositorio.

## 🚀 Modalidad de Entrega

- Sube el proyecto completo (código fuente y documentación) a un repositorio público en **GitHub**.
- El repositorio debe contener:
  - Código fuente claramente comentado.
  - Breve documento técnico (`PROPUESTA_TECNICA.md` o `.pdf`).
  - Archivo breve (`README.md`) que indique cómo ejecutar tu proyecto.

- (Opcional) Puedes desplegar tu solución gratuitamente en plataformas como **Railway**, **Vercel**, **AWS**, **Azure**, etc. (no obligatorio, pero aporta valor adicional).

## 🧾 Aspectos importantes para tu desarrollo local

**Para simular el entorno IaaS:**

- No necesitas tener acceso real a una infraestructura IaaS (VM en la nube). Puedes desarrollar y testear en tu máquina local simulando un entorno similar usando Docker, máquinas virtuales locales (VirtualBox, VMware), o incluso directamente con SQL Server instalado localmente.

**Bases de datos:**

- Puedes usar **SQL Server Express (gratuito)**, Docker, Azure SQL (gratuito en modalidad prueba), o cualquier alternativa gratuita compatible.

**API REST:**

- Asegúrate de usar librerías estándar, frameworks robustos y estables según la tecnología que escojas (Express, FastAPI, Flask, Oak para Deno, etc.).

## ✅ Criterios de evaluación

- Claridad, coherencia y calidad general del código.
- Seguridad básica implementada en la solución propuesta.
- Claridad en la documentación y propuesta técnica.
- Razonabilidad y realismo de tu solución frente al problema propuesto.
- Consideración de aspectos adicionales como rendimiento, escalabilidad y eficiencia.
- Breve reflexión sobre otras alternativas tecnológicas modernas que podrían aportar valor.

## 📆 Plazo sugerido

- **2 días hábiles desde la recepción de esta prueba**.

¡Mucho éxito, esperamos ver tu mejor trabajo!