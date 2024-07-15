from dataclasses import dataclass, field
import datetime
from reviews_management.domain.entities.enum.general_review import GeneralReview
import uuid

@dataclass
class CommentRainting:
    raiting: int
    comment: str