from fastapi import APIRouter, Depends
from sqlalchemy import select
from datetime import date
from app.users.exceptions import RoomCannotBeBooked
from app.database import async_session_maker
from app.users.dependencies import get_current_user
from app.bookings.schemas import SBooking
from app.bookings.service import BookingService
from app.bookings.models import Bookings
from app.users.models import Users
from app.rooms.models import Rooms

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"],
)


@router.get("")
async def get_bookings(
    user: Users = Depends(get_current_user)
) -> list[SBooking]:
    return await BookingService.find_all()


@router.get("/{booking_id}")
async def get_one_booking(booking_id):
    pass


@router.post("")
async def add_booking(
    room_id: int,
    date_to: date,
    date_from: date,
    user: Users = Depends(get_current_user),
):
    booking = await BookingService.add(user.id, room_id, date_to, date_from)
    if not booking:
        raise RoomCannotBeBooked


@router.delete("/{booking_id}")
async def delete_booking(booking_id):
    pass
