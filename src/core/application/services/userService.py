from ...domain.entities.User import User
from ...domain.repositories.userRepositoryPort import UserRepositoryPort

class UserService():
    def __init__(self, userRepository: UserRepositoryPort) -> None:
        self.userRepository = userRepository
    
    def createUser(self, user: User):
        return self.userRepository.save(user)