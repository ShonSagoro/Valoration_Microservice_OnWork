from datetime import datetime
from typing import List
from pydantic import BaseModel

from publication_management.application.dtos.response.comment_response import CommentResponse


class PublicationResponse(BaseModel):
    uuid: str
    title: str
    description: str
    user_uuid: str
    content: List[str]
    comments: List[CommentResponse]
    url_image: str
    createdAt: datetime
    updatedAt: datetime
    
    def to_dict(self):
        return {
            "uuid": self.uuid,
            "title": self.title,
            "description": self.description,
            "user_uuid": self.user_uuid,
            "content": self.content,
            "comments": [comment.to_dict() for comment in self.comments],
            "url_image": self.url_image,
            "createdAt": self.createdAt.isoformat(),
            "updatedAt": self.updatedAt.isoformat()
        }