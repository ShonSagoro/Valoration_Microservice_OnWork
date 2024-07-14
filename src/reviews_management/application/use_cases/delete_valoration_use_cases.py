from reviews_management.application.dtos.request.create_valoration_request import CreateValorationRequest
from reviews_management.application.dtos.response.base_response import BaseResponse
from reviews_management.application.mappers.valoration_mappers_dtos import ValorationDTOMapper
from reviews_management.domain.ports.valoration_interface import ValorationInterface


class DeleteValorationUseCase:
    def __init__(self, repository: ValorationInterface):
        self.repository = repository

    async def execute(self, uuid:str) -> BaseResponse:
        result = await self.repository.delete_valoration(uuid)
        if result is False:
            return BaseResponse(
                data=None,
                message="Valoration not deleted",
                status=False,
                status_code=400
            )
        return BaseResponse(
            data=True,
            message="Valoration has been deleted successfully",
            status=True,
            status_code=200
        )