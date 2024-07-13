from pydantic import BaseModel, constr, conint
from uuid import UUID


class CreateValorationRequest(BaseModel):
    user_uuid: str
    provider_uuid: str
    rating: int
    comment: str