from publication_management.application.mappers.publication_mapper_dtos import PublicationMapperDTO
from publication_management.domain.ports.publication_interface import PublicationInterface
from reviews_management.application.dtos.response.base_response import BaseResponse

class GetPublicationByUserUuidUseCases:
    def __init__(self, repository: PublicationInterface):
        self.repository = repository

    async def execute(self, uuid:str) -> BaseResponse:
        publications = await self.repository.get_by_uuid_user(uuid)
        if publications is None:
            return BaseResponse(
                data=None,
                message="publications not found",
                status=False,
                status_code=404
            )
        responses = [PublicationMapperDTO.to_response(publication) for publication in publications]
        return BaseResponse(
            data=responses,
            message="publications has been found successfully",
            status=True,
            status_code=200
        )