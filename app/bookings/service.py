from app.database import async_session_maker
from sqlalchemy import select
from app.bookings.models import Bookings
from app.base_repository import BaseRepository


class BookingService(BaseRepository):
    model = Bookings

    @classmethod
    async def add(cls):
        pass
