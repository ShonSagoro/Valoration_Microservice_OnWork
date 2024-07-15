import logging

from publication_management.application.dtos.request.create_comment_request import CreateCommentRequest
from publication_management.application.mappers.comment_mappers_dtos import CommentMapperDTO
from publication_management.domain.ports.comment_interface import CommentInterface
from reviews_management.application.dtos.response.base_response import BaseResponse

logger = logging.getLogger(__name__)

class CreateCommentUseCase:
    def __init__(self, repository: CommentInterface):
        self.repository = repository

    async def execute(self, Comment: CreateCommentRequest) -> BaseResponse:
        commentDomain = CommentMapperDTO.to_domain_comment_create(Comment)
        if commentDomain is None:
            return BaseResponse(
                data=None,
                message="Bad request",
                status=False,
                status_code=400
            )
        result = await self.repository.create_comment(commentDomain)

        if result is None:
            return BaseResponse(
                data=None,
                message="Comment not created",
                status=False,
                status_code=400
            )
        return BaseResponse(
            data=CommentMapperDTO.to_response_comment(result),
            message="Comment created successfully",
            status=True,
            status_code=201
        )