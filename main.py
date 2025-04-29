from fastapi import FastAPI, HTTPException
from typing import List, Optional
from database import get_db_connection
from models import Beneficiary
from datetime import date

app = FastAPI()

@app.get("/beneficiaries", response_model=List[Beneficiary])
def get_beneficiaries(skip: int = 0, limit: int = 10):
    conn = get_db_connection()
    cursor = conn.cursor()
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
        raise HTTPException(status_code=404, detail="No beneficiaries found")
    beneficiaries = []
    for row in rows:
        # Asumiendo que birth_date es un date, no un string
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


@app.get("/beneficiaries/{beneficiary_id}", response_model=Beneficiary)
def get_beneficiary(beneficiary_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, first_name, last_name, gender, birth_date, rut_number, program, process_date FROM beneficiaries WHERE id = %s",
        (beneficiary_id,)  # <-- pasa como tupla
    )
    row = cursor.fetchone()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Beneficiary not found")
    
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

@app.get("/beneficiaries/program/{program_name}", response_model=List[Beneficiary])
def get_beneficiaries_by_program(program_name: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
    "SELECT id, first_name, last_name, gender, birth_date, rut_number, program, process_date FROM beneficiaries WHERE program = %s",
    (program_name,)
)
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        raise HTTPException(status_code=404, detail="No beneficiaries found for this program")
    
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