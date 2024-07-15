from publication_management.application.mappers.publication_mapper_dtos import PublicationMapperDTO
from publication_management.domain.ports.publication_interface import PublicationInterface
from reviews_management.application.dtos.response.base_response import BaseResponse

class GetByUuidPublicationUseCase:
    def __init__(self, repository: PublicationInterface):
        self.repository = repository

    async def execute(self, uuid:str) -> BaseResponse:
        result = await self.repository.get_publication(uuid)
        if result is None:
            return BaseResponse(
                data=None,
                message="publication not found",
                status=False,
                status_code=404
            )
        return BaseResponse(
            data=PublicationMapperDTO.to_response(result),
            message="publication has been found successfully",
            status=True,
            status_code=302
        )