from fastapi import APIRouter, Depends
from typing import List
from middleware.jwt_middleware import verify_token
from publication_management.application.dtos.request.create_publication_request import CreatePublicationRequest
from publication_management.application.dtos.request.update_publication_request import UpdatePublicationRequest
from publication_management.infraestructure.dependencies.publication_dependencies import get_create_controller, get_delete_controller, get_get_by_uuid_controller, get_list_controller, get_update_controller
from reviews_management.application.dtos.response.base_response import BaseResponse



router = APIRouter()

@router.post("/publications", response_model=BaseResponse, dependencies=[Depends(verify_token)])
async def create_Publication(Publication_request: CreatePublicationRequest, controller = Depends(get_create_controller)):
    return await controller.execute(Publication_request)

@router.get("/publications/health", response_model=BaseResponse)
async def health_check():
    return BaseResponse(
        data='OK',
        message='Tu mensaje aquí',
        status=True,
        status_code=200
    ).apply()

@router.get("/publications", response_model=List[BaseResponse], dependencies=[Depends(verify_token)])
async def list_publications(controller = Depends(get_list_controller)):
    return await controller.execute()

@router.get("/publications/{uuid}", response_model=BaseResponse, dependencies=[Depends(verify_token)])
async def get_Publication(uuid: str, controller = Depends(get_get_by_uuid_controller)):
    return await controller.execute(uuid)

@router.put("/publications/{uuid}", response_model=BaseResponse, dependencies=[Depends(verify_token)])
async def update_Publication(uuid: str, Publication_request: UpdatePublicationRequest, controller = Depends(get_update_controller)):
    return await controller.execute(uuid, Publication_request)

@router.delete("/publications/{uuid}", response_model=BaseResponse, dependencies=[Depends(verify_token)])
async def delete_Publication(uuid: str, controller = Depends(get_delete_controller)):
    return await controller.execute(uuid)
