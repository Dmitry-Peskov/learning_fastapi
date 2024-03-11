from fastapi import APIRouter
from .users.views import user_router

api_v1_router = APIRouter(prefix="/api/v1")
api_v1_router.include_router(user_router)
