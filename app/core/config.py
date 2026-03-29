from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    openweather_api_key: str
    redis_url: str
    cache_expire: int

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()