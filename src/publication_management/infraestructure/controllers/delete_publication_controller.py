import logging
from publication_management.application.use_cases.delete_publication_use_cases import DeletePublicationUseCase
from reviews_management.application.dtos.response.base_response import BaseResponse

logger = logging.getLogger(__name__)

class DeletePublicationController:
    def __init__(self, useCases: DeletePublicationUseCase):
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

        