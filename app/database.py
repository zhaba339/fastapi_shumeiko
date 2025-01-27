from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


#Адрес нахождения базы данных, как с ней контактировать
DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
#Создаем движок
engine = create_async_engine(DATABASE_URL)
#Создатель сессий
async_session_maker=sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

#Класс для миграций, наследуемся при создании моделей, аккумулируются данные миграций
class Base(DeclarativeBase):
    pass