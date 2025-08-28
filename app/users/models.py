import sqlalchemy as sa
from app.database import Base


class Users(Base):

    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    email = sa.Column(sa.String(30), unique=True, nullable=False)
    hashed_password = sa.Column(sa.String(100), nullable=False)
