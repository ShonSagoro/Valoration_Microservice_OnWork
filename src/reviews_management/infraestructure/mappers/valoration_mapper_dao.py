from reviews_management.domain.entities.valoration import Valoration as ValorationDomain
from reviews_management.infraestructure.daos.valoration_entity import ValorationEntity
from reviews_management.domain.entities.comment import CommentRainting
from reviews_management.domain.entities.enum.general_review import GeneralReview

class ValorationMapperDAO:
    @staticmethod
    def from_domain(valoration: ValorationDomain) -> ValorationEntity:
        return ValorationEntity(
            uuid=str(valoration.uuid),
            rating=valoration.comment.rating,
            comment=valoration.comment.comment,
            general_review=valoration.general_review.value,
            user_uuid=valoration.user_uuid,
            provider_uuid=valoration.provider_uuid,
            createdAt=valoration.createdAt,  
            updatedAt=valoration.updatedAt  
        )

    @staticmethod
    def to_update(entity: ValorationEntity, update: ValorationEntity) -> ValorationEntity:
        entity.comment = update.comment
        entity.rating = update.rating
        return entity
    

    @staticmethod
    def to_domain(valoration_dao: ValorationEntity) -> ValorationDomain:
        valoration_domain= ValorationDomain(
            comment=CommentRainting(
                rating=valoration_dao.rating,
                comment=valoration_dao.comment
            ),
            general_review=GeneralReview(valoration_dao.general_review),
            user_uuid=valoration_dao.user_uuid,
            provider_uuid=valoration_dao.provider_uuid,
        )
        valoration_domain.uuid = valoration_dao.uuid
        valoration_domain.createdAt = valoration_dao.createdAt
        valoration_domain.updatedAt = valoration_dao.updatedAt
        return valoration_domain
