import logging
import sys
from fastapi import FastAPI
from app.api.weather import router as weather_router

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout,
)

app = FastAPI()
app.include_router(weather_router)
