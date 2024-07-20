from reviews_management.application.dtos.response.base_response import BaseResponse
from reviews_management.application.use_cases.get_time_serie_use_cases import GetTimeSerieUseCases
from reviews_management.application.use_cases.get_valorations_by_provider_uuid_use_cases import GetByProviderUuidValorationUseCase
import logging

logger = logging.getLogger(__name__)

class GetTimeSerieController:
    def __init__(self, useCases: GetTimeSerieUseCases):
        self.use_cases = useCases

    async def execute(self, uuid:str, days:str) -> BaseResponse:
        try:
            days = int(days)
            base_response = await self.use_cases.execute(uuid, days)
            return base_response.apply()
        except Exception as e:
            logger.error(e)
            base_response = BaseResponse(
                data=None,
                message="Internal server error",
                status=False,
                status_code=500
            )
            return base_response.apply()