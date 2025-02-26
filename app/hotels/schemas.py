from pydantic import BaseModel
import json


class SHotel(BaseModel):
    id: int
    name: str
    location: str
    services: json
    rooms_quantity: int
    image_id: int

    class Config:
        orm_mode = True
