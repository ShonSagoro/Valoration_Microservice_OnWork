from publication_management.application.mappers.comment_mappers_dtos import CommentMapperDTO
from publication_management.domain.ports.comment_interface import CommentInterface
from reviews_management.application.dtos.response.base_response import BaseResponse


class GetByUuidCommentUseCase:
    def __init__(self, repository: CommentInterface):
        self.repository = repository

    async def execute(self, uuid:str) -> BaseResponse:
        result = await self.repository.get_comment(uuid)
        if result is None:
            return BaseResponse(
                data=None,
                message="comment not found",
                status=False,
                status_code=404
            )
        return BaseResponse(
            data=CommentMapperDTO.to_response_comment(result),
            message="comment has been found successfully",
            status=True,
            status_code=302
        )