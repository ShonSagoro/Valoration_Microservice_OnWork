from publication_management.application.dtos.request.create_publication_request import CreatePublicationRequest
from publication_management.application.dtos.request.update_publication_request import UpdatePublicationRequest
from publication_management.application.dtos.response.publication_response import PublicationResponse
from publication_management.domain.entities.publication import Publication as PublicationDomain


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
    def to_response(entity: PublicationDomain) -> PublicationResponse:
        return PublicationResponse(
            uuid= entity.uuid,
            title= entity.title,
            description= entity.description,
            user_uuid= entity.user_uuid,
            content= entity.content,
            comments= entity.comments,
            createdAt= entity.createdAt,
            updatedAt= entity.updatedAt
        ).to_dict()