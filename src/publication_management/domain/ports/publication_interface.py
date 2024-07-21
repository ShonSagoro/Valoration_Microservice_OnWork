from abc import ABC, abstractmethod
from publication_management.domain.entities.publication import Publication


class PublicationInterface(ABC):
    @abstractmethod
    def get_publication(self, uuid: str) -> dict:
        pass
    
    @abstractmethod
    def create_publication(self, publication: Publication) -> dict:
        pass
    
    @abstractmethod
    def update_publication(self, uuid: str,  publication: Publication) -> dict:
        pass
    
    @abstractmethod
    def update_image_publication(self, uuid: str,  url_image: str) -> dict:
        pass
    
    @abstractmethod
    def get_by_uuid_user(self, uuid: str) -> dict:
        pass
    
    @abstractmethod
    def list_publication(self) -> list:
        pass
    
    @abstractmethod
    def delete_publication(self, uuid: str) -> bool:
        pass