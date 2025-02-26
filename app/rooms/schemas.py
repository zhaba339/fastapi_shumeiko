from pydantic import BaseModel


class SRoom(BaseModel):
    id: int
    hotel_id: int
    name: str
    description: str
    price: float
    quantity: int
    image_id: int

    class Config:
        orm_mode = True
