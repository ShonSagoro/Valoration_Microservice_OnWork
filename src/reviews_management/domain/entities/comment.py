from dataclasses import dataclass, field
from reviews_management.domain.entities.enum.general_review import GeneralReview

@dataclass
class CommentRainting:
    rating: int
    comment: str