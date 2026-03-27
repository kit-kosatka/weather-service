from pydantic import BaseModel,Field, field_validatori

class WeatherResponse(BaseModel):
    city: str
    temperature: float
    pressure: int
    wind_speed: float
