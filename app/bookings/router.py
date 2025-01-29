from fastapi import APIRouter
from app.database import async_session_maker
from app.bookings.models import Booking
from sqlalchemy import select
from app.bookings.service import BookingService


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"],
)


@router.get("")
async def get_bookings():
    return await BookingService.find_all()


@router.get("/{booking_id}")
async def get_one_booking(booking_id):
    pass

