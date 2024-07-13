from reviews_management.application.dtos.request.create_valoration_request import CreateValorationRequest
from reviews_management.application.dtos.response.base_response import BaseResponse
from reviews_management.application.mappers.valoration_mappers_dtos import ValorationDTOMapper
from reviews_management.domain.ports.valoration_interface import ValorationInterface


class CreateValorationUseCase:
    def __init__(self, repository: ValorationInterface):
        self.repository = repository

    def execute(self, valoration: CreateValorationRequest) -> BaseResponse:
        valorationDomain = ValorationDTOMapper.to_domain_valoration_create(valoration)
        if valorationDomain is None:
            return BaseResponse(
                data=None,
                message="Bad request",
                status=False,
                status_code=400
            )
        result = self.repository.create(valorationDomain)

        if result is None:
            return BaseResponse(
                data=None,
                message="Valoration not created",
                status=False,
                status_code=400
            )
        return BaseResponse(
            data=ValorationDTOMapper.to_response_valoration(result),
            message="Valoration created successfully",
            status=True,
            status_code=201
        )