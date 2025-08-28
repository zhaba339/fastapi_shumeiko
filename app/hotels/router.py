from datetime import datetime
from idlelib.query import Query
from fastapi_cache.decorator import cache
import asyncio
from typing import List
from fastapi import APIRouter
from app.database import async_session_maker
from app.hotels.models import Hotels
from app.hotels.schemas import SHotel
from sqlalchemy import select
from app.hotels.service import HotelService

router = APIRouter(
    prefix="/hotels",
    tags=["Отели"],
)


@router.get("", description="Получить все отели")
async def get_hotels() -> List[SHotel]:
    hotels = await HotelService.find_all()
    return hotels


@router.get("/{location}", description="Получить отели в определенной локации")
@cache(expire=30)
async def get_hotels_by_location(
    location: str,
) -> List[SHotel]:
    await asyncio.sleep(3)
    hotels = await HotelService.find_all(location=location)
    return hotels


@router.get("/{hotel_id}", description="Получить отель по его ID")
async def get_one_hotel(hotel_id: int):
    hotel = await HotelService.find_by_id(hotel_id)
    return hotel
