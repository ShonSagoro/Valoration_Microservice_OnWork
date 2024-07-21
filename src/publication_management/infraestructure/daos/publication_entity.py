from typing import List
from beanie import Document
from pydantic import Field
from enum import Enum
from datetime import datetime, timezone

class PublicationEntity(Document):
    uuid: str  
    title: str
    description: str
    user_uuid: str
    url_image: str
    content: List[str] = Field(default_factory=list)
    createdAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updatedAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))    

    async def insert(self, *args, **kwargs):
        self.updatedAt = datetime.now(timezone.utc)
        await super().insert(*args, **kwargs)

    async def update(self, *args, **kwargs):
        self.updatedAt = datetime.now(timezone.utc)
        await super().update(*args, **kwargs)
