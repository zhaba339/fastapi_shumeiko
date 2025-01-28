from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel

app = FastAPI()


class HotelSearchArgs:
    def __init__(self,
                 location: Optional[str] = None,
                 date_from: Optional[date] = None,
                 date_to: Optional[date] = None,
                 stars: Optional[int] = Query(None, ge=1, le=5),
                 ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars


@app.get("/hotels", description='Получить список отелей', tags=['Отели'])
async def get_hotels(
    search_args: HotelSearchArgs = Depends()
):
    return search_args


# Создание pydantic схемы брони
class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings", description='Создать бронь номера', tags=['Бронирование'])
def add_booking(booking: SBooking):
    return booking
