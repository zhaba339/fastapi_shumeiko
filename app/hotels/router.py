from fastapi import APIRouter
from app.database import async_session_maker
from app.hotels.models import Hotels
from sqlalchemy import select
from app.hotels.service import HotelService

# from app.hotels.schemas import SHotel

router = APIRouter(
    prefix="/hotels",
    tags=["Отели"],
)


@router.get("", description="Получить все отели")
async def get_hotels():
    return await HotelService.find_all()


@router.get("/{hotel_id}", description="Получить отель по его ID")
async def get_one_hotel(hotel_id: int):
    return await HotelService.find_by_id(hotel_id)
