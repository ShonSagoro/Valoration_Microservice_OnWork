from publication_management.domain.ports.publication_interface import PublicationInterface
from reviews_management.application.dtos.response.base_response import BaseResponse


class DeletePublicationUseCase:
    def __init__(self, repository: PublicationInterface):
        self.repository = repository

    async def execute(self, uuid:str) -> BaseResponse:
        result = await self.repository.delete_publication(uuid)
        if result is False:
            return BaseResponse(
                data=None,
                message="publication not deleted",
                status=False,
                status_code=400
            )
        return BaseResponse(
            data=True,
            message="publication has been deleted successfully",
            status=True,
            status_code=200
        )