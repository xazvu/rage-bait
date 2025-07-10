from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


DATABASE_URL = "sqlite+aiosqlite:///./rage-bite.db"

# Создание асинхронного движка
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# Создание асинхронной сессии
AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

# Инициализация базы данных (один раз)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Зависимость получения сессии (для FastAPI или других фреймворков)
async def get_session():
    async with AsyncSessionLocal() as session:
        yield session
