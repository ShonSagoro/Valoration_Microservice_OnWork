from reviews_management.application.dtos.request.create_valoration_request import CreateValorationRequest
from reviews_management.application.dtos.request.update_valoration_request import UpdateValorationRequest
from reviews_management.application.dtos.response.base_response import BaseResponse
from reviews_management.application.mappers.valoration_mappers_dtos import ValorationDTOMapper
from reviews_management.domain.ports.valoration_interface import ValorationInterface


class UpdateValorationUseCase:
    def __init__(self, repository: ValorationInterface):
        self.repository = repository

    def execute(self, valoration: UpdateValorationRequest) -> BaseResponse:
        valorationDomain = ValorationDTOMapper.to_domain_valoration_update(valoration)
        if valorationDomain is None:
            return BaseResponse(
                data=None,
                message="Bad request",
                status=False,
                status_code=400
            )
        result = self.repository.update_valoration(valorationDomain)
        if result is None:
            return BaseResponse(
                data=None,
                message="Valoration not updated",
                status=False,
                status_code=400
            )
        return BaseResponse(
            data=ValorationDTOMapper.to_response_valoration(result),
            message="Valoration updated successfully",
            status=True,
            status_code=200
        )