import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.database import Base


class Rooms(Base):

    __tablename__ = 'rooms'
    __table_args__ = {'extend_existing': True}

    id = sa.Column(sa.Integer, primary_key=True)
    hotel_id = sa.Column(sa.Integer, sa.ForeignKey('hotels.id'))
    name = sa.Column(sa.String(50), nullable=False)
    description = sa.Column(sa.Text, nullable=True)
    price = sa.Column(sa.Float, nullable=False)
    services = sa.Column(sa.JSON, nullable=True)
    quantity = sa.Column(sa.Integer, nullable=False)
    image_id = sa.Column(sa.Integer, nullable=True)
