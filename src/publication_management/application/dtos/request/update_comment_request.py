from pydantic import BaseModel

class UpdateCommentRequest(BaseModel):
    comment: str
    rating: int