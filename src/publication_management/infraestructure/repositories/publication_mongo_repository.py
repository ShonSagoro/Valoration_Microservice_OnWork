import logging
from typing import List
from database.mongodb import Database
from publication_management.domain.ports.publication_interface import PublicationInterface
from publication_management.infraestructure.daos.publication_entity import PublicationEntity
from publication_management.domain.entities import Publication as PublicationDomain
from publication_management.infraestructure.mappers.publication_mapper_dao import PublicationMapperDAO

logger = logging.getLogger(__name__)
class PublicationMongoRepository(PublicationInterface):
    def __init__(self, mongodb: Database):
        self.mongodb = mongodb
    
    async def init_db(self, document: PublicationEntity):
        await self.mongodb.init_db([document])
        
    async def initialize(self):
        await self.init_db(PublicationEntity)
    
    @staticmethod
    async def get_publication(uuid: str) -> PublicationDomain:
        publication_entity = await PublicationEntity.find_one(PublicationEntity.uuid == uuid)
        if publication_entity:
            return PublicationMapperDAO.to_domain(publication_entity)
        else:
            logging.error(f"publication with UUID {uuid} not found.")
            return None

    @staticmethod
    async def create_publication(publication: PublicationDomain) -> PublicationDomain:
        publication_entity = PublicationMapperDAO.from_domain(publication)
        await publication_entity.insert()
        return PublicationMapperDAO.to_domain(publication_entity)

    @staticmethod
    async def update_publication(uuid: str, publication: PublicationDomain) -> PublicationDomain:
        entity = await PublicationEntity.find_one(PublicationEntity.uuid == uuid)
        if not entity:
            logging.error(f"publication with UUID {uuid} not found.")
            return None
        update = PublicationMapperDAO.from_domain(publication)
        update = PublicationMapperDAO.to_update(entity, update)
        await entity.update({"$set": update.dict(exclude_unset=True)})
        return PublicationMapperDAO.to_domain(update)

    @staticmethod
    async def list_publication() -> List[PublicationDomain]:
        publication_entities = await PublicationEntity.find_all().to_list()
        return [PublicationMapperDAO.to_domain(entity) for entity in publication_entities]

    @staticmethod
    async def delete_publication(uuid: str) -> bool:
        publication_entity = await PublicationEntity.find_one(PublicationEntity.uuid == uuid)
        if not publication_entity:
            logging.error(f"publication with UUID {uuid} not found.")
            return False
        await publication_entity.delete()
        return True
