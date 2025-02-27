from typing import List

from fastapi import APIRouter, HTTPException, status

from app.users.auth import get_password_hash
from app.users.schemas import UserCreate, UserOutput
from app.users.services import UserServices
from app.models.user import User as User_db

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/", summary="Get all users", response_model=List[UserOutput])
async def get_users_list():
    return await UserServices.get_all_users()

@router.post("/create", summary="Create user", response_model=UserCreate)
async def create_user(user: UserCreate):
    return await UserServices.create_user(user)

@router.post("/register", summary="User registration", response_model=dict)
async def register_user(user_data: UserCreate):
    user = await UserServices.find_one_or_none(user_data.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists"
        )
    user_dict = user_data.model_dump()
    user_dict["password"] = get_password_hash(user_data.password)
    user_dict["hashed_password"] = user_dict.pop("password")
    await UserServices.register_user(user_dict)
    return {"message": "Registration successful"}