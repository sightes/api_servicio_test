from pydantic import BaseModel

class Beneficiary(BaseModel):
    id: int
    name: str
    age: int
    program: str


