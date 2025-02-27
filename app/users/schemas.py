from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    username: str = Field(min_length=3, max_length=15, description="Username must be between 3 and 15 symbols")
    email: EmailStr = Field(description="Use a valid email")
    first_name: str = Field(min_length=2, max_length=15, description="First name must be between 2 and 15 symbols")
    last_name: str = Field(min_length=2, max_length=15, description="Last name must be between 2 and 15 symbols")
    password: str = Field(min_length=5, max_length=50, description="Password must be between 5 and 50 symbols")

class UserCreate(UserBase):
    """
    Create new user with username and email
    """

class UserOutput(UserBase):
    """
    To output created user
    """

class User(UserBase):
    """
    The main User cls
    """