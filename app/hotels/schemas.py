from pydantic import BaseModel
import json


class SHotel(BaseModel):
    id: int
    name: str
    location: str
    services: dict
    rooms_quantity: int
    image_id: int

    class Config:
        from_attributes = True
