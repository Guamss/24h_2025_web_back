from uuid import UUID
from pydantic import BaseModel


class PersonIn(BaseModel):
    name: str
    age: int
    address: str

class PersonOut(BaseModel):
    id: UUID
    name: str
    age: int
    address: str