import logging
from reviews_management.application.dtos.request.create_valoration_request import CreateValorationRequest
from reviews_management.application.dtos.request.update_valoration_request import UpdateValorationRequest
from reviews_management.application.dtos.response.base_response import BaseResponse
from reviews_management.application.use_cases.create_valoration_use_cases import CreateValorationUseCase
from reviews_management.application.use_cases.update_valoration_use_cases import UpdateValorationUseCase

logger = logging.getLogger(__name__)


class UpdateValorationController:
    def __init__(self, useCases: UpdateValorationUseCase):
        self.use_cases = useCases

    async def execute(self, uuid:str, valoration_request: UpdateValorationRequest):
        try:
            base_response = await self.use_cases.execute(uuid, valoration_request)
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

        