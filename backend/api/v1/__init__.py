from fastapi import APIRouter
from core.user import auth_backend, fastapi_users_inc
from schemas.user import UserCreate, UserRead, UserUpdate
from api.v1.home import router as home_router
from api.v1.payments import router as payments_router

router = APIRouter()

router.include_router(home_router, prefix="/home", tags=["Home"])

router.include_router(
    fastapi_users_inc.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["Auth"]
)

# Регистрация -> /v1/auth/register
router.include_router(
    fastapi_users_inc.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

# Профиль мерчанта -> /v1/users/me
router.include_router(
    fastapi_users_inc.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["Users"],
)

# Платежи
router.include_router(payments_router, prefix="/billing", tags=["Billing"])
