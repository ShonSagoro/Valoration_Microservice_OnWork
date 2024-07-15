from datetime import datetime
from pydantic import BaseModel


class CommentResponse(BaseModel):
    uuid: str
    comment: str
    rating: int
    user_uuid: str
    publication_uuid: str
    createdAt: datetime
    updatedAt: datetime
    
    def to_dict(self):
        return {
            "uuid": self.uuid,
            "comment": self.comment,
            "rating": self.rating,
            "user_uuid": self.user_uuid,
            "publication_uuid": self.publication_uuid,
            "user_uuid": self.user_uuid,
            "createdAt": self.createdAt.isoformat(),
            "updatedAt": self.updatedAt.isoformat()
        }