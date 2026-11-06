import uuid
import enum
from datetime import datetime, timezone
from sqlalchemy import String, ForeignKey, DateTime, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.user import Base, User


class MerchantStore(Base):
    __tablename__ = "merchant_stores"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(
        String(100)
    )  # Название магазина (например, "My Shoes Shop")
    website_url: Mapped[str] = mapped_column(String(255))

    # Секретный ключ, который мерчант вставит на свой сайт для подписи платежей (Stripe-style)
    api_key: Mapped[str] = mapped_column(
        String(255), unique=True, default=lambda: f"sk_live_{uuid.uuid4().hex}"
    )

    # Привязка к пользователю из fastapi-users
    owner_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE")
    )

    # Отношения (Relationship)
    owner = relationship("User", back_populates="stores")
    payments = relationship("Transaction", back_populates="store")


# Расширяем вашу модель User в backend/models/user.py, добавив обратную связь:
User.stores = relationship("MerchantStore", back_populates="owner")


class PaymentStatus(str, enum.Enum):
    PENDING = "pending"  # Создан, ожидает оплаты
    SUCCESS = "success"  # Успешно оплачен
    FAILED = "failed"  # Отклонен (нет денег / фрод)


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    amount: Mapped[float] = mapped_column(Float)
    currency: Mapped[str] = mapped_column(String(3), default="RUB")  # RUB, USD, EUR
    status: Mapped[PaymentStatus] = mapped_column(default=PaymentStatus.PENDING)

    # Какую покупку оплачивают (передается от сайта мерчанта)
    order_id: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(255), nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc)
    )

    # Привязка платежа к конкретному магазину мерчанта
    store_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("merchant_stores.id", ondelete="RESTRICT")
    )
    store = relationship("MerchantStore", back_populates="payments")
