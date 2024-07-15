from publication_management.application.dtos.request.create_comment_request import CreateCommentRequest
from publication_management.application.dtos.request.update_comment_request import UpdateCommentRequest
from publication_management.application.dtos.response.comment_response import CommentResponse
from publication_management.domain.entities.comment import CommentUser as CommentDomain

class CommentMapperDTO:
    @staticmethod
    def to_domain_create(request: CreateCommentRequest) -> CommentDomain:
        return CommentDomain(
            rating=request.rating,
            comment=request.comment,
            publication_uuid=request.publication_uuid,
            user_uuid=request.user_uuid,
        )
        
    @staticmethod
    def to_domain_update(request: UpdateCommentRequest) -> CommentDomain:
        return CommentDomain(
            rating=request.rating,
            comment=request.comment,
            publication_uuid="",
            user_uuid="",
        )

    @staticmethod
    def to_response(comment: CommentDomain) -> CommentResponse:
        return CommentResponse(
            uuid= comment.uuid,
            comment= comment.comment,
            rating= comment.rating,
            user_uuid= comment.user_uuid,
            publication_uuid= comment.publication_uuid,
            createdAt= comment.createdAt,
            updatedAt= comment.updatedAt
        ).to_dict()