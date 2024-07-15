from dataclasses import dataclass, field
from datetime import datetime, timezone
import uuid


@dataclass
class CommentUser:
    uuid: str = field(default_factory=uuid.uuid4, init=False)
    rating: int
    comment: str
    user_uuid: str
    publication_uuid: str
    createdAt: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updatedAt: datetime = field(default_factory=lambda: datetime.now(timezone.utc))  