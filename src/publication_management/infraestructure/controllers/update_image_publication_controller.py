from fastapi import UploadFile
from publication_management.application.use_cases.update_image_publication_use_cases import UpdateImagePublicationUseCases
from publication_management.infraestructure.services.S3_upload_image import S3Service
from reviews_management.application.dtos.response.base_response import BaseResponse
import logging

logger = logging.getLogger(__name__)

class UpdateImagePublicationController:

    def __init__(self, useCases: UpdateImagePublicationUseCases, service_img: S3Service):
        self.use_cases = useCases
        self.service_img = service_img

    async def execute(self, uuid:str, file: UploadFile) -> BaseResponse:
        try:
            file_content = await file.read()
            file_name = file.filename
            mime_type = file.content_type
            s3_url = await self.service_img.execute(file_content, file_name, mime_type)
            base_response = await self.use_cases.execute(uuid, s3_url)
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