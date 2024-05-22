from ..entities.User import User
from ..ports.userRepositoryPort import UserRepositoryPort

class UserService():
    def __init__(self, userRepository: UserRepositoryPort) -> None:
        self.userRepository = userRepository
    
    def create(self, user: User):
        return self.userRepository.save(user)