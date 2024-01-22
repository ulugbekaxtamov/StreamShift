from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
import os

from core.config import settings
from app import router as router_v1

os.makedirs(settings.hls_output_dir, exist_ok=True)

app = FastAPI(title="My StreamShift API", description="For StreamShift", version="0.1.0")
app.include_router(router_v1, prefix=settings.api_v1_prefix)

app.mount("/hls", StaticFiles(directory=settings.hls_output_dir), name="hls")

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
