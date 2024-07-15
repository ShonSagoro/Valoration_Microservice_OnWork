import logging
from publication_management.application.dtos.request.update_publication_request import UpdatePublicationRequest
from publication_management.application.use_cases.update_publication_use_cases import UpdatePublicationUseCase
from reviews_management.application.dtos.response.base_response import BaseResponse

logger = logging.getLogger(__name__)


class UpdatePublicationController:
    def __init__(self, useCases: UpdatePublicationUseCase):
        self.use_cases = useCases

    async def execute(self, uuid:str, Publication_request: UpdatePublicationRequest):
        try:
            base_response = await self.use_cases.execute(uuid, Publication_request)
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

        