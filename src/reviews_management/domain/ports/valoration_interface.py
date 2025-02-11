from abc import ABC, abstractmethod
from reviews_management.domain.entities.valoration import Valoration

class ValorationInterface(ABC):
    @abstractmethod
    def get_valoration(self, uuid: str) -> dict:
        pass
    
    @abstractmethod
    def get_valorations_by_user_uuid(self, uuid: str) -> dict:
        pass
    
    @abstractmethod
    def get_valorations_by_provider_uuid(self, uuid: str) -> dict:
        pass
    
    @abstractmethod
    def create_valoration(self, valoration: Valoration) -> dict:
        pass
    
    @abstractmethod
    def update_valoration(self, uuid:str, valoration: Valoration) -> dict:
        pass
    
    @abstractmethod
    def list_valoration(self) -> list:
        pass
    
    @abstractmethod
    def delete_valoration(self, uuid: str) -> bool:
        pass
    