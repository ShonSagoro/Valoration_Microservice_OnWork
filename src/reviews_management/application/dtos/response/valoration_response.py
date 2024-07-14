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

    def to_dict(self):
        return {
            "uuid": self.uuid,
            "rating": self.rating,
            "comment": self.comment,
            "general_review": self.general_review,
            "user_uuid": self.user_uuid,
            "provider_uuid": self.provider_uuid,
            "createdAt": self.createdAt.isoformat(),
            "updatedAt": self.updatedAt.isoformat()
        }