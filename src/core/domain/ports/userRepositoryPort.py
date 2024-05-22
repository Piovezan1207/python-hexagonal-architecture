import abc
from ..entities.User import User

class UserRepositoryPort(metaclass=abc.ABCMeta):
    def __init__(self) -> None:
        pass
    
    @abc.abstractmethod
    def save(self, user: User):
        pass