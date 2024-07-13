from beanie import Document
from pydantic import BaseModel, Field
from enum import Enum
import datetime
import uuid

class ValorationEntity(Document):
    uuid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    rating: int
    comment: str
    general_review: str
    user_uuid: str
    provider_uuid: str
    createdAt: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    updatedAt: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

    async def insert(self, *args, **kwargs):
        if not self.createdAt:
            self.createdAt = datetime.datetime.utcnow()
        self.updatedAt = datetime.datetime.utcnow()
        await super().insert(*args, **kwargs)

    async def update(self, *args, **kwargs):
        self.updatedAt = datetime.datetime.utcnow()
        await super().update(*args, **kwargs)
