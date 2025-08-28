import logging
from starlette.requests import Request
from starlette.responses import Response
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis

from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from typing import Optional
from datetime import date
from app.bookings.router import router as bookings_router
from app.hotels.router import router as hotels_router
from app.users.router import router as users_router
from app.rooms.router import router as rooms_router
from app.pages.router import router as pages_router
from app.files.router import router as files_router

app = FastAPI(title="Бронирование отелей")

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost:6379", encoding="utf-8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="cache")


app.include_router(users_router)
app.include_router(bookings_router)
app.include_router(hotels_router)
app.include_router(rooms_router)
app.include_router(pages_router)
app.include_router(files_router)
