from abc import ABC, abstractmethod
from publication_management.domain.entities.comment import CommentUser


class CommentInterface(ABC):
    
    @abstractmethod
    def get_comment(self, uuid: str) -> list:
        pass
    
    @abstractmethod
    def create_comment(self, comment: CommentUser) -> list:
        pass
    
    @abstractmethod
    def update_comment(self, uuid: str,  comment: CommentUser) -> list:
        pass
    
    @abstractmethod
    def list_comment(self) -> list:
        pass
    
    @abstractmethod
    def delete_comment(self, uuid: str) -> bool:
        pass