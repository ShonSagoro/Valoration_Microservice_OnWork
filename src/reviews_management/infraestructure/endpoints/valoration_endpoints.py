from fastapi import APIRouter, Depends
from typing import List
from middleware.jwt_middleware import verify_token
from reviews_management.application.dtos.request.create_valoration_request import CreateValorationRequest
from reviews_management.application.dtos.request.update_valoration_request import UpdateValorationRequest
from reviews_management.application.dtos.response.base_response import BaseResponse
from reviews_management.infraestructure.dependencies.valorations_dependencies import (
    get_create_controller, get_list_controller, get_update_controller,
    get_delete_controller, get_get_by_uuid_controller
)


router = APIRouter()

@router.post("/valorations", response_model=BaseResponse, dependencies=[Depends(verify_token)])
async def create_valoration(valoration_request: CreateValorationRequest, controller = Depends(get_create_controller)):
    return await controller.execute(valoration_request)

@router.get("/valorations/health", response_model=BaseResponse)
async def health_check():
    return BaseResponse(
        data='OK',
        message='Tu mensaje aquí',
        status=True,
        status_code=200
    ).apply()

@router.get("/valorations", response_model=List[BaseResponse], dependencies=[Depends(verify_token)])
async def list_valorations(controller = Depends(get_list_controller)):
    return await controller.execute()

@router.get("/valorations/{uuid}", response_model=BaseResponse, dependencies=[Depends(verify_token)])
async def get_valoration(uuid: str, controller = Depends(get_get_by_uuid_controller)):
    return await controller.execute(uuid)

@router.put("/valorations/{uuid}", response_model=BaseResponse, dependencies=[Depends(verify_token)])
async def update_valoration(uuid: str, valoration_request: UpdateValorationRequest, controller = Depends(get_update_controller)):
    return await controller.execute(uuid, valoration_request)

@router.delete("/valorations/{uuid}", response_model=BaseResponse, dependencies=[Depends(verify_token)])
async def delete_valoration(uuid: str, controller = Depends(get_delete_controller)):
    return await controller.execute(uuid)
