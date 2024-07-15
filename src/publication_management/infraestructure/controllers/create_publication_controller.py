import logging
from publication_management.application.dtos.request.create_publication_request import CreatePublicationRequest
from publication_management.application.use_cases.create_publication_use_cases import CreatePublicationUseCase
from reviews_management.application.dtos.response.base_response import BaseResponse

logger = logging.getLogger(__name__)

class CreatePublicationController:
    def __init__(self, useCases: CreatePublicationUseCase):
        self.use_cases = useCases

    async def execute(self, request: CreatePublicationRequest):
        try:
            base_response = await self.use_cases.execute(request)
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

        