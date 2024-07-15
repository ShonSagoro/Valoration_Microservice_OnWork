import logging
from publication_management.application.mappers.comment_mapper_dtos import CommentMapperDTO
from publication_management.domain.ports.comment_interface import CommentInterface
from reviews_management.application.dtos.response.base_response import BaseResponse

logger = logging.getLogger(__name__)

class ListCommentUseCase:
    def __init__(self, repository: CommentInterface):
        self.repository = repository

    async def execute(self) -> BaseResponse:
        comments = await self.repository.list_comment()
        responses = [CommentMapperDTO.to_response_comment(comment) for comment in comments]
        return BaseResponse(
            data=responses,
            message="comments listed successfully",
            status=True,
            status_code=302
        )