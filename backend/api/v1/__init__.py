from fastapi import APIRouter
from api.v1.home import router as home_router

router = APIRouter()

router.include_router(home_router, prefix="/home", tags=["Home"])
