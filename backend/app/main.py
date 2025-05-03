from fastapi import FastAPI
from app.api.v1.api import api_router

app = FastAPI(title="Fitness Community Super App API")

app.include_router(api_router, prefix="/api/v1")
