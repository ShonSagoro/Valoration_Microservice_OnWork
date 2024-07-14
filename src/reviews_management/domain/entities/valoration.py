from dataclasses import dataclass, field
from datetime import datetime, timezone
from reviews_management.domain.entities.comment import CommentRainting
from reviews_management.domain.entities.enum.general_review import GeneralReview
import uuid

@dataclass
class Valoration:
    uuid: str = field(default_factory=uuid.uuid4, init=False)
    comment: CommentRainting
    general_review: GeneralReview
    user_uuid: str
    provider_uuid: str
    createdAt: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updatedAt: datetime = field(default_factory=lambda: datetime.now(timezone.utc))    
    