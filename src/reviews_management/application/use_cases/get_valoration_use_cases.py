from reviews_management.application.dtos.request.create_valoration_request import CreateValorationRequest
from reviews_management.application.dtos.response.base_response import BaseResponse
from reviews_management.application.mappers.valoration_mappers_dtos import ValorationDTOMapper
from reviews_management.domain.ports.valoration_interface import ValorationInterface


class GetByUuidValorationUseCase:
    def __init__(self, repository: ValorationInterface):
        self.repository = repository

    async def execute(self, uuid:str) -> BaseResponse:
        result = await self.repository.get_valoration(uuid)
        if result is None:
            return BaseResponse(
                data=None,
                message="Valoration not found",
                status=False,
                status_code=404
            )
        return BaseResponse(
            data=ValorationDTOMapper.to_response_valoration(result),
            message="Valoration has been found successfully",
            status=True,
            status_code=201
        )