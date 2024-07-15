from fastapi import Depends
from publication_management.application.use_cases.create_publication_use_cases import CreatePublicationUseCase
from publication_management.application.use_cases.delete_publication_use_cases import DeletePublicationUseCase
from publication_management.application.use_cases.get_publication_use_cases import GetByUuidPublicationUseCase
from publication_management.application.use_cases.list_publications_use_cases import ListPublicationUseCase
from publication_management.application.use_cases.update_publication_use_cases import UpdatePublicationUseCase
from publication_management.infraestructure.controllers.create_publication_controller import CreatePublicationController
from publication_management.infraestructure.controllers.delete_publication_controller import DeletePublicationController
from publication_management.infraestructure.controllers.get_publication_controller import GetPublicationController
from publication_management.infraestructure.controllers.list_publication_controller import ListPublicationController
from publication_management.infraestructure.controllers.update_publication_controller import UpdatePublicationController
from publication_management.infraestructure.repositories.publication_mongo_repository import PublicationMongoRepository
from database.mongodb import Database

database = Database()
repository = PublicationMongoRepository(database)

async def get_create_use_case() -> CreatePublicationUseCase:
    await repository.initialize()
    return CreatePublicationUseCase(repository)

async def get_list_use_case() -> ListPublicationUseCase:
    await repository.initialize()
    return ListPublicationUseCase(repository)

async def get_update_use_case() -> UpdatePublicationUseCase:
    await repository.initialize()
    return UpdatePublicationUseCase(repository)

async def get_delete_use_case() -> DeletePublicationUseCase:
    await repository.initialize()
    return DeletePublicationUseCase(repository)

async def get_get_by_uuid_use_case() -> GetByUuidPublicationUseCase:
    await repository.initialize()
    return GetByUuidPublicationUseCase(repository)

async def get_create_controller(create_use_case: CreatePublicationUseCase = Depends(get_create_use_case)) -> CreatePublicationController:
    return CreatePublicationController(create_use_case)

async def get_list_controller(list_use_case: ListPublicationUseCase = Depends(get_list_use_case)) -> ListPublicationController:
    return ListPublicationController(list_use_case)

async def get_update_controller(update_use_case: UpdatePublicationUseCase = Depends(get_update_use_case)) -> UpdatePublicationController:
    return UpdatePublicationController(update_use_case)

async def get_delete_controller(delete_use_case: DeletePublicationUseCase = Depends(get_delete_use_case)) -> DeletePublicationController:
    return DeletePublicationController(delete_use_case)

async def get_get_by_uuid_controller(get_by_uuid_use_case: GetByUuidPublicationUseCase = Depends(get_get_by_uuid_use_case)) -> GetPublicationController:
    return GetPublicationController(get_by_uuid_use_case)
