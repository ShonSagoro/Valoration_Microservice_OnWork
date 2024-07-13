from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from reviews_management.application.dtos.request.create_valoration_request import CreateValorationRequest
from reviews_management.application.dtos.request.update_valoration_request import UpdateValorationRequest
from reviews_management.application.dtos.response.base_response import BaseResponse
from reviews_management.infraestructure.controllers.create_valoration_controller import CreateValorationController
from reviews_management.infraestructure.controllers.delete_valoration_controller import DeleteValorationController
from reviews_management.infraestructure.controllers.get_valoration_controller import GetValorationController
from reviews_management.infraestructure.controllers.list_valorations_controller import ListValorationController
from reviews_management.infraestructure.controllers.update_valoration_controller import UpdateValorationController

router = APIRouter()

from reviews_management.infraestructure.dependencies.tag_dependencies import (
    create_controller, list_controller, update_controller,
    delete_controller, get_by_uuid_controller
)

@router.post("/valorations", response_model=BaseResponse)
async def create_valoration(valoration_request: CreateValorationRequest, controller: CreateValorationController = Depends(lambda: create_controller)):
    return await controller.execute(valoration_request)

@router.get("/valorations", response_model=List[BaseResponse])
async def list_valorations(controller: ListValorationController = Depends(lambda: list_controller)):
    return await controller.execute()

@router.get("/valorations/{uuid}", response_model=BaseResponse)
async def get_valoration(uuid: str, controller: GetValorationController = Depends(lambda: get_by_uuid_controller)):
    return await controller.execute(uuid)

@router.put("/valorations/{uuid}", response_model=BaseResponse)
async def update_valoration(uuid: str, valoration_request: UpdateValorationRequest, controller: UpdateValorationController = Depends(lambda: update_controller)):
    return await controller.execute(uuid, valoration_request)

@router.delete("/valorations/{uuid}", response_model=BaseResponse)
async def delete_valoration(uuid: str, controller: DeleteValorationController = Depends(lambda: delete_controller)):
    return await controller.execute(uuid)
