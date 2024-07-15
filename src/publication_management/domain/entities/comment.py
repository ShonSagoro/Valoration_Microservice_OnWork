from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid1


@dataclass
class CommentUser:
    uuid: str = field(default_factory=uuid1.uuid4, init=False)
    comment: str
    raiting: int
    user_uuid: str
    publication_uuid: str
    createdAt: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updatedAt: datetime = field(default_factory=lambda: datetime.now(timezone.utc))  