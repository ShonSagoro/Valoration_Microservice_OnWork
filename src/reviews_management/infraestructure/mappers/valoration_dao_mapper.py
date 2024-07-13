from reviews_management.domain.entities.comment import CommentRainting
from reviews_management.domain.entities.enum.general_review import GeneralReview
from reviews_management.domain.entities.valoration import Valoration as ValorationDomain
from reviews_management.infraestructure.daos.valoration_entity import ValorationEntity

class ValorationMapperDAO:
    @staticmethod
    def from_domain(valoration: ValorationDomain) -> ValorationEntity:
        return ValorationEntity(
            uuid=valoration.uuid,
            rating=valoration.comment.rating,
            comment=valoration.comment.comment,
            general_review=valoration.general_review.value, 
            user_uuid=valoration.user_uuid,
            provider_uuid=valoration.provider_uuid,
            date=valoration.date
        )

    @staticmethod
    def to_domain(valoration_dao: ValorationEntity) -> ValorationDomain:
        return ValorationDomain(
            uuid=valoration_dao.uuid,
            comment=CommentRainting(  # Asume que `CommentRainting` es parte del dominio
                rating=valoration_dao.rating,
                comment=valoration_dao.comment
            ),            
            general_review=GeneralReview(valoration_dao.general_review),  # Convierte el string al enum
            user_uuid=valoration_dao.user_uuid,
            provider_uuid=valoration_dao.provider_uuid,
            date=valoration_dao.date
        )
