import sqlalchemy as sa
from app.database import Base

class User(Base):

    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.String(30), unique=True, nullable=False)
    hashed_password = sa.Column(sa.String(50), nullable=False)
