from fastapi import FastAPI
from app.api.api_v1.api import api_router

app = FastAPI(title = "IMA-B 5 Reporter")

app.include_router(api_router,prefix='/api/v1')