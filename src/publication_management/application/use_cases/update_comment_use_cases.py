from publication_management.application.dtos.request.update_comment_request import UpdateCommentRequest
from publication_management.application.mappers.comment_mapper_dtos import CommentMapperDTO
from publication_management.domain.ports.comment_interface import CommentInterface
from reviews_management.application.dtos.response.base_response import BaseResponse


class UpdateCommentUseCase:
    def __init__(self, repository: CommentInterface):
        self.repository = repository

    async def execute(self, uuid:str, comment: UpdateCommentRequest) -> BaseResponse:
        commentDomain = CommentMapperDTO.to_domain_comment_update(comment)
        if commentDomain is None:
            return BaseResponse(
                data=None,
                message="Bad request",
                status=False,
                status_code=400
            )
        result = await self.repository.update_comment(uuid, commentDomain)
        if result is None:
            return BaseResponse(
                data=None,
                message="comment not updated",
                status=False,
                status_code=400
            )
        return BaseResponse(
            data=CommentMapperDTO.to_response_comment(result),
            message="comment updated successfully",
            status=True,
            status_code=200
        )