from publication_management.infraestructure.daos.comment_entity import CommentEntity
from reviews_management.domain.entities.enum.general_review import GeneralReview
from publication_management.domain.entities.comment import CommentUser as CommentDomain

class CommentMapperDAO:
    @staticmethod
    def from_domain(comment: CommentDomain) -> CommentEntity:
        return CommentEntity(
            uuid=str(comment.uuid),
            raiting=comment.comment.raiting,
            comment=comment.comment.comment,
            user_uuid=comment.user_uuid,
            publication_uuid=comment.publication_uuid,
            createdAt=comment.createdAt,  
            updatedAt=comment.updatedAt  
        )

    @staticmethod
    def to_update(entity: CommentEntity, update: CommentEntity) -> CommentEntity:
        entity.comment = update.comment
        entity.raiting = update.raiting
        return entity
    
    @staticmethod
    def to_domain(comment_dao: CommentEntity) -> CommentDomain:
        comment_domain= CommentDomain(
            raiting=comment_dao.raiting,
            comment=comment_dao.comment,
            user_uuid=comment_dao.user_uuid,
            publication_uuid=comment_dao.publication_uuid,
        )
        comment_domain.uuid = comment_dao.uuid
        comment_domain.createdAt = comment_dao.createdAt
        comment_domain.updatedAt = comment_dao.updatedAt
        return comment_domain
