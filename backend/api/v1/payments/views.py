from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.user import current_active_user  # Импортируем вашу зависимость защиты
from models.user import User, get_async_session
from models.payment import Transaction, MerchantStore

router = APIRouter()


@router.get("/transactions")
async def get_merchant_transactions(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(
        current_active_user
    ),  # Роут заблокирован для неавторизованных!
):
    # Находим транзакции, которые принадлежат ТОЛЬКО магазинам текущего пользователя
    query = (
        select(Transaction)
        .join(MerchantStore)
        .where(MerchantStore.owner_id == user.id)
        .order_by(Transaction.created_at.desc())
    )

    result = await session.execute(query)
    transactions = result.scalars().all()

    return transactions
