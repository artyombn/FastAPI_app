from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone

from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.users.services import UserServices

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=30)
    to_encode.update({"exp": expire})
    auth_data = settings.get_auth_data()
    encode_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encode_jwt

async def authenticate_user(email: EmailStr, password: str, session: AsyncSession):
    user = await UserServices.find_one_or_none(email=email, session=session)
    if not user or not verify_password(
            plain_password=password,
            hashed_password=user.password,
    ):
        return False
    return user


