from typing import List
from dataclasses import dataclass, field
from datetime import datetime, timezone
import uuid

from publication_management.domain.entities.comment import CommentUser

@dataclass
class Publication:
	uuid: str = field(default_factory=uuid.uuid4, init=False)
	title: str
	description: str
	user_uuid: str
	content: List[str] = field(default_factory=list)
	comments: List[CommentUser] = field(default_factory=list) 
	createdAt: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
	updatedAt: datetime = field(default_factory=lambda: datetime.now(timezone.utc))