from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from app.models.database import async_session_maker
from app.models.user import User as User_db
from app.users.schemas import UserCreate


class UserServices:
    @classmethod
    async def get_all_users(cls):
        async with async_session_maker() as session:
            query = select(User_db)
            users = await session.execute(query)
            return users.scalars().all()

    @classmethod
    async def find_one_or_none(cls, email: str):
        async with async_session_maker() as session:
            user = await session.execute(select(User_db).where(User_db.email == email))
            existed_user = user.scalar_one_or_none()
            return existed_user

    @classmethod
    async def create_user(cls, user_input: UserCreate):
        async with async_session_maker() as session:
            async with session.begin():
                user = User_db(**user_input.model_dump())
                session.add(user)
                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
                return user

    @classmethod
    async def register_user(cls, user_dict):
        async with async_session_maker() as session:
            async with session.begin():
                user = User_db(**user_dict)
                session.add(user)
                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
                return user


