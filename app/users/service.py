from app.base_repository import BaseRepository
from app.users.models import Users


class UserService(BaseRepository):
    model = Users
