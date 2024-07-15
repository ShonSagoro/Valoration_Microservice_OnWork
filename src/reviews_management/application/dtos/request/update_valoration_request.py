from pydantic import BaseModel

class UpdateValorationRequest(BaseModel):
    raiting: int
    comment: str