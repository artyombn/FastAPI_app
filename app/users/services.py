from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.database import async_session_maker
from app.models.user import User as User_db
from app.users.schemas import UserCreate


class UserServices:
    @classmethod
    async def get_all_users(cls, session: AsyncSession):
        query = select(User_db)
        users = await session.execute(query)
        return users.scalars().all()

    @classmethod
    async def find_one_or_none(cls, email: str, session: AsyncSession):
        user = await session.execute(select(User_db).where(User_db.email == email))
        return user.scalar_one_or_none()

    @classmethod
    async def register_user(cls, user_dict, session: AsyncSession):
        user = User_db(**user_dict)
        session.add(user)
        await session.commit()
        return user


