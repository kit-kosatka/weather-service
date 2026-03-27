from fastapi import APIRouter, HTTPException

from app.schemas.weather import WeatherResponse
from app.services.weather import get_weather

router = APIRouter(prefix="/weather", tags=["weather"])


@router.get("/", response_model=WeatherResponse)
async def weather(city: str):
    result = await get_weather(city)
    if result is None:
        raise HTTPException(status_code=404, detail=f"Город {city} не найден")
    return result
