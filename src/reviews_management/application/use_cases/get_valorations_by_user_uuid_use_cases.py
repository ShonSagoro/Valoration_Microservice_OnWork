from reviews_management.application.dtos.response.base_response import BaseResponse
from reviews_management.application.mappers.valoration_mappers_dtos import ValorationMapperDTO
from reviews_management.domain.ports.valoration_interface import ValorationInterface


class GetByUserUuidValorationUseCase:
    def __init__(self, repository: ValorationInterface):
        self.repository = repository

    async def execute(self, uuid:str) -> BaseResponse:
        result = await self.repository.get_valorations_by_user_uuid(uuid)
        if result is None:
            return BaseResponse(
                data=None,
                message="Valoration not found",
                status=False,
                status_code=404
            )
        responses = [ValorationMapperDTO.to_response_valoration(valoration) for valoration in result]
        return BaseResponse(
            data=responses,
            message="Valorations by user uuid has been found successfully",
            status=True,
            status_code=200
        )