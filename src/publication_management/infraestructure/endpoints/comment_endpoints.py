from fastapi import APIRouter, Depends
from typing import List
from middleware.jwt_middleware import verify_token
from publication_management.application.dtos.request.create_comment_request import CreateCommentRequest
from publication_management.application.dtos.request.update_comment_request import UpdateCommentRequest
from reviews_management.application.dtos.response.base_response import BaseResponse
from reviews_management.infraestructure.dependencies.valorations_dependencies import get_create_controller, get_delete_controller, get_get_by_uuid_controller, get_list_controller, get_update_controller



router = APIRouter()

@router.post("/comments", response_model=BaseResponse, dependencies=[Depends(verify_token)])
async def create_Comment(Comment_request: CreateCommentRequest, controller = Depends(get_create_controller)):
    return await controller.execute(Comment_request)

@router.get("/comments/health", response_model=BaseResponse)
async def health_check():
    return BaseResponse(
        data='OK',
        message='Tu mensaje aquí',
        status=True,
        status_code=200
    ).apply()

@router.get("/comments", response_model=List[BaseResponse], dependencies=[Depends(verify_token)])
async def list_Comments(controller = Depends(get_list_controller)):
    return await controller.execute()

@router.get("/comments/{uuid}", response_model=BaseResponse, dependencies=[Depends(verify_token)])
async def get_Comment(uuid: str, controller = Depends(get_get_by_uuid_controller)):
    return await controller.execute(uuid)

@router.put("/comments/{uuid}", response_model=BaseResponse, dependencies=[Depends(verify_token)])
async def update_Comment(uuid: str, Comment_request: UpdateCommentRequest, controller = Depends(get_update_controller)):
    return await controller.execute(uuid, Comment_request)

@router.delete("/comments/{uuid}", response_model=BaseResponse, dependencies=[Depends(verify_token)])
async def delete_Comment(uuid: str, controller = Depends(get_delete_controller)):
    return await controller.execute(uuid)
