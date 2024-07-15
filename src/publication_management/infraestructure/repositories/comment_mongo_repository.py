import logging
from typing import List
from database.mongodb import Database
from publication_management.domain.ports.comment_interface import CommentInterface
from publication_management.infraestructure.daos.comment_entity import CommentEntity
from publication_management.domain.entities.comment import CommentUser as CommentDomain
from publication_management.infraestructure.mappers.comment_mapper_dao import CommentMapperDAO

class CommentMongoRepository(CommentInterface):
    def __init__(self, mongodb: Database):
        self.mongodb = mongodb
    
    async def init_db(self, document: CommentEntity):
        await self.mongodb.init_db([document])
        
    async def initialize(self):
        await self.init_db(CommentEntity)
    
    @staticmethod
    async def get_comment(uuid: str) -> CommentDomain:
        comment_entity = await CommentEntity.find_one(CommentEntity.uuid == uuid)
        if comment_entity:
            return CommentMapperDAO.to_domain(comment_entity)
        else:
            logging.error(f"comment with UUID {uuid} not found.")
            return None

    @staticmethod
    async def create_comment(comment: CommentDomain) -> CommentDomain:
        comment_entity = CommentMapperDAO.from_domain(comment)
        await comment_entity.insert()
        return CommentMapperDAO.to_domain(comment_entity)

    @staticmethod
    async def update_comment(uuid: str, comment: CommentDomain) -> CommentDomain:
        entity = await CommentEntity.find_one(CommentEntity.uuid == uuid)
        if not entity:
            logging.error(f"comment with UUID {uuid} not found.")
            return None
        update = CommentMapperDAO.from_domain(comment)
        update = CommentMapperDAO.to_update(entity, update)
        await entity.update({"$set": update.dict(exclude_unset=True)})
        return CommentMapperDAO.to_domain(update)

    @staticmethod
    async def list_comment() -> List[CommentDomain]:
        comment_entities = await CommentEntity.find_all().to_list()
        return [CommentMapperDAO.to_domain(entity) for entity in comment_entities]

    @staticmethod
    async def delete_comment(uuid: str) -> bool:
        comment_entity = await CommentEntity.find_one(CommentEntity.uuid == uuid)
        if not comment_entity:
            logging.error(f"comment with UUID {uuid} not found.")
            return False
        await comment_entity.delete()
        return True
