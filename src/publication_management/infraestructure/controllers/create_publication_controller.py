import logging

from fastapi import UploadFile
from publication_management.application.dtos.request.create_publication_request import CreatePublicationRequest
from publication_management.application.use_cases.create_publication_use_cases import CreatePublicationUseCase
from publication_management.infraestructure.services.S3_upload_image import S3Service
from reviews_management.application.dtos.response.base_response import BaseResponse

logger = logging.getLogger(__name__)

class CreatePublicationController:
    def __init__(self, useCases: CreatePublicationUseCase, service_img: S3Service):
        self.use_cases = useCases
        self.service_img = service_img


    async def execute(self, request: CreatePublicationRequest, file: UploadFile=None):
        try:
            s3_url = ""
            if file:
                file_content = await file.read()
                file_name = file.filename
                mime_type = file.content_type
                s3_url = await self.service_img.execute(file_content, file_name, mime_type)
            base_response = await self.use_cases.execute(request, s3_url)
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

        