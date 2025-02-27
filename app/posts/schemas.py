from pydantic import BaseModel, Field

class PostBase(BaseModel):
    title: str = Field(min_length=5, max_length=50, description="Title must be between 3 and 15 symbols")
    content: str = Field(min_length=20, max_length=500, description="Post content must be between 20 and 500 symbols")

class PostCreate(PostBase):
    """
    Create new post with title and content
    """

class PostOutput(PostBase):
    """
    To output created post
    """

class Post(PostBase):
    """
    The main Post cls
    """