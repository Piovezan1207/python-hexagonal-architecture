from ...core.domain.entities.User import User
from ...core.application.userCases.userUseCase import UserUseCase

class Controller():
    def __init__(self, userUseCase: UserUseCase) -> None:
        self.userUseCase = userUseCase
    
    def createUser(self, request):
        user = User(request.args["name"])
        response = self.userUseCase.createUser(user)
        return response



    
    