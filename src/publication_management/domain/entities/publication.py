from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import List
from uuid import uuid1

from publication_management.domain.entities.comment import CommentUser


@dataclass
class Publication:
    uuid: str = field(default_factory=uuid1.uuid4, init=False)
    title: str
    description: str
    user_uuid: str
    content: List[str] = []
    comments: List[CommentUser] = []
    createdAt: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updatedAt: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    