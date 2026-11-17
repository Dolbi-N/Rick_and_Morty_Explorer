from pydantic import BaseModel


class Character(BaseModel):
    id: int
    name: str
    status: str
    species: str
    gender: str
    origin: str
    location: str
    image: str