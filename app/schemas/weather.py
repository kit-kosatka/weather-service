from pydantic import BaseModel

class Main(BaseModel):
    temp: float
    feels_like: float
    humidity: float
    pressure: float

class Wind(BaseModel):
    speed: float

class Weather(BaseModel):
    description: str

class WeatherResponse(BaseModel):
    name: str
    main: Main
    wind: Wind
    weather: list[Weather]



