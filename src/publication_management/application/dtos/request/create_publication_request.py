from pydantic import BaseModel

class CreatePublicationRequest(BaseModel):
    title: str
    description: str
    user_uuid: str