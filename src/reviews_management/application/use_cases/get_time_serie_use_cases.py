from reviews_management.application.dtos.response.base_response import BaseResponse
from reviews_management.application.utils.get_time_per_day_to_profile import GetTimeSerieProfile
from reviews_management.domain.ports.valoration_interface import ValorationInterface


class GetTimeSerieUseCases:
    def __init__(self, repository: ValorationInterface):
        self.repository = repository

    async def execute(self, uuid:str, days:int) -> BaseResponse:
        result = await self.repository.get_valorations_by_provider_uuid(uuid)
        if result is None:
            return BaseResponse(
                data=None,
                message="Valoration not found",
                status=False,
                status_code=404
            )
        result = GetTimeSerieProfile(result, days)
        return BaseResponse(
            data=result,
            message="Valorations by provider uuid has been found successfully",
            status=True,
            status_code=200
        )