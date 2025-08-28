import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app.database import Base


class Hotels(Base):

    __tablename__ = 'hotels'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    location = sa.Column(sa.String(100), nullable=False)
    services = sa.Column(sa.JSON)
    rooms_quantity = sa.Column(sa.Integer, nullable=False)
    image_id = sa.Column(sa.Integer)
