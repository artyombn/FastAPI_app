from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/items",
    tags=["items"],
)

@router.get("/")
async def get_items_list():
    return {
        "data": [
            {"id": 1, "name": "Item 1"},
            {"id": 2, "name": "Item 2"},
            {"id": 3, "name": "Item 3"},
        ]
    }

@router.get("/{item_id}")
async def get_item(item_id: int):
    items = {
        "data": [
            {"id": 1, "name": "Item 1"},
            {"id": 2, "name": "Item 2"},
            {"id": 3, "name": "Item 3"},
        ]
    }
    return (item for item in items["data"] if item["id"] == item_id)


class ItemCreate(BaseModel):
    name: str
    description: str
@router.post("/create")
async def create_item(item: ItemCreate):
    return {
        "data": {
            "id": 0,
            "name": item.name,
            "description": item.description,
        }
    }