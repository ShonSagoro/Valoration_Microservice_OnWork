from fastapi import Depends
from reviews_management.application.use_cases.get_time_serie_use_cases import GetTimeSerieUseCases
from reviews_management.application.use_cases.get_valorations_by_provider_uuid_use_cases import GetByProviderUuidValorationUseCase
from reviews_management.application.use_cases.get_valorations_by_user_uuid_use_cases import GetByUserUuidValorationUseCase
from reviews_management.infraestructure.controllers.create_valoration_controller import CreateValorationController
from reviews_management.infraestructure.controllers.delete_valoration_controller import DeleteValorationController
from reviews_management.infraestructure.controllers.get_time_serie_controller import GetTimeSerieController
from reviews_management.infraestructure.controllers.get_valoration_controller import GetValorationController
from reviews_management.infraestructure.controllers.get_valorations_by_provider_uuid_controller import GetByProviderUuidValorationController
from reviews_management.infraestructure.controllers.get_valorations_by_user_uuid_controller import GetByUserUuidValorationController
from reviews_management.infraestructure.controllers.list_valorations_controller import ListValorationController
from reviews_management.infraestructure.controllers.update_valoration_controller import UpdateValorationController
from reviews_management.application.use_cases.create_valoration_use_cases import CreateValorationUseCase
from reviews_management.application.use_cases.delete_valoration_use_cases import DeleteValorationUseCase
from reviews_management.application.use_cases.get_valoration_use_cases import GetByUuidValorationUseCase
from reviews_management.application.use_cases.list_valorations_use_cases import ListValorationUseCase
from reviews_management.application.use_cases.update_valoration_use_cases import UpdateValorationUseCase
from reviews_management.infraestructure.repositories.valorations_mongo_repository import ValorationMongoRepository
from database.mongodb import Database

database = Database()
repository = ValorationMongoRepository(database)

async def get_create_use_case() -> CreateValorationUseCase:
    await repository.initialize()
    return CreateValorationUseCase(repository)

async def get_list_use_case() -> ListValorationUseCase:
    await repository.initialize()
    return ListValorationUseCase(repository)

async def get_update_use_case() -> UpdateValorationUseCase:
    await repository.initialize()
    return UpdateValorationUseCase(repository)

async def get_delete_use_case() -> DeleteValorationUseCase:
    await repository.initialize()
    return DeleteValorationUseCase(repository)

async def get_get_by_uuid_use_case() -> GetByUuidValorationUseCase:
    await repository.initialize()
    return GetByUuidValorationUseCase(repository)

async def get_get_by_uuid_user_use_case() -> GetByUserUuidValorationUseCase:
    await repository.initialize()
    return GetByUserUuidValorationUseCase(repository)

async def get_get_by_uuid_provider_use_case() -> GetByProviderUuidValorationUseCase:
    await repository.initialize()
    return GetByProviderUuidValorationUseCase(repository)

async def get_get_time_serie_use_cases() -> GetTimeSerieUseCases:
    await repository.initialize()
    return GetTimeSerieUseCases(repository)

async def get_create_controller(create_use_case: CreateValorationUseCase = Depends(get_create_use_case)) -> CreateValorationController:
    return CreateValorationController(create_use_case)

async def get_list_controller(list_use_case: ListValorationUseCase = Depends(get_list_use_case)) -> ListValorationController:
    return ListValorationController(list_use_case)

async def get_update_controller(update_use_case: UpdateValorationUseCase = Depends(get_update_use_case)) -> UpdateValorationController:
    return UpdateValorationController(update_use_case)

async def get_delete_controller(delete_use_case: DeleteValorationUseCase = Depends(get_delete_use_case)) -> DeleteValorationController:
    return DeleteValorationController(delete_use_case)

async def get_get_by_uuid_controller(get_by_uuid_use_case: GetByUuidValorationUseCase = Depends(get_get_by_uuid_use_case)) -> GetValorationController:
    return GetValorationController(get_by_uuid_use_case)

async def get_get_by_uuid_user_controller(get_by_uuid_user_use_case: GetByUserUuidValorationUseCase = Depends(get_get_by_uuid_user_use_case)) -> GetByUserUuidValorationController:
    return GetByUserUuidValorationController(get_by_uuid_user_use_case)

async def get_get_by_uuid_provider_controller(get_by_uuid_provider_use_case: GetByProviderUuidValorationUseCase = Depends(get_get_by_uuid_provider_use_case)) -> GetByProviderUuidValorationController:
    return GetByProviderUuidValorationController(get_by_uuid_provider_use_case)

async def get_get_time_serie_controller(get_time_serie_use_cases: GetTimeSerieUseCases = Depends(get_get_time_serie_use_cases)) -> GetTimeSerieController:
    return GetTimeSerieController(get_time_serie_use_cases)

