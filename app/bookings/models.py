import sqlalchemy as sa
from app.database import Base


class Booking(Base):

    __tablename__ = 'bookings'

    id = sa.Column(sa.Integer, primary_key=True)
    room_id = sa.Column(sa.ForeignKey('rooms.id'))
    user_id = sa.Column(sa.ForeignKey('users.id'))
    date_from = sa.Column(sa.Date, nullable=False)
    date_to = sa.Column(sa.Date, nullable=False)
    price = sa.Column(sa.Float, nullable=False)
    total_cost = sa.Column(sa.Integer, sa.Computed("(date_to - date_from) * price"))
    total_days = sa.Column(sa.Integer, sa.Computed("date_to - date_from"))
