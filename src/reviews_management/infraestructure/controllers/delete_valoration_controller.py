from fastapi import logger
from reviews_management.application.dtos.response.base_response import BaseResponse
from reviews_management.application.use_cases.delete_valoration_use_cases import DeleteValorationUseCase


class DeleteValorationController:
    def __init__(self, useCases: DeleteValorationUseCase):
        self.useCases = useCases

    async def execute(self, uuid:str):
        try:
            base_response = self.use_cases.execute(uuid)
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

        