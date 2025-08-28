from pydantic import BaseModel

from app.hotels.schemas import SHotel


class SRoom(BaseModel):
    id: int
    hotel_id: int
    name: str
    description: str
    price: float
    quantity: int
    image_id: int

    class Config:
        from_attributes = True
