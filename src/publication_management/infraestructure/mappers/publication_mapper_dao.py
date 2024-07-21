from publication_management.infraestructure.daos.publication_entity import PublicationEntity
from publication_management.domain.entities.publication import Publication as PublicationDomain

class PublicationMapperDAO:
    @staticmethod
    def from_domain(publication: PublicationDomain) -> PublicationEntity:
        return PublicationEntity(
            uuid=str(publication.uuid),
            title=str(publication.title),
            url_image=publication.url_image,
            description=publication.description,
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
            url_image=publication_dao.url_image
        )
        publication_domain.uuid = publication_dao.uuid
        publication_domain.content = publication_dao.content
        publication_domain.createdAt = publication_dao.createdAt
        publication_domain.updatedAt = publication_dao.updatedAt
        return publication_domain
