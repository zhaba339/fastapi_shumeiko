from app.database import async_session_maker
from sqlalchemy import select
from app.bookings.models import Booking
from app.repository.base_repository import BaseRepository


class BookingService(BaseRepository):
    model = Booking
