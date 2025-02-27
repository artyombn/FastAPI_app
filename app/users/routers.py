from fastapi import APIRouter
from app.users.schemas import UserCreate
from app.users.services import UserServices

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/", summary="Get all users")
async def get_users_list():
    return await UserServices.get_all_users()

# @router.get("/{user_id}", response_model=UserOutput)
# async def get_user_by_id(user_id: int) -> User:
#     user = storage.get_user_by_id(user_id)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"User with id #{user_id} doesn't exist"
#         )
#     return user
#
@router.post("/create")
async def create_user(user: UserCreate):
    return await UserServices.create_user(user)
