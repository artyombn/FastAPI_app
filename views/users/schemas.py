from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    """
    Create new user with username and email
    """

class UserOutput(UserBase):
    id: int

class User(UserBase):
    id: int