from pydantic import BaseModel


class UpdatePublicationRequest(BaseModel):
    title: str
    description: str