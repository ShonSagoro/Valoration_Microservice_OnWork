
import logging
from publication_management.application.use_cases.get_publication_use_cases import GetByUuidPublicationUseCase
from reviews_management.application.dtos.response.base_response import BaseResponse

logger = logging.getLogger(__name__)


class GetPublicationController:
    def __init__(self, useCases: GetByUuidPublicationUseCase):
        self.use_cases = useCases

    async def execute(self, uuid:str):
        try:
            base_response = await self.use_cases.execute(uuid)
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

        