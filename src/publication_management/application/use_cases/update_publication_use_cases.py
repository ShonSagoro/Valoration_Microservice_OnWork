from publication_management.application.dtos.request.update_publication_request import UpdatePublicationRequest
from publication_management.application.mappers.publication_mapper_dtos import PublicationMapperDTO
from publication_management.domain.ports.publication_interface import PublicationInterface
from reviews_management.application.dtos.response.base_response import BaseResponse


class UpdatePublicationUseCase:
    def __init__(self, repository: PublicationInterface):
        self.repository = repository

    async def execute(self, uuid:str, publication: UpdatePublicationRequest) -> BaseResponse:
        publicationDomain = PublicationMapperDTO.to_domain_update(publication)
        if publicationDomain is None:
            return BaseResponse(
                data=None,
                message="Bad request",
                status=False,
                status_code=400
            )
        result = await self.repository.update_publication(uuid, publicationDomain)
        if result is None:
            return BaseResponse(
                data=None,
                message="publication not updated",
                status=False,
                status_code=400
            )
        return BaseResponse(
            data=PublicationMapperDTO.to_response(result),
            message="publication updated successfully",
            status=True,
            status_code=200
        )