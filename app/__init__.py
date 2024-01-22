from fastapi import APIRouter
from .views import router as stream_router

router = APIRouter()
router.include_router(router=stream_router, prefix="/stream")
