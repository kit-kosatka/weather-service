from fastapi import FastAPI
from app.api.weather import router as weather

app = FastAPI()
app.include_router(weather)
