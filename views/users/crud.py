from pydantic import BaseModel
from .schemas import User, UserCreate

class Storage(BaseModel):
    users: dict[int, User] = {}
    last_id: int = 0

    @property
    def next_id(self):
        self.last_id += 1
        return self.last_id

    def create_user(self, user_input: UserCreate) -> User:
        # user = UserCreate(id=self.next_id, username=user_input.username, email=user_input.email)
        user = User(id=self.next_id, **user_input.model_dump())
        self.users[user.id] = user
        return user

    def get_users(self) -> list[User]:
        return list(self.users.values())

    def get_user_by_id(self, user_id: int) -> User | None:
        return self.users.get(user_id)


storage = Storage()
storage.create_user(
    UserCreate(
        username="Artem",
        email="balabashinan@gmail.com",
    ),
)
storage.create_user(
    UserCreate(
        username="Nina",
        email="Nina@gmail.com",
    ),
)
storage.create_user(
    UserCreate(
        username="Tolia",
        email="tolia@gmail.com",
    ),
)
