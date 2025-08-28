from datetime import date
from typing import Optional
from pydantic import BaseModel


class SBooking(BaseModel):
    id: int
    room_id: Optional[int] = None
    user_id: int
    date_from: Optional[date] = None
    date_to: Optional[date] = None
    price: float
    total_cost: float
    total_days: int
