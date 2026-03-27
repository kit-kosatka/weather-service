from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    OPENWEATHER_API_KEY: str
    REDIS_URL: str
    CACHE_EXPIRE: int

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()