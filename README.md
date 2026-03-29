# Weather Service

FastAPI service for obtaining weather data via the OpenWeatherMap API with caching in Redis.

## Stack
- FastAPI
- httpx
- Redis
- Pydantic
- Docker

## Launch

1. Clone the repository
2. Create an `.env` file like `env.example`
3. Run via Docker:

docker-compose up --build


## Endpoints

GET /weather/{city} — get weather forecast for the city

## Example response
```json
{
  "name": "Amsterdam",
  "main": {"temp": 7.25, "feels_like": 2.5, "humidity": 71, "pressure": 1020},
  "wind": {"speed": 10.29},
  "weather": [{"description": "moderate rain"}]
}
```