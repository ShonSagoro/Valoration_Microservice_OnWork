from fastapi import Depends
from publication_management.infraestructure.repositories.comment_mongo_repository import CommentMongoRepository
from database.mongodb import Database

database = Database()
repository = CommentMongoRepository(database)

async def get_create_use_case() -> CreateCommentUseCase:
    await repository.initialize()
    return CreateCommentUseCase(repository)

async def get_list_use_case() -> ListCommentUseCase:
    await repository.initialize()
    return ListCommentUseCase(repository)

async def get_update_use_case() -> UpdateCommentUseCase:
    await repository.initialize()
    return UpdateCommentUseCase(repository)

async def get_delete_use_case() -> DeleteCommentUseCase:
    await repository.initialize()
    return DeleteCommentUseCase(repository)

async def get_get_by_uuid_use_case() -> GetByUuidCommentUseCase:
    await repository.initialize()
    return GetByUuidCommentUseCase(repository)

async def get_create_controller(create_use_case: CreateCommentUseCase = Depends(get_create_use_case)) -> CreateCommentController:
    return CreateCommentController(create_use_case)

async def get_list_controller(list_use_case: ListCommentUseCase = Depends(get_list_use_case)) -> ListCommentController:
    return ListCommentController(list_use_case)

async def get_update_controller(update_use_case: UpdateCommentUseCase = Depends(get_update_use_case)) -> UpdateCommentController:
    return UpdateCommentController(update_use_case)

async def get_delete_controller(delete_use_case: DeleteCommentUseCase = Depends(get_delete_use_case)) -> DeleteCommentController:
    return DeleteCommentController(delete_use_case)

async def get_get_by_uuid_controller(get_by_uuid_use_case: GetByUuidCommentUseCase = Depends(get_get_by_uuid_use_case)) -> GetCommentController:
    return GetCommentController(get_by_uuid_use_case)
