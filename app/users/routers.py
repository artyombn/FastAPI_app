from typing import List

from fastapi import APIRouter, HTTPException, Response, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import logger
from app.dependencies.db_session import get_async_session
from app.users.auth import get_password_hash, create_access_token, get_current_user_id
from app.users.schemas import UserCreate, UserOutput, UserAuth, User, TokenResponse
from app.users.services import UserServices


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/", summary="Get all users", response_model=List[UserOutput])
async def get_users_list(session: AsyncSession = Depends(get_async_session)):
    return await UserServices.get_all_users(session)

@router.post("/register", summary="User registration", response_model=dict)
async def register_user(user_data: UserCreate, session: AsyncSession = Depends(get_async_session)):
    user = await UserServices.find_one_or_none(user_data.email, session)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists"
        )
    user_dict = user_data.model_dump()
    user_dict["password"] = get_password_hash(user_data.password)

    await UserServices.register_user(user_dict, session)
    return {"message": "Registration successful"}


@router.post("/login", summary="Login", response_model=TokenResponse)
async def auth_user(response: Response, user_data: UserAuth, session: AsyncSession = Depends(get_async_session)):
    check = await UserServices.authenticate_user(email=user_data.email, password=user_data.password, session=session)
    if check is False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Incorrect username or password')
    access_token = create_access_token(data={"sub": str(check.id)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return {'access_token': access_token, 'refresh_token': None}

async def get_current_user(session: AsyncSession = Depends(get_async_session), user_id: int = Depends(get_current_user_id)):
    user = await UserServices.get_current_user_db(session=session, user_id=user_id)
    logger.debug(f"USER: {user}")
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user

@router.get("/me", summary="My profile", response_model=UserOutput)
async def get_my_profile(user: User = Depends(get_current_user)):
    return user

@router.post("/logout", summary="Logout", response_model=dict)
async def logout_user(response: Response):
    response.delete_cookie(key="users_access_token")
    return {"massage": "Logout successful"}