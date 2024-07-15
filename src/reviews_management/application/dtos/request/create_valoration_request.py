from pydantic import BaseModel, constr, conint

class CreateValorationRequest(BaseModel):
    user_uuid: str
    provider_uuid: str
    rating: int
    comment: str