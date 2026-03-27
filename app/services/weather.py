import httpx
from app.core.config import settings
from app.core.redis import client
from app.schemas.weather import WeatherResponse

async def get_weather(city: str) -> WeatherResponse | None:
    cached = await client.get(city)
    if cached:
        return WeatherResponse.model_validate_json(cached)

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.OPENWEATHER_API_KEY}&units=metric'

    async with httpx.AsyncClient() as http:
        response = await http.get(url)
        if response.status_code != 200:
            return None
        data = response.json()

    result = WeatherResponse(
        city=data["name"],
        temperature=f"{data['main']['temp']}°C",
        pressure=f"{round(data['main']['pressure'] * 0.750064)} мм рт.ст.",
        wind_speed=f"{data['wind']['speed']} м/с"
    )

    await client.setex(city, settings.CACHE_EXPIRE, result.model_dump_json())
    return result
