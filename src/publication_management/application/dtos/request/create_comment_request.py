from pydantic import BaseModel

class CreateCommentRequest(BaseModel):
    comment: str
    rating : int
    user_uuid: str
    publication_uuid: str