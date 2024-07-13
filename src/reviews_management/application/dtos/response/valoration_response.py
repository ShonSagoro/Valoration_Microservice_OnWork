from pydantic import BaseModel
import datetime

class ValorationResponse(BaseModel):
    uuid: str
    rating: int
    comment: str
    user_uuid: str
    general_review: str
    provider_uuid: str
    createdAt: datetime.datetime
    updatedAt: datetime.datetime
