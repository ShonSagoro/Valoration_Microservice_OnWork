from pydantic import BaseModel

class CreateCommentRequest(BaseModel):
    comment: str
    raiting: int
    user_uuid: str
    publication_uuid: str