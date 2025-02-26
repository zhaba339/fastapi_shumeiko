from fastapi import APIRouter, Depends
from app.database import async_session_maker
from app.bookings.models import Bookings
from app.bookings.schemas import SBooking
from sqlalchemy import select
from app.bookings.service import BookingService
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"],
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
    return await BookingService.find_all(user_id=user.id)


@router.post("")
async def create_booking(user: Users = Depends(get_current_user)) -> SBooking:
    return await BookingService.add(user_id=user.id)


@router.get("/{booking_id}")
async def get_one_booking(booking_id):
    pass
