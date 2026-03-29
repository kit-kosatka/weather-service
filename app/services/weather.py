import httpx
import logging
from app.core.config import settings
from app.core.redis import client
from app.schemas.weather import WeatherResponse

logger = logging.getLogger(__name__)


async def get_weather(city: str) -> WeatherResponse | None:
    cache_key = f"weather:{city.lower()}"

    cached_data = await client.get(cache_key)
    if cached_data:
        logger.info(f"CACHE HIT - {city}")
        return WeatherResponse.model_validate_json(cached_data)

    logger.info(f"CACHE MISS - {city}")
    try:
        async with httpx.AsyncClient(timeout=5) as http:
            response = await http.get(
                "https://api.openweathermap.org/data/2.5/weather",
                params={
                    "q": city,
                    "appid": settings.openweather_api_key,
                    "units": "metric",
                },
            )
            response.raise_for_status()
            data = response.json()

        result = WeatherResponse(**data)
        await client.setex(cache_key, settings.cache_expire, result.model_dump_json())
        logger.info(f"Cached weather for {city}")
        return result

    except Exception as e:
        logger.error(f"Error {e}")
        return None
