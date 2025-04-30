from pydantic import BaseModel
from typing import Optional
class Beneficiary(BaseModel):
    id: int
    name: str
    age: Optional[int]  #puede ser None
    program: str


