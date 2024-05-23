from ...core.domain.entities.User import User
# from ...core.application.userCases.userUseCase import UserUseCase
from ...core.application.ports.userPort import UserPort

class Controller():
    def __init__(self, userPort: UserPort) -> None:
        self.userPort = userPort
    
    def createUser(self, request):
        user = User(request.args["name"])
        response = self.userPort.createUser(user)
        return response

