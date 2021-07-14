from fastapi import APIRouter

from auth_service.app.app.api.api_v1.endpoints import core

api_router = APIRouter()
api_router.include_router(core.router, tags=["core"])
