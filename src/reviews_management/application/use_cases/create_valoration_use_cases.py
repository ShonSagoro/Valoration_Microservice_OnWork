import logging
from publication_management.application.utils.analisys_comment import analysis_comment
from reviews_management.application.dtos.request.create_valoration_request import CreateValorationRequest
from reviews_management.application.dtos.response.base_response import BaseResponse
from reviews_management.application.mappers.valoration_mappers_dtos import ValorationMapperDTO
from reviews_management.domain.ports.valoration_interface import ValorationInterface
logger = logging.getLogger(__name__)

class CreateValorationUseCase:
    def __init__(self, repository: ValorationInterface):
        self.repository = repository

    async def execute(self, valoration: CreateValorationRequest) -> BaseResponse:
        valorationDomain = ValorationMapperDTO.to_domain_valoration_create(valoration)
        commentStatus, commentStar = analysis_comment(valorationDomain.comment.comment)
        valorationDomain = ValorationMapperDTO.update_comment(valorationDomain, commentStatus, commentStar)
        if valorationDomain is None:
            return BaseResponse(
                data=None,
                message="Bad request",
                status=False,
                status_code=400
            )
        result = await self.repository.create_valoration(valorationDomain)

        if result is None:
            return BaseResponse(
                data=None,
                message="Valoration not created",
                status=False,
                status_code=400
            )
        return BaseResponse(
            data=ValorationMapperDTO.to_response_valoration(result),
            message="Valoration created successfully",
            status=True,
            status_code=201
        )