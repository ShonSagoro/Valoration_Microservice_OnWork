import logging
from reviews_management.application.dtos.request.create_valoration_request import CreateValorationRequest
from reviews_management.application.dtos.response.base_response import BaseResponse
from reviews_management.application.mappers.valoration_mappers_dtos import ValorationDTOMapper
from reviews_management.domain.ports.valoration_interface import ValorationInterface

logger = logging.getLogger(__name__)

class ListValorationUseCase:
    def __init__(self, repository: ValorationInterface):
        self.repository = repository

    async def execute(self) -> BaseResponse:
        valorations = await self.repository.list_valoration()
        responses = [ValorationDTOMapper.to_response_valoration(valoration) for valoration in valorations]
        return BaseResponse(
            data=responses,
            message="Valorations listed successfully",
            status=True,
            status_code=201
        )