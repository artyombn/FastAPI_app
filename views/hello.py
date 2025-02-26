from fastapi import APIRouter

router = APIRouter(
    prefix="/hello",
    tags=["hello"],
)

@router.get("/")
async def hello_user(name: str):
    return {"message": f"Hello, {name}"}

@router.get("/{name}")
async def hello_user_name(name: str):
    return {"message": f"Hello, {name}"}