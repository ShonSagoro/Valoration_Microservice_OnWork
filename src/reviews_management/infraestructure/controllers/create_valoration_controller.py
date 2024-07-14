import logging
from reviews_management.application.dtos.request.create_valoration_request import CreateValorationRequest
from reviews_management.application.dtos.response.base_response import BaseResponse
from reviews_management.application.use_cases.create_valoration_use_cases import CreateValorationUseCase

logger = logging.getLogger(__name__)

class CreateValorationController:
    def __init__(self, useCases: CreateValorationUseCase):
        self.use_cases = useCases

    async def execute(self, valoration_request: CreateValorationRequest):
        try:
            base_response = await self.use_cases.execute(valoration_request)
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

        