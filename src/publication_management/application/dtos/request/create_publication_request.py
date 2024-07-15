from pydantic import BaseModel

class CreatePublicationRequest(BaseModel):
    title: str
    description: str
    description: str