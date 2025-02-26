from app.base_repository import BaseRepository
from app.rooms.models import Rooms


class RoomService(BaseRepository):
    model = Rooms
