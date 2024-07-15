from pydantic import BaseModel

class UpdateValorationRequest(BaseModel):
    rating: int
    comment: str