import logging
from typing import List
from database.mongodb import Database
from reviews_management.domain.entities.valoration import Valoration as ValorationDomain
from reviews_management.domain.ports.valoration_interface import ValorationInterface
from reviews_management.infraestructure.daos.valoration_entity import ValorationEntity
from reviews_management.infraestructure.mappers.valoration_mapper_dao import ValorationMapperDAO

logger = logging.getLogger(__name__)
class ValorationMongoRepository(ValorationInterface):
    def __init__(self, mongodb: Database):
        self.mongodb = mongodb
    
    async def init_db(self, document: ValorationEntity):
        await self.mongodb.init_db([document])
        
    async def initialize(self):
        await self.init_db(ValorationEntity)
    
    @staticmethod
    async def get_valoration(uuid: str) -> ValorationDomain:
        valoration_entity = await ValorationEntity.find_one(ValorationEntity.uuid == uuid)
        if valoration_entity:
            return ValorationMapperDAO.to_domain(valoration_entity)
        else:
            logging.error(f"Valoration with UUID {uuid} not found.")
            return None
        
    @staticmethod
    async def get_valorations_by_user_uuid(uuid: str) -> List[ValorationDomain]:
        valoration_entities = await ValorationEntity.find(ValorationEntity.user_uuid == uuid).to_list()
        if valoration_entities:
            return [ValorationMapperDAO.to_domain(entity) for entity in valoration_entities]
        else:
            logging.error(f"Valoration with UUID {uuid} not found.")
            return None
        
    @staticmethod
    async def get_valorations_by_provider_uuid(uuid: str) -> List[ValorationDomain]:
        valoration_entities = await ValorationEntity.find(ValorationEntity.provider_uuid == uuid).to_list()
        if valoration_entities:
            return [ValorationMapperDAO.to_domain(entity) for entity in valoration_entities]
        else:
            logging.error(f"Valoration with UUID {uuid} not found.")
            return None

    @staticmethod
    async def create_valoration(valoration: ValorationDomain) -> ValorationDomain:
        valoration_entity = ValorationMapperDAO.from_domain(valoration)
        await valoration_entity.insert()
        return ValorationMapperDAO.to_domain(valoration_entity)

    @staticmethod
    async def update_valoration(uuid: str, valoration: ValorationDomain) -> ValorationDomain:
        valoration_entity = await ValorationEntity.find_one(ValorationEntity.uuid == uuid)
        if not valoration_entity:
            logging.error(f"Valoration with UUID {uuid} not found.")
            return None
        updated_entity = ValorationMapperDAO.from_domain(valoration)
        updated_entity = ValorationMapperDAO.to_update(valoration_entity, updated_entity)
        await valoration_entity.update({"$set": updated_entity.dict(exclude_unset=True)})
        return ValorationMapperDAO.to_domain(updated_entity)

    @staticmethod
    async def list_valoration() -> List[ValorationDomain]:
        valoration_entities = await ValorationEntity.find_all().to_list()
        return [ValorationMapperDAO.to_domain(entity) for entity in valoration_entities]

    @staticmethod
    async def delete_valoration(uuid: str) -> bool:
        valoration_entity = await ValorationEntity.find_one(ValorationEntity.uuid == uuid)
        if not valoration_entity:
            logging.error(f"Valoration with UUID {uuid} not found.")
            return False
        await valoration_entity.delete()
        return True
