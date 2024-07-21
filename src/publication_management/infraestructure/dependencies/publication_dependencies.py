from fastapi import Depends
from publication_management.application.use_cases.create_publication_use_cases import CreatePublicationUseCase
from publication_management.application.use_cases.delete_publication_use_cases import DeletePublicationUseCase
from publication_management.application.use_cases.get_publication_by_user_uuid_use_cases import GetPublicationByUserUuidUseCases
from publication_management.application.use_cases.get_publication_use_cases import GetByUuidPublicationUseCase
from publication_management.application.use_cases.list_publications_use_cases import ListPublicationUseCase
from publication_management.application.use_cases.update_image_publication_use_cases import UpdateImagePublicationUseCases
from publication_management.application.use_cases.update_publication_use_cases import UpdatePublicationUseCase
from publication_management.infraestructure.controllers.create_publication_controller import CreatePublicationController
from publication_management.infraestructure.controllers.delete_publication_controller import DeletePublicationController
from publication_management.infraestructure.controllers.get_publication_by_user_uuid_controller import GetPublicationByUserUuidController
from publication_management.infraestructure.controllers.get_publication_controller import GetPublicationController
from publication_management.infraestructure.controllers.list_publication_controller import ListPublicationController
from publication_management.infraestructure.controllers.update_image_publication_controller import UpdateImagePublicationController
from publication_management.infraestructure.controllers.update_publication_controller import UpdatePublicationController
from publication_management.infraestructure.repositories.publication_mongo_repository import PublicationMongoRepository
from database.mongodb import Database
from publication_management.infraestructure.services.S3_upload_image import S3Service

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

async def get_get_publication_by_user_uuid_use_cases() -> GetPublicationByUserUuidUseCases:
    await repository.initialize()
    return GetPublicationByUserUuidUseCases(repository)

async def get_update_image_publication_use_cases() -> UpdateImagePublicationUseCases:
    await repository.initialize()
    return UpdateImagePublicationUseCases(repository)

async def get_create_controller(use_case: CreatePublicationUseCase = Depends(get_create_use_case)) -> CreatePublicationController:
    img_service = S3Service()
    return CreatePublicationController(use_case, img_service)

async def get_list_controller(use_case: ListPublicationUseCase = Depends(get_list_use_case)) -> ListPublicationController:
    return ListPublicationController(use_case)

async def get_update_controller(use_case: UpdatePublicationUseCase = Depends(get_update_use_case)) -> UpdatePublicationController:
    return UpdatePublicationController(use_case)

async def get_delete_controller(use_case: DeletePublicationUseCase = Depends(get_delete_use_case)) -> DeletePublicationController:
    return DeletePublicationController(use_case)

async def get_get_by_uuid_controller(use_case: GetByUuidPublicationUseCase = Depends(get_get_by_uuid_use_case)) -> GetPublicationController:
    return GetPublicationController(use_case)

async def get_get_publication_by_user_uuid_controller(use_case: GetPublicationByUserUuidUseCases = Depends(get_get_publication_by_user_uuid_use_cases)) -> GetPublicationByUserUuidController:
    return GetPublicationByUserUuidController(use_case)

async def get_update_image_publication_controller(use_case: UpdateImagePublicationUseCases = Depends(get_update_image_publication_use_cases)) -> UpdateImagePublicationController:
    img_service = S3Service()
    return UpdateImagePublicationController(use_case, img_service)
