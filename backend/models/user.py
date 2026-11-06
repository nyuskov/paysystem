import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String
from fastapi_users.db import SQLAlchemyBaseUserTableUUID


class Base(DeclarativeBase):
    pass


# Модель пользователя в PostgreSQL
class User(SQLAlchemyBaseUserTableUUID, Base):
    # Поля id (UUID), email, hashed_password, is_active, is_verified уже включены
    company_name: Mapped[str] = mapped_column(String(length=100), nullable=True)
    balance: Mapped[float] = mapped_column(default=0.0)


# URL подключения к Postgres внутри Docker-сети
# Формат: postgresql+asyncpg://user:password@хост_контейнера:5432/db_name
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://payment_user:secret_payment_pass@db:5432/payment_gate",
)

engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session():
    async with async_session_maker() as session:
        yield session
