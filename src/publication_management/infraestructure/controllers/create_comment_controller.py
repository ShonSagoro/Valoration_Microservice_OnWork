import logging
from publication_management.application.dtos.request.create_comment_request import CreateCommentRequest
from publication_management.application.use_cases.create_comment_use_cases import CreateCommentUseCase
from reviews_management.application.dtos.response.base_response import BaseResponse

logger = logging.getLogger(__name__)

class CreateCommentController:
    def __init__(self, useCases: CreateCommentUseCase):
        self.use_cases = useCases

    async def execute(self, request: CreateCommentRequest):
        try:
            logging.info(request)
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

        