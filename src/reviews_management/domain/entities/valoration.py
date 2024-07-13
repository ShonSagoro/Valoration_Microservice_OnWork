from dataclasses import dataclass, field
import datetime
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
    createdAt: datetime.datetime = field(default_factory=datetime.datetime.utcnow, init=False)
    updatedAt: datetime.datetime = field(default_factory=datetime.datetime.utcnow, init=False)
