import logging
from publication_management.application.dtos.request.update_comment_request import UpdateCommentRequest
from publication_management.application.use_cases.update_comment_use_cases import UpdateCommentUseCase
from reviews_management.application.dtos.response.base_response import BaseResponse

logger = logging.getLogger(__name__)


class UpdateCommentController:
    def __init__(self, useCases: UpdateCommentUseCase):
        self.use_cases = useCases

    async def execute(self, uuid:str, Comment_request: UpdateCommentRequest):
        try:
            base_response = await self.use_cases.execute(uuid, Comment_request)
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

        