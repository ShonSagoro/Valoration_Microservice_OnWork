from beanie import Document
from pydantic import Field
from enum import Enum
from datetime import datetime, timezone

class ValorationEntity(Document):
    uuid: str  
    rating: int
    comment: str
    general_review: str
    user_uuid: str
    provider_uuid: str
    createdAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updatedAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))    

    async def insert(self, *args, **kwargs):
        self.updatedAt = datetime.now(timezone.utc)
        await super().insert(*args, **kwargs)

    async def update(self, *args, **kwargs):
        self.updatedAt = datetime.now(timezone.utc)
        await super().update(*args, **kwargs)
