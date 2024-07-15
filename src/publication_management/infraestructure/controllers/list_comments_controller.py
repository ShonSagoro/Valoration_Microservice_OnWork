
import logging
from publication_management.application.use_cases.list_comments_use_cases import ListCommentUseCase
from reviews_management.application.dtos.response.base_response import BaseResponse

logger = logging.getLogger(__name__)

class ListCommentController:
    def __init__(self, useCases: ListCommentUseCase):
        self.use_cases = useCases

    async def execute(self):
        try:
            base_response = await self.use_cases.execute()
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

        