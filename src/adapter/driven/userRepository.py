from ...core.domain.entities.User import User
from ...core.domain.ports.userRepositoryPort import UserRepositoryPort

class UserRepository(UserRepositoryPort):
    def __init__(self) -> None:
        super().__init__()
    
    def save(self,user: User):
        print(user.name)
        return "Feito! {}".format(user.name)