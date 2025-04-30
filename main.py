#lectura de librerias carga 

from fastapi import FastAPI, HTTPException, Query, Depends, Header,status,Request
from typing import List, Optional
from database import get_db_connection
from models import Beneficiary
from datetime import date
import os
from dotenv import load_dotenv
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address
from fastapi.middleware.gzip import GZipMiddleware




load_dotenv()
API_KEY = os.getenv("API_KEY")

#funcion que verifica que la apikey exista , verifica informacion en .env local esto puede ser trasladado a una variable de entorno en plataforma cloud
def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Falta apikey o es incorrecta",
        )



#app fastapi con checkeo de apikey
app = FastAPI(dependencies=[Depends(verify_api_key)])
limiter = Limiter(key_func=get_remote_address)
#elementos de seguridad para evitar sobre llamada
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)



# aqui endpoint infformacion por beneficiario
#llamada : curl -H "X-API-Key: [API_KEY]" "http://localhost:8000/beneficiaries?skip=0&limit=10"
#por defaul toma los 100 primeros y pagina 0 si es que no se indica ( evita traer demasiada data )
@app.get("/beneficiaries", response_model=List[Beneficiary])
@limiter.limit("5/minute")
def get_beneficiaries(request: Request,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, gt=0, le=1000),
    
):
    conn = get_db_connection()
    cursor = conn.cursor()
    #conexion a db 
    cursor.execute(
        """
        SELECT id, first_name, last_name, gender, birth_date, rut_number, program, process_date
        FROM beneficiaries
        ORDER BY id
        LIMIT %s OFFSET %s
        """,
        (limit, skip)
    )
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        raise HTTPException(status_code=404, detail="no se encuentra informacion")

    beneficiaries = []
    for row in rows:
        age = None
        if row[4]:  # birth_date
            today = date.today()
            age = today.year - row[4].year - ((today.month, today.day) < (row[4].month, row[4].day))

        beneficiaries.append(Beneficiary(
            id=row[0],
            name=f"{row[1]} {row[2]}",
            age=age,
            program=row[6]
        ))
    return beneficiaries

# aqui endpoint infformacion por beneficiario
#llamada : curl -H "X-API-Key: [API_KEY]" "http://localhost:8000/beneficiaries/1"

@app.get("/beneficiaries/{beneficiary_id}", response_model=Beneficiary)
@limiter.limit("5/minute")
def get_beneficiary(request: Request,beneficiary_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    #conexion a db 
    cursor.execute(
        "SELECT id, first_name, last_name, gender, birth_date, rut_number, program, process_date FROM beneficiaries WHERE id = %s",
        (beneficiary_id,)  # <-- pasa como tupla
    )
    row = cursor.fetchone()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="No existe Beneficiario con ese id")
    
    # Calcula edad si birth_date existe
    age = None
    if row[4]:  # birth_date
        today = date.today()
        age = today.year - row[4].year - ((today.month, today.day) < (row[4].month, row[4].day))
    
    return Beneficiary(
        id=row[0],
        name=f"{row[1]} {row[2]}",  # Combina first_name + last_name
        age=age,
        program=row[6]
    )


# aqui endpoint infformacion por beneficiario
#llamada : curl -H "X-API-Key: [API_KEY]" "http://localhost:8000/beneficiaries/program/P3"

@app.get("/beneficiaries/program/{program_name}", response_model=List[Beneficiary])
@limiter.limit("5/minute")
def get_beneficiaries_by_program(request: Request,program_name: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    #conexion a db 
    cursor.execute(
    "SELECT id, first_name, last_name, gender, birth_date, rut_number, program, process_date FROM beneficiaries WHERE program = %s",
    (program_name,)
)
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        raise HTTPException(status_code=404, detail="No se enuentran beneficiarios en este programa")
    
    beneficiaries = []
    for row in rows:
        age = None
        if row[4]:  # birth_date
            today = date.today()
            age = today.year - row[4].year - ((today.month, today.day) < (row[4].month, row[4].day))

        beneficiaries.append(Beneficiary(
            id=row[0],
            name=f"{row[1]} {row[2]}",  # Combinar first_name y last_name
            age=age,
           program=row[6]
        ))
 
    return beneficiaries