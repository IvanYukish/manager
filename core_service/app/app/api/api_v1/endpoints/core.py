from typing import Any

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def home() -> Any:
    """
    Home endpoint
    """
    return {'message': 'Hello world'}
