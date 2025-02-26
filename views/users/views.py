from fastapi import APIRouter, HTTPException, status
from .schemas import UserCreate, UserOutput, User
from .crud import storage

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/", response_model=list[UserOutput])
async def get_users_list():
    return storage.get_users()

@router.get("/{user_id}", response_model=UserOutput)
async def get_user_by_id(user_id: int) -> User:
    user = storage.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id #{user_id} doesn't exist"
        )
    return user

@router.post("/create", response_model=User)
async def create_user(user: UserCreate):
    user = storage.create_user(user)
    return user
