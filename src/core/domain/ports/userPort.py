import abc
from ..entities.User import User

class UserPort(metaclass=abc.ABCMeta):
    def __init__(self) -> None:
        pass
    
    @abc.abstractmethod
    def createUser(self, user: User):
        pass

