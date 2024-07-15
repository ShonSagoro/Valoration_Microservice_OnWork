from publication_management.application.dtos.request.create_publication_request import CreatePublicationRequest
from publication_management.application.dtos.request.update_publication_request import UpdatePublicationRequest
from publication_management.application.dtos.response.publication_response import PublicationResponse
from publication_management.domain.entities import Publication as PublicationDomain


class PublicationMapperDTO:
    @staticmethod
    def to_domain_create(request: CreatePublicationRequest) -> PublicationDomain:
        return PublicationDomain(
            title=request.title,
            description=request.description,
            user_uuid=request.user_uuid,
        )
        
    @staticmethod
    def to_domain_update(request: UpdatePublicationRequest) -> PublicationDomain:
          return PublicationDomain(
            title=request.title,
            description=request.description,
            user_uuid="",
        )
        

    @staticmethod
    def to_response(comment: PublicationDomain) -> PublicationResponse:
        return PublicationResponse(
            uuid= comment.uuid,
            title= comment.comment,
            description= comment.raiting,
            user_uuid= comment.user_uuid,
            content= comment.content,
            comments= comment.comments,
            createdAt= comment.createdAt,
            updatedAt= comment.updatedAt
        )