import logging
from publication_management.application.mappers.publication_mapper_dtos import PublicationMapperDTO
from publication_management.domain.ports.publication_interface import PublicationInterface
from reviews_management.application.dtos.response.base_response import BaseResponse

logger = logging.getLogger(__name__)

class ListPublicationUseCase:
    def __init__(self, repository: PublicationInterface):
        self.repository = repository

    async def execute(self) -> BaseResponse:
        publications = await self.repository.list_publication()
        responses = [PublicationMapperDTO.to_response(publication) for publication in publications]
        return BaseResponse(
            data=responses,
            message="publications listed successfully",
            status=True,
            status_code=302
        )