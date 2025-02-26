from fastapi import APIRouter
from app.rooms.schemas import SRoom
from app.rooms.service import RoomService

router = APIRouter(
    prefix='/rooms',
    tags=['Номера'],
)


@router.get("", description="Получить все номера")
async def get_rooms() -> list[SRoom]:
    return await RoomService.find_all()


@router.post("", description="Добавить номер")
async def create_room(room: SRoom) -> SRoom:
    return await RoomService.add()
