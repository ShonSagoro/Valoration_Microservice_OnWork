from publication_management.infraestructure.daos.publication_entity import PublicationEntity, publicationEntity
from reviews_management.domain.entities.enum.general_review import GeneralReview
from publication_management.domain.entities.publication import Publication as PublicationDomain

class PublicationMapperDAO:
    @staticmethod
    def from_domain(publication: PublicationDomain) -> PublicationEntity:
        return publicationEntity(
            uuid=str(publication.uuid),
            title=publication.publication.title,
            description=publication.publication.description,
            user_uuid=publication.user_uuid,
            content=publication.content,
            createdAt=publication.createdAt,  
            updatedAt=publication.updatedAt  
        )
        
    @staticmethod
    def to_update(entity: PublicationEntity, update: PublicationEntity) -> PublicationEntity:
        entity.title = update.title
        entity.description = update.description
        return entity
    
    @staticmethod
    def to_domain(publication_dao: PublicationEntity) -> PublicationDomain:
        publication_domain= PublicationDomain(
            title=publication_dao.title,
            description=publication_dao.description,
            user_uuid=publication_dao.user_uuid,
        )
        publication_domain.uuid = publication_dao.uuid
        publication_domain.content = publication_dao.content
        publication_domain.createdAt = publication_dao.createdAt
        publication_domain.updatedAt = publication_dao.updatedAt
        return publication_domain
