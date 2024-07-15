import logging
from publication_management.application.dtos.request.create_publication_request import CreatePublicationRequest
from publication_management.application.mappers.publication_mappers_dtos import PublicationMapperDTO
from publication_management.domain.ports.publication_interface import PublicationInterface
from reviews_management.application.dtos.response.base_response import BaseResponse

logger = logging.getLogger(__name__)

class CreatePublicationUseCase:
    def __init__(self, repository: PublicationInterface):
        self.repository = repository

    async def execute(self, publication: CreatePublicationRequest) -> BaseResponse:
        publicationDomain = PublicationMapperDTO.to_domain_publication_create(publication)
        if publicationDomain is None:
            return BaseResponse(
                data=None,
                message="Bad request",
                status=False,
                status_code=400
            )
        result = await self.repository.create_publication(publicationDomain)

        if result is None:
            return BaseResponse(
                data=None,
                message="publication not created",
                status=False,
                status_code=400
            )
        return BaseResponse(
            data=PublicationMapperDTO.to_response_publication(result),
            message="publication created successfully",
            status=True,
            status_code=201
        )