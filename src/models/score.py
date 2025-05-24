from uuid import UUID
from pydantic import BaseModel


class ScoreDAO(BaseModel):
    name: str
    score: int

class ScoreDTO(BaseModel):
    name: str
    score: int