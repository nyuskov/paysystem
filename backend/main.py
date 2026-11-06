from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import router as api_router
from models.user import Base, engine

origins = [
    # dev-адреса фронта (на случай прямых запросов к API в обход Traefik)
    "http://localhost",
    "https://localhost",
    "http://127.0.0.1",
    "https://127.0.0.1",
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    # При старте контейнера автоматически создаем таблицы в Postgres, если их нет
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title="Payment Gate API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.middleware("http")
async def set_secure_scheme(request, call_next):
    # Читаем заголовок от Traefik и подменяем scheme для FastAPI
    if request.headers.get("x-forwarded-proto") == "https":
        request.scope["scheme"] = "https"
    response = await call_next(request)
    return response
