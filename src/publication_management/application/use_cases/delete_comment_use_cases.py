from publication_management.domain.ports.comment_interface import CommentInterface
from reviews_management.application.dtos.response.base_response import BaseResponse


class DeleteCommentUseCase:
    def __init__(self, repository: CommentInterface):
        self.repository = repository

    async def execute(self, uuid:str) -> BaseResponse:
        result = await self.repository.delete_comment(uuid)
        if result is False:
            return BaseResponse(
                data=None,
                message="comment not deleted",
                status=False,
                status_code=400
            )
        return BaseResponse(
            data=True,
            message="comment has been deleted successfully",
            status=True,
            status_code=200
        )