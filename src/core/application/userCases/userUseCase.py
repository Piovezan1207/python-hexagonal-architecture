from ...domain.entities.User import User
from ...domain.services.userService import UserService

class UserUseCase():
    def __init__(self, userService: UserService) -> None:
        self.userService = userService
    
    def createUser(self, user: User):
        return self.userService.create(user)