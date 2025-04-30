from pydantic import BaseModel
from typing import Optional
class Beneficiary(BaseModel):
    id: int
    name: str
    age: Optional[int]  #puede ser None
    gender: str
    birth_date: str
    rut_number: str
    program: str
    process_date: str