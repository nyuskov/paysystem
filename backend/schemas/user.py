import uuid
from typing import Optional
from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    company_name: Optional[str] = None
    balance: float


class UserCreate(schemas.BaseUserCreate):
    company_name: Optional[str] = None


class UserUpdate(schemas.BaseUserUpdate):
    company_name: Optional[str] = None
