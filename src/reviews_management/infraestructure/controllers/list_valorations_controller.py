
from reviews_management.application.dtos.response.base_response import BaseResponse
from fastapi import logger
from reviews_management.application.use_cases.list_valorations_use_cases import ListValorationUseCase


class ListValorationController:
    def __init__(self, useCases: ListValorationUseCase):
        self.useCases = useCases

    async def execute(self):
        try:
            base_response = self.use_cases.execute()
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

        