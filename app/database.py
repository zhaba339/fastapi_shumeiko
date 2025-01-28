from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config import settings

#Создаем движок
engine = create_async_engine(settings.DATABASE_URL)
#Создатель сессий
async_session_maker=sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

#Класс для миграций, наследуемся при создании моделей, аккумулируются данные миграций
class Base(DeclarativeBase):
    pass