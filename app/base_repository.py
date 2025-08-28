from app.database import async_session_maker
from sqlalchemy import select, insert, delete
from sqlalchemy.orm import sessionmaker
from app.hotels.models import Hotels
from app.rooms.models import Rooms


class BaseRepository:
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filters_by):
        async with async_session_maker() as session:
            try:
                query = select(cls.model).filter_by(**filters_by)
                result = await session.execute(query)
                return result.scalar_one_or_none()
            except Exception as e:
                raise e

    @classmethod
    async def find_all(cls, **filters_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filters_by)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()
