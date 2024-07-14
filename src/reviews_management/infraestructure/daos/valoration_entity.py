from beanie import Document
from bson import ObjectId
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime, timezone
import uuid

class ValorationEntity(Document):
    uuid: str  
    rating: int
    comment: str
    general_review: str
    user_uuid: str
    provider_uuid: str
    createdAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updatedAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))    
    
    def __init__(self, **data):
        if '_id' in data and isinstance(data['_id'], ObjectId):
            data['_id'] = str(data['_id'])
        super().__init__(**data)


    async def insert(self, *args, **kwargs):
        self.updatedAt = datetime.now(timezone.utc)
        await super().insert(*args, **kwargs)

    async def update(self, *args, **kwargs):
        self.updatedAt = datetime.now(timezone.utc)
        await super().update(*args, **kwargs)
