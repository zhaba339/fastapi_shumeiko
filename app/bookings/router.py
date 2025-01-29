from fastapi import APIRouter
from app.database import async_session_maker
from app.bookings.models import Booking
from sqlalchemy import select


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"],
)


@router.get("")
async def get_bookings():
    async with async_session_maker() as session:
        query = select(Booking)
        result = await session.execute(query)
        return result.scalars().all()

@router.get("/{booking_id}")
async def get_one_booking(booking_id):
    pass

