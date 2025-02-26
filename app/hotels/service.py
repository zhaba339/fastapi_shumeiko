from app.base_repository import BaseRepository
from app.hotels.models import Hotels


class HotelService(BaseRepository):
    model = Hotels
